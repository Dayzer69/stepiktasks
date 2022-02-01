from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_ass(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    x = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert x, "not found"

