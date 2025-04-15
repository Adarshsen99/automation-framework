import string
import time
from random import random

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
from Dinero_automation.pageObjects.Accounts_menu.local_bank import Add_banks, Account_profile
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
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        self.acc = Account_pulldownmenu(self.driver)
        account_menu = self.acc.click_account_menu()

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(account_menu).perform()
        time.sleep(1)
        self.acc.click_local_bank().click()
        time.sleep(2)

        for i in range(5):
            banknames = ["Loss Bank", "Capital Bank", "Unity Bank", "Future Bank", "Crescent Bank"]
            branchnames = ["Downtown Branch", "Central Avenue Branch", "Eastside Branch", "Lakeshore Branch",
                           "Westpark Branch"]
            branch_short_nme = ["DTB", "CAB", "ESB", "LSB", "WPB"]
            bank_short_nms = ["LSB", "CAP", "UNT", "FUT", "CRS"]
            cont_pers = ["John Smith", "Alice Johnson", "Rajesh Kumar", "Fatima Ahmed", "Carlos Garcia"]
            branch_cds = ["B001", "B002", "B003", "B004", "B005"]

            self.add_b = Add_banks(self.driver)
            self.add_b.add_bank_click().click()
            time.sleep(2)

            bank_name = self.add_b.bank_name()
            bank_name.send_keys(banknames[i])
            bank_short_name = self.add_b.Bank_short_name()
            bank_short_name.send_keys(bank_short_nms[i])
            arabic_name = self.add_b.arabic_name()
            arabic_name.send_keys(banknames[i])
            branch_code = self.add_b.branch_code()
            branch_code.send_keys(branch_cds[i])
            branch_name = self.add_b.branch_name()
            branch_name.send_keys(branchnames[i])
            branch_short_name = self.add_b.branch_short_name()
            branch_short_name.send_keys(branch_short_nme[i])
            contact_person = self.add_b.contact_person()
            contact_person.send_keys(cont_pers[i])
            designation = self.add_b.designation()
            designation.send_keys("Sweeper/ peon")
            telephone = self.add_b.telephone_no()
            telephone.send_keys("0484" + random_string_generator_numbers(7))
            mob_no = self.add_b.mob_no()
            mob_no.send_keys(random_string_generator_numbers(9))

            self.acp = Account_profile(self.driver)
            self.acp.click_account_profile().click()
            time.sleep(2)

            acc_typ = Select(self.acp.drp_account_type())
            acc_typ.select_by_index(3)
            curr = Select(self.acp.drp_currency())
            curr.select_by_visible_text("Qatari Rial")
            acc_num = self.acp.account_num()
            acc_num.send_keys(random_string_generator_numbers(9))
            Iban = self.acp.IBAN_num()
            Iban.send_keys(random_string_generator_numbers(5))
            self.acp.over_draft_click().click()
            over_draft_lim = self.acp.overdraft_limit()
            over_draft_lim.send_keys("900000")

            card1 = Select(self.acp.cardType_1())
            card1.select_by_index(1)
            card_number_1 = self.acp.card_number_1()
            card_number_1.send_keys(random_string_generator_numbers(9))
            cardExp1 = self.acp.card_expiry_1()
            cardExp1.send_keys("22122055")
            cardlimit1 = self.acp.card_limit_1()
            cardlimit1.send_keys("500000")

            self.acp.click_new_card_row().click()
            time.sleep(3)

            card2 = Select(self.acp.cardType_2())
            card2.select_by_index(2)
            card_number_2 = self.acp.card_number_2()
            card_number_2.send_keys(random_string_generator_numbers(9))
            cardExp2 = self.acp.card_expiry_2()
            cardExp2.send_keys("22122055")
            cardlimit2 = self.acp.card_limit_2()
            cardlimit2.send_keys("500000")

            self.acp.pos_enabled().click()
            self.acp.cover_up_fund().click()
            time.sleep(2)

            fund_curr1 = Select(self.acp.drp_fund_curr_1())
            fund_curr1.select_by_visible_text("US Dollar")
            daily_fund_lim1 = self.acp.daily_fund_lim_1()
            daily_fund_lim1.send_keys("60000")
            rate1 = self.acp.fund_rate_1()
            rate1.send_keys("3.65")

            self.acp.new_fund_row().click()
            time.sleep(3)

            fund_curr2 = Select(self.acp.drp_fund_curr_2())
            fund_curr2.select_by_visible_text("Euro")
            daily_fund_lim2 = self.acp.daily_fund_lim_2()
            daily_fund_lim2.send_keys("60000")
            rate2 = self.acp.fund_rate_2()
            rate2.send_keys("3.85")

            self.acp.Add_click().click()
            time.sleep(2)

            self.acp.click_update().click()
            time.sleep(2)
