import os
import random
import string
import time

import controller
import pyautogui
import self
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib3.exceptions import MaxRetryError

from DineroQa.Dinero_automation.utilities.randomString import random_string_generator_numbers_18, \
    random_string_generator_max_28, random_string_generator_max_31, random_string_generator_numbers
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Pulldownmenu import Account_pulldownmenu
from Dinero_automation.pageObjects.Accounts_menu.transit_agent import Transit_agent
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
from selenium import webdriver


def generate_random_digits(length=8):
    return ''.join(random.choices(string.digits, k=length))


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_email():
    return generate_random_string(5) + "@example.com"


class TestSendingDocs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        # time.sleep(2)
        self.lp.clickLogin()

        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)

        time.sleep(3)
        self.acc = Account_pulldownmenu(self.driver)

        # Locate the customer pull-down element
        Acc_pull_element = self.driver.find_element(By.XPATH,
                                                    "//div[normalize-space()='Accounts']")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Acc_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        trans_element = self.driver.find_element(By.XPATH,
                                                   "//div[normalize-space()='Transit Agent']")
        trans_element.click()

        self.tra = Transit_agent(self.driver)
        for i in range(5):
            Name = ["Money india", "Group Force", "Agent Dollar", "Bank Safer", "Provider Group"]

            address = ["Kottayam", "Kannur", "Trivandrum", "Palakkad", "Wayanad"]

            Contact_person = ["Athul Rajakkad", "Akash Wayanad", "Anish Kannur", "Yadhu Guruvayoor", "Thasni Kottayam"]

            Region = ["South", "West", "East", "North", "Zone"]

            new = self.tra.click_create_new()
            new.click()

            name = self.tra.transit_agent_name()
            name.send_keys(Name[i])
            short_name = self.tra.short_name()
            short_name.send_keys(Name[i].split())
            adress = self.tra.address()
            adress.send_keys(address[i], Region[i])
            email = self.tra.email()
            email.send_keys(Name[i] + "gmail.com")
            tel_num = self.tra.telephone_number()
            tel_num.send_keys("0484" + random_string_generator_numbers(7))

            cont_pers = self.tra.contact_person()
            cont_pers.send_keys(Contact_person[i])
            cont_pers_num = self.tra.contact_person_number()
            cont_pers_num.send_keys("91" + random_string_generator_numbers(7))
            city = self.tra.transit_agent_city()
            city.send_keys(address[i])
            region = self.tra.region()
            region.send_keys(Region[i])

            self.tra.buttton_save().click()
            time.sleep(2)
