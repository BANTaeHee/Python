'''
    * 사이킷런 가상 데이터 생성
        1) 분류(classification) 모델 학습을 위한 가상 데이터 생성하기
        2) make_blobs
            - 정규 분포를 따르는 가상의 데이터 생성함
            - 여러 개의 클러스터가 존재하는 형태로 데이터가 생성됨
            - 파라미터
                - n_samples : 생성할 데이터 개수(default : 100)
                - centers : 생성할 크러스터의 수 (default : 3)
                - n_features : 입력 차원(default=2)
                - random_state : 랜덤 데이터 생성 시도 (seed)
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=1234)
df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
print(df.head(10))

print("데이터 개수 : ", len(df))

plt.scatter(df["x"], df["y"], s=100, c=y)
plt.show()