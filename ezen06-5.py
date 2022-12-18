# ezen06-5
'''
    6) Dataframe
        - index 행
        - columns 열
        - 데이터 선택 (slicing)
            - 데이터 위치를 활용한 데이터 가공 : loc(), iloc()
        - 데이터 삭제 (drop)
            - 필요없는 데이터 삭제
            - 행(index), 열(columns) 단위로 삭제
        - 중복 데이터 삭제 (duplicated(), drop_duplicates())

'''

import pandas as pd

df = pd.DataFrame()
print(type(df))

stu_list = [['Susan', 'Jessica', 'John', 'Michael'], [19, 15, 16, 17]]
print(stu_list)

df = pd.DataFrame(stu_list)
print(df)

df = df.T
print(df)

colums_name = ['name', 'age']
df.columns = colums_name
print(df)


'''
    "I am quitting this exam."
    "This is the quickest approach I ever seen"
    "The king should make quick dscision"

    문장을 입력하다가 'q'라고 작성을 하였습니다.
    원래는 'w'를 작성해야했습니다. 

    주어진 문장들을 모두 맞게 변경하시오.(replace())

    "I am wuitting this exam."
    "This is the wuickest approach I ever seen"
    "The king should make wuick decision"

'''
# 리스트 

sentences_list = ["I am quitting this exam.", "This is the quickest approach I ever seen", "The king should make quick decision"]
for sentence in sentences_list:
    print(sentence.replace("w", "q"))

# 주어진 문장들에 대해서 몇 개의 단어가 있는지 출력하시오. (split())
# 5
# 8
# 6

sentences_list = ["I am quitting this exam.", "This is the quickest approach I ever seen", "The king should make quick decision"] 
for sentence in sentences_list:
    print(len(sentence.split()))


'''
    차범근 축구감독이 미래 축구 꿈나무를 선발하여 축구부를 만듭니다. 
    키가 175cm 이상인 사람들을 뽑아서 축구부를 결정합니다. 
    soccer_team이라는 빈 리스트를 작성하여, 축구부가 될 사람들의 이름만 추가하는 코드를 작성해 보시오.
'''
candidates = {"이순신": 146, "이도": 160, "유성룡": 167, "정철": 175.3, "이황": 207}
soccer_team = []

for name, height in candidates.items():
    if height >= 175:
        soccer_team.append(name)

print(soccer_team)
print()

soccer_team2 = [name for name, height in candidates.items() if height >=175]
print(soccer_team2)

# 구구단 출력 for 문
'''
    중괄호를 이용해서 format 함수에서 넣어줄 것들을 표기 해줍니다.
    인덱스는 0 부터 시작합니다. 이렇게 표시를 해주고 .format 함수의 인자로 순서대로 넣을 변수들을 지정해 줍니다.
    
    {인덱스0}, {인덱스1}'.format(값0, 값1)
'''
for num2 in range(1,10):
    for num1 in range(2, 10):
        print("{} x {} = {}".format(num1, num2, num1*num2), end = "\t")
    print()


print()
# 구구단 가로 출력(while문 출력)
num2 = 1
while num2 < 10:
    num1 = 2
    while num1 < 10:
        print("{} x {} = {}".format(num1, num2, num1*num2), end = "\t")
        num1 += 1
    print() 
    num2 +=1


'''
    얼마나 시간이 걸리고 개수가 몇개인지 확인하시오
    - for문 이용하여 1부터 1000000까지의 숫자 중에서 3의 배수인 숫자들을 찾고, 몇 개 있는지 알아보자. 
    - 이 코드를 수행하는데 걸린 시간을 확인해보자
'''
import time
start = time.time()

ls = []

for num in range(1, 1000000+1):
    if num % 3 == 0:
        ls.append(num)

end = time.time()
print(f"소요시간 : {end - start}")
print(f"리스트 원소 개수 :  {len(ls)}개")

# 앞서 구구단은 얼마나 시간이 걸릴까요?
import time
start = time.time()

for num2 in range(1,10):
    for num1 in range(2, 10):
        print("{} x {} = {}".format(num1, num2, num1*num2), end = "\t")
    print()

end = time.time()
print(f"소요시간 : {end - start}")

'''
    도준이가 5000원 이상 소지하고 있을 경우 택시를 타고 집에 귀가할 수 있지만,
    걸어서 귀가할 수도 있습니다.
    택시를 탈 경우, 3000원이 소비됩니다. 잔액을 표시하시오.

    2000원 이상 있을 경우 버스를 타고 귀가할 수 있습니다. 
    버스를 탈 경우, 1000원이 소비됩니다. 

    2000원 미만일 경우 걸어서 귀가할 수 있습니다. 
    위 조건을 반영하는 코드를 작성하시오.
'''
money = 5000
taxi = True

if money >= 5000:
    if taxi:
        print("택시를 탑니다.")
        print(f"잔액 : {money - 3000}원")
    else:
        print("걸어서 귀가합니다.")
elif money >= 2000:
    print ("버스를 탑니다.")
    print(f"잔액 : {money - 1000}원")
else:
    print("걸어서 귀가합니다.")

'''
    도준이가 택시에 내려서 걸어서 귀가하던 중,
    집 근처 오락실에서 '철권' 게임을 하고 싶어졌습니다. 
    회당 500원인 이 게임을 몇번이나 할 수 있을까요?

    매번 게임을 진행한 후 가지고 있는 잔액과 몇 번 게임을 했는지 횟수를 출력하는 코드를 작성하시오.

    Ex.
    현재까지의 게임한 횟수는 :
    현재 잔액 :

    최종 게임 횟수 :
    최종 잔액 :
'''
money = 7000
counts = 0

while money > 0 : 
    counts += 1             
    money -= 500

    print(f"현재까지의 게임한 횟수는 : {counts}")
    print(f"현재 잔액 : {money}")

print()
print("최종 게임 횟수 : {counts}")
print(f"최종 잔액 : {money}")