import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"], help="browser")
    parser.addoption('--url', action='store', default='http://localhost')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError('unrecognized browser %s' % browser)

    if maximized:
        driver.maximize_window()

    def fin():
        driver.close()

    request.addfinalizer(fin)

    return driver
