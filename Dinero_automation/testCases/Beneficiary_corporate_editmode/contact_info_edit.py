import string
import time

from random import random

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_corporate_edit import Company_Information,Contact_Information,Bank_Information,Final_Preview
from Dinero_automation.testCases.Customer_Registration_Individual_editmode.personal_information_edit_mode_test import \
    generate_random_string
from Dinero_automation.utilities.randomString import generate_random_email_new,random_string_generator_numbers,random_string_generator_numbers_new,random_string_generator_new,random_string_generator,random_string_generator_max_30,random_string_generator_max_50,generate_random_email,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig

class Test_Contact_info_editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_email(self, length):
        return generate_random_string(5) + "@example.com"

    def test_null_value_field(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for corporate beneficiary
        self.nav.click_benificiary_corporate()
        time.sleep(2)

        self.ci = Company_Information(self.driver)
        self.con_info = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)
        self.fp = Final_Preview(self.driver)

        # Assigning data
        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)
        self.ci.btn_next()

        build_num = self.con_info.building_number()
        # build_name = self.con_info.building_name()
        street = self.con_info.street()
        city_dist = self.con_info.city_district()
        drp_country = Select(self.con_info.drp_country())
        drp_country_code = Select(self.con_info.drp_country_code())
        mobile_num = self.con_info.mobile_number()
        email = self.con_info.email()

        build_num.send_keys(random_string_generator_numbers_new())
        # build_name.send_keys(random_string_generator_new())
        street.send_keys(random_string_generator())
        city_dist.send_keys(random_string_generator())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys(random_string_generator_numbers())
        email.send_keys(generate_random_email_new())

        self.con_info.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("pun")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kod")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(4)

        self.ci.btn_next()
        time.sleep(2)
        self.con_info.btn_next()
        build_num_val_before = self.con_info.building_name().get_attribute("value")
        print("build_num_val_before:",build_num_val_before)
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(4)

        # time.sleep(2)
        # self.bi.btn_next()
        # time.sleep(2)
        # self.fp.btn_save().click()
        # time.sleep(4)

        self.ci.btn_next()
        time.sleep(2)



        self.con_info.btn_next()
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(4)
        # time.sleep(2)
        # self.bi.btn_next()
        # self.fp.btn_save().click()
        # time.sleep(4)

        self.ci.btn_next()
        time.sleep(2)
        self.con_info.btn_next()
        build_num_val_after = self.con_info.building_name().get_attribute("value")
        print("build_num_val_after:",build_num_val_after)
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)

        self.fp.btn_save().click()
        time.sleep(4)
        self.ci.btn_next()
        time.sleep(2)

        time.sleep(2)

        ### test failed ( null value is showing on field )
        ### last passed on built 03/09/2024 - Adarsh Sen Madhu

    def test_null_value_in_preview(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for corporate beneficiary
        self.nav.click_benificiary_corporate()
        time.sleep(2)

        self.ci = Company_Information(self.driver)
        self.con_info = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)
        self.fp = Final_Preview(self.driver)

        # Assigning data
        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)
        self.ci.btn_next()

        build_num = self.con_info.building_number()
        build_name = self.con_info.building_name()
        street = self.con_info.street()
        city_dist = self.con_info.city_district()
        drp_country = Select(self.con_info.drp_country())
        drp_country_code = Select(self.con_info.drp_country_code())
        mobile_num = self.con_info.mobile_number()
        email = self.con_info.email()

        build_num.send_keys(random_string_generator_numbers_new())
        # build_name.send_keys(random_string_generator_new())
        street.send_keys(random_string_generator())
        city_dist.send_keys(random_string_generator())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys(random_string_generator_numbers())
        email.send_keys(generate_random_email_new())

        build_name = self.con_info.building_name()
        print("build name",build_name.get_attribute('value'))

        self.con_info.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("pun")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kod")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(4)
        self.ci.btn_next()
        time.sleep(2)
        self.con_info.btn_next()
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(4)
        self.ci.btn_next()
        time.sleep(4)
        self.con_info.btn_next()
        time.sleep(4)
        self.bi.click_contact_info_pre()
        time.sleep(3)
        print("build name preview", self.bi.building_name_pre())

        ## test case failed ( null value showing in preview)
        ## last tested on built 03/09/2024 - Adarsh sen madhu
























