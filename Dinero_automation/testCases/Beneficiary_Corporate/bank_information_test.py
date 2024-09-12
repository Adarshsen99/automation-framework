import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Corporate import Company_Information,Contact_Information,Bank_Information,Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator,random_string_generator_numbers,random_string_generator_new,generate_random_email_new,random_string_generator_numbers_new,random_string_generator_max_30,random_string_generator_max_50,generate_random_email,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Company_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    def test_with_add_bank(self, setup):
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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_valid_data.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_diff_ac_num(self, setup):
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
        account_num.send_keys("12345789")
        confirm_account_num.send_keys("32145789")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_diff_ac_num.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_spchar(self, setup):
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
        account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        confirm_account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message_2()
        if not error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_diff_ac_num.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_char(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("qwertyuiop")
        confirm_account_num.send_keys("qwertyuiop")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message()
        print(error_msg)
        #
        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_with_char.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_only_account_num(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_with_only_account_num.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_only_account_number(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_with_only_account_number.png")
            assert False

        self.driver.quit()

    def test_without_adding_bank_click_next(self, setup):
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
        self.bi.btn_next()
        time.sleep(4)

        print(self.fp.btn_save().is_enabled())

        if not self.fp.btn_save().is_enabled() == True:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_without_adding_bank_click_next.png")
            assert False

        self.driver.quit()

    def test_without_adding_bank(self, setup):
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
        self.bi.btn_add_bank()
        time.sleep(4)

        error_msg = self.bi.message()

        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_without_adding_bank.png")
            assert False

        self.driver.quit()

    def test_adding_bank_next_back_clear(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text

        print(acc_type_val, currency_val)

        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_back()
        time.sleep(2)
        self.bi.btn_clear()

        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        acc_type_af = acc_type.first_selected_option.text
        currency_af = currency.first_selected_option.text


        print(acc_type_af, currency_af)

        time.sleep(2)

        if acc_type_val == acc_type_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_bank_next_back_clear_acc_type.png")
            assert False

        if currency_val == currency_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_bank_next_back_clear_currency.png")
            assert False

        self.driver.quit()

    def test_adding_bank_without_bank_branch(self, setup):
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

        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        # bank_name.send_keys("sbi")
        # click_bank = self.bi.click_bank_name()
        # click_bank.click()
        # branch_name.send_keys("kaloor")
        # click_branch = self.bi.click_branch_name()
        # click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(3)

        error_msg = self.bi.message()

        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_bank_without_bank_branch.png")
            assert False

        self.driver.quit()

    def test_adding_bank_with_same_bank_branch(self, setup):
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

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(3)

        error_msg = self.bi.meassage_text()

        if error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_bank_with_same_bank_branch.png")
            assert False

        self.driver.quit()

    def test_adding_bank_with_same_account_diff_bank_branch(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()

        error_msg = self.bi.meassage_text()

        if not error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_bank_with_same_account_diff_bank_branch.png")
            assert False

        self.driver.quit()

    def test_adding_multilple_bank_account(self, setup):
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
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back()
        time.sleep(2)

        error_msg = self.bi.meassage_text()

        if not error_msg == "Bank already exists in the list.":
            assert True

        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_adding_multilple_bank_account.png")
            assert False

        self.driver.quit()

    def test_updating_account_number(self, setup):
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
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        bank_name_val_bf = bank_name.get_attribute('value')
        branch_name_val_bf = branch_name.get_attribute('value')
        account_num_val_bf = account_num.get_attribute('value')
        confirm_account_num_val_bf = confirm_account_num.get_attribute('value')
        acc_type_val_bf = acc_type.first_selected_option.text
        currency_val_bf = currency.first_selected_option.text

        print(
            bank_name_val_bf,
            branch_name_val_bf,
            account_num_val_bf,
            confirm_account_num_val_bf,
            acc_type_val_bf,
            currency_val_bf
        )

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back()
        time.sleep(2)

        self.bi.banks_data_1().click()
        time.sleep(3)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        account_num.clear()
        account_num.send_keys("123456789")
        confirm_account_num.clear()
        confirm_account_num.send_keys("123456789")
        acc_type.select_by_index(1)
        currency.select_by_index(1)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text

        print(
            bank_name_val,
            branch_name_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val

        )

        if bank_name_val_bf == bank_name_val:
            assert True
        else:
            assert False

        if branch_name_val_bf == branch_name_val:
            assert True
        else:
            assert False

        if account_num_val_bf != account_num_val:
            assert True
        else:
            assert False

        if confirm_account_num_val_bf != confirm_account_num_val:
            assert True
        else:
            assert False

        if acc_type_val_bf != acc_type_val:
            assert True
        else:
            assert False

        if currency_val_bf != currency_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_updating_account_number_with_same_bank_and_branch(self, setup):
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

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        bank_name_val_bf = bank_name.get_attribute('value')
        branch_name_val_bf = branch_name.get_attribute('value')
        account_num_val_bf = account_num.get_attribute('value')
        confirm_account_num_val_bf = confirm_account_num.get_attribute('value')
        acc_type_val_bf = acc_type.first_selected_option.text
        currency_val_bf = currency.first_selected_option.text

        print(
            "Before:",
            bank_name_val_bf,
            branch_name_val_bf,
            account_num_val_bf,
            confirm_account_num_val_bf,
            acc_type_val_bf,
            currency_val_bf

        )

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back()
        time.sleep(2)

        self.bi.banks_data_1().click()

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.clear()
        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.clear()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.clear()
        account_num.send_keys("4578965544")
        confirm_account_num.clear()
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(1)
        currency.select_by_index(1)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text

        print(
            "After:",
            bank_name_val,
            branch_name_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val
        )
        self.bi.btn_update()
        time.sleep(2)

        error_msg = self.bi.meassage_text()

        if error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BEN_CO_BANKINFO_test_updating_account_number_with_same_bank_and_branch.png")
            assert False

        self.driver.quit()

    def test_validating_preview(self, setup):
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
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text

        branch_val = self.bi.branch_address().get_attribute('value')
        branch_code_val = self.bi.branch_code().get_attribute('value')

        print(
            bank_name_val,
            branch_name_val,
            branch_val,
            branch_code_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val

        )

        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_back()
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.click_bank_info_preview()

        print(
            self.bi.bank_name_pre(),
            self.bi.branch_name_pre(),
            self.bi.branch_address_pre(),
            self.bi.branch_code_pre(),
            self.bi.account_num_pre(),
            self.bi.confirm_account_num_pre(),
            self.bi.account_type_pre(),
            self.bi.currency_pre())

        if bank_name_val == self.bi.bank_name_pre():
            assert True
        else:
            assert False

        if branch_name_val == self.bi.branch_name_pre():
            assert True
        else:
            assert False

        if branch_val == self.bi.branch_address_pre():
            assert True
        else:
            assert False

        if branch_code_val == self.bi.branch_code_pre():
            assert True
        else:
            assert False

        if account_num_val == self.bi.account_num_pre():
            assert True
        else:
            assert False

        if confirm_account_num_val == self.bi.confirm_account_num_pre():
            assert True
        else:
            assert False

        if acc_type_val == self.bi.account_type_pre():
            assert True
        else:
            assert False

        if currency_val == self.bi.currency_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_after_update_preview(self, setup):
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
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text

        branch_val = self.bi.branch_address().get_attribute('value')
        branch_code_val = self.bi.branch_code().get_attribute('value')

        print(
            bank_name_val,
            branch_name_val,
            branch_val,
            branch_code_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val

        )

        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_back()
        time.sleep(2)
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.btn_update()
        time.sleep(4)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_back()
        time.sleep(2)
        self.bi.click_bank_info_preview()
        time.sleep(4)

        print(
            self.bi.bank_name_pre(),
            self.bi.branch_name_pre(),
            self.bi.branch_address_pre(),
            self.bi.branch_code_pre(),
            self.bi.account_num_pre(),
            self.bi.confirm_account_num_pre(),
            self.bi.account_type_pre(),
            self.bi.currency_pre())
        if bank_name_val == self.bi.bank_name_pre():
            assert True
        else:
            assert False

        if branch_name_val == self.bi.branch_name_pre():
            assert True
        else:
            assert False

        if branch_val == self.bi.branch_address_pre():
            assert True
        else:
            assert False

        if branch_code_val == self.bi.branch_code_pre():
            assert True
        else:
            assert False

        if account_num_val == self.bi.account_num_pre():
            assert True
        else:
            assert False

        if confirm_account_num_val == self.bi.confirm_account_num_pre():
            assert True
        else:
            assert False

        if acc_type_val == self.bi.account_type_pre():
            assert True
        else:
            assert False

        if currency_val == self.bi.currency_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_updating_second_bank(self, setup):
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
        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back()
        self.bi.banks_data_1().click()
        time.sleep(2)
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        time.sleep(2)
        self.bi.banks_data_2().click()
        time.sleep(2)
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        time.sleep(2)
        click_branch = self.bi.click_branch_name_second()
        print(click_branch.text)

        # if click_branch.click():
        #     assert True
        # else:
        #     assert False

        self.driver.quit()

    def test_maxlength(self, setup):
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
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()

        account_num = account_num.get_attribute('maxlength')
        confirm_account_num = confirm_account_num.get_attribute('maxlength')

        print("maxlength of account number:", account_num)
        print("maxlength of confirm account number:", confirm_account_num)

        if account_num == confirm_account_num:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_click_update_and_click_save(self, setup):
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

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name_second()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name_second()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back()
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.btn_update()
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(2)

        print(self.fp.meassge_final())

        if not self.fp.meassge_final() == "Field 'id' expected a number but got ''.":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BEN_CO_BANKINFO_test_click_update_and_click_save.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_without_drps(self, setup):
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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)

        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message()
        #
        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_BANKINFO_test_with_add_bank_without_drps.png")
            assert False

        self.driver.quit()