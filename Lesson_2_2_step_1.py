from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_element = browser.find_element(By.XPATH, "//*[@id='num1']")
    a = a_element.text
    b_element = browser.find_element(By.XPATH, "//*[@id='num2']")
    b = b_element.text
    c = str(int(a)+int(b))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    ##input1 = browser.find_element(By.CSS_SELECTOR, "div.container .form-group input")
    #input1.send_keys(y)
    #option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    #option1.click()
    #option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    #option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()