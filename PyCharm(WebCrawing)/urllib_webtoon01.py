'''
    * 크롤링
        1) urllib 라이브러리 이용한 웹 페이지 크롤링
            - urllib.request 모듈
                - url을 열어서 내용을 읽어 들이는 모듈
                - 웹을 통하여 데이터를 요청하는 기능
                - http 클라이언트의 인터페이스를 위한 함수 및 클래스 제공함
                    - urlretrieve(url, savename) : url을 savename이라는 이름의 파일로 다운로드함

'''
import urllib.request               # 라이브러리 읽어들임.

# url과 저장 경로 지정하기
url ="https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg"
savename = "urldownload_webtoon01.png"

# 다운로드
urllib.request.urlretrieve(url,savename)

print('웹이 있는 이미지'+ url+ '를', end='')
print(savename + "파일로 저장하였습니다.")
