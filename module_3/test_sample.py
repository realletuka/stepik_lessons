from selenium import webdriver

try:
    # ARRANGE
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/")

    # ACT
    element1 = browser.find_element_by_xpath("//a[text()='Hacking Exposed Wireless']").click()
    button_add_to_basket = browser.find_element_by_id("add_to_basket_form").click()
    button2_view_basket = browser.find_element_by_xpath("//a[text()='Посмотреть корзину']").click()
    delete_from_basket = browser.find_element_by_class_name("inline").click()
    # Assert
    assert element1 is delete_from_basket

finally:
    browser.quit()
