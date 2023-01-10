import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets
import torchvision.transforms as tr
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
import numpy as np

'''
    * pytorch에서 제공하는 데이터 셋(Dataset)
        - 토치비전(torchvision) : pytorch에서 제공하는 데이터셋들이 모여있는 패키지 
        - data와 label
        - Ex) Fashion-MNIST data
        
    * Dataloader
        - Dataset을 model에 공급할 수 있도록 iterable 객체로 감싸준다. 
        
'''
# 공개데이터셋에서 학습데이터를 내려받기
traing_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

print(traing_data)
print(type(traing_data))

print("-"*50)
print(traing_data[0])

# 데이터 시각화하기
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "PullOver",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot"
}
figure = plt.figure(figsize=(8,8))
cols, rows = 3, 3

for i in range(1, cols*rows + 1):
    sample_idx = torch.randint(len(traing_data), size=(1,)).item()
    img, label = traing_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")

plt.show()

print("-"*50)
'''
    # DataLoader 만들기
        - 데이터 준비 
        - 학습에 사용될 데이터 전체를 보관했다가 모델 학습을 할 때 배치(batch) 크기만큼 데이터를 꺼내서 사용
        - 내부적으로 반복자(iterator)에 포함된 인덱스(index)을 이용해서 
          배치크기만큼 데이터를 반환함
'''
train_dataloader = DataLoader(traing_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=False)

# DataLoader를 통해 반복하기(iterate)
# 이미지와 정답(label)을 표시하기
train_features, train_labels = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label : {label}")

'''
    * Custom Dataset, Data Loader 만들기 
        - 딥러닝은 기본적으로 대량의 데이터 이용하여 모델을 학습
        - 데이터를 한번에 메모리레 불러와서 훈련시키면 시간과 비용 측면에서 비효율적이다. 
        - 데이터를 한번에 다 부르지 않고 조금씩 나누어 불러서 사용하는 방식
        
        - 1) CustomDataSet 클래스 구현 
'''
class CustomDataset(Dataset):
    # 필요한 변수 선언하고, 데이터셋의 전처리를 해주는 함수
    def __init__(self,np_data, transform=None):
        self.data = np_data
        self.transform = transform
        self.len = np_data.shape[0]
    # 데이터셋의 길이, 즉 샘플의 수를 가져오는 함수
    def __len__(self):
        return self.len
    # 데이터셋에서 특정 데이터를 가져오는 함수(index번째 데이터를 반환하는 함수)
    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
        return sample

'''
    tr.Compose() : 여러개의 이미지 전처리 기능을 연결해서 사용할 수 있게 해주는 함수이다. 
                   여기서는 하나의 전처리 기능(square) 함수만 연결이 되어 있다.
'''

def square(sample):
    return sample ** 2

trans = tr.Compose([square])

# 커스텀 데이터 셋 생성
np_data = np.arange(10)

# CustomDataset 클래스의 인스턴스 생성
# 이미지 전처리 기능인 square함수를 적용할 수 있는 데이터셋
custom_dataset = CustomDataset(np_data, transform=trans)

# custom_dataset으로부터 새로운 데이터로더 생성
# batch_size는 각각의 샘플 개수, shuffle은 샘플을 섞어서 읽어옴
custom_dataloader = DataLoader(custom_dataset, batch_size=2, shuffle=True)

for _ in range(3):
    for data in custom_dataloader:
        print(data)
    print("=" * 20)

# device 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

'''
    * Model Class 만들기 
        1) nn.Module을 상속하여 정의
            - nn.Module을 상속받는 모델은 기본적으로 __init()__과 forward() 함수를 포함
            - __init()__
                - 활성화 함수
            - forward()
                - 모델에서 실행되어야 하는 연산을 정의 
'''
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()       # nn.Module의 생성자를 호출
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.flatten(x)         # 입력 x를 전달받아 전체 신경망을 순전파하는 함수
        ezen = self.linear_relu_stack(x)   # 입력 x를 펼치는 flatten 계층을 적용한 후, linear_relu_stack 객체 적용
        return ezen

# Model instance 생성, device 설정
model = NeuralNetwork().to(device)
print(model)

# 가상의 data로 예측하기
# 입력 데이터 X 생성 - 28 * 28 크기의 이미지가 1개 들어있는 텐서임
X = torch.rand(1, 28, 28, device=device)

# 신경망 객체 model을 적용해 순전파 수행하기
# 입력 X를 신경망의 각 계층으로 전달해 결과를 출력
ezen = model(X)

pred_result = nn.Softmax(dim=1)(ezen)
y_pred = pred_result.argmax(1)          # 가장 큰 값을 갖는 예측된 클래스

print(f"예측된 클래스 : {y_pred}")








