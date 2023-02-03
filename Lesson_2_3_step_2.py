from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button1.click()
    # действия в алерте
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    # находим элемент x
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    # вводим значение функции в строку
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)
    # нажимаем на кнопку
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()