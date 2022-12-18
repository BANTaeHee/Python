'''
    1. 데이터 삭제 : drop()
        - 필요없는 데이터를 삭제
        - 행(index), 열(column) 단위로 삭제
    2. 중복 데이터 삭제 :
        - duplicated() : 데이터 중복 여부를 true, false로 변환
                        keep : 중복이 있다면 처음과 마지막 값 중 어떤 것을 중복이라고 판단 
        - drop_ duplicated() : 중복된 데이터를 삭제 
                        keep : 중복이 있다면 처음과 마지막 값 중 어떤 것을 삭제
'''
import pandas as pd

df = pd.DataFrame({
    'SIZE' : ['L', 'M', 'L', 'S', 'XS'],
    'product_type' : ['Jacket', 'Shirt', 'Jacket', 'Trousers', 'Shirt'],
    'color' : ['red', 'black', 'black', 'red', 'blue'],
    'quantity' : [5, 15, 10, 20, 15]
})
print(df)
# 열삭제 
print()
print(df.drop(['color'], axis=1))

print()
print(df.drop(['color', 'quantity'], axis=1))

print()
print(df.drop(['SIZE', 'product_type'], axis=1))

print()
# print(df.drop(['SIZE', 'product_type']))

# 행 삭제
print(df)
print()
print(df.drop([0], axis=0))

print()
print(df.drop([0]))

print()
print(df.drop([1, 4]))

print()
print(df)

print()
print(df.duplicated(['product_type'], keep='first'))

print()
print(df.duplicated(['product_type'], keep='last'))

print()
print(df)

print()
print(df.drop_duplicates(['product_type'], keep='first'))

print()
print(df)

print()
print(df.drop_duplicates(['product_type'], keep='last'))