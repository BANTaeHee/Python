'''
    1. 파이썬 예외 처리
        1) 예외(exception) : 코드 실행 도중 발생하는 오류(error)

        2) try:
            기본적으로 실행할 코드
           except:
            예외가 발생했을 때 실행할 코드


'''
try:
    x = 10
    result = x / 0
    print(result)
except:
    print("예외 발생")

print()

arr = [7, 5, 3]
index = 3

try:
    data = arr[index]
    print(data)
except IndexError as e:
    print("배열의 크기를 벗어난 인덱스에 접근할 수 없습니다.")
    print(e)

print()

try:
    data = data_list[index]
    result = data / x
    print(result)
except IndexError as e:
    print("배열의 크기를 벗어난 인덱스에 접근할 수 없습니다.")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print("[오류 메시지 : ]")
    print(e)
















