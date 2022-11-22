'''
    턱걸이 평균 측정 프로그램을 만들어 보시오
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
    그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장하시오
    리스트에 저장된 데이터의 평균을 구해 출력하시오

    Ex.
        1일차 턱걸이 횟수 >>>
        2일차 턱걸이 횟수 >>>
        3일차 턱걸이 횟수 >>>
        4일차 턱걸이 횟수 >>>
        5일차 턱걸이 횟수 >>>
        6일차 턱걸이 횟수 >>>
        7일차 턱걸이 횟수 >>>

        턱걸이 평균 횟수 = 22개

'''
# 빈 리스트 생성
pull_up = []

x = int(input("1일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
pull_up.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
pull_up.append(x)

total = pull_up[0] + pull_up[1] + pull_up[2] + pull_up[3] + pull_up[4] + pull_up[5] + pull_up[6]
avg = total / 7

print("턱걸이 평균횟수 >>> ", int(avg))