import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
import numpy as np

# MNIST Data down 받기
# 공개 데이터셋에서 학습 데이터를 내려받기
training_data = datasets.MNIST(
    root = "data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# 공개 데이터셋에서 테스트 데이터를 내려받기
test_data = datasets.MNIST(
    root = "data",
    train=True,
    download=True,
    transform=ToTensor(),
)

'''
    * 데이터 준비
        1) torch.utils.data import DataLoader
           데이터로더 (DataLoader) 객체
           - 학습에 사용될 데이터 전체를 보관했다가 
           - 모델 학습을 할 때 배치 크기만큼 데이터를 꺼내서 사용.
        2) 내부적으로 반복자(iterator)에 포함된 인덱스를 이용해 배치 크기 만큼 반환함 
        
'''
batch_size = 64

# 데이터로드 생성
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X : ", X.shape)
    print("Shape of y : ", y.shape, y.dtype)
    break

# 학습에 사용할 CPU나 GPU 장치를 얻기

# 모델을 정의(클래스)

# Loss 함수와 Optimizer 설정

# Training을 위한 함수

# Test를 위한 함수





