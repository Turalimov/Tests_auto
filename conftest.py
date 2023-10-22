import pytest
from selenium import webdriver




@pytest.fixture(scope="function")
def browser():
    print("\nоткрываем браузер для тестирования..")
    browser = webdriver.Chrome()
    yield browser
    print("\nзакрываем браузер..")
    browser.quit()
