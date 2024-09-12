import string
import time

from random import random

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Bank import Add_Bank

from Dinero_automation.utilities.randomString import generate_random_email_new, random_string_generator_numbers, \
    random_string_generator_numbers_new, random_string_generator_new, random_string_generator, \
    random_string_generator_max_30, random_string_generator_max_50, generate_random_email, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51, random_string_generator
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_add_bank:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_click_on_bank_name(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to add bank page
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_add_bank()
        time.sleep(2)

        # Pass the driver to Add_Bank
        self.ab = Add_Bank(self.driver)

        # Retrieve and print the bank names
        elements = self.ab.get_banknames()

        for ele in elements:
            # Print the element's XPath (if you know how to retrieve it, or you could print the text)
            print(ele)
