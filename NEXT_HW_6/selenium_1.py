from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from openpyxl import Workbook

# chrome web driver의 경로 지정
chromedriver_path ='C:/Users/xiolr/Desktop/NEXT/Session/NEXT_Session_6/chromedriver/chromedriver-win64/chromedriver-win64/chromedriver.exe'
# 데이터 저장할 디렉토리 지정
user_data_dir = 'C:/Users/xiolr/Desktop/NEXT/Session/NEXT_Session_6/chromedriver/datacash'
# web driver에 대한 option 설정
chrome_options = Options()
# 데이터 디렉토리를 chrome option에 추가
chrome_options.add_argument(f'user-data-dir={user_data_dir}')
service = Service(executable_path=chromedriver_path)
# chrome web driver 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)
# web driver에 접속
driver.get('https://www.29cm.co.kr/shop/category/list?category_large_code=291100100&category_medium_code=&sort=')

try:
    wb = Workbook()
    ws = wb.active
    ws.append(['순위', '회사 이름', '제품 이름', '가격'])

    for i in range(1, 51):
        rank = i
        company_name = driver.find_element(By.XPATH, f'/html/body/shop-root/div/section/ui-list-category/div/div/div[3]/ul/li[{i}]/ruler-product-list-large-item/div/a[2]').text
        product_name = driver.find_element(By.XPATH, f'/html/body/shop-root/div/section/ui-list-category/div/div/div[3]/ul/li[{i}]/ruler-product-list-large-item/div/a[1]/div[2]/div[2]').text
        price = driver.find_element(By.XPATH, f'/html/body/shop-root/div/section/ui-list-category/div/div/div[3]/ul/li[{i}]/ruler-product-list-large-item/div/a[1]/div[2]/div[3]/div/ruler-price-text[1]/span/span[1]').text
        ws.append([rank, company_name, product_name, price])

    wb.save("29cm_products.xlsx")
    print("데이터를 엑셀 파일로 내보냈습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
finally:
    driver.quit()
