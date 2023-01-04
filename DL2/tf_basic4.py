'''
    5) 텐서의 모양 변경
        - reshape() : 텐서의 모양을 변경할 때 사용
            - 이때 텐서(tensor)의 순서는 변경되지 않음

    6) 텐서의 차원 교환
        - 하나의 텐서에서 특정한 차원끼리 순서를 교체할 수 있다.

'''
import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



a = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
print(a)
b = tf.reshape(a, (4, 2))
print(b)

print("-------------------------------------------------")

# a와 b는 서로 다른 객체
a.assign_add([1, 1, 1, 1, 1, 1, 1, 1])
print(a)
print(b)

print("-------------------------------------------------")

a = tf.random.uniform((64, 32, 3))
# print(a)
print(a.shape)

print("-------------------------------------------------")

b = tf.transpose(a, perm=[2, 1, 0])     # 차원자체를 교환
# (2번째 축, 1번째 축, 0번째 축)의 형태가 됨
print(b)
print(b.shape)









