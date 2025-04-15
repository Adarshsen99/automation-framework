import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Fund_manager import Requests
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig

class Test_Requests:
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
        self.rq.click_request()
        time.sleep(2)

        serpro = self.rq.drp_serv_pro()
        time.sleep(2)

        self.rq.ser_pro_search().send_keys("Phenomenal")

        self.rq.select_phenom_money()
        self.rq.search_btn()
        time.sleep(2)

        self.rq.click_phenom()
        time.sleep(2)

        self.rq.fund_request().send_keys("210000")
        time.sleep(2)

        self.rq.req_for_apprval()
        time.sleep(2)