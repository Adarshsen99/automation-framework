import random
import string
import time

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib3.exceptions import MaxRetryError

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Remittance_details, Beneficiary_details, \
    Delegate_details, Payment_details, Transaction_Review
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

    def test_sending_docs(self, setup):

        # List of 4 different customer names
        customer_names = [
            "Pele Marie Jones",
            "Messi Marie Brown",
            "Mardona Rose Smith",
            "Dimaria Rose Jones"
        ]

        # Fixed values for lc, rate, and cash10 to be used across 4 iterations
        lc_values = [6000, 2000, 2500, 3000]
        rate_values = [25, 20, 25, 30]
        cash10_values = [3, 2, 3, 4]

        for i in range(4):
            responce = []
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)

            # Initialize page objects

            self.lp = LoginPage(self.driver)
            self.nav = Navigation_Page(self.driver)
            self.cd = Customer_Details(self.driver)
            self.rd = Remittance_details(self.driver)
            self.bd = Beneficiary_details(self.driver)
            self.dd = Delegate_details(self.driver)
            self.pd = Payment_details(self.driver)
            self.tr = Transaction_Review(self.driver)

            # Login
            self.lp.setUsername(self.uname)
            self.lp.setPassword(self.upass)
            self.lp.clickLogin()

            # Navigate to Remittance
            self.nav.click_navbar()
            self.nav.click_remitance()

            # Customer Details
            transcation_type = Select(self.cd.drp_transcation_type())
            transcation_type.select_by_index(1)

            # Use the customer name from the list based on the current iteration
            self.cd.customer_search_bar().send_keys(customer_names[i])
            self.cd.custom_select1()
            time.sleep(3)

            self.cd.btn_next()
            time.sleep(2)

            # Delegate Details
            transctn_mode = Select(self.dd.drp_transaction_mode())
            transctn_mode.select_by_index(1)
            time.sleep(2)
            self.dd.btn_nexte()
            time.sleep(2)

            # Beneficiary Details
            benefiary_name = self.bd.beneficiary_search_bar()
            benefiary_name.send_keys("ronaldo")
            self.bd.beneficiary_selectbar()
            time.sleep(2)
            bank_selct = Select(self.bd.drp_bank())
            bank_selct.select_by_index(1)
            time.sleep(1)
            self.bd.btn_nexte()
            time.sleep(2)

            # Remittance Details

            # Use values for LC and Rate from the lists based on the iteration index
            lc_value = lc_values[i]
            rate_value = rate_values[i]
            tax_value = random.randint(5, 15)

            transctn_pin = self.rd.transaction_pin()
            transctn_pin.send_keys(generate_random_digits(5))
            remittance_purpse = Select(self.rd.drp_remittance_purpose())
            remittance_purpse.select_by_index(2)
            sourc_inc = Select(self.rd.drp_source_of_income())
            sourc_inc.select_by_index(2)
            currenc = Select(self.rd.drp_currency())
            currenc.select_by_index(1)
            service_pro = Select(self.rd.drp_service_provider())
            service_pro.select_by_index(1)

            self.rd.click_cash()

            # Set the LC, rate, and tax with the assigned values
            lc = self.rd.lc_type_area()
            lc.send_keys(str(lc_value))
            rate = self.rd.rate_type_area()
            rate.send_keys(str(rate_value))  # Integer value from the list
            tax = self.rd.tax_typing()
            tax.send_keys(str(tax_value))  # Random tax value between 5 and 15
            time.sleep(3)
            self.rd.btn_nxtee()
            time.sleep(2)

            # Transaction review

            self.tr.btn_confrm()
            self.tr.confirm_yes_btn()
            time.sleep(2)

            # Scroll to the bottom of the page

            cash_element = self.pd.cash_ampunt()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
            time.sleep(2)  # Allow time for scrolling to finish
            cash_element.click()

            # Set values for thousand, hundred, and ten notes
            self.pd.cash1000().send_keys("1")
            self.pd.cash100().send_keys("2")

            # Use cash10 values from the list
            ten_value = cash10_values[i]
            self.pd.cash10().send_keys(str(ten_value))

            time.sleep(2)

            self.pd.submit()
            time.sleep(3)

            self.pd.save_remittance()
            time.sleep(5)

            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

            responce.append(document)
            for res in responce:
                print(res['root']['baseURL'])

        self.driver.quit()
