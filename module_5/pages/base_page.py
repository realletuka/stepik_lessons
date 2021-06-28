from selenium import webdriver
import pytest

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        browser = webdriver.Chrome()
        self.browser.get(self.url)
