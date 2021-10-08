import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from exp import exp
from selection_polyclinic import clinic_selection
from site_login import login_site
from general_selection import gen_select
from home_hospital import home_hospital
from hospital_selection import hosp_selection
from selection_MTP import mtp_selection
from selection_ambulance import ambulance_select
from selection_outgoing import outgoing_select


@pytest.fixture()
def driver(request):
    fox_driver = WebDriver()
    fox_driver.implicitly_wait(3)
    yield fox_driver


def test_login_site(driver: WebDriver):

    login_site(driver)

    exp(driver)


# def test_selection_MTP(driver: WebDriver):
#     login_site(driver)
#
#     mtp_selection(driver)
#
#
# def test_hospital_selection(driver: WebDriver):
#     login_site(driver)
#
#     hosp_selection(driver)
#
#
# def test_selection_outgoing(driver: WebDriver):
#     login_site(driver)
#
#     outgoing_select(driver)
#
#
# def test_selection_polyclinic(driver: WebDriver):
#     login_site(driver)
#
#     clinic_selection(driver)
#
#
# def test_selection_home(driver: WebDriver):
#     login_site(driver)
#
#     home_hospital(driver)
#
#
# def test_selection_ambulance(driver: WebDriver):
#     login_site(driver)
#
#     ambulance_select(driver)
#

# def test_general_selection(driver: WebDriver):
#     login_site(driver)
#
#     gen_select(driver)
