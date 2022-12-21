from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = 'https://comic.naver.com/webtoon/weekday'

# 페이지에 데이터를 가져옴
response =urlopen(myurl)
print(type(response))

# BeautifulSoup()를 이용해서 데이터를 파싱함
soup = BeautifulSoup(response, 'html.parser')

# BeautifulSoup 객체를 들여쓰기 형태로 출력
# print(soup.prettify())

title = soup.find("title").string
print(title)