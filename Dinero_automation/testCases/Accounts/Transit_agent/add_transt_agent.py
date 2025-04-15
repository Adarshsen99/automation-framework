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
        time.sleep(3)
        self.acc = Account_pulldownmenu(self.driver)
        account_menu = self.acc.click_account_menu()

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(account_menu).perform()
        time.sleep(1)
        self.acc.click_transit_agent().click()
        time.sleep(2)

        self.tra = Transit_agent (self.driver)
        new = self.tra.click_create_new()
        new.click()

        name = self.tra.transit_agent_name()
        name.send_keys("Money Group")
        adress = self.tra.address()
        adress.send_keys("Kaloor")
        email = self.tra.email()
        email.send_keys("money@example.com")
        tel_num = self.tra.telephone_number()
        tel_num.send_keys("048402354789")

        cont_pers = self.tra.contact_person()
        cont_pers.send_keys("Bala fort Wiliam")
        cont_pers_num = self.tra.contact_person_number()
        cont_pers_num.send_keys("9784512365")
        city = self.tra.transit_agent_city()
        city.send_keys("Kochi")
        region = self.tra.region()
        region.send_keys("India")

        self.tra.buttton_save().click()