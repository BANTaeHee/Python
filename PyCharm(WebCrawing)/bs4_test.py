from bs4 import BeautifulSoup

html = open("fruits.html", "r", encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
body = soup.select_one("body")         # 객체.select_one(<선택자>) : css 선택자로 요소 하나를 추출함
ptag = body.find('p')          # 객체.find(tag[, attributes]) : tag라는 태그 중 조건에 맞는 1번째 태그를 찾아줌

print('1번째 p태그 : ', ptag)
print('1번째 p태그 : ', ptag['class'])




