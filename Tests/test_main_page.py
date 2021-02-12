def test_open_page(browser, base_url):
    browser.get(base_url)


def test_main_page_title(browser, base_url):
    browser.get(base_url)
    assert browser.title == "Your Store"


def test_find_search_bar(browser):
    assert browser.find_element_by_name("search")


def test_find_cart(browser):
    assert browser.find_element_by_css_selector("#cart > .btn")


def test_find_featured_products(browser):
    assert browser.find_elements_by_class_name("product-thumb")


def test_find_menu(browser):
    assert browser.find_element_by_class_name("navbar-header")
