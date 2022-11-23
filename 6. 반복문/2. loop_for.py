a =[1, 2, 4, 3, 5]
for i in a:
    print(i, i*2)       #들여쓰기 한 부분이 for문에 걸려있는 부분
print('ezen')

print()

for x in 'hello world':
    print(x, end = " ")

print()

a = [1, 10, 3, 4, 5]
for num in a:
    if num % 2 == 0:
        print(num/2)
    else:
        print(num+1)
