from pages.main import MainPage


def test_main_page_title(browser, base_url):
    browser.get(base_url)
    assert browser.title == "Your Store"


def test_check_five_elements_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.open_home_page()
    main_page.check_elements()
