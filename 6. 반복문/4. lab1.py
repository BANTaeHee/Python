'''
    구구단 출력 프로그램을 만들어 보시오
    사용자로부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램입니다.

    몇 단을 출력할까요? >>>

    5 * 1 = 5
    5 * 2 = 10
    ...
    5 * 9 = 45

'''

x = int(input("몇 단을 출력할까요? >>> "))
for  i in range(1, 10):
    print(x, "*", i, "=", x*i)
