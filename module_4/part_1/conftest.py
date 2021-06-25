from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= None, help='Chose language: ru, en, de')

@pytest.fixture(scope="function")
def browser(language):
    print(f'\nstart {language} vesion')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\nstart Chrome browser...')
    browser = webdriver.Chrome(options=options)

    yield browser
    print('\nquit Chrome browser...')
    browser.quit()

@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption('language')
