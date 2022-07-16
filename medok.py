"""
Данный скрипт записывает к врачу
"""
import time
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

opts = FirefoxOptions()
##opts.add_argument("--headless")
opts.page_load_strategy = 'none'
fp = webdriver.FirefoxProfile('C:\\Users\\Юлия\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8ob6u95l.ufo2') # вместо ... Ваш профиль.
driver = webdriver.Firefox(options=opts, firefox_profile=fp)

try:
    URL = "https://uslugi.mosreg.ru/zdrav/"
    print(f'Мы находимся тут: {URL}')
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".btn--make-to-appointment").click()
    time.sleep(5)
    driver.find_element(By.ID, "btn-continue-doctor-appointment-in-popup").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".b-doctor-spec__list-item:nth-child(29) > .b-doctor-spec__text").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#lpu_code_4401042 .b-clinic-doctors-list__row:nth-child(3) .b-doctor-schedule__item:nth-child(1) .b-doctor-schedule__item-no").click()
    time.sleep(5)
    der = driver.find_element_by_xpath("/html/body/div[10]/div/div/div[3]/div[4]/div[2]/div[4]/div/div[2]").find_elements_by_class_name("b-doctor-schedule__item-tickets")
    print(len(der))
    try:
        if der[0].is_enabled:
            der[0].click()
            time.sleep(5)
            print('1')
        else:
            pass
    except:
        der[0] = None

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
