import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_add_button(browser):
    browser.get(link)
    # time.sleep(30)  # for language check
    browser.implicitly_wait(15)
    add_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert add_button, "Button not found"
