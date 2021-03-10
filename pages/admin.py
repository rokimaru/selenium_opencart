from pages.base import Base
from locators.admin import AdminLocators
from locators.common import CommonLocators
from selenium.common.exceptions import TimeoutException


class AdminPage(Base):
    path = "/admin/"

    def open_admin_page(self):
        self.logger.info('open admin page')
        self.browser.get(self.url + self.path)

    def login_to_admin_page(self, username, password):
        self.logger.info('login to admin page')
        input_username = self._wait_element_to_be_clickable(AdminLocators.LoginToAdminPage.INPUT_USERNAME)
        self._input_text(input_username, username)
        input_pass = self._wait_element_to_be_clickable(AdminLocators.LoginToAdminPage.INPUT_PASS)
        self._input_text(input_pass, password)
        login_button = self._find_elements(AdminLocators.LoginToAdminPage.LOGIN_BUTTON)[0]
        login_button.click()
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)

    def logout_from_admin_page(self):
        self.logger.info('logout from admin page')
        logout_button = self._find_elements(CommonLocators.LOGOUT_BUTTON)[0]
        logout_button.click()
        self._wait_element_to_be_presence(AdminLocators.LoginToAdminPage.LOGIN_BUTTON)

    def go_to_the_last_order_card(self):
        self.logger.info('go to last order')
        latest_orders = self._find_elements(AdminLocators.Dashboard.VIEW_LATEST_ORDERS)
        latest_orders[0].click()
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)

    def go_to_print_shipping_list(self):
        self.logger.info('print shipping list')
        print_shipping_list = self._find_elements(AdminLocators.LastOrderCard.PRINT_SHIPPING_LIST)[0]
        window_before = self.browser.window_handles[0]  # Сохранить текущее окно
        print_shipping_list.click()
        window_after = self.browser.window_handles[1]  # Сохранить новое окно с открывшейся накладной
        self.browser.switch_to.window(window_after)  # Свичнуться на окно с накладной

    def check_dispatch(self):
        self.logger.info('check dispatchr')
        try:
            self._wait_element_to_be_presence(AdminLocators.Dispatch.CONTAINER)
            self._wait_element_to_be_presence(AdminLocators.Dispatch.DISPATCH_NOTE)
        except TimeoutException:
            raise AssertionError("Dispatch note is not downloaded")

    def go_to_sales_orders(self):
        self.logger.info('go to sales orders')
        sale = self._find_elements(AdminLocators.Dashboard.SALES)[0]
        sale.click()
        self._wait_element_to_be_clickable(AdminLocators.Dashboard.SECTIONS_IN_SALES)
        orders = self._find_elements(AdminLocators.Dashboard.SECTIONS_IN_SALES)[0]
        orders.click()

    def add_new_order(self):
        self.logger.info('add new order')
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)
        add_new_order = self._find_elements(AdminLocators.Orders.ADD_NEW_ORDER)[0]
        add_new_order.click()

    def check_new_order_form(self):
        self.logger.info('checking new order form')
        try:
            self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)
            self._wait_element_to_be_presence(AdminLocators.NewOrderCard.CUSTOMER_FIELD)
        except TimeoutException:
            raise AssertionError("There is no customer field")

    def check_elements_on_admin_page(self):
        self.logger.info('checking elements on admin page')
        self._find_element(AdminLocators.LoginToAdminPage.INPUT_USERNAME)
        self._find_element(AdminLocators.LoginToAdminPage.INPUT_PASS)
        self._find_element(AdminLocators.LoginToAdminPage.LOGIN_BUTTON)
        self._find_element(AdminLocators.LoginToAdminPage.FORGOTTEN_PASSWORD)
        self._find_element(CommonLocators.GO_TO_HOMEPAGE)

    def go_to_catalog_products(self):
        self.logger.info('go to products catalog')
        catalog = self._find_elements(AdminLocators.Dashboard.MENU_CATALOG)[0]
        catalog.click()
        self._wait_element_to_be_clickable(AdminLocators.Dashboard.SECTIONS_IN_CATALOG)
        products = self._find_elements(AdminLocators.Dashboard.SECTIONS_IN_CATALOG)[1]
        products.click()

    def check_products_page(self):
        self.logger.info('checking products page')

        try:
            self._wait_element_to_be_presence(AdminLocators.Catalog.TABLE_WITH_PRODUCT_LIST)
        except TimeoutException:
            raise AssertionError("Page is not downloaded")