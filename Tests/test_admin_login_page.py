def test_open_page(browser, base_url):
    browser.get(base_url + "/admin/")


def test_username_field(browser):
    browser.find_element_by_id("input-username")


def test_password_field(browser):
    browser.find_element_by_id("input-password")


def test_forgotten_password_link(browser):
    browser.find_element_by_link_text("Forgotten Password")


def test_login_button(browser):
    browser.find_elements_by_css_selector(".btn-primary")


def test_return_to_home_page_link(browser):
    browser.find_element_by_link_text("OpenCart")
