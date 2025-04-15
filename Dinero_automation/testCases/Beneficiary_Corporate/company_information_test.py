import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Corporate import Company_Information, Contact_Information, \
    Bank_Information, Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator, random_string_generator_new, \
    random_string_generator_max_30, random_string_generator_max_50, random_string_generator_max_28, \
    random_string_generator_max_48, random_string_generator_max_31, random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Company_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_with_valid_data(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_with_valid_data.png")
            assert False
        self.driver.quit()

    def test_without_data(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())

        # comp_name.send_keys("Zooker Technology")
        # short_name.send_keys("Zooker")
        # drp_count_of_incorp.select_by_index(14)

        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_without_data.png")
            assert False

    def test_with_spchar(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())

        comp_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        short_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_count_of_incorp.select_by_index(14)
        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_with_spchar.png")
            assert False

    def test_with_spchar_nums_char(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        comp_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        short_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)
        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_with_spchar_nums_char.png")
            assert False
        self.driver.quit()

    def test_with_data_have_spaces(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())

        comp_name.send_keys("Zooker Technology")
        short_name.send_keys("Zooker Tech")
        drp_count_of_incorp.select_by_index(14)
        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_with_data_have_spaces.png")
            assert False
        self.driver.quit()

    def test_with_data_have_spacess(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        comp_name.send_keys("Zooker Technology")
        short_name.send_keys("Zooker Tech")
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)
        self.ci.btn_next()

        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CI_test_with_data_have_spaces.png")
            assert False
        self.driver.quit()

    def test_with_validating_preview(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())


        comp_name.send_keys("zooker technology")
        short_name.send_keys("zooker tech")
        drp_count_of_incorp.select_by_index(14)


        # Getting Values
        compa_val = comp_name.get_attribute('value')
        short_val = short_name.get_attribute('value')
        incorp_val = drp_count_of_incorp.first_selected_option.text


        print(compa_val, short_val, incorp_val)

        self.ci.btn_next()
        self.con_info.click_company_info_pre()
        time.sleep(2)

        if compa_val == self.con_info.company_name_pre():
            assert True
        else:
            assert False
        if short_val == self.con_info.short_name_pre():
            assert True
        else:
            assert False
        if incorp_val == self.con_info.country_of_incorporation_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_validating_preview_capital(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())


        comp_name.send_keys("ZOOKER TECHNOLOGY")
        short_name.send_keys("ZOOKER TECH")
        drp_count_of_incorp.select_by_index(14)


        # Getting Values
        compa_val = comp_name.get_attribute('value')
        short_val = short_name.get_attribute('value')
        incorp_val = drp_count_of_incorp.first_selected_option.text


        print(compa_val, short_val, incorp_val)

        self.ci.btn_next()
        self.con_info.click_company_info_pre()
        time.sleep(2)

        if compa_val == self.con_info.company_name_pre():
            assert True
        else:
            assert False
        if short_val == self.con_info.short_name_pre():
            assert True
        else:
            assert False
        if incorp_val == self.con_info.country_of_incorporation_pre():
            assert True
        else:
            assert False


        self.driver.quit()

    def test_with_validating_maxlen(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        compa_max = int(comp_name.get_attribute('maxlength'))
        short_max = int(short_name.get_attribute('maxlength'))
        print(compa_max, short_max)

        comp_name.send_keys(random_string_generator_max_50())
        short_name.send_keys(random_string_generator_max_30())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)

        compa_val = len(comp_name.get_attribute('value'))
        short_val = len(short_name.get_attribute('value'))
        print(compa_val, short_val)

        self.ci.btn_next()

        if compa_max == compa_val:
            assert True
        else:
            assert False

        if short_max == short_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_validating_maxlen_lessthen(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        compa_max = int(comp_name.get_attribute('maxlength'))
        short_max = int(short_name.get_attribute('maxlength'))
        print(compa_max, short_max)

        comp_name.send_keys(random_string_generator_max_48())
        short_name.send_keys(random_string_generator_max_28())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)

        compa_val = len(comp_name.get_attribute('value'))
        short_val = len(short_name.get_attribute('value'))
        print(compa_val, short_val)

        self.ci.btn_next()

        if compa_max > compa_val:
            assert True
        else:
            assert False

        if short_max > short_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_validating_maxlen_greaterthen(self, setup):
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

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        compa_max = int(comp_name.get_attribute('maxlength'))
        short_max = int(short_name.get_attribute('maxlength'))
        print(compa_max, short_max)

        comp_name.send_keys(random_string_generator_max_51() + random_string_generator_max_48())
        short_name.send_keys(random_string_generator_max_48())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)

        compa_val = len(comp_name.get_attribute('value'))
        short_val = len(short_name.get_attribute('value'))
        print(compa_val, short_val)

        self.ci.btn_next()

        if compa_max == compa_val:
            assert True
        else:
            assert False

        if short_max == short_val:
            assert True
        else:
            assert False

        self.driver.quit()
