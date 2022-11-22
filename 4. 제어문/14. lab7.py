'''
    사용자로부터 국어, 수학, 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80점 이상이면 합격입니다.
    그런데 프로그램의 오류가 발생하여
    80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해 보시오.
    (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력했습니다."를 출력하시오)
    Ex.
        국어 >>>
        수학 >>>
        영어 >>>

        불합격             합격              잘못 입력했습니다.

'''

#방법 1

kor = int(input("국어 >>> "))
math = int(input("수학 >>> "))
en = int(input("영어 >>> "))

subject_num = 3

sum = kor + math + en
avg = sum/subject_num

if 0 <= kor <= 100 and 0 <= math <= 100 and 0 <= en <= 100:
    if avg >= 80:
        print("불합격입니다.")
    else:
        print("합격")
else:
    print("잘못 입력했습니다.")


# 방법 2
'''
if kor < 0 or kor > 100 or math < 0 or math > 100 or en < 0 or en > 100:
    print("잘못입력했습니다.")
elif aㅍg >= 80:
    print("불합격")
else:
    print("합격")
'''
