import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import ActionChains


class ExpectedConditions:
    pass


def gen_select(driver: WebDriver):
    driver.implicitly_wait(10)
    driver.fullscreen_window()
    driver.find_element_by_css_selector('li.ant-menu-item:nth-child(2) > span:nth-child(2)').click()  # select expertise
    driver.find_element_by_css_selector('.ant-layout-sider-light.ant-layout-sider-has-trigger > '
                                        'div.ant-layout-sider-children > ul > li:nth-child(1)').click()
    # selection of elections
    driver.find_element_by_css_selector('div.ant-row > .ant-col.ant-col-12:nth-child(1) button').click()
    # choice of a common selection
    wait = WebDriverWait(driver, 10)
    search_in_table = driver.find_element_by_css_selector(".dx-first-cell > div > div:nth-child(2) > div > "
                                                          "div:nth-child(2) > div > input")
    search_in_table.click()
    search_in_table.send_keys('854')  # input num of selection

    time.sleep(1)
    twoclick_selection = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".dx-datagrid-rowsview > div > div > div > div > "
                                                     "table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("
                                                     "1) "
                                                     "> td:nth-child(2)")))
    action = ActionChains(driver)
    action.double_click(twoclick_selection).perform()

    driver.find_element_by_css_selector(".dx-scrollable-content > div > table > tbody > "
                                        "tr.dx-row.dx-data-row.dx-column-lines.dx-row-alt").click()
    driver.find_element_by_css_selector(".dx-scrollable-content > div > table > tbody > "
                                        "tr.dx-row.dx-data-row.dx-column-lines.dx-row-alt").click()

    # open new window
    # action.double_click(twoclick_select).perform()
    # window_before = driver.window_handles[0]  # definition win one
    # window_after = driver.window_handles[1]  # definition win two
    # driver.switch_to_window(window_after)  # transition to win two

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Все случаи')]"))).click()

    time.sleep(1)
    driver.find_element_by_css_selector(".dx-menu-item-text").click()  # button update
    time.sleep(1)
    elem_list = driver.find_elements_by_css_selector('div.dx-datagrid-content.dx-datagrid-content-fixed > table > '
                                                     'tbody > tr > '
                                                     'td.dx-command-select.dx-editor-cell.dx-editor-inline-block')
    # definition list of item

    time.sleep(1)
    choice_here_1 = elem_list[1:3]
    random.choice(choice_here_1).click()
    time.sleep(1)
    choice_here_2 = elem_list[3:7]
    random.choice(choice_here_2).click()

    driver.find_element_by_css_selector(".caseSelectionFormAnt_footerBtn__1BHNe > div:nth-child(1) "
                                        "> button:nth-child(1)").click()  # create selection
    time.sleep(1)

    assert True
    # driver.close()
    # driver.switch_to_window(window_before)

    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ant-space-item:nth-child(2) > div:nth-child(1) > "
    #                                                         "button:nth-child(1)"))).click()  # form create
    time.sleep(1)
    driver.find_element_by_css_selector("div:nth-child(3) > span > svg").click()
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".ant-space-align-center > div:nth-child(2) > div > button"))).click()
    # type_form
    time.sleep(1)
    driver.find_element_by_css_selector("div:nth-child(2) > label > span.ant-checkbox").click()
    driver.find_element_by_css_selector("button.ant-btn:nth-child(2)").click()  # end election

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-modal-wrap:nth-child(2) > div > "
                                                            "div:nth-child(2) > div:nth-child(4) > "
                                                            "button:nth-child(2) > span"))).click()
    time.sleep(1)

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ant-modal-wrap:nth-child(2) > div:nth-child(1) > "
                                                     "div:nth-child(2) > div:nth-child(4) > button:nth-child(2)"))).click()
    time.sleep(1)

    select_application = driver.find_element_by_css_selector(".dx-datagrid-rowsview > div > div > div > div > table > "
                                                             "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)")
    action = ActionChains(driver)
    action.double_click(select_application).perform()
    time.sleep(1)
    elem_list_app = driver.find_elements_by_css_selector('div.dx-datagrid-content.dx-datagrid-content-fixed > table > '
                                                         'tbody > tr > '
                                                         'td.dx-command-select.dx-editor-cell.dx-editor-inline-block')
    choice_here_3 = elem_list_app[1:2]
    random.choice(choice_here_3).click()
    choice_here_4 = elem_list_app[2:4]
    random.choice(choice_here_4).click()

    driver.find_element_by_css_selector(".RequestForExpertiseForm_footerBTN_expert__24wYX > "
                                        "div:nth-child(1) > div > button:nth-child(1)").click()  # check fact of MEE
    assert True

    driver.quit()
