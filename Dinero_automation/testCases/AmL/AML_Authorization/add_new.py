import string
import time
from random import random

import self
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Pulldownmenu import AML_MENU
from Dinero_automation.pageObjects.AML_MENU.AUTHORISATION import Add_new
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_add_new:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_name_self(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)

        # click action for nav bar arrow
        self.aml = AML_MENU(self.driver)

        # Locate the customer pull-down element
        Aml_pull_element = self.driver.find_element(By.XPATH,
                                                    "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[7]/div[1]")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Aml_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        auth_element = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]")
        auth_element.click()
        time.sleep(2)

        self.an = Add_new(self.driver)

        self.an.create_new().click()

        name = self.an.name()
        name.send_keys("TEST DILIGENCE")
        Description = self.an.descriptiopn()
        Description.send_keys("testers only")
        name_search = self.an.user_search()
        name_search.send_keys("adarsh")
        time.sleep(2)
        user_sel = self.an.user_select()
        user_sel.click()
        # time.sleep(2)
        #
        # self.an.save_btn().click()

    def test_add_multiple_auth(self, setup):
        def generate_random_digits(self, length=8):
            return ''.join(random.choices(string.digits, k=length))

        def generate_random_string(self, length=8):
            return ''.join(random.choices(string.ascii_letters, k=length))

        responce = []

        # Arrays holding bank names and local bank names
        auth_nam = [


            "Enhanced Due Diligence (EDD)",
            "Ongoing Due Diligence (ODD)",
            "Third-Party Due Diligence (TPDD)",
            "Risk-Based Due Diligence (RBDD)",
            "Event-Driven Due Diligence (EDDD)",
            "Politically Exposed Person Due Diligence (PEP DD)",
            "High-Risk Customer Due Diligence (HRCDD)",
            "Transaction Monitoring Due Diligence (TMDD)"
        ]
        descrip_name = [


            "Enhanced Due Diligence (EDD)",
            "Ongoing Due Diligence (ODD)",
            "Third-Party Due Diligence (TPDD)",
            "Risk-Based Due Diligence (RBDD)",
            "Event-Driven Due Diligence (EDDD)",
            "Politically Exposed Person Due Diligence (PEP DD)",
            "High-Risk Customer Due Diligence (HRCDD)",
            "Transaction Monitoring Due Diligence (TMDD)"
        ]

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)

        # click action for nav bar arrow
        self.aml = AML_MENU(self.driver)

        # Locate the customer pull-down element
        Aml_pull_element = self.driver.find_element(By.XPATH,
                                                    "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[7]/div[1]")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Aml_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        auth_element = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]")
        auth_element.click()
        time.sleep(2)

        for i in range(8):
            self.an = Add_new(self.driver)

            self.an.create_new().click()

            name = self.an.name()
            name.send_keys( auth_nam[i])
            Description = self.an.descriptiopn()
            Description.send_keys(descrip_name[i])
            name_search = self.an.user_search()
            name_search.send_keys("adarsh")
            time.sleep(2)
            user_sel = self.an.user_select()
            user_sel.click()
            time.sleep(3)

            self.an.save_btn().click()
            time.sleep(2)
            for res in responce:
                print(res['root']['baseURL'])
