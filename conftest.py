import configparser
import pytest
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level=logging.INFO, filename="../logs/logs.log")


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        logging.error(f'there is a {exception}')
        driver.save_screenshot(f'../logs/{exception}.png')


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="firefox", choices=["chrome", "firefox"], help="browser")
    parser.addoption('--url', action='store', default='http://localhost')


@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent / 'config.ini')
    return config


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        driver = EventFiringWebDriver(webdriver.Opera(), MyListener())
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(options=options)

    else:
        raise ValueError('unrecognized browser %s' % browser)

    if maximized:
        driver.maximize_window()
    logger = logging.getLogger('BrowserLogger')
    logger.info('Browser {} started'.format(browser))

    def fin():
        driver.close()

    request.addfinalizer(fin)
    return driver
