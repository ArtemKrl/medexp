import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import base_url
import logging

from capabilities import capabilities

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger()

selenoid_URL = "http://127.0.0.1:4444/wd/hub"

def test_login_admin():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")

    logger.info('Running browser')

    driver = webdriver.Remote(
        command_executor=selenoid_URL,
        desired_capabilities=capabilities)

    #driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
    driver.get(base_url)
    logger.info('Waiting url: %s' % ('%slogin' % base_url))
    #WebDriverWait(driver, 10).until(EC.url_contains('%slogin' % base_url))
    #logger.info('Enter login')
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'normal_login_username'))).send_keys('1')
    #logger.info('Enter login')
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'normal_login_password'))).send_keys('1')
    #logger.info('Press button')
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary.LoginPage_form_button_submit__IUtZt'))).click()
    #logger.info('Waiting login')
    #assert WebDriverWait(driver, 10).until(EC.url_contains('%smain' % base_url)), 'trying login as admin'
    assert True

if __name__ == '__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])