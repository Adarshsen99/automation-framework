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

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def test_add_mul_bank(self, setup):

        responce = []

        # Arrays holding bank names and local bank names
        bank_nam = ["Industrial Bank", "South Indian Bank", "Canara Bank", "Kerala Grameen Bank",
                    "Union Bank", "Indian Bank", "Federal Bank", "Dhanalakshmi Bank", "IDBI Bank", "RBI"]
        bank_loc_name = ["Industrial Bank", "South Indian Bank", "Canara Bank", "Kerala Grameen Bank",
                         "Union Bank", "Indian Bank", "Federal Bank", "Dhanalakshmi Bank", "IDBI Bank", "RBI"]

        # Run the test 10 times
        for i in range(10):
            # login setup
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)
            self.lp = LoginPage(self.driver)
            self.lp.setUsername(self.uname)
            self.lp.setPassword(self.upass)
            self.lp.clickLogin()
            # time.sleep(2)

            # click action for nav bar arrow
            self.nav = Navigation_Page(self.driver)
            self.nav.click_navbar()
            # time.sleep(2)
            self.nav.click_bank()
            time.sleep(2)

            self.add_bank = Add_Bank(self.driver)
            time.sleep(3)
            self.add_bank.btn_add_bank()

            # Accessing form fields
            bank_name_field = self.add_bank.bank_name()
            bank_loc_name_field = self.add_bank.bank_name_local_language()
            bank_cod = self.add_bank.bank_code()
            drp_count = Select(self.add_bank.drp_country())
            btn_sav = self.add_bank.btn_save_bank()

            # Iterating over bank names and bank local names
            bank_name_field.send_keys(bank_nam[i])
            bank_loc_name_field.send_keys(bank_loc_name[i])
            bank_cod.send_keys(random_string_generator())
            drp_count.select_by_visible_text("India")
            self.add_bank.btn_save_bank()
            time.sleep(2)

            # Capture the response for debugging or verification
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
            responce.append(document)

            for res in responce:
                print(res['root']['baseURL'])

        self.driver.quit()
