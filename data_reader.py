# 데이터 처리 클래스
import  os
import random
import time

#로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF ']

try:
    from matplotlib import pyplot as plt
except ModuleNotFoundError:
    import  pip

    pip.main('install', 'matplotlib')
    try:
        from matplotlib import pyplot as plt
    except ModuleNotFoundError:
        time.sleep(2)
        from matplotlib import pyplot as plt

try:
    import numpy as np
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'numpy'])
    try:
        import numpy as np
    except ModuleNotFoundError:
        time.sleep(2)
        import numpy as np


class DataReader():
    def __init__(self):
        # 데이터를 저장할 변수들
        self.train_X, self.train_Y, self.test_X, self.test_Y = self.read_data()

        # 데이터 초기화(읽기) 완료 (읽어온 데이터 출력)
        print("\n\n데이터 읽기 완료!")
        print("훈련(Training) X Size : " + str(self.train_X.shape))
        print("훈련(Training) Y Size : " + str(self.train_Y.shape))
        print("테스트(Training) X Size : " + str(self.train_X.shape))
        print("테스트(Training) Y Size : " + str(self.train_Y.shape))


    # 데이터 읽어오기 위한 함수
    def read_data(self):
        # 파일을 실행
        filename = os.listdir("ezen")[0]
        file = open("ezen/" + filename, encoding="utf-8")

        # 헤더를 제거
        file.readline()

        #데이터와 비어있는 리스트 변수
        data = []

        # 파일을 한 줄씩 읽어오기
        for line in file:
            #컴파를 기준으로 split() 실행
            splt = line.split(",")
            # splt 결과물을 정리해 x값 Y값으로 추출하기
            x, compulsory = self.process_data(splt)

            # 추출한 데이터를 리스트에 저장
            data.append((x, compulsory))

            # 학습, 테스트 작업하기전 전체 데이터 섞음
            random.shuffle(data)

            X = []          # 독립변수
            Y = []          # 종속변수 (정답)

            for el in data:
                X.append(el[0])
                Y.append(el[1])

            # 넘파이 배열로 생성함
            X = np.asarray(X)
            Y = np.asarray(Y)

            # 훈련데이터셋 : 테스트데이터셋 = 8 : 2
            train_X = X[:int(len(X) * 0.8)]
            train_Y = X[:int(len(Y) * 0.8)]

            test_X = X[int(len(X) * 0.8):]
            test_Y = X[int(len(X) * 0.8):]

            return train_X, train_Y, test_X, test_Y


    # split() 한값을 정리해서 독립변수, 종속변수 추출하는 메서드
    def process_data(self, splt):
        # 읽어온 splt 값에서 학교, 성별, 키, 몸무게만 추출
        school = splt[9]        # 종속변수
        gender = splt[13]       # 독립변수
        height = float(splt[15]) / 194.2        #독립변수
        weight = float(splt[16]) / 130.7        # 독립변수

        # 추출한 4개 데이터를 저장할 비어있는 리스트 함수
        data2 = []

        # 비어있는 리스트에 키와 몸무게 추가
        data2.append(height)
        data2.append(weight)

        # 성별을 남자일 경우 1, 여자일 경우 0
        if gender == "남":
            data2.append(1)
        else:
            data2.append(0)

        # 초등학교, 중학교, 고등학교 정보를 one hot 벡터값 정리
        # compulsory는 예측값(레이블) 역할 수행함
        if school.endswith("초등학교"):
            compulsory = 0
        elif school.endswith("중학교"):
            compulsory = 1
        elif school.endswith("고등학교"):
            compulsory = 2

        # 추출한 결과물 리턴
        return data2, compulsory



















