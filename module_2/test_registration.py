from selenium import webdriver

import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    input3.send_keys("123@gmail.com")
    input4 = browser.find_element_by_class_name("form-control")
    input4.send_keys("98737625323")
    input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    button = browser.find_element_by_xpath("//*[@type='submit']")
    button.click()

    time.sleep(1)


    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    browser.quit()

