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
from Dinero_automation.pageObjects.Accounts_menu.self_depostis import Self_cash
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
        self.acc.click_self_cash().click()
        time.sleep(2)
        for i in range(4):
            cashw1000 = ["2", "4", "8" "9"]
            self.slf = Self_cash(self.driver)
            new = self.slf.click_new()
            new.click()

            bank = Select(self.slf.bank_account())
            bank.select_by_index(i+1)
            trans_agent = Select(self.slf.transit_agent())
            trans_agent.select_by_index(4)

            cash1000 = self.slf.cash1000()
            cash1000.send_keys(cashw1000[i])

            self.slf.click_save().click()
            time.sleep(2)

            self.slf.click_intiater().click()
            time.sleep(2)
            self.slf.click_intrasnit().click()
            time.sleep(2)

            self.slf.click_og_in_transit().click()
            time.sleep(2)
            self.slf.click_intransiter().click()
            time.sleep(2)
            self.slf.click_completed().click()
            time.sleep(2)

            self.slf.click_og_completed().click()
            time.sleep(2)
            self.slf.click_complterer().click()
