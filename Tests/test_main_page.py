import time
def test_main_page(browser, base_url):
    browser.get(base_url)
    time.sleep(10)
    assert browser.title == "Your Store"
