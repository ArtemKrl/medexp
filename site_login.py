from config import base_url
from selenium.webdriver.chrome.webdriver import WebDriver


def login_site(driver: WebDriver):
    driver.get(base_url)
    driver.find_element_by_id('normal_login_username').send_keys('1')  # field login
    driver.find_element_by_id('normal_login_password').send_keys('1')  # field pass

    driver.find_element_by_tag_name('button').click()  # enter button
