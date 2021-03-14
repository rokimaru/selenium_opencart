import allure

from pages.product import ProductPage


@allure.feature('Наличие элементов страницы')
@allure.title('Страница товара')
def test_productpage(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page()
    product_page.check_elements_on_product_page()
