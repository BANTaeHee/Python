'''
    Author : Ezen
    Date : 2022. 12. 29
'''

'''
    keras : tensorflow를 활용해서 인공지능을 더 쉽게 만들 수 있도록 도와주는 소프트웨어 
            tensorflow의 기본 기능으로 내장됨 
'''
from tensorflow import keras
import data_reader

EPOCHS = 20     # 전체 데이터셋을 몇 회 학습시킬 것이냐, 몇 번 반복할 것이냐 의미

# 데이터를 읽어옴
dr = data_reader.DataReader()

# 인공신경망 제작
model = keras.Sequential([
    keras.layers.Dense(12)       # 첫번째 층은 3개의 유닛은 가지고 있으며 한 레이어 구성
    , keras.layers.Dense(128, activation="relu")        # 두번째 층은 128개의 유닛을 가지고 한 레이어 구성, 렐루함수
    , keras.layers.Dense(3, activation="softmax")       # 세번째 층은 3개의 유닛을 가지고 있으며 한 레이어 구성
])

# 인공신경망 컴파일
'''
    model 변수에 저장한 인공신경망을 압축하고 
    메모리 위에 올려서 당장 사용할 수 있게 함. 
    optimizer : 신경망을 학습시키기 위해 사용하는 알고리즘 
    metrics : 어떤 점수를 기준으로 인공지능의 성능을 채점할 것인지 기준
    loss : 인공지능의 학습 방향을 결정하는 함수 
'''
model.compile(optimizer="adam", metrics=["accuracy"]
              , loss="sparse_categorical_crossentropy")

print("============================== 학습 시작 ==============================")
# 인공신경망 학습
model.fit(dr.train_X, dr.train_Y, epochs=EPOCHS
          , validation_data=(dr.test_X, dr.test_Y))
















