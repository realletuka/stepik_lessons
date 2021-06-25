from pytest import fixture
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
expected_add_goods_to_basket = {'ru': 'Добавить в корзину', 'en': 'Add to basket', 'de': 'Zum Warenkorb hinzufügen'}

def test_availability_button_to_add(browser, language):
    # Arrange
    browser.get(link)
    browser.implicitly_wait(15)
    # Act
    browser.get(link)
    add_goods_to_basket = browser.find_element_by_css_selector('[class=btn btn-lg btn-primary btn-add-to-basket]')

    # Assert
    assert add_goods_to_basket in expected_add_goods_to_basket[language], 'Текст кнопки неверный'

    browser.implicitly_wait(15)
    browser.quit()