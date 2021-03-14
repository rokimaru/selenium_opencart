import allure

from pages.login import LoginPage


@allure.feature('Наличие элементов страницы')
@allure.title('Логин юзера')
@allure.severity(allure.severity_level.CRITICAL)
def test_loginpage(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.check_elements_on_login_page()
