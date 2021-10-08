import time

import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

@pytest.fixture()
def driver(request):
    fox_driver = WebDriver()
    fox_driver.implicitly_wait(3)
    yield fox_driver
    fox_driver.close()

def test_fixture_pytest(driver: WebDriver):
    driver.get('http://google.com')
    time.sleep(3)
