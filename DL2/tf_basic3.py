'''
    1. 텐서의 형변환 및 차원 변경
        1) 텐서는 넘파이(NumPy) 배열처럼 조작할 수 있음
        2) 텐서의 특정 차원 접근하기
        3) 텐서의 이어붙이기(concate)
            - 두 텐서를 이어 붙여 연결하여 새로운 텐서를 생성함


'''
import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

tensor = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(tensor[0])        # first row
print(tensor[:, 0])     # first column
print(tensor[..., -1])  # last column
print(tensor[..., -2])  # 텐서의 마지막에서 2번째 요소

print("-----------------------------------------------")

# axis : 축(0, 1)
result = tf.concat([tensor, tensor, tensor], axis=0)
print(result)

print("-----------------------------------------------")

# 1번 축(열)을 기준으로 이어붙이기
result = tf.concat([tensor, tensor, tensor], axis=1)
print(result)

print("-----------------------------------------------")
a = tf.constant([2])
b = tf.constant([5, 0])

print(a.dtype)
print(b.dtype)

# 텐서 a를 float32 형식으로 변경한 뒤에 더하기 수행
print(tf.cast(a, tf.float32) + b)





