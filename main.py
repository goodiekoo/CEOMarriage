from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색할 CEO 이름 (반드시 영문):') #코드 테스트용, 최종버전에서는 csv 파일을 자동으로 읽어서 처리할 예정
url = baseUrl + quote_plus(plusUrl)
#url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser") #parser로 지정해줘야함

#selenium 그대로 사용 코드인데 결과가 안나옴
r = soup.select('.r')
for i in r:
    print(i.select_one('.ellip').text)
    print(i.select_one('.iUh30.bc').text)
    print(i.a.attrs['href'])
    print()

#사용 안함
#r = soup.select('GLI8Bc UK95Uc')

#for i in r:
#    print(i.select_one('.ellip').text)
#    print(i.select_one('.LC20lb MBeuO DKV0Md').text)
#    print(i.a.attrs['href'])
#    print()

driver.close()