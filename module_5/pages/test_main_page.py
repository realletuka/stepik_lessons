from selenium import webdriver
from module_5 import MainPage

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
