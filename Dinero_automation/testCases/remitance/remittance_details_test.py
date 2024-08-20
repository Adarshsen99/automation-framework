from pynput.keyboard import Controller, Key
from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from Dinero_automation.pageObjects.Remitance import Remittance_Details
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Other_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    def test_sending_docs(self ,setup):
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

        # click action for customer registration
        self.nav.click_remitance()
        self.rm = Remittance_Details(self.driver)

        self.driver.execute_script("window.debugmode = true;")
        # debug_mode = self.driver.execute_script("return window.debugmode;")
        # print("Debug mode is set to:", debug_mode)

        self.rm.click_remitance().click()
        drp_currency = Select(self.rm.drp_currency_details())
        lc = self.rm.lc_amount()
        rev_rate = self.rm.rev_rate()
        rate = self.rm.rate()
        fc = self.rm.fc_amount()
        self.rm.sc()
        self.rm.tax()

        drp_currency.select_by_visible_text("United States Dollar")
        lc.send_keys("1")
        rev_rate.send_keys("83.785243")
        print(rate.get_attribute('value'))
        print(fc.get_attribute('value'))
        time.sleep(5)