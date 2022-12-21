'''
    * os 모듈과 예외 처리
        - os.mkdir(폴더)
        - os.path.join(str1, str2) : str1과 str2의 문자열을 연결하여 파일이나 폴더에 대한
                                    전체 경로를 생성해줌
    * 예외처리
        - try : 예외발생 가능성이 있는 코드
        - except : 예외 발생시 처리할 내용
        - finally : 항상 실행될 내용
'''
import os

myfolder = 'C:\\Users\\bever\\OneDrive\\Desktop'
newpath = os.path.join (myfolder, 'hello')

try:
    os.mkdir(path=newpath)

    for idx in range(1, 11):
        newfile = os.path.join(newpath, 'ezenfolder' + str(idx).zfill(2))
        os.mkdir(path=newfile)

except FileExistsError:
    print('디렉터리가 이미 존재합니다.')

print('finished')


