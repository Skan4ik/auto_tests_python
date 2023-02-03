from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button1.click()
    # переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # находим элемент x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # вводим ответ функции в поле ввода
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    # нажимаем кнопку для подтверждения
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()