from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "div.container .form-group input")
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()