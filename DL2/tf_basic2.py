'''
    1. 텐서 생성
        1) TensorFlow에서의 텐서(tensor)는 기능적으로 넘파이(NumPy)와 매우 유사함
        2) 기본적으로 다차우너 배열을 처리하기에 적헙한 자료구조로 이해할 수 있음
        3) 텐서는 "자동 미분" 기능을 제공함

    2. 텐서 기본 속성
        1) 모양(Shape)
        2) 자료형(data type)
        3) 저장된 장치
'''
import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.python.client import device_lib

# 구체적으로 사용 중인 장치(device) 정보 출력
x = device_lib.list_local_devices()
# print(x)

data = [
    [1, 2]
    , [3, 4]
]

x = tf.constant(data)
print(x)
print(tf.rank(x))  # 차원 출력 (axis 개수)
print("----------------------------------------------------------------------")

data = tf.constant("ezen string")
print(data)
print("----------------------------------------------------------------------")

a = tf.constant([5])
b = tf.constant([7])
print(a)
print(b)
print("----------------------------------------------------------------------")

c = (a + b).numpy()
print(c)
print(type(c))

result = c * 10
tensor = tf.convert_to_tensor(result)
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")

x = tf.constant([
    [5, 7]
    , [1, 2]
])

# x와 같은 모양과 자료형을 가지지만, 값이 1인 텐서 생성
x_ones = tf.ones_like(x)
print(x_ones)

# x와 같은 모양을 가지되, 자료형은 float으로 덮어쓰고, 값은 랜덤으로 채우기
x_rand = tf.random.uniform(shape=x.shape, dtype=tf.float32)
print(x_rand)
















