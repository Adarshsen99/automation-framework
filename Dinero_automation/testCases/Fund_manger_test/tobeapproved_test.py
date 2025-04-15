import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Fund_manager import Requests, Tobeapproved
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_approved:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_name(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        # time.sleep(2)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer details
        self.nav.click_fund_manger()
        time.sleep(2)

        self.rq = Requests(self.driver)
        self.tba = Tobeapproved(self.driver)

        self.tba.approveclick()
        time.sleep(2)

        serpro = self.tba.drp_serv_pro()
        time.sleep(2)

        self.tba.ser_pro_search().send_keys("Phenomenal")

        self.tba.select_phenom_money()
        self.tba.search_btn()
        time.sleep(2)

        self.tba.click_phenom()
        time.sleep(2)

        self.tba.fund_approved().send_keys("210000")
        time.sleep(2)

        self.tba.Add_bank()
        time.sleep(2)
        self.tba.click_new()
        time.sleep(2)

        bank = Select(self.tba.drp_bank())
        bank.select_by_index(1)

        self.tba.Fc_amount().send_keys("210000")

        self.tba.click_confirm()
        time.sleep(3)

        self.tba.click_approve()
        time.sleep(2)







