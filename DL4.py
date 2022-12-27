'''
    1. 인공지능 : 인간처럼 학습하고 추론하는 프로그램 연구
       머신러닝 : 인공지능의 한 분야, 스스로 학습하는 프로그램 연구

       딥러닝(Deep Learning) : 인공신경망 사용하여 빅데이터로부터 학습하는 프로그램 연구
       1) 신경망 (Neural Network)은 1950년대부터 연구됨
       2) 최근의 인공지능 붐은 전적으로 딥러닝의 성공 때문임
       3) 많은 레이어(layer)가 있는 신경 회로망을 사용하여 데이터의 추상화를 모델링하는 기계 학습의
          한 분야임.

    2. 인공지능 역사
        1) 탐색의 시대
        2) 지식의 시대
        3) 학습의 시대
            - AI의 부활
            - 자율 주행 자동차
            - 광고 (추천 시스템)
            - 챗봇
            - 의료분야, 진단
            - 언어 번역(자연어 처리)
            - 경영 분야(빅데이터 -> 인공지능 -> 경영의사결정)
            - 딥러닝 예술( 화풍 모방)
            - 음악

    3. 신경망
        1) 인공 신경망(artificial neural network : ANN)
            - 생물학적인 신경망에서 영감을 받아서 만들어진 컴퓨팅 구조임
                - 인간의 뇌 구조 모방
            - 장점
                - 학습이 가능함 (데이터가 주어지면 신경망은 배울 수 있음)
                - 몇 개의 소자가 오동작하더라도 전체적으로 큰 문제가 발생하지 않음

    4. 퍼셉트론(perceptron)
        1) 생물학적 뉴런을 모방하여 만든 인공 신경망의 기본 단위
            이전 perceptron과 연결 ==> inputs    weights     input function      activation function     output ==> 다음

        2) activation function(활성화 함수)
            - 입력 신호의 가중치의 함이 어떤 임계값을 넘는 경우에만 뉴런이 활성화되어서 1을 출력함.
              그렇지 않으면 0을 출력함
            - if (w1x1 + w2x2 + b >= 1) ==> 1
              otherwise ==> 0
            - 계단(step) 함수

        3) 논리 연산을 하는 퍼셉트론
            x1          x2          y(X1 AND X2)        y(X1 OR X2)         y(X1 XOR X2)
            0           0                0                   0                   0
            0           1                0                   1                   1
            1           0                0                   1                   1
            1           1                1                   1                   0

        4) AND / OR 연산
            - 각 표본의 입력에 대한 출력값을 X-Y 평면 표시
            - 서로 다른 두 그룹을 구분하기 위해 선형 분류자 1개 필요
            - XOR 연산의 경우는 하나의 선형 분류자로 두 그룹을 분류 불가


'''
import numpy as np

epsilon = 0.0000001                     # 부동소수점 오차를 방지하기 위함

def perceptron(x1, x2):
    w1, w2, b = 1.0, 1.0, -1.5
    sum_ = w1 * x1 + w2 * x2 + b
    if sum_ > epsilon:
        return 1
    else:
        return 0

print(perceptron(0,0))
print(perceptron(0,1))
print(perceptron(1,0))
print(perceptron(1,1))