import allure

from pages.admin import AdminPage


@allure.feature('Наличие элементов страницы')
@allure.title('Вход администратора')
@allure.severity(allure.severity_level.CRITICAL)
def test_open_product_page(browser, config):
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    admin_page.go_to_catalog_products()
    admin_page.check_products_page()
