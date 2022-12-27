'''
    1. 파이선 리스트 & 넘파이
        1) 넘파이 배열
            - 형상 (shape) : 차원의 크기를 지정하는 정수의 튜플
                - Ex. (3, 3)
            - 축 (axis) : 차원
                - axis = 1 (컬럼)
                - axis = 0 (행)

            - shape : (3, )    <== 1d 배열
                - 2, 3, 4
                    axis = 0 (행)
            - shape: (2, 3)     <== 2d 배열
                - 2 3 4
                  6 7 8
                    axis = 0 (행)
                    axis = 1 (컬럼)
            - shape: (4, 3, 2)      <== 3d 배열
                - 2 3 4
                  6 7 8
                  2 3 4
                  6 7 8
                            2 3 4
                            6 7 8
                            2 3 4
                            6 7 8
                    axis = 0
                    axis = 1
                    axis = 2
        2) 넘파이의 핵심은 다차원 배열(ndarray)임
        3) 리스트와 넘파이의 가장 큰 차이는 계산 성능임
            - 넘파이는 대용량의 배열, 행령 연산 수행 함수를 포함, 성능 우수
        4) 파이썬의 리스트
                - 동일하지 않은 자료형을 가진 항목들을 담을 수 있음.
                - 단순히 여러 데이터가 나열된 것
           넘파이는 ndarray 객체
                - 동일한 자료형의 항목들만 저장함
                - 넘파이는 배열을 선형대수의 벡터 개념으로 다룸
        5) 넘파이는 강력한 배열 프로그래밍 기능이 넘파이가 인기있는 이유임.
            - 스칼라(scalar) 언어의 for문
                - 각각의 원소들을 순차적으로 처리해야 함
            - 데이터 병렬성 방식
                - 데이터를 잘게 쪼개어 각각에 대해 동일한 연산을 독립적으로 수행하는 방식
                - 그래픽 처리 장치(GPU)는 고성능 데이터 병렬 처리기로 현재 슈퍼컴퓨팅 차원에서 적극 활용됨\
                - SIMD(Single instruction multiple data) : 하나의 연산이 다수의 데이터에 동시에 적용되는 방식(CPU)
                - 벡터화 연산
                    - 프로그래머가 효율적으로 고성능의 데이터 병렬 처리를 할 수 있게 해줌
                    - 계산 시간은 대략 20배 정도 단축됨.
'''
import numpy as np

a = np.array([2, 3, 4])
print(a.shape)      # a 객체의 형상
print(a.ndim)       #         차원
print(a.dtype)      # 요소의 자료형
print(a.itemsize)   # 요소의 크기(byte)
print(a.size)       # 요소의 수

print()

store_a = [20, 10, 30]      # 파이썬 리스트 (매장 A의 매출)
store_b = [70, 90, 70]      # 파이썬 리스트 (매장 B의 매출)

# 월별 매출 합을 구하기
list_sum = store_a + store_b

print(list_sum)     # 리스트를 이루는 원소들의 인덱스가 특별한 의미를 갖지 않음 (단순히 리스트내의 순서만 나타냄)

print()

# 넘파이 곱셈
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([[2, 2], [2, 2], [2, 2]])

result = arr1 * arr2
print(result)

print()

# 넘파이 행렬 곱셈
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[2, 2], [2, 2], [2, 2]])

# result = arr1 @ arr2
result = arr1.dot(arr2)
print(result)









