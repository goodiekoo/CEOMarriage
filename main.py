import bs4
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input('검색할 CEO 이름 (반드시 영문):')
#base_url = 'https://www.linkedin.com/search/results/people/?keywords='
#base_url = 'https://www.google.com/search?q='+''.join(sys.argv[1:]))  #구글은 별도 검색 url 따와야함
#코드 테스트용, 최종버전에서는 csv 파일을 자동으로 읽어서 처리할 예정

search_url = base_url + keyword

r = requests.get(search_url)

soup = bs4.BeautifulSoup(r.text,"html.parser")

items = soup.select(".api_txt_lines.total_tit")
for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")