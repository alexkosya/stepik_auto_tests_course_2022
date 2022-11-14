#2.4 Настройка ожиданий
#Есть способы получше: Selenium Waits (Implicit Waits)

from selenium import webdriver
from selenium.webdriver.common.by import By

#Открыть страницу http://suninjuly.github.io/wait1.html
#Нажать на кнопку "Verify"
#Проверить, что появилась надпись "Verification was successful!"

try:
    #1.Открыть страницу
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    #2.Нажать на кнопку "Verify"
    button = browser.find_element(By.ID, "verify")
    button.click()

    #3. Проверить, что появилась надпись "Verification was successful!"
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text

finally:
    # успеваем скопировать код за 10 секунд
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

