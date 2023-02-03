from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input3.send_keys("gmail")

    # находим элемент отвечающий за отправку файла на странице и сохраняем в объект
    name_object = browser.find_element(By.CSS_SELECTOR, '#file')
    # текущая дериктория txt файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляет имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    # это тот злополучный element, который непонятно откуда берется
    name_object.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    time.sleep(5)
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()