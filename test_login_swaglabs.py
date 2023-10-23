import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_login_standard(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
@pytest.mark.xfail
def test_login_locked_out(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('locked_out_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
@pytest.mark.smoke
def test_login_problem(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('problem_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
def test_login_glitch(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('performance_glitch_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
def test_login_error(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('error_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
def test_login_visual(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('visual_user')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    url = browser.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'
def test_login_error(browser):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    browser.find_element('xpath', '//input[@id="user-name"]').send_keys('random')
    browser.find_element('xpath', '//input[@id="password"]').send_keys('random_text')
    browser.find_element('xpath', '//input[@id="login-button"]').click()
    error = browser.find_element('xpath', '//h3[text()="Epic sadface: Username and password do not match any user in this service"]')
    assert error.text == 'Epic sadface: Username and password do not match any user in this service'




