import random
import re
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ExpectedConditions:
    pass


def clinic_selection(driver: webdriver):
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('li.ant-menu-item:nth-child(2) > span:nth-child(2)').click()  # select expertise
    driver.find_element_by_css_selector('.ant-layout-sider-light.ant-layout-sider-has-trigger > '
                                        'div.ant-layout-sider-children > ul > li:nth-child(1) > '
                                        'span.ant-menu-title-content').click()
    # selection of elections
    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element_by_css_selector('div:nth-child(5) > div > button').click()
    # choice of a common selection
    time.sleep(1)
    driver.find_element_by_css_selector("div.command-menu:nth-child(6) > div > div> div:nth-child(1) > ul "
                                        "> li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                        "span").click()  # create selection
    time.sleep(1)
    driver.find_element_by_css_selector(
        ".ant-form-item-has-error > div > div.ant-form-item-control-input > div > div > div").click()  # open drop menu
    time.sleep(1)
    driver.find_element_by_css_selector("div:nth-child(2) > div >div > div:nth-child(6) > div > div > div > div > "
                                        "table > tbody:nth-child(2) > tr:nth-child(1)").click()  #
    # select type of
    # selection

    driver.find_element_by_css_selector("div.ant-col.ant-form-item-control > div > div > div > div > "
                                        "span.ant-picker-clear > span > svg").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.ant-picker-input.ant-picker-input-active > input'))).send_keys(
        '01.01.2018')  # date input
    time.sleep(1)
    driver.find_element_by_css_selector(".ant-picker-cell-range-start-single.ant-picker-cell-selected > div").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-picker-input.ant-picker-input-active > input'))).send_keys(
        '01.01.2022')  # date input
    time.sleep(1)
    driver.find_element_by_css_selector(".ant-picker-cell-range-end.ant-picker-cell-selected > div").click()

    time.sleep(1)
    driver.find_element_by_css_selector("div:nth-child(2) > div > div.ant-row.ant-form-item.ant-form-item-has-success "
                                        "> div > div > div > div > div").click()  # open SMO drop menu

    time.sleep(1)
    driver.find_element_by_css_selector("div.widget-wrapper:nth-child(3) > div > div > div:nth-child(6) > div > div > "
                                        "div > div > table > tbody:nth-child(2) > tr:nth-child(1)").click() # select
    # type of SMO

    driver.find_element_by_css_selector("div.ant-col.ant-col-8 > div > "
                                        "div.ant-row.ant-form-item.ant-form-item-has-success > div > div > div > "
                                        "label > span > input").click()

    elem_list = driver.find_elements_by_css_selector('div.dx-datagrid-content.dx-datagrid-content-fixed > table > '
                                                     'tbody > tr > td.dx-command-select.dx-editor-cell.dx-editor'
                                                     '-inline-block')  # defining a list of items

    choice_here_1 = elem_list[:1]
    random.choice(choice_here_1).click()  # select all items
    time.sleep(1)
    elem_list_2 = driver.find_elements_by_css_selector('div.dx-datagrid-content.dx-datagrid-content-fixed > table > '
                                                       'tbody > tr > td.dx-command-select.dx-editor-cell.dx-editor'
                                                       '-inline-block')  # defining a list of items in table two
    time.sleep(1)
    choice_here_2 = elem_list_2[28:33]
    random.choice(choice_here_2).click()  # random select one item

    choice_here_3 = elem_list_2[34:40]
    random.choice(choice_here_3).click()  # random select one item

    search_text = driver.find_element_by_css_selector(
        "div.rootBox > div.appbar-div > div > div:nth-child(2) > div")
    num_of_selection = re.search(r'3\d*', search_text.text)  # search num of selection
    num_of_selection.group(0)

    driver.find_element_by_css_selector(".anticon-close > svg:nth-child(1)").click()  # close window of selection

    search_in_table = driver.find_element_by_css_selector(".dx-first-cell > div > div:nth-child(2) > div > "
                                                          "div:nth-child(2) > div > input")
    search_in_table.click()
    search_in_table.send_keys(num_of_selection.group(0))  # input num selection in table

    time.sleep(1)
    check_selection = driver.find_element_by_css_selector(".dx-datagrid-rowsview > div > div > div > div > "
                                                          "table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) "
                                                          "> td:nth-child(2)").text  # search num selection in table

    assert check_selection == num_of_selection.group(0)

    driver.quit()
