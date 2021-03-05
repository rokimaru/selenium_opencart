from pages.base import Base
from locators.catalog import CatalogLocators


class CatalogPage(Base):
    path = "/index.php?route=product/category&path=20"

    def open_catalog_page(self):
        self.browser.get(self.url + self.path)

    def check_elements_on_catalog_page(self):
        self._find_element(CatalogLocators.MENU_SOFTWARE)
        self._find_element(CatalogLocators.MENU_TABLETS)
        self._find_element(CatalogLocators.MENU_COMPONENTS)
        self._find_element(CatalogLocators.MENU_LAPTOPS_AND_NOTEBOOKS)
        self._find_element(CatalogLocators.MENU_DESKTOPS)
