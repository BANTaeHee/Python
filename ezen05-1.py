# ezen05-1
# 파이썬 흐름제어 (제어문)
# 조건문, 반복문

#1. 두 개의 숫자 a, b에 원하는 숫자를 넣고 a가 b의 배수인지 확인하는 코드를 작성하시오. 
# 배수라면 "a는 b의 배수입니다." 를 출력하고, 그렇지 않다면 "a는 b의 배수가 아닙니다."를 출력하시오.

a, b = 100, 6;

if a % b == 0:
    print("%d는 %d의 배수입니다." % (a, b))
else:
    print("%d는 %d의 배수가 아닙니다." % (a, b) )



'''
    머신러닝에서는 모델이 학습을 하게 되면, 학습에 주어진 인자들을 가지고 어떤 결과가 나왔는지 출력을 하게 됩니다.
    주어진 인자를 해당하는 자리에 위치하는 출력문을 작성하시오.
    아래는 출력문의 예시입니다. 

    - Ezen777 모델로 10 epoch를 반복 학습시킨 결과는 학습 정확도 : 0.85, 검증 정확도 : 0.83, 테스트 정확도 : 0.76으로 나왔습니다. 

'''
# 다음 주어진 변수를 활용하여 코드를 작성하시오.
epoch = 10 
train_accuracy = 0.85
val_accuracy = 0.83
test_accuracy = 0.76
model_name = "Ezen777"

# case1 
print(f"{model_name} 모델로 {epoch} epoch를 반복 학습시킨 결과는 학습 정확도 : {train_accuracy}, 검증 정확도 : {val_accuracy}, 테스트 정확도 : {test_accuracy}으로 나왔습니다.")

# case2
print("{} 모델로 {} epoch를 반복 학습시킨 결과는 학습 정확도 : {}, 검증 정확도 : {}, 테스트 정확도 : {}으로 나왔습니다.".format("Ezen777",10,0.85,0.83,0.76))

# case3
print("%s 모델로 %d epoch를 반복 학습시킨 결과는 학습 정확도 : %.2f, 검증 정확도 : %.2f, 테스트 정확도 : %.2f으로 나왔습니다." %("Ezen777",10,0.85,0.83,0.76))


'''
    어떤 반의 학생 5명의 키에 대한 정보가 주어집니다. 
    이를 리스트로 만들고 height라는 변수에 저장하시오.
    167, 160, 175.5,184, 170
'''
heights = [167, 160, 175.5, 184, 170]
print(heights)

# 학생 5명의 키가 작은 순부터 큰 순서로 정렬하여 출력하시오.
heights.sort(reverse=False)
print(heights)

# 위에서 만든 리스트의 데이터 타입을 확인해 보시오.
print(type(heights))

# 위의 리스트의 데이터 길이를 출력하시오.
print(len(heights))

# 학생들 중 키가 제일 컸던 학생이 전학을 가게 되었습니다. 이를 코드로 구현하시오.
# 위의 리스트의 데이터 길이를 출력하시오

heights.remove(184)
print(heights)
print(len(heights))

'''
    전학을 갔던 친구보다 더 키가 큰 순신이 라는 친구가 전학을 왔습니다. 
    이 친구의 키는 200cm 입니다. 
    이를 반영하여 코드를 구현하시오. heights의 길이를 구하시오.
'''
heights.append(200)
print(heights)
print(len(heights))

'''
학교에서 더이상 전학을 받지도, 보내지도 않기로 결정을 하였습니다. 
키 데이터의 값이 더 이상 변경되지 않기를 원합니다.
리스트의 값을 변경할 수 없게 코드를 작성하시오.
'''
heights = tuple(heights)
print(heights)
print(type(heights))

'''
    5명의 학생들의 키는 있지만, 누구의 키인지 알 수 없습니다. 
        최선혜(160), 전수정(167), 이규황(170), 반태희(175.5), 이경빈(200)
    데이터 타입 중 Dictionary로 위처럼 이름(name-key)과 키(height-value)를 같이 붙여주려고 합니다.
    이를 코드로 작성해서 class-A라는 변수에 저장하시오.
'''
class_A = {"최선혜" : 160, "전수정" : 167, "이규황" : 170, "반태희" : 175.5, "이경빈" : 200}
print(class_A)
print(type(class_A))
print(class_A["반태희"])

'''
    주어진 리스트의 평균을 계산하는 코드를 작성하시오.

'''
grade = [65, 70, 100, 43, 50]
avg = sum(grade)/len(grade)
print(avg)

'''
    주민등록번호들의 뒤에 6자리를 가려주는 코드를 작성하시오.
    911209-1234567 => 911209-1******
'''
ezen_man = "911209-1234567"
ezen_woman = "201210-2519860"
ezen_man2 = "891209-3234567"
ezen_woman2 = "041210-4519860"


print(ezen_man[:-6] + "******")
print(ezen_woman[:-6] + "******")
print(ezen_man2[:-6] + "******")
print(ezen_woman2[:-6] + "******")

print()
ezen = [1, ['a',2], 3.14, "누구세요?"]
print(ezen)

# ezen의 index2부터 끝까지 잘라내기를 하시오
print(ezen[2:])

print(ezen[-1])


# ezen 원소 중 'a'를 출력해 보시오

print(ezen[1][0])

# 리스트에서 제공하는 함수들이 무엇이 있는지 확인하세요
print(type(ezen))
print(dir(ezen))






