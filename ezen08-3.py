
page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

import requests 
source = requests.get(page_url).text

import bs4 
source = bs4.BeautifulSoup(source)

dates =  source.find_all('td', class_ = 'date')
#print(dates)
#print(dates[0])
#print(dates[0].text)

date_list = []

# 날짜 크롤링 
for date in dates:
    date_list.append(date.text)

print(date_list) 

# 체결가 추출
prices = source.find_all("td", class_= "number_1")


print(prices[::4])

price_list = []

for price in prices[::4]:
    price_list.append(price.text)

print(price_list)

#print(len(date_list))
#print(len(price_list))

# /html/body/div/table[1]/tbody/tr[3]/td[2]
result = source.find_all("td", class_= "pgRR")[0]
print(result)

last_url = source.find_all("td", class_= "pgRR")[0].find_all("a")[0]["href"]
print(last_url)

result = last_url.split('&page=')
print(result)

last_page = last_url.split('&page=')[-1]
print(last_page)

last_page = int(last_url.split('&page=')[-1])
print(last_page)


