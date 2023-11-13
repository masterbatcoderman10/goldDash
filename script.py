from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt
import re
import time

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options) # replace with the path to your chromedriver
    return driver

def get_data(driver):
    today = dt.datetime.now().date()
    driver.get('https://www.khaleejtimes.com/gold-forex') # replace with your website URL

    row_nums = [2,3, 5]
    gold_prices = []
    driver.implicitly_wait(2)
    for row in row_nums:
        x_path = f"(//div[@class = 'draft-rates-main-wrapper-nf maxwidth-67'])[1]/div/table/tbody/tr[{row}]/td[2]"
        element = driver.find_element(by=By.XPATH, value=x_path).text
        gold_prices.append(element)

    currency_xpath = "//div[@class = 'draft-rates-main-wrapper-nf']/div[2]/table/tbody/tr[1]/td[2]"
    currency = driver.find_element(by=By.XPATH, value=currency_xpath).text

    currency_val = re.search(r'\d\d.\d\d', currency).group()

    driver.quit()

    return today, gold_prices, currency_val

# start = time.time()
# print(get_data(init_driver()))
# end = time.time()
# print(end - start)
