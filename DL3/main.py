'''
    * 피마 인디언을 대상으로 당뇨병 여부를 측정한 데이터
        1) 피마 인디언 데이터
            - 샘플 수 : 768개
            - 속성 (8개)
                - pregnant (과거 임식 횟수)
                - plasma (공복 혈당 농도)
                - pressure (혈압)
                - thickness (심두근 피부 주름 두께)
                - insulin (혈청 인슐린)
                - bmi (체질량 지수)
                - pedigree (당뇨병 가족력)
                - age (나이)
                - diabetes (당뇨 1, 당뇨 아님 0)
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 피마 인디언 당뇨병 데이터셋 불러오기
df = pd.read_csv('./ezen/pima-indians-diabetes3.csv')

# 처음 10줄 보기
print(df.head(10))

print("------------------------------------------------------")
# 정상과 당뇨 환자가 각각 몇 명인지 확인 (정상만 500명, 당뇨병 환자 268명)
print(df["diabetes"].value_counts())

print("------------------------------------------------------")
# 각 정보별 특징 자세히 출력하기 (샘플수, 평균, 표준편차, 최소값, 백분위 수로 25%, 50%, 75%에 해당하는 값, 최대값)
print(df.describe())

print("------------------------------------------------------")
# 각 항목이 어느 정도의 상관 관계가 있는지 확인
print(df.corr())

print("------------------------------------------------------")
# 그래프로 표현하기
colormap = plt.cm.gist_heat         # 그래프 색상 구성 정하기
plt.figure(figsize=(12, 12))        # 그래프 크기 정하기

# 그래프 속성
'''
    seaborn 라이브러리 중 각 항목 간 상관관계를 나타내는 heatmap() 함수 통계 그래프 표시
    - 두 항목씩 짝을 지은 후 각각 어떤 패턴으로 변화하는지 관찰하는 함수 
    - vmax : 색상의 밝기를 조절하는 인자
    - cmap : 미리 정해진 matplotlib 색상 설정값을 불러옴
    - 숫자가 높을수록 밝은 색상으로 채워져 있음
'''
# sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)
# plt.show()

# plasma를 기준으로 각각 정상과 당뇨가 어느 정도 비율 분포하는지 확인하기
'''
    hist() 함수 안에 x축 지정 (가져올 칼럼)
        - diabetes 값이 0인 것과 1인 것을 구분해 불러옴
        - bins : x축을 몇개의 막대로 쪼개어 줄 것인지 정함 
    => plasma 수치가 높아질수록 당뇨인 경우가 많음
'''
plt.hist(x=[df.plasma[df.diabetes == 0], df.plasma[df.diabetes == 1]], bins=30, histtype='barstacked',
         label=['normal', 'diabetes'])
plt.legend()
plt.show()

# bmi를 기준으로 각각 정상과 당뇨가 어느 정도의 비율로 분포 확인
'''
    BMI가 높아질 경우 당뇨의 발병률도 함께 증가하는 추세임
    평균이나 중앙값으로 대치하거나, 이상치를 제거 과정 등이 데이터 전처리에 포함 가능(성능높임)
'''
# plt.hist(x=[df.bmi[df.diabetes == 0], df.bmi[df.diabetes == 1]], bins=30, histtype='barstacked',
#          label = ['normal', 'diabetes'])
# plt.legend()
# plt.show()

# 피마 인디언 당뇨병 예측

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 세부 정보(독립변수)를 X로 지정
X = df.iloc[:, 0:8]
# 당뇨병 여부(종속변수)를 y로 지정
y = df.iloc[:, 8]

# 모델 설정
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()

# 모델을 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 실행(학습)
# 100번 반복한 결과 약 77%의 정확도를 보이고 있음
model.fit(X, y, epochs=100, batch_size=5)



