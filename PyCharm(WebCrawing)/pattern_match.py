'''
    * 정규 표현식
        1) regular expression
            - 특정한 패턴과 일치하는 문자열을 '검색', '치환', '제거'하는 기능을 지원
            - 정규표현식의 도움없이 패턴을 찾는 작업은 불완전하거나, 작업의 cost가 높음

        2) 정규 표현식 메타 문자 (기호)
            - [문자들] : 대괄호 내의 문자 1개 일치해야 함
            - \d : 숫자 1개에 해당하고, [0-9]와 동일한 표현식
                   d는 decimal을 의미함
            - {n} : 패턴의 반복 횟수가 n번이어야 함

        3) 함수들
            - Boolean match() : 정규식과 매칭이 되는지 검사함
            - Match search() : 정규식과 매칭이 되는지 검사하고 반환값은 match 객체임
            - findall() : 정규식과 매칭되는 모든 문자열을 리스트로 반환함
            - finditer() : 정규식과 매칭되는 모든 문자열을 반복가능한 객체(iterator)로 반환함

        - 문자열 패턴
                                                패턴 비교
            문자열1        ab123           동일한 패턴
            문자열2        cd456               즉, 문자 2개 / 숫자 3개
            문자열3        ef789
            문자열4        abc12           3가지와 다른 패턴
'''
import re

mylist = ['ab123 ','cd456', 'ef789', 'abc12']

# 정규 표현식 작성
regex = '[a-z]{2}\d{3}'         # [a-z]는 알파벳 소문자 중 1개 글자를 선택함

# 패턴 객체 생성
# compile() : 정규 표현식을 컴파일함
pattern = re.compile(regex)

print('# 문자 2개로 시작하고, 숫자 3개로 끝나는 항목')
matchlist = []

for item in mylist:
    if pattern.match(item):
        print(item, ' 은(는) 조건에 적합')
        matchlist.append(item)
    else:
        print(item, ' 은(는) 조건에 부적합')

print('적합한 항목들')
print(matchlist)


































































