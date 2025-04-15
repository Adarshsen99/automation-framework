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
from Dinero_automation.pageObjects.Accounts_menu.vendor import Vendor_reg
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
        self.acc.click_vendor().click()
        time.sleep(2)

        self.ven = Vendor_reg(self.driver)
        self.ven.click_new().click()

        # Get all open window handles (tabs)
        window_handles = self.driver.window_handles

        # Switch to the new tab (the second tab should be the new one)
        self.driver.switch_to.window(window_handles[1])
        time.sleep(2)

        self.ven.click_both().click()
        comp_name = self.ven.company_name()
        comp_name.send_keys("Uncle John")
        arabic_name = self.ven.arabic_name()
        arabic_name.send_keys("Uncle John")
        buiding_num = self.ven.building_number()
        buiding_num.send_keys("432")
        building_name = self.ven.building_name()
        building_name.send_keys("Uncle's Godown")
        street = self.ven.street()
        street.send_keys("Golden road")
        post_code = self.ven.postal_code()
        post_code.send_keys("86546")
        city = self.ven.city()
        city.send_keys("Kaloor")
        country = Select(self.ven.country())
        country.select_by_visible_text("India")
        country_code = Select(self.ven.country_code())
        country_code.select_by_index(26)
        mob_no = self.ven.mob_number()
        mob_no.send_keys("9746552154")
        email = self.ven.email()
        email.send_keys("uncle@gmail.com")

        self.ven.click_next().click()

        coun_of_inco = Select(self.ven.country_of_incorp())
        coun_of_inco.select_by_visible_text("India")
        lisence = Select(self.ven.license_nature())
        lisence.select_by_index(2)
        entity = Select(self.ven.entity_type())
        entity.select_by_index(1)
        operations_field = Select(self.ven.operation_field())
        operations_field.select_by_index(1)
        trade = Select(self.ven.trade())
        trade.select_by_index(1)
        captital = self.ven.capital()
        captital.send_keys("50000")

        auth_pers = self.ven.Auth_person()
        auth_pers.send_keys("Rajendra Panickar")
        desgntn = Select(self.ven.designation())
        desgntn.select_by_index(3)
        nationality = Select(self.ven.nationality())
        nationality.select_by_visible_text("India")
        id_typ = Select(self.ven.IdType())
        id_typ.select_by_index(2)

        id_num = self.ven.Id_number()
        id_num.send_keys("4564565656")
        id_expiry = self.ven.id_expiry()
        id_expiry.send_keys("30012029")

        cr_num = self.ven.cr_number()
        cr_num.send_keys("4857465")
        cc_num = self.ven.cc_number()
        cc_num.send_keys("9754545")
        cr_issue_date = self.ven.cr_issue_date()
        cr_issue_date.send_keys("24012021")
        cc_issue_date = self.ven.cc_issue_date()
        cc_issue_date.send_keys("20081995")
        cr_expiry =  self.ven.cr_expiry_dt()
        cr_expiry.send_keys("26112039")
        cc_exp = self.ven.cc_exp_date()
        cc_exp.send_keys("23062088")

        self.ven.brn_save().click()
        

