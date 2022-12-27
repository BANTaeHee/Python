'''
    1. matplotlib
        1) 시각화 도구
        2) 서브 모듈 pyplot
            - 핵심적인 함수들, 클래스 정의
'''
import matplotlib as mpl
import  matplotlib.pyplot as plt            # 그림을 그리기 위한 pyplot 서브 모듈을 가져오는 작업

# plt.plot([1,2,3,4])
plt.plot([0,1,2,3], [1,2,3,4])
plt.ylabel('y label')
plt.xlabel('x label')
# plt.show()

import numpy as np
x = np.arange(10)           # 0에서 9 사이의 정수값을 생성함
plt.plot(x**2)              # x^2 함수를 그림
# plt.show()

x = np.arange(10)
plt.plot(x**2)
plt.axis([0, 100, 0, 100])          # 범위를 지정함
# plt.show()                          # x 값이 증가할 경우 y값이 매우 가파르게 증가하는 형태의 모양 확인

x = np.arange(-20, 20)                # -20에서 20 사이의 수를 1의 간격으로 생성 (다차원 배열)
y1 = 2 * x
y2 = (1/3) * x **2 + 5
y3 = -x ** 2 - 5

# 각각 다른 스타일로 그림
# 녹색 실선, 빨간 점선과 세모기호, 파란색 별표와 점선
plt.plot(x, y1, 'g--', x, y2, 'r^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])        # 그림을 그릴 영역
# plt.show()

x = np.linspace(0,2 * np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
plt.show()