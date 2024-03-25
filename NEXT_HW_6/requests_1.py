from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from openpyxl import Workbook

url='https://printbakery.com/product/list.html?cate_no=238&sort_method=6#Product_ListMenu'

try:
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html_text = response.text
        
        soup = bs(response.text, 'html.parser')
        
        artist_names=soup.find_all(class_='artist fs-14 fw-500')
        artist_names = list(map(lambda x: x.text.strip(), artist_names))
        print(artist_names)
        
        product_names = soup.select('.name')
        product_names=list(map(lambda x: x.text.strip(), product_names))
        print(product_names)
        
        prices = soup.select('.price.list')
        prices=list(map(lambda x: x.text.strip(), prices))
        print(prices)
        
        #phase2 : 엑셀에 저장
        wb = Workbook() #새 엘셀 워크북 생성
        ws = wb.active #워크북의 활성 시트에 접근
        
        ws.append(['작가 이름', '작품 이름', '가격']) #첫 행에 열 제목 추가
        
        #순회하며 엑셀시트에 추가
        for artist_name, product_name, price in zip(artist_names, product_names, prices):
            ws.append([artist_name, product_name, price])
        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'printbakery_{today}.xlsx'
        wb.save(filename) #엑셀 저장
        print(f'엑셀 파일 저장 완료: {filename}')
    else:
        print(f'Error: HTTP 요청 실패. 상태 코드: {response.status_code}')
        
except requests.exceptions.RequestException as e:
    print(f'Error: 요청 중 오류 발생. 오류 메세지: {e}')
