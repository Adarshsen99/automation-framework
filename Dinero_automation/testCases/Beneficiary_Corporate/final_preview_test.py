import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Corporate import Company_Information, Contact_Information, \
    Bank_Information, Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator, random_string_generator_numbers, \
    random_string_generator_new, generate_random_email_new, random_string_generator_numbers_new, \
    random_string_generator_max_30, random_string_generator_max_50, generate_random_email, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Company_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_saving_Benificiary_corporate(self, setup):
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

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
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
        time.sleep(3)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("CANARA")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kochi")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        time.sleep(2)
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

        if self.fp.editmode_message() == "You're in edit mode":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BEN_CO_FP_test_saving_Benificiary_corporate.png")
            assert False

        self.driver.quit()

    def test_saving_Benificiary_corporate_with_alredyreg_bank(self, setup):
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

        bank_name.send_keys("icici")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("1234")
        confirm_account_num.send_keys("1234")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(2)

        if self.fp.message_error() == "Account number already exist (Bank).":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BEN_CO_FP_test_saving_Benificiary_corporate_with_alredyreg_bank.png")
            assert False
        self.driver.quit()

    def test_saving_Benificiary_corporate_with_alredyreg_bank_with_update(self, setup):
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

        bank_name.send_keys("icici")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("1234")
        confirm_account_num.send_keys("1234")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(4)
        self.fp.btn_back()

        self.bi.click_index_bank()
        time.sleep(2)

        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()

        account_num.clear()
        confirm_account_num.clear()

        account_num.send_keys("12345")
        confirm_account_num.send_keys("12345")
        self.bi.btn_update()
        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(2)

        if self.fp.editmode_message() == "You're in edit mode":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BEN_CO_FP_test_saving_Benificiary_corporate_with_alredyreg_bank_with_update.png")
            assert False
        self.driver.quit()
