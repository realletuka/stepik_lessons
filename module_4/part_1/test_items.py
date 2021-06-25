from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
expected_add_goods_to_basket = {'ru': 'Добавить в корзину', 'en': 'Add to basket', 'de': 'Zum Warenkorb hinzufügen'}


def test_availability_button_to_add(browser, language):
    # Arrange
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(30)
    # Act
    browser.get(link)
    add_goods_to_basket = browser.find_element_by_css_selector('[class=btn btn-lg btn-primary btn-add-to-basket]')
    lang_of_page = browser.find_element_by_class_name('no-js').get_attribute("lang")

    # Assert
    assert add_goods_to_basket in expected_add_goods_to_basket[language], 'Текст кнопки неверный'
    assert lang_of_page == language, 'Язык страницы выбран не верно'

    browser.implicitly_wait(15)
    browser.quit()
