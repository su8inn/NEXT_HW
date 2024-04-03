from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime

chromedriver_path = '/Users/kimsubin/Desktop/NEXT/chromedriver-mac-x64 2/chromedriver'
user_data_dir = "/Users/kimsubin/Desktop/NEXT/subin github/NEXT_HW/HW6"

chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={user_data_dir}')
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.ikea.com/kr/ko/cat/armchairs-16239/')

# IKEA의 암체어 리스트업 되어있는 제품명 가져오기
product_elements = driver.find_elements(By.XPATH, "//span[@class='notranslate plp-price-module__product-name']")
# IKEA의 암체어 리스트업 되어있는 제품 가격 가져오기
product_price_list = driver.find_elements(By.XPATH, "//span[@class='plp-price__integer']")
# IKEA의 암체어 리스트업 되어있는 제품 리뷰 수 가져오기
product_review_list = driver.find_elements(By.XPATH, "//span[@class='plp-rating__label']")

# 제품 정보를 출력
for product_element, product_price, product_review in zip(product_elements, product_price_list, product_review_list):
    print(f"Product: {product_element.text}, Price: {product_price.text}, Review: {product_review.text}")

# CSV 파일 생성 및 헤더 작성
today = datetime.now().strftime('%Y%m%d')
file_path = f'{today}_ikea_armchair_list.csv'

with open(file_path, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["product", "price", "review"])

    # 제품명, 가격, 리뷰를 각각 리스트에 저장
    products = [product_element.text for product_element in product_elements]
    prices = [product_price.text for product_price in product_price_list]
    reviews = [product_review.text for product_review in product_review_list]

    # 각각의 리스트에서 제품명, 가격, 리뷰를 하나씩 가져와서 CSV 파일에 쓰기
    for product, price, review in zip(products, prices, reviews):
        writer.writerow([product, price, review])

# 특정 제품으로 들어가기
productbtn = driver.find_element(By.XPATH,'//*[@id="product-list"]/div[1]/div[1]/div/div[3]/a/div/div[1]/h3/span[1]/span')
productbtn.click()
time.sleep(1)

# 특정 제품 설명보기
productDetailbtn = driver.find_element(By.XPATH,'//*[@id="pip-product-information-section-list-0"]/button/span[1]/span/span/span')
productDetailbtn.click()

time.sleep(2)
