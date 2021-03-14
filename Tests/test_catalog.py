import allure

from pages.catalog import CatalogPage


@allure.feature('Наличие элементов страницы')
@allure.title('Каталог товаров')
@allure.severity(allure.severity_level.CRITICAL)
def test_catalogpage(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page()
    catalog_page.check_elements_on_catalog_page()
