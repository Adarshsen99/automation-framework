import random
import string
import time

from DineroQa.Dinero_automation.utilities.randomString import generate_random_email_new
from Dinero_automation.testCases.Customer_Registration_Individual_editmode.personal_information_edit_mode_test import \
    generate_random_string
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_corporate_edit import Company_Information, Contact_Information, \
    Bank_Information, Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator, random_string_generator_new, \
    random_string_generator_max_30, random_string_generator_max_50, random_string_generator_max_28, \
    random_string_generator_max_48, random_string_generator_max_31, random_string_generator_max_51, \
    random_string_generator_numbers_new, random_string_generator_numbers
from selenium.webdriver.support.ui import Select


class Test_company_info_edit:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_email(self):
        return generate_random_string(5) + "@example.com"

    def test_going_to_editmode(self, setup):

        response = []

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

        # click action for customer registration
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
        build_name.send_keys(random_string_generator_new())
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
        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(4)

        document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

        if self.fp.editmode_message() == "You're in edit mode":
            response.append(document)
            self.return_url = document['root']['baseURL']
            assert True

        print(self.return_url)

        self.driver.quit()

    def test_relationship_value_missing(self, setup):
        ## testing on manual reports
        ## relationship field got emptied after saving

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

        drp_relation_val_bef = drp_relation.first_selected_option.text
        print("drp_relation_val_bef:", drp_relation_val_bef)

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

        # drp_relation = Select(self.ci.drp_relation())
        drp_relation = Select(self.ci.drp_relation())
        drp_relation_val_aft = drp_relation.first_selected_option.text

        print("drp_relation_val_aft:", drp_relation_val_aft)
        time.sleep(2)

        self.ci.btn_next()

        if drp_relation_val_bef == drp_relation_val_aft:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "self.ci.relationship_missing.png")
        assert False

        ## test case failed ( relationship is missing after saving )
        ## last tested on built 03/09/2024 - Adarsh Sen Madhu
