def test_open_page(browser, base_url):
    browser.get(base_url + '/index.php?route=account/login')


def test_find_registration_button(browser):
    assert browser.find_element_by_xpath("//a[contains(text(),'Continue')]")


def test_find_login_button(browser):
    assert browser.find_element_by_link_text("Login")


def test_find_email_field(browser):
    assert browser.find_element_by_id("input-email")


def test_find_password_field(browser):
    assert browser.find_element_by_id("input-password")


def test_find_footer(browser):
    assert browser.find_element_by_tag_name("footer")
