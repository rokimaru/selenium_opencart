def test_open_page(browser, base_url):
    browser.get(base_url + "/index.php?route=product/category&path=20")


def test_side_menu(browser):
    assert browser.find_element_by_css_selector("#column-left")


def test_sort_menu(browser):
    assert browser.find_element_by_css_selector("#input-sort")


def test_show_menu(browser):
    assert browser.find_element_by_css_selector("#input-limit")


def test_home_button(browser):
    assert browser.find_element_by_class_name("fa-home")


def test_add_to_card_buttons(browser):
    assert browser.find_elements_by_css_selector(".button-group .fa-shopping-cart")
