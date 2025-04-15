import random
import string
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Pulldownmenu import Account_pulldownmenu
from Dinero_automation.pageObjects.Accounts_menu.Withdrawal_Voucher import withdrawalVoucher
from Dinero_automation.utilities.readProperties import ReadConfig


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

    def test_sending_valid_data_cheque(self, setup):
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

        self.acc = Account_pulldownmenu(self.driver)
        account_menu = self.acc.click_account_menu()

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(account_menu).perform()
        time.sleep(1)
        self.acc.click_withdrawal_voucher().click()
        time.sleep(2)

        self.wd = withdrawalVoucher(self.driver)
        self.wd.create_new()

        bank_account = Select(self.wd.drp_bankaccount())
        bank_account.select_by_index(2)
        transit_agent = Select(self.wd.drp_transitagent())
        transit_agent.select_by_index(1)
        time.sleep(2)

        self.wd.cheque_number().send_keys("23132132")
        self.wd.cheque_amount().click()
        self.wd.cash1000().send_keys(2)
        self.wd.submit().click()
        time.sleep(1)
        self.wd.click_save().click()

    def test_adding_valid_data_card(self, setup):
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

        self.acc = Account_pulldownmenu(self.driver)
        account_menu = self.acc.click_account_menu()

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(account_menu).perform()
        time.sleep(1)
        self.acc.click_withdrawal_voucher().click()
        time.sleep(2)

        self.wd = withdrawalVoucher(self.driver)
        self.wd.create_new()

        bank_account = Select(self.wd.drp_bankaccount())
        bank_account.select_by_index(2)
        transit_agent = Select(self.wd.drp_transitagent())
        transit_agent.select_by_index(1)
        time.sleep(2)
        self.wd.click_card().click()
        time.sleep(3)
        debit_card = Select(self.wd.drp_creditcard())
        debit_card.select_by_index(1)
        card_amount = self.wd.card_amount()
        card_amount.click()
        cash_1000 = self.wd.cash1000()
        cash_1000.send_keys("25")
        self.wd.submit().click()



        time.sleep(1)
        self.wd.click_save().click()





        
