# ezen06-3
'''
    4) 튜플(Tuple) 자료형
        - 리스트와 비슷
        - 대괄호([])가 아닌 ()
        - 리스트는 추가/수정/삭제할 수 있지만, 듀플은 추가/수정/삭제 불가 
       집합(set) 자료형
        - 튜플과 비슷하지만 ()가 아닌 set()
        - 순서가 없고, 중복을 허용하지 않음


                        리스트(list)                   튜플(Tuple)                     집합(Set)
    -------------------------------------------------------
     문법            age = [19, 15, 16, 17]      age = (19, 15, 16, 17)      age = set([19, 15, 16, 17])    

추가/수정/삭제              가능                          불가                           가능
     
     순서                   있음                          있음                           없음
                           age[0]                        age[0]

     중복                   가능                          가능                           불가

'''
list_age = [19, 15, 16, 17] 
tuple_age = (19, 15, 16, 17) 
set_age = set(set_age, type(set_age))

print(list_age, type(list_age))
print(tuple_age, type(tuple_age))
print(set_age, type(set_age))

print(list_age[0])
print(tuple_age[0])
# print(set_age[0])

print(list(set_age))
print(tuple(set_age))