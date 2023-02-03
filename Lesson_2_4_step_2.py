from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # запускам страницу браузера
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку с ожиданием цены с помощью нового модулем expected_conditions
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button1.click()

    # находим элемент x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # вводим ответ функции в поле ввода
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    # нажимаем кнопку для подтверждения
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()