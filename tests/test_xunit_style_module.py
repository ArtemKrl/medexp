from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = None


def setup_module():
    print('setup module started')
    global driver
    driver = WebDriver()
    driver.implicitly_wait(3)


def teardown_module():
    print('teardown module started')
    global driver
    driver.close()


def test_module_setup_driver():
    print('test invocation started')
    driver.get('https://google.com')
    import time
    time.sleep(3)
    assert True
