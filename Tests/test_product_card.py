def test_open_page(browser, base_url):
    browser.get(base_url + "/index.php?route=product/product&path=57&product_id=49")


def test_find_add_to_card_button(browser):
    assert browser.find_element_by_xpath("//button[@id='button-cart']")


def test_find_title_of_the_product(browser):
    assert browser.find_element_by_xpath("//h1[contains(text(),'Samsung Galaxy Tab 10.1')]")


def test_find_quantity_field(browser):
    assert browser.find_element_by_name("quantity")


def test_find_reviews_section(browser):
    assert browser.find_element_by_partial_link_text("reviews")


def test_find_rating_checkboxes(browser):
    reviews_section = browser.find_element_by_partial_link_text("reviews")
    reviews_section.click()
    rating_check_boxes = browser.find_elements_by_name("rating")
    assert rating_check_boxes
    assert len(rating_check_boxes) == 5
