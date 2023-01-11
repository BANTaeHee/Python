import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('ezen/car_evaluation.csv')
print(dataset.head())

# 컬럼들의 목록
categorical_columns = ['price', 'maint', 'doors', 'persons', 'lug_capacity', 'safety']

# astype() 메서드를 이용해서 데이트를 범주형(단어)으로 변환
for category in categorical_columns:
    dataset[category] = dataset[category].astype('category')

# 범주형(단어)으로 변환 => 넘파이 배열
price = dataset['price'].cat.codes.values
maint = dataset['maint'].cat.codes.values
doors = dataset['doors'].cat.codes.values
persons = dataset['persons'].cat.codes.values
lug_capacity = dataset['lug_capacity'].cat.codes.values
safety = dataset['safety'].cat.codes.values

# 두개 이상의 넘파일 객체를 합침
category_data = np.stack([price, maint, doors, persons, lug_capacity, safety], 1)
print(category_data[:10])

print("-" * 30)

# torch 모듈을 이용하여 텐서로 변환
category_data = torch.tensor(category_data, dtype=torch.int64)
print(category_data[:10])

print("-" * 30)

# 레이블(output)로 사용할 컬럼도 텐서로 변환
outputs = pd.get_dummies(dataset.output)        # get_dummies() : 가변수(dummy variable)로 만들어주는 함수 (0,1)
outputs = outputs.values
outputs = torch.tensor(outputs).flatten()       # 1차원 텐서로 변환

print(category_data.shape)
print(outputs.shape)

# 범주형 데이터와 레이블을 텐서로 변환함 ---------------------

'''
    컬럼의 고유 값의 수를 2로 나누는 것을 많이 사용
    - 예를 들어 price 컬럼은 4개의 고유 값을 갖기 때문에 4/2 = 2 (임베딩 크기)
'''
print("+" * 30)

