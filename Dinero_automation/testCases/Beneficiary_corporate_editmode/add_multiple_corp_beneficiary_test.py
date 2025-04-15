import string
import time

from random import random

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_corporate_edit import Company_Information, Contact_Information, \
    Bank_Information, Final_Preview

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

    def generate_random_email(self):
        return generate_random_string(5) + "@example.com"

    def test_sending_docs(self, setup):
        # Lists of details for each corporate beneficiary
        company_names = ["Greenstone Ventures Ltd.", "Horizon Capital Partners Inc.", "Quantum Innovations Group",
                         "BrightPath Investments LLC", "Unity Global Holdings", "Silverline Finance Corporation",
                         "Evergreen Resources Limited", "Pinnacle Wealth Management", "Aurora Trust Company",
                         "BlueSky Equity Partners"]

        streets = ["123 Maple Avenue", "456 Oak Street", "789 Cedar Lane", "101 Pine Drive", "202 Elm Road",
                   "303 Willow Way", "404 Birch Street", "505 Chestnut Avenue", "606 Maplewood Lane",
                   "707 Poplar Street"]

        cities = ["New York", "Los Angeles", "San Francisco", "Chicago", "Houston", "Miami", "Seattle", "Boston",
                  "Atlanta", "Dallas"]

        emails = ["contact@greenstoneventures.com", "info@horizoncapital.com", "support@quantuminnovations.com",
                  "services@brightpathinvestments.com", "inquiries@unityglobal.com", "hello@silverlinefinance.com",
                  "contact@evergreenresources.com", "team@pinnaclewealth.com", "info@auroratrust.com",
                  "admin@blueskyequity.com"]

        # Main loop
        for i in range(10):
            responce = []

            # login setup
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.lp = LoginPage(self.driver)
            self.lp.setUsername(self.uname)
            self.lp.setPassword(self.upass)
            self.lp.clickLogin()

            # click action for nav bar arrow and corporate beneficiary
            self.nav = Navigation_Page(self.driver)
            self.nav.click_navbar()
            self.nav.click_benificiary_corporate()
            time.sleep(2)

            # Assigning data
            self.ci = Company_Information(self.driver)
            self.ci.company_name().send_keys(company_names[i])
            self.ci.short_name().send_keys(company_names[i][:10])  # Example: Short name as first 10 chars
            Select(self.ci.drp_country_of_incorporation()).select_by_index(14)
            self.ci.btn_next()

            # Contact Information
            self.con_info = Contact_Information(self.driver)
            self.con_info.building_number().send_keys("Bldg " + str(i + 1))  # Sample building number
            self.con_info.building_name().send_keys("Building " + str(i + 1))
            self.con_info.street().send_keys(streets[i])
            self.con_info.city_district().send_keys(cities[i])
            Select(self.con_info.drp_country()).select_by_index(2)
            Select(self.con_info.drp_country_code()).select_by_index(6)
            self.con_info.mobile_number().send_keys(random_string_generator_numbers())  # Sample number
            self.con_info.email().send_keys(emails[i])
            self.con_info.btn_next()
            time.sleep(3)

            # Bank Information
            self.bi = Bank_Information(self.driver)
            bank_name = self.bi.send_bank_name()
            # branch_name = self.bi.send_branch_name()
            account_num = self.bi.account_number()
            confirm_account_num = self.bi.confirm_account_numb()
            acc_type = Select(self.bi.drp_account_type())
            currency = Select(self.bi.drp_currency())

            bank_name.send_keys("canara")
            self.bi.click_bank_name()

            time.sleep(2)
            branch_name = self.bi.send_branch_name()
            branch_name.send_keys("kochi")
            click_branch = self.bi.click_branch_name()
            click_branch.click()

            # bank_name.send_keys("canara")
            # self.bi.click_bank_name()
            #
            # time.sleep(2)
            acc_no = random_string_generator_numbers_new()
            account_num.send_keys(acc_no)
            confirm_account_num.send_keys(acc_no)
            acc_type.select_by_index(2)
            currency.select_by_index(2)
            self.bi.btn_next()
            self.fp = Final_Preview(self.driver)
            self.fp.btn_save().click()
            time.sleep(4)

            # Capture response document
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
            responce.append(document)
            for res in responce:
                print(res['root']['baseURL'])

        self.driver.quit()
