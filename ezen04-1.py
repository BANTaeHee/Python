# ezen04-1
# 파이썬 데이터 타입 (자료형)
# 리스트, 튜플
# 리스트는 대괄호 안에 원소들을 쉼표로 구분해서 넣을 수 있음
# 리스트 - 가변(mutable),           문자열은 불변(immutable)

odds = [1, 3, 5, 7, 9]
print(odds)

# 일반적으로 리스트의 각 원소는 같은 자료형이 되도록 쓰이지만, 서로 다른 자료형의 데이터가 들어갈 수 있음
data = ["Hello", 7, 0.5]
print(data)

# 리스트에 대하여 인덱싱과 슬라이싱을 사용 가능함
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(evens[3])     # 4번째 원소
print(evens[0:5])   # 1번째 원소부터 5번째 원소까지 

# 리스트 덧셈 : 리스트끼리 더할 수 있는데, 단순히 두 리스트를 이어 붙인 결과가 반환됨
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(a+b)

# 리스트 중첩 
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# 리스트 전체 출력
print(arr)
#1행 2열의 원소 출력
print(arr[0][1])
#3행 3열의 원소를 출력
print(arr[2][2])


# 메서드 
'''
    insert(삽입할 인덱스, 삽입할 원소)
    append(삽입할 원소)
    remove(삭제할 원소)
    sort()
'''
arr = [1, 3, 4]
print(arr)

# 인덱스 1의 위치에 원소 3를 삽입하시오 
arr.insert(1, 2)
print(arr)

# 마지막 위치에 5를 삽입하시오.
arr.append(5)
print(arr)

# 원소 3을 제거하시오 
arr.remove(3)
print(arr)

# 내림차순으로 정렬하시오 
arr.sort(reverse=True)
print(arr)


arr = [] 
for x in  range(10):
    arr.append(x)

print(arr)

arr = []
row1 = [1, 2, 3, 4, 5]
arr.append(row1)
print(arr)

row2 = [6, 7, 8, 9, 0]
arr.append(row2)
print(arr)

# 리스트 컴프리핸션 (2차원 이상의 리스트 초기화할 때 사용)
# 원소를 8개 포함한는 1차원 리스트 초기화
arr = [5] * 8
print(arr)

# 4 X 5 크기를 갖는 2차원 리스트 초기화 
arr = [[0] * 5 for _ in range(4)]
print(arr)

# 4 X 5 크기를 갖는 2차원 리스트 초기화 
arr = [[i] * 5 for i in range(4)]
print(arr)

# 4 X 5 크기를 갖는 2차원 리스트 초기화 
arr =[[(i * 5) + j for j in range(5)] for i in range(4)]
print(arr)



