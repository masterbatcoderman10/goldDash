from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt
import re
import time

def init_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    service = Service("./geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def get_data(driver):
    # today = dt.datetime.now().date()
    driver.get('https://www.khaleejtimes.com/gold-forex') # replace with your website URL

    row_nums = [2,3, 5]
    gold_prices = []
    driver.implicitly_wait(2)
    for row in row_nums:
        x_path = f"(//div[@class = 'draft-rates-main-wrapper-nf maxwidth-67'])[1]/div/table/tbody/tr[{row}]/td[2]"
        element = driver.find_element(by=By.XPATH, value=x_path).text
        try:
            gold_prices.append(float(element))
        except:
            x_path = f"(//div[@class = 'draft-rates-main-wrapper-nf maxwidth-67'])[1]/div/table/tbody/tr[{row}]/td[1]"
            element = driver.find_element(by=By.XPATH, value=x_path).text
            gold_prices.append(float(element))


    currency_xpath = "//div[@class = 'draft-rates-main-wrapper-nf']/div[2]/table/tbody/tr[1]/td[2]"
    currency = driver.find_element(by=By.XPATH, value=currency_xpath).text

    try:
        currency_val = float(re.search(r'\d\d.\d\d', currency).group())
    except:
        currency_xpath = "//div[@class = 'draft-rates-main-wrapper-nf']/div[2]/table/tbody/tr[1]/td[2]"
        currency = driver.find_element(by=By.XPATH, value=currency_xpath).text
        currency_val = float(re.search(r'\d\d.\d\d', currency).group())


    driver.quit()

    return gold_prices, currency_val

# start = time.time()
# print(get_data(init_driver()))
# end = time.time()
# print(end - start)
