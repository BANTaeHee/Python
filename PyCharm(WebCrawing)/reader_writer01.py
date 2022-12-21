'''
    * 파일 입출력
        1) 파일을 읽어 다른 파일에 기록하기
            - 파일_객체 = open(file, mode)
        2) read()
           readline() : 파일 내애서 1줄을 읽어온다.
           readlines() : 파일의 모든 내용을 읽어, 각 라인을 요소로 하는 리스트를 생성함

'''
print('파일을 읽기 모드로 오픈한다.')
myfile01 = open('ezen.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
#print(linelists)
myfile01.close()

total = 0 # 총점
for one in linelists:
    score = int(one)
    total += score


average = total / len(linelists)        # 평균

print('파일을 쓰기 모드로 오픈한다')
myfile02 = open('result.txt', 'wt', encoding='utf-8')
myfile02.write('총점 : ' + str(total) + '\n')
myfile02.write('평균 : ' + str(average))
myfile02.close()

print('작업 완료됨')