import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_login_standard(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'
@pytest.mark.xfail
def test_login_locked_out(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('locked_out_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'
def test_login_problem(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('problem_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'
def test_login_glitch(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('performance_glitch_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'
def test_login_error(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('error_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'
def test_login_visual(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "user-name").send_keys('visual_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    title = browser.find_element(By.CLASS_NAME,'app_logo')
    assert title.text == 'Swag Labs'




