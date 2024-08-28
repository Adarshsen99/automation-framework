import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Corporate import Company_Information,Contact_Information,Bank_Information,Final_Preview
from Dinero_automation.utilities.randomString import generate_random_email_new,random_string_generator_numbers,random_string_generator_numbers_new,random_string_generator_new,random_string_generator,random_string_generator_max_30,random_string_generator_max_50,generate_random_email,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
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
        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_valid_data.png")
            assert False
        self.driver.quit()

    def test_with_out_data(self, setup):
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

        build_num.send_keys("")
        build_name.send_keys("")
        street.send_keys("")
        city_dist.send_keys("")
        # drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("")
        email.send_keys("")

        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_valid_data.png")
            assert False
        self.driver.quit()

    def test_data_have_spaces(self, setup):
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

        # time.sleep(4)
        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_valid_data.png")
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

        b_num = build_num.get_attribute('value')
        b_name = build_name.get_attribute('value')
        street = street.get_attribute('value')
        ci_dist = city_dist.get_attribute('value')
        country = drp_country.first_selected_option.text
        number = mobile_num.get_attribute('value')
        mail = email.get_attribute('value')

        # time.sleep(4)
        self.con_info.btn_next()
        time.sleep(2)
        self.bi.click_contact_info_pre()
        # time.sleep(2)

        print(self.bi.building_numb_pre(),
        self.bi.building_name_pre(),
        self.bi.street_pre(),
        self.bi.city_district_pre(),
        self.bi.country_pre(),
        self.bi.mobile_num_pre(),
        self.bi.email_pre())

        if b_num == self.bi.building_numb_pre():
            assert True
        else:
            assert False

        if b_name == self.bi.building_name_pre():
            assert True
        else:
            assert False

        if street == self.bi.street_pre():
            assert True
        else:
            assert False

        if ci_dist == self.bi.city_district_pre():
            assert True
        else:
            assert False

        if country == self.bi.country_pre():
            assert True
        else:
            assert False

        if number == self.bi.mobile_num_pre():
            assert True
        else:
            assert False

        if mail == self.bi.email_pre():
            assert True
        else:
            assert False



        self.driver.quit()

    def test_validating_preview_smallletter(self, setup):
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

        b_num = build_num.get_attribute('value')
        b_name = build_name.get_attribute('value')
        street = street.get_attribute('value')
        ci_dist = city_dist.get_attribute('value')
        country = drp_country.first_selected_option.text
        number = mobile_num.get_attribute('value')
        mail = email.get_attribute('value')

        # time.sleep(4)
        self.con_info.btn_next()
        time.sleep(2)
        self.bi.click_contact_info_pre()
        # time.sleep(2)

        print(self.bi.building_numb_pre(),
        self.bi.building_name_pre(),
        self.bi.street_pre(),
        self.bi.city_district_pre(),
        self.bi.country_pre(),
        self.bi.mobile_num_pre(),
        self.bi.email_pre())

        if b_num == self.bi.building_numb_pre():
            assert True
        else:
            assert False

        if b_name == self.bi.building_name_pre():
            assert True
        else:
            assert False

        if street == self.bi.street_pre():
            assert True
        else:
            assert False

        if ci_dist == self.bi.city_district_pre():
            assert True
        else:
            assert False

        if country == self.bi.country_pre():
            assert True
        else:
            assert False

        if number == self.bi.mobile_num_pre():
            assert True
        else:
            assert False

        if mail == self.bi.email_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_mobilenumb(self, setup):
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

        country = drp_country.first_selected_option.text
        mobile = drp_country_code.first_selected_option.text
        print(country,mobile)


        # time.sleep(4)
        self.con_info.btn_next()
        time.sleep(2)
        self.bi.btn_back()
        time.sleep(3)

        drp_country_code = Select(self.con_info.drp_country_code())
        mobile_num = self.con_info.mobile_number()

        build_num = self.con_info.building_number()
        build_name = self.con_info.building_name()
        street = self.con_info.street()
        city_dist = self.con_info.city_district()
        # drp_country = Select(self.con_info.drp_country())
        email = self.con_info.email()

        build_num.clear()
        build_name.clear()
        street.clear()
        city_dist.clear()
        mobile_num.clear()
        # drp_country.deselect_all()
        email.clear()

        country_af = drp_country_code.first_selected_option.text
        print(country_af)

        if mobile != country_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_validating_mobilenumb.png")
            assert False

    def test_validating_maxlen(self, setup):
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

        b_num_max = int(build_num.get_attribute('maxlength'))
        b_name_max = int(build_name.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        ci_dist_max = int(city_dist.get_attribute('maxlength'))
        number_max = int(mobile_num.get_attribute('maxlength'))
        mail_max = int(email.get_attribute('maxlength'))

        print(b_num_max, b_name_max,street_max,ci_dist_max,number_max,mail_max)

        build_num.send_keys(random_string_generator_max_50())
        build_name.send_keys(random_string_generator_max_50())
        street.send_keys(random_string_generator_max_50())
        city_dist.send_keys(random_string_generator_max_30())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("2578411145555556")
        email.send_keys("kjdeghuvfjciinjvfkwsdfscxsddsffcscdscmmc@gmail.com")

        b_num = len(build_num.get_attribute('value'))
        b_name = len(build_name.get_attribute('value'))
        street = len(street.get_attribute('value'))
        ci_dist = len(city_dist.get_attribute('value'))
        number = len(mobile_num.get_attribute('value'))
        mail = len(email.get_attribute('value'))

        print(b_num,b_name,street,ci_dist,number,mail)

        # time.sleep(4)
        self.con_info.btn_next()

        if b_num_max == b_num:
            assert True
        else:
            assert False

        if b_name_max == b_name:
            assert True
        else:
            assert False

        if street_max == street:
            assert True
        else:
            assert False

        if ci_dist_max == ci_dist:
            assert True
        else:
            assert False

        if number_max == number:
            assert True
        else:
            assert False

        if mail_max == mail:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_maxlen_lessthen(self, setup):
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

        b_num_max = int(build_num.get_attribute('maxlength'))
        b_name_max = int(build_name.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        ci_dist_max = int(city_dist.get_attribute('maxlength'))
        number_max = int(mobile_num.get_attribute('maxlength'))
        mail_max = int(email.get_attribute('maxlength'))

        print(b_num_max, b_name_max,street_max,ci_dist_max,number_max,mail_max)

        build_num.send_keys(random_string_generator_max_48())
        build_name.send_keys(random_string_generator_max_48())
        street.send_keys(random_string_generator_max_48())
        city_dist.send_keys(random_string_generator_max_28())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("25784556")
        email.send_keys("kjdeghuvfjciinjvfcscdscmmc@gmail.com")

        b_num = len(build_num.get_attribute('value'))
        b_name = len(build_name.get_attribute('value'))
        street = len(street.get_attribute('value'))
        ci_dist = len(city_dist.get_attribute('value'))
        number = len(mobile_num.get_attribute('value'))
        mail = len(email.get_attribute('value'))

        print(b_num,b_name,street,ci_dist,number,mail)

        # time.sleep(4)
        self.con_info.btn_next()

        if b_num_max > b_num:
            assert True
        else:
            assert False

        if b_name_max > b_name:
            assert True
        else:
            assert False

        if street_max > street:
            assert True
        else:
            assert False

        if ci_dist_max > ci_dist:
            assert True
        else:
            assert False

        if number_max > number:
            assert True
        else:
            assert False

        if mail_max > mail:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_maxlen_greaterthen(self, setup):
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

        b_num_max = int(build_num.get_attribute('maxlength'))
        b_name_max = int(build_name.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        ci_dist_max = int(city_dist.get_attribute('maxlength'))
        number_max = int(mobile_num.get_attribute('maxlength'))
        mail_max = int(email.get_attribute('maxlength'))

        print(b_num_max, b_name_max,street_max,ci_dist_max,number_max,mail_max)

        build_num.send_keys(random_string_generator_max_51())
        build_name.send_keys(random_string_generator_max_51())
        street.send_keys(random_string_generator_max_51())
        city_dist.send_keys(random_string_generator_max_51())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("257841116645555556")
        email.send_keys("kjdeghuvfjciinjvfkwsdfscxsddsffcscfghtgfdscmmc@gmail.com")

        b_num = len(build_num.get_attribute('value'))
        b_name = len(build_name.get_attribute('value'))
        street = len(street.get_attribute('value'))
        ci_dist = len(city_dist.get_attribute('value'))
        number = len(mobile_num.get_attribute('value'))
        mail = len(email.get_attribute('value'))

        print(b_num,b_name,street,ci_dist,number,mail)

        # time.sleep(4)
        self.con_info.btn_next()

        if b_num_max == b_num:
            assert True
        else:
            assert False

        if b_name_max == b_name:
            assert True
        else:
            assert False

        if street_max == street:
            assert True
        else:
            assert False

        if ci_dist_max == ci_dist:
            assert True
        else:
            assert False

        if number_max == number:
            assert True
        else:
            assert False

        if mail_max == mail:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_onlyreq_field(self, setup):
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
        # build_name = self.con_info.building_name()
        # street = self.con_info.street()
        city_dist = self.con_info.city_district()
        drp_country = Select(self.con_info.drp_country())
        drp_country_code = Select(self.con_info.drp_country_code())
        mobile_num = self.con_info.mobile_number()
        email = self.con_info.email()

        build_num.send_keys(random_string_generator_numbers_new())
        # build_name.send_keys("1245637")
        # street.send_keys("Kochi")
        city_dist.send_keys(random_string_generator())
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys(random_string_generator_numbers())
        email.send_keys(generate_random_email_new())

        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_onlyreq_field.png")
            assert False
        self.driver.quit()

    def test_with_nonreq_field(self, setup):
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

        build_name = self.con_info.building_name()
        street = self.con_info.street()

        build_name.send_keys(random_string_generator_new())
        street.send_keys(random_string_generator())

        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_nonreq_field.png")
            assert False

        self.driver.quit()

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

        # Assigning data
        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)

        compa_val = comp_name.get_attribute('value')
        short_val = short_name.get_attribute('value')
        incorp_val = drp_count_of_incorp.first_selected_option.text
        relation_val = drp_relation.first_selected_option.text

        print("Before:",compa_val, short_val, incorp_val, relation_val)

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

        b_num = build_num.get_attribute('value')
        b_name = build_name.get_attribute('value')
        street = street.get_attribute('value')
        ci_dist = city_dist.get_attribute('value')
        country = drp_country.first_selected_option.text
        country_code = drp_country_code.first_selected_option.text
        number = mobile_num.get_attribute('value')
        mail = email.get_attribute('value')

        print("Before:",b_num, b_name,street,ci_dist,country,country_code,number,mail)

        self.con_info.btn_next()
        time.sleep(2)
        self.bi.btn_cancel()
        time.sleep(2)
        self.bi.btn_cancel_confirm()
        time.sleep(2)

        comp_name = self.ci.company_name()
        short_name = self.ci.short_name()
        drp_count_of_incorp = Select(self.ci.drp_country_of_incorporation())
        drp_relation = Select(self.ci.drp_relation())

        compa_val_af = comp_name.get_attribute('value')
        short_val_af = short_name.get_attribute('value')
        incorp_val_af = drp_count_of_incorp.first_selected_option.text
        relation_val_af = drp_relation.first_selected_option.text

        print("After:", compa_val_af, short_val_af, incorp_val_af, relation_val_af)

        comp_name.send_keys(random_string_generator())
        short_name.send_keys(random_string_generator_new())
        drp_count_of_incorp.select_by_index(14)
        drp_relation.select_by_index(2)

        self.ci.btn_next()
        time.sleep(4)

        build_num = self.con_info.building_number()
        build_name = self.con_info.building_name()
        street = self.con_info.street()
        city_dist = self.con_info.city_district()
        drp_country = Select(self.con_info.drp_country())
        drp_country_code = Select(self.con_info.drp_country_code())
        mobile_num = self.con_info.mobile_number()
        email = self.con_info.email()

        b_num_af = build_num.get_attribute('value')
        b_name_af = build_name.get_attribute('value')
        street_af = street.get_attribute('value')
        ci_dist_af = city_dist.get_attribute('value')
        country_af = drp_country.first_selected_option.text
        country_code_af = drp_country_code.first_selected_option.text
        number_af = mobile_num.get_attribute('value')
        mail_af = email.get_attribute('value')

        print("After:", b_num_af, b_name_af, street_af, ci_dist_af, country_af, country_code_af, number_af, mail_af)

        if compa_val != compa_val_af:
            assert True
        else:
            assert False

        if short_val != short_val_af:
            assert True
        else:
            assert False

        if incorp_val != incorp_val_af:
            assert True
        else:
            assert False

        if relation_val != relation_val_af:
            assert True
        else:
            assert False

        if b_num != b_num_af:
            assert True
        else:
            assert False

        if b_name != b_name_af:
            assert True
        else:
            assert False

        if street != street_af:
            assert True
        else:
            assert False

        if ci_dist != ci_dist_af:
            assert True
        else:
            assert False

        if country != country_af:
            assert True
        else:
            assert False

        if country_code != country_code_af:
            assert True
        else:
            assert False

        if number != number_af:
            assert True
        else:
            assert False

        if mail != mail_af:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_valid_spchar(self, setup):
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

        build_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        build_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        street.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        city_dist.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("21324")
        email.send_keys(generate_random_email_new())

        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_valid_data.png")
            assert False
        self.driver.quit()

    def test_with_sending_onlynumbers(self, setup):
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
        error_msg = self.ci.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_valid_numbers.png")
            assert False
        self.driver.quit()

    def test_with_sending_sp_char_num_data(self, setup):
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

        build_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        build_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        street.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        city_dist.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        drp_country.select_by_index(2)
        drp_country_code.select_by_index(6)
        mobile_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        email.send_keys(generate_random_email_new())

        self.con_info.btn_next()
        error_msg = self.ci.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BEN_CO_CONTACTINFO_test_with_sending_sp_char_num_data.png")
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

        b_num = build_num.get_attribute('value')
        b_name = build_name.get_attribute('value')
        street = street.get_attribute('value')
        ci_dist = city_dist.get_attribute('value')
        country = drp_country.first_selected_option.text
        number = mobile_num.get_attribute('value')
        mail = email.get_attribute('value')

        print("Actual Data:",b_num,b_name,street,ci_dist,country,number,mail)

        self.con_info.btn_next()
        time.sleep(2)
        self.bi.click_contact_info_pre()

        print("Data from the preview:",self.bi.building_numb_pre(),
            self.bi.building_name_pre(),
            self.bi.street_pre(),
            self.bi.city_district_pre(),
            self.bi.country_pre(),
            self.bi.mobile_num_pre(),
            self.bi.email_pre())

        if b_num == self.bi.building_numb_pre():
            assert True
        else:
            assert False

        if b_name == self.bi.building_name_pre():
            assert True
        else:
            assert False

        if street == self.bi.street_pre():
            assert True
        else:
            assert False

        if ci_dist == self.bi.city_district_pre():
            assert True
        else:
            assert False

        if country == self.bi.country_pre():
            assert True
        else:
            assert False

        if mail == self.bi.email_pre():
            assert True
        else:
            assert False

        if number == self.bi.mobile_num_pre():
            assert True
        else:
            assert False

        self.driver.quit()
