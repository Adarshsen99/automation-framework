import string
import time

from random import random

from selenium.webdriver.common.by import By

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Chart_of_accounts import adding_account

from Dinero_automation.utilities.randomString import generate_random_email_new, random_string_generator_numbers, \
    random_string_generator_numbers_new, random_string_generator_new, random_string_generator, \
    random_string_generator_max_30, random_string_generator_max_50, generate_random_email, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


class TestSendingDocs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def test_sending_docs(self, setup):

        # List of chart of account names without underscores
        account_names = [
             "Service Revenue", "Interest Income", "Rental Income",
            "Commission Income", "Cost of Goods Sold", "Salaries and Wages",
            "Rent Expense", "Utilities Expense", "Marketing and Advertising"
        ]

        for i in range(9):
            responce = []
            # login setup
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.lp = LoginPage(self.driver)
            time.sleep(12)

            # click action for nav bar arrow
            self.nav = Navigation_Page(self.driver)
            self.nav.click_navbar()

            sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

            # Locate the "Remittance" element inside the sidebar container
            self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
            time.sleep(2)
            self.nav.click_chart_of_account()
            time.sleep(3)

            self.ad = adding_account(self.driver)

            new_btn = self.ad.new_btn()
            self.driver.execute_script("arguments[0].scrollIntoView(0,200);", new_btn)
            time.sleep(2)

            # Optionally, interact with the element after scrolling into view
            new_btn.click()

            time.sleep(2)
            # Set account name and Arabic name to the same value from the account_names list
            account_name = account_names[i]
            self.ad.account_name().send_keys(account_name)
            self.ad.arabic_name().send_keys(account_name)  # Arabic name set to same as account name
            time.sleep(2)

            self.ad.suffix().send_keys(random_string_generator_numbers(5))
            time.sleep(3)

            self.ad.save_btn().click()
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
            responce.append(document)
            for res in responce:
                print(res['root']['baseURL'])

        self.driver.quit()