categorical_columns_sizes = [len(dataset[column].cat.categories) for column in categorical_columns]
categorical_embedding_sizes = [(col_size, min(50, (col_size + 1)//2)) for col_size in categorical_columns_sizes]
print(categorical_embedding_sizes)

print("+" * 30)
total_records = 1728
test_records = int(total_records * .2)      # 데이터셋을 훈련셋과 테스트셋 용도로 분리

categorical_train_data = category_data[:total_records - test_records]                   # 80
categorical_test_data = category_data[total_records - test_records:total_records]       # 20
train_outputs = outputs[:total_records - test_records]                                  # 80
test_outputs = outputs[total_records - test_records:total_records]                      # 20

print(len(categorical_train_data))
print(len(categorical_test_data))
print(len(train_outputs))
print(len(test_outputs))

# 모델의 네트워크 생성
class Model(nn.Module):                 # 클래스 형태로 구현되는 모델은 nn.Module을 상속받음
    '''
        self : 첫번째 파라미터로 self 지정해야 함, 자기 자신을 가리킴
        embedding_size : 범주형 컬럼의 임베딩 크기
        output_size : 출력층의 크기
        layers : 모든 계층에 대한 목록
        p : 드롭아웃 (기본값은 0.5)
    '''

    def __init__(self, embedding_size, output_size, layers, p=0.4):
        super().__init__()
        self.all_embeddings = nn.ModuleList([nn.Embedding(ni, nf) for ni, nf in embedding_size])
        self.embedding_dropout = nn.Dropout(p)          # 입력에서 정해진 비율만큼 무작위로 뉴런을 삭제

        all_layers = []                                 # 비어있는 리스트 생성
        num_categorical_cols = sum((nf for ni, nf in embedding_size))
        input_size = num_categorical_cols               # 입력층의 크기로 범주형 컬럼 개수를 저장함

        for i in layers:                # 모델의 네트워크 계층 구축
            all_layers.append(nn.Linear(input_size, i))    # 선형 계층은 입력 데이터에 선형 변환을 위해서 사용(입력과 가중치를 곱한 후 바이어스를 더한 결과 )
            all_layers.append(nn.ReLU(inplace=True))       # 활성화 함수 사용
            all_layers.append(nn.BatchNorm1d(i))           # 배치 정규화 (batch normalization) 사용
            all_layers.append(nn.Dropout(p))               # Dropout : 과적합 방지에 사용
            input_size = i

        all_layers.append(nn.Linear(layers[-1], output_size))
        self.layers = nn.Sequential(*all_layers)        # 레이어를 all_layers 리스트에 append된 순서대로 적용시킴


    def forward(self, x_categorical):                   # 학습 데이터를 입력받아서 연산을 진행
        embeddings = []                                 # 모델 객체를 데이터와 함께 호출하면 자동으로 forward() 실행됨
        for i, e in enumerate(self.all_embeddings):
            embeddings.append(e(x_categorical[:, i]))
        x = torch.cat(embeddings, 1)
        x = self.embedding_dropout(x)
        x = self.layers(x)
        return x

'''
    Model 클래스의 객체를 생성하기 
    객체를 생성하면서 범주형 컬럼의 임베딩 크기, 출력 크기, 은닉층의 뉴런, 드롭아웃을 전달
    은닉층의 뉴런을 정의는 여러 크기로 지정하여 테스트해 보는 것이 학습에 도움이 될것임.
'''
model = Model(categorical_embedding_sizes, 4, [200, 100, 50], p=0.4)
print(model)

'''
    모델을 훈련시키기 전 손실 함수와 옵티마이저에 대해 정의
    이 DL4의 경우 데이터를 분류해야 하는 것으로 크로스 엔트로피(cross entropy) 손실함수를 사용함
    옵티마이저는 아담(Adam)을 사용함
    
    lr(Learning Rate) : 미분값을 얼마만큼 이동시킬 것인가를 결정함.
                        초기값이 크다면 초반에 loss값이 빠르게 줄어들 것이다. 나중에 가면 underfitting이 발생함
                        
'''
print("-" * 30)
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
'''
    파이토치는 GPU에 최적화된 딥러닝 프레임워크이다. 
    GPU가 있으면 GPU를 사용하고, 없다면 CPU를 사용하도록 함
'''

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

'''
    모델 훈련 (학습)시킴
'''
epochs = 500
aggregated_loss = []            # 오차값을 누적 저장할 용도의 리스트

train_outputs = train_outputs.to(device=device, dtype=torch.int64)
for i in range(epochs):
    i += 1
    y_pred = model(categorical_train_data).to(device)       # 예측값
    single_loss = loss_function(y_pred, train_outputs)
    aggregated_loss.append(single_loss)

    if i % 25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

    optimizer.zero_grad()       # 기울기 초기화
    single_loss.backward()      # 역전파 계산
    optimizer.step()            # 기울기 이용하여 파라미터 업데이트

'''
    학습을 했고 테스트 데이터햇으로 예측 진행하기
    categorical_test_data 데이터셋을 모델에 적용하기
'''
print("-" * 30)
test_outputs = test_outputs.to(device=device, dtype=torch.int64)
with torch.no_grad():
    y_val = model(categorical_test_data).to(device)         # 예측값
    loss = loss_function(y_val, test_outputs)
print(f'Loss : {loss:.8f}')             # 테스트데이터셋에 대한 손실값을 출력
                                        # 훈련데이터셋에서 도출된 값과 비슷하므로 과적합은 발생하지 않음

print("-" * 30)
'''
    정확도, 정밀도, 재현율 출력하기 
'''
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

y_val = np.argmax(y_val.cpu().numpy(), axis = 1)
test_outputs = test_outputs.cpu().numpy()
print (confusion_matrix(test_outputs, y_val))               # 정밀도
print(classification_report(test_outputs, y_val))           # 정확도
print(accuracy_score(test_outputs,y_val))                   # 재현율





