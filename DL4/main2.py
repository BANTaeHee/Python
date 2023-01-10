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

# 범주형 데이터와 레이블을 텐서로 변환함 ----------------











