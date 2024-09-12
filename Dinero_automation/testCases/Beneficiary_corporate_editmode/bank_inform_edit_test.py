import string
import time

from random import random

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_corporate_edit import Company_Information, Contact_Information, \
    Bank_Information, Final_Preview
from Dinero_automation.testCases.Customer_Registration_Individual_editmode.personal_information_edit_mode_test import \
    generate_random_string
from Dinero_automation.utilities.randomString import generate_random_email_new, random_string_generator_numbers, \
    random_string_generator_numbers_new, random_string_generator_new, random_string_generator, \
    random_string_generator_max_30, random_string_generator_max_50, generate_random_email, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Bank_inform_edit:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_email(self, length):
        return generate_random_string(5) + "@example.com"

    def test_bank_values_remain_after_delete(self, setup):

        # test according to manual reports
        # bank values remaining after deleting bank account and save without error

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

        branch_name_val_before = branch_name.get_attribute("value")
        print("branch_name_val_before:", branch_name_val_before)

        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        account_num_val_before = account_num.get_attribute("value")
        print("account_num_val_before:", account_num_val_before)

        confirm_account_num.send_keys(acc_no)
        confirm_account_num_val_before = confirm_account_num.get_attribute("value")
        print("confirm_account_num_val_before:", confirm_account_num_val_before)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()

        time.sleep(3)
        self.bi.btn_bank_table()
        time.sleep(4)
        self.bi.btn_bank_dlt()
        time.sleep(4)
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name_val_after = branch_name.get_attribute("value")
        print("branch_name_val_after:", branch_name_val_after)
        account_num_val_after = account_num.get_attribute("value")
        print("account_num_val_after:", account_num_val_after)
        confirm_account_num.send_keys(acc_no)
        confirm_account_num_val_after = confirm_account_num.get_attribute("value")
        print("confirm_account_num_val_after:", confirm_account_num_val_after)
        self.bi.btn_update()
        time.sleep(2)

        if branch_name_val_before != branch_name_val_after:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "fp_error_messsage_not_proper.png")
            assert False
        if account_num_val_before != account_num_val_after:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "fp_error_messsage_not_proper.png")
            assert False

        ### test case failed( fields are not clearing after deleting an entire bank after selecting it)
        ## last tested on built 03/09/2024- Adarsh Ssn Madhu

    def test_accounnum_confirm_numbers_notsame(self, setup):

        # test according to manual reports
        # confirm account number field is not equal to account number

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
        account_num = self.bi.account_number()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        acc_no_len = int(account_num.get_attribute('maxlength'))
        print("acc_no_len:", acc_no_len)

        confirm_account_num = self.bi.confirm_account_numb()
        confirm_account_num.send_keys(acc_no)
        confirm_account_num_len = int(confirm_account_num.get_attribute('maxlength'))
        print("confirm_account_num_len:", confirm_account_num_len)

        if acc_no_len == confirm_account_num_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "bi_test_validity_max_length_accountnum.png")
            assert False

        ## test failed( numbers are different)
        ## tested on last built 03/09/2024

    def test_clear_bank_info_details(self, setup):

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

        # drp_account_type_val_bef = acc_type.first_selected_option.text
        # print(" drp_account_type_val_bef:", drp_account_type_val_bef)
        #
        # drp_currency_val_bef = currency.first_selected_option.text
        # print(" drp_currency_val_bef:", drp_currency_val_bef)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        time.sleep(2)
        self.bi.btn_back()
        time.sleep(2)
        self.bi.btn_bank_table()
        time.sleep(3)
        self.bi.btn_clear()

        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        drp_account_type_val_aft = acc_type.first_selected_option.text
        print("  drp_account_type_val_aft:", drp_account_type_val_aft)

        drp_currency_val_aft = currency.first_selected_option.text
        print(" drp_currency_val_aft:", drp_currency_val_aft)

        time.sleep(4)

        if not drp_account_type_val_aft:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "clear_bank.png")
            assert False

        if not drp_currency_val_aft:
            # print("True", drp_currency_val_aft)
            assert True
        else:
            print("false", drp_currency_val_aft)
            self.driver.save_screenshot(screenShort.screen_short() + "clear_bank.png")
            assert False

            ## test failed (values remains there after clearing)
            ## last tested on built 03/09/2024- Adarsh Sen Madhu

    def test_saving_without_accountnum_and_currency(self, setup):

        # testing based on manual reports
        # bank can be saved without account type and currency even if it is mandatory

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
        # acc_type.select_by_index(2)
        # currency.select_by_index(2)
        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        if self.bi.error_message == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "accountype_notfilled_bank.png")
            assert False

            ## test failed( we can add bank without account type and currency
            ### last tested on built 03/09/2024 -Adarsh Sen Madhus

    def test_while_updating_branch_value_dissappers(self, setup):
        # testing based on manual report
        # if adding  banks and trying to update second bank the branch name is not showing automatically

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

        bank_name.send_keys("pun")
        click_bank2 = self.bi.click_bank_name_second()
        click_bank2.click()
        branch_name.send_keys("kod")
        click_branch2 = self.bi.click_branch_name_second()
        click_branch2.click()

        branch_name_val_1st = branch_name.get_attribute("value")
        print("branch_name_val_1st:", branch_name_val_1st)

        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        # bank_name.send_keys("pun")
        # click_bank = self.bi.click_bank_name()
        # click_bank.click()
        # branch_name.send_keys("kod")
        # click_branch = self.bi.click_branch_name()
        # click_branch.click()
        # acc_no = random_string_generator_numbers_new()
        # account_num.send_keys(acc_no)
        # confirm_account_num.send_keys(acc_no)
        # acc_type.select_by_index(2)
        # currency.select_by_index(2)
        # time.sleep(2)
        # self.bi.btn_add_bank()

        # time.sleep(2)

        self.bi.btn_bank_table()
        time.sleep(2)

        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        time.sleep(2)

        click_branch = self.bi.click_branch_name_second()
        click_branch.click()

        time.sleep(2)

        self.bi.btn_bank_table2().click()

        click_bank2 = self.bi.click_bank_name_second()
        click_bank2.click()
        # click_branch2 = self.bi.click_branch_name()
        # click_branch2.click()
        time.sleep(3)

        branch_name_val_2nt = branch_name.get_attribute("value")
        print("branch_name_val_2nt:", branch_name_val_2nt)

        if branch_name_val_1st == branch_name_val_2nt:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "branchupdate_bank.png")
            assert False

            ## test case failed( branch is not showing on clicking)
            ## tested on built 03/09/2024- Adarsh Sen Madhu

    def test_account_type_currency_notcleared_to_save(self, setup):

        # testing based on manual reports
        ## after clearing values the account type and currency remains there but when updating other fields and tries to save these values are missing

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
        self.bi.btn_back()
        time.sleep(2)
        self.bi.btn_bank_table()
        time.sleep(3)
        self.bi.btn_clear()
        time.sleep(3)
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        bank_name.send_keys("pun")
        click_bank2 = self.bi.click_bank_name_second()
        click_bank2.click()
        branch_name.send_keys("kod")
        click_branch2 = self.bi.click_branch_name_second()
        click_branch2.click()
        time.sleep(2)
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)

        acc_type_val = Select(self.bi.drp_account_type()).first_selected_option.text
        currenc = Select(self.bi.drp_currency()).first_selected_option.text

        print("acc_type_val", acc_type_val)
        print("currenc", currenc)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_bank_table2().click()
        time.sleep(2)

        if acc_type_val == "NRI Account":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "acctypesavungs_bank.png")
            assert False









