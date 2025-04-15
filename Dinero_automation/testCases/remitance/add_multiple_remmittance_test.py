import random
import string
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Remittance_details, Beneficiary_details, \
    Delegate_details, Payment_details, Transaction_Review
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

    def test_sending_docs(self, setup):
        # List of 4 different customer names
        customer_names = [
            "RAJAKKAD BAKERY"

        ]

        # Fixed values for lc, rate, and cash10 to be used across 4 iterations
        lc_values = ["6000"]

        for i in range(1):
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

            Remi_pull = self.driver.find_element(By.XPATH,
                                                 "//div[@class='pullDwnMenu_Head'][normalize-space()='Remittance']")

            # Hover over the customer pull-down menu
            actions = ActionChains(self.driver)
            actions.move_to_element(Remi_pull).perform()

            # Locate and click the "Individual Customers" submenu
            remi_element = self.driver.find_element(By.XPATH,
                                                    "//div[normalize-space()='Outward Remittance']")
            remi_element.click()
            time.sleep(2)

            self.cd = Customer_Details(self.driver)
            self.rd = Remittance_details(self.driver)
            self.bd = Beneficiary_details(self.driver)
            self.dd = Delegate_details(self.driver)
            self.pd = Payment_details(self.driver)
            self.tr = Transaction_Review(self.driver)

            # Customer Details
            # transcation_type = Select(self.cd.drp_transcation_type())
            # transcation_type.select_by_index(1)

            # Use the customer name from the list based on the current iteration
            self.cd.customer_search_bar().send_keys(customer_names[i])
            self.cd.custom_selectcorp()
            time.sleep(2)
            self.cd.btn_verifyandnext().click()
            time.sleep(2)

            # Delegate Details
            # transctn_mode = Select(self.dd.drp_transaction_mode())
            # transctn_mode.select_by_index(2)
            time.sleep(2)
            self.dd.btn_nexte()
            time.sleep(2)

            # Beneficiary Details
            benefiary_name = self.bd.beneficiary_search_bar()
            benefiary_name.send_keys("Sharooq bin laden")
            self.bd.beneficiary_selectbar_man()
            time.sleep(2)
            bank_selct = Select(self.bd.drp_bank())
            bank_selct.select_by_index(1)
            time.sleep(1)
            self.bd.btn_nexte()
            time.sleep(2)

            # Remittance Details

            # Use values for LC and Rate from the lists based on the iteration index



            # transctn_pin = self.rd.transaction_pin()
            # transctn_pin.send_keys(generate_random_digits(5))
            remittance_purpse = Select(self.rd.drp_remittance_purpose())
            remittance_purpse.select_by_index(2)
            sourc_inc = Select(self.rd.drp_source_of_income())
            sourc_inc.select_by_index(2)
            currenc = Select(self.rd.drp_currency())
            currenc.select_by_index(1)
            service_pro = Select(self.rd.drp_service_provider())
            service_pro.select_by_visible_text("INNOVATIVE TECHNOLOGIES")

            self.rd.click_cash()

            # Set the LC, rate, and tax with the assigned values
            lc = self.rd.lc_type_area()
            lc.send_keys(lc_values[i])
            # rate = self.rd.rate_type_area()
            # rate.send_keys(str(rate_value))  # Integer value from the list
            # tax = self.rd.tax_typing()
            # tax.send_keys("0")  # Random tax value between 5 and 15
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
            cash_element.send_keys("5000")

            time.sleep(2)

            self.pd.submit()
            time.sleep(3)

            self.pd.verifyand_proceed()
            time.sleep(5)
