from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB', help='Chose language: ru, en-GB, de, fr')

@pytest.fixture(scope='function')
def language_browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\nstart Chrome browser...')
    browser = webdriver.Chrome(options=options)

    yield browser
    print('\nquit Chrome browser...')
    browser.quit()
