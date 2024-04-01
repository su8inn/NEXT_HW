from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromedriver_path='/Users/kimsubin/Desktop/NEXT/chromedriver-mac-x64 2'
user_data_dir="/Users/kimsubin/Desktop/NEXT/subin github/NEXT_HW/HW6"                                                                                                                                                                                                                                       

chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={user_data_dir}')
service = Service(executable_path=chromedriver_path)

driver=webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.kurly.com/main')

#[베스트] 버튼 누르기
chartbtn = driver.find_element(By.XPATH, '//*[@id="header"]/div/ul/li[2]/span')
chartbtn.click()
time.sleep(3)