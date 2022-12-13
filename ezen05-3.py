# 기본 반복문(while, for)
v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

print()

for v2 in range(10):
    print("v2 is : ", v2)

print()

for v3 in range(1, 11):
    print("v3 is : ", v3)

print()

for v4 in range(1, 11, 2):
    print("v4 is : ", v4)

# 1 ~ 100 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(0, 101, 3)))

# 시퀀스 (순서가 있는) 자료형
# 문자열, 리스트, 튜플, 사전, 집합
# iterable 리턴함수 : range(), reversed(), enumerate(), filter(), map()...


#1 
names = ["Ezen1", "Ezen2", "Ezen3", "Ezen4", "Ezen5", "Ezen6"]

for name in names:
    print("You are", name)

print()

#2
word = 'dreams'
for s in word:
    print("word : ", s)

print()


#3
my_info = {
    "name": "Ezen", 
    "age" : 30,
    "city" : "Seoul"
}

for key in my_info:
    print(key, " : ", my_info[key])

for val in my_info.values():
    print(val)

for key, val in my_info.items():
    print(key, val)

print()

#4 
name = "EzenIT"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())