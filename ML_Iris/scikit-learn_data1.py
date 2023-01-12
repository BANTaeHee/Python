'''
    * 머신러닝 분야의 고전적인 붓꽃(Iris) 데이터셋
        0) 대표적인 지도 학습 데이터임
        1) 출력 데이터는 3개의 클래스
            - 부채붓꽃(Setosa)
            - 버시컬러(Versicolor)
            - 버지니카(Virginica) 세 종류(품종)

        2) 입력 데이터 4개의 특징
            - sepal length (꽃받침 길이)
            - sepal width (꽃받침 넓이)
            - petal length (꽃잎 길이)
            - petal width (꽃잎 넓이)

        3) 150개의 꽃 샘플에서 꽃잎 길이와 꽃잎 너비
'''

from sklearn import datasets
import numpy as np

# 데이터 세트 불러오기
dataset = datasets.load_iris()

data = dataset["data"]
target = dataset["target"]
feature_names = dataset["feature_names"]

print(f"총 데이터 개수 : {len(data)}")
print(f"총 타겟 개수 : {len(target)}")
print("[입력 특징]")
for i in range(len(feature_names)):
    feature_name = feature_names[i]
    print(f"{i + 1} : {feature_name}")

print("입력 데이터 출력")
print(data[:5])

print("-" * 50)

target_names = dataset["target_names"]
print("[출력 특징]")
for i in range(len(target_names)):
    target_name = target_names[i]
    print(f"{i + 1} : {target_name}")

print("출력 데이터 출력")
print(target[:5])

print("-" * 50)


# print(iris.data)
# X = iris.data.data[:, [2, 3]]
# y = iris.data.target
#
# # iris.data.target에 저장된 세 개의 고유한 클래스 레이블을 반환
# # 붓꽃 클래스 이름 : Iris-setosa, Iris-versicolor, Iris-virginica는 이미 정수로 저장되어 있음(0, 1, 2)
# print('클래스 레이블 : ', np.unique(y))
#
# # 훈련된 모델 성능을 평가하기 위한 데이터셋을 훈련 데이터셋과 테스트 데이터셋으로 분할
# # 30%는 테스트 데이터, 70%는 훈련 데이터
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
# print('y의 레이블 카운트 :', np.bincount(y))
# print('y_train의 레이블 카운트 :', np.bincount(y_train))
# print('y_test의 레이블 카운트 :', np.bincount(y_test))

























