'''
    1. 사이킷런을 이용한 선형 회귀
        1) scikit-learn
            - 2007년 구글 코드 프로젝트 모임에 개발자 중심이 되어 시작된 라이브러리
            - 지도 학습, 비지도 학습을 위한 다양한 모델을 제공
            - 시각화 도구, 검증 도구 기능 제공
        2) 머신러닝
            - 특성(features)과 레이블로 이루어진 데이터
                - 특성 : 관찰되는 현상에서 측정할 수 있는 개별적인 속성
                - 이 특성을 입력으로 사용하여 학습한다는 것을 의미함
                    - 사람의 키, 몸무게, 개의 길이, 높이, 주택 가격, 주택 면적
            - 데이터를 바탕으로 동작이 결정되는 모델
                - y = f(x)
            - 모델을 위한 적절한 하이퍼파라미터(hyperparameter)
            - 학습을 위한 훈련
            - 검증

    2. 선형 회귀 모델의 계수와 절편
        - 가장 간단한 모델로 이차원 평면상에 있는 직선 방정식
            - y = mx + b
                - m : 직선의 기울기, 입력 변수 x에 곱해지는 계수(coefficient)임
                - b : x와 관계없이 y에 영향을 주는 값, 절편(intercept)임
                      회귀선을 위 또는 아래로 얼마나 평행이동 시킬지 결정함
        - 선형 회귀 알고리즘
            - 데이터를 설명하는 가장 적절한 기울기와 절편값을 찾는 것임.

        - 2개 이상의 변수가 있는 경우까지 확장될 수 있음. 다중 회귀분석이라고 함.
            - 종속변수 y는 여러 독립변수에 종속됨
            - 2차원 공간에서 선형 회귀 모형은 직선이고,
              3차원에서는 평면임.
            - 평면을 선형 회귀로 찾은 결과임.
            - p + 1개의 독립변수가 포함된 다중 회귀분석 모델
                - y(w,x) = w0 + w1x1 + ... + wpxp
                    - w와 x는 모두 벡터
                    - 계수 : w1, ... , wp
                    - 절편 : w0

'''

import numpy as np
# 사이킷런을 코드에 가져오기 위해서 sklearn이라는 이름으로 가져와야 함
# 선형 회귀를 구현하기 위해서 linear_model을 import 함
from sklearn import linear_model

# LinearRegression() 생성자를 통해 선형 회귀 모델(객체)을 생성함
regr = linear_model.LinearRegression()

# 입력 데이터 집합 x
X = [[163], [179], [166], [169], [171]]         # 입력 데이터(2차원 리스트)
y = [53, 63, 57, 56, 58]                        # 정답
regr.fit(X, y)                                  # 데이터 사용하여 훈련(학습)하기

# 직선의 기울기
coef = regr.coef_                   # regr 모델의 coef_ 속성값으로 얻음
# 직선의 절편
intercept = regr.intercept_         # regr 모델의 intecept_ 속성값으로 얻음

score = regr.score(X, y)            # score() 함수를 통해서 이 모델의 점수 구함

#
print("y= {} * x + {:.2f}".format(coef.round(2), intercept))
print("데이터와 선형 회귀 직선의 관계 점수 : {:.1%}".format(score))

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))

# 학습 데이터와 y값을 산포도로 그리기
plt.scatter(X, y, color='blue', marker='D')
y_pred = regr.predict(X)            # 학습 데이터를 입력하여 예측값을 계산함
plt.plot(X, y_pred, 'r:')           # 계산된 기울기와 y절편을 가지는 점선 그리기

fig.savefig("LinearRegression_result.png")

# 167인 순신이의 키를 넣어서 그 추정값을 출력하기
sunsin = [[167]]
result = regr.predict(sunsin)
print('순신이의 키가 {}cm 이므로 몸무게는 {}kg으로 추정됨.'.format(\
                    sunsin, result.round(1)))






















