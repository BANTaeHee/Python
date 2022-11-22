# 비만도 계산기를 만들어 보시오

'''
Ex)
    BMI 계산기 입니다.
    신장 : (입력)
    체중 : (입력)
    BMI :
'''
print("BMI 계산기 입니다.")
height = int(input("신장 : >>> "))
weight = int(input("체중 :  >>> "))
BMI = weight / (height**2) *10000

print("BMI : ", BMI)

if BMI <= 18.5:
    print("저체중입니다.")
elif BMI <= 23:
    print("정상입니다.")


