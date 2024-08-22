import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Bank_Information
from Dinero_automation.utilities.randomString import random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Contact_Information:
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        self.ci.btn_next()
        time.sleep(2)

        error_msg = self.pi.error_message()
        print(error_msg)

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_with_valid_data.png")
            assert True

        self.driver.quit()

    def test_with_special_char_data(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        hb_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        street.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        email.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        city.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_contry.select_by_index(4)
        drp_phone.select_by_index(10)
        phone.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        self.ci.btn_next()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_with_special_char_data.png")
            assert False

        self.driver.quit()

    def test_sending_numbers(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("123456789")
        email.send_keys("123456789")
        city.send_keys("123456789")
        drp_contry.select_by_index(4)
        drp_phone.select_by_index(10)
        phone.send_keys("123456789")

        self.ci.btn_next()
        time.sleep(2)

        # error_msg = self.pi.error_message()
        #
        # if error_msg == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(screenShort.screen_short() + "CI_test_sending_numbers.png")
        #     assert False

        self.driver.quit()

    def test_sending_spchar_num_char(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        hb_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        street.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        email.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        city.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        drp_contry.select_by_index(4)
        drp_phone.select_by_index(10)
        phone.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")

        self.ci.btn_next()
        time.sleep(2)
        # error_msg = self.pi.error_message()
        #
        # if error_msg == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(screenShort.screen_short() + "CI_test_sending_spchar_num_char.png")
        #     assert False
        self.driver.quit()


    def test_validating_clear(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        hb_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        street.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        email.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        city.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        drp_contry.select_by_index(4)
        drp_phone.select_by_index(10)
        phone.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")

        self.ci.btn_next()

        time.sleep(2)
        # error_msg = self.pi.error_message()
        #
        # if error_msg == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(screenShort.screen_short() + "CI_test_sending_spchar_num_char.png")
        #     assert False
        self.driver.quit()

    def test_validating_clear(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        fh_num_val = fh_num.get_attribute('value')
        hb_num_val = hb_num.get_attribute('value')
        street_val = street.get_attribute('value')
        email_val = email.get_attribute('value')
        city_val = city.get_attribute('value')
        drp_contry_val = drp_contry.first_selected_option.text
        drp_phone_val = drp_phone.first_selected_option.text
        phone_val = phone.get_attribute('value')

        print(fh_num_val,hb_num_val,street_val,email_val,city_val,drp_contry_val,drp_phone_val,phone_val)

        self.ci.btn_next()
        time.sleep(2)
        self.bi.btn_back()
        time.sleep(2)
        self.ci.btn_cancel()
        self.ci.btn_cancel_confirm()

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num_af = fh_num.get_attribute('value')
        hb_num_af = hb_num.get_attribute('value')
        street_af = street.get_attribute('value')
        email_af = email.get_attribute('value')
        city_af = city.get_attribute('value')
        drp_contry_af = drp_contry.first_selected_option.text
        drp_phone_af = drp_phone.first_selected_option.text
        phone_af = phone.get_attribute('value')

        print(fh_num_af, hb_num_af, street_af, email_af, city_af, drp_contry_af, drp_phone_af, phone_af)

        if fh_num_val != fh_num_af:
            assert True
        else:
            assert False
        if hb_num_val != hb_num_af:
            assert True
        else:
            assert False
        if street_val != street_af:
            assert True
        else:
            assert False
        if email_val != email_af:
            assert True
        else:
            assert False
        if city_val != city_af:
            assert True
        else:
            assert False
        if drp_contry_val != drp_contry_af:
            assert True
        else:
            assert False
        if drp_phone_val != drp_phone_af:
            assert True
        else:
            assert False
        if phone_val != phone_af:
            assert True
        else:
            assert False
        self.driver.quit()

    def test_sending_data_have_spaces(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("1234 56789")
        hb_num.send_keys("1234 56789")
        street.send_keys("Kochi street")
        email.send_keys("person al@gmail.com us")
        city.send_keys("Ernakulam City")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("98765 43210")

        time.sleep(5)
        self.ci.btn_next()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_sending_data_have_spaces.png")
            assert True

        self.driver.quit()

    def test_with_char_data(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("qwertyuiop")
        hb_num.send_keys("qwertyuiop")
        street.send_keys("qwertyuiop")
        email.send_keys("qwertyuiop@gmail.com")
        city.send_keys("qwertyuiop")
        drp_contry.select_by_index(4)
        drp_phone.select_by_index(10)
        phone.send_keys("qwertyuiop")

        time.sleep(2)
        self.ci.btn_next()
        time.sleep(2)

        # error_msg = self.pi.error_message()
        #
        # if error_msg == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(screenShort.screen_short() + "CI_test_with_char_data.png")
        #     assert False

        self.driver.quit()

    def test_validating_only_reqfields(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("")
        street.send_keys("")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        self.ci.btn_next()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_validating_only_reqfields.png")
            assert True

        self.driver.quit()

    def test_validating_only_nonreqfields(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("")
        city.send_keys("")
        drp_contry.select_by_visible_text("")
        # drp_phone.select_by_visible_text("")
        time.sleep(4)
        # phone.send_keys("")

        self.ci.btn_next()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_validating_only_nonreqfields.png")
            assert False

        self.driver.quit()

    def test_validating_pre(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        fh_num_val = fh_num.get_attribute('value')
        hb_num_val = hb_num.get_attribute('value')
        street_val = street.get_attribute('value')
        email_val = email.get_attribute('value')
        city_val = city.get_attribute('value')
        drp_contry_val = drp_contry.first_selected_option.text

        print(f"fh_num_val: {fh_num_val}, hb_num_val: {hb_num_val}, street_val: {street_val}, email_val: {email_val}, city_val: {city_val}, drp_contry_val: {drp_contry_val}")

        self.ci.btn_next()
        time.sleep(2)

        self.bi.click_contact_infirmation_pre()

        print(self.bi.fl_hn_num_pre(),
            self.bi.ho_bu_name_pre(),
            self.bi.street_pre(),
            self.bi.cty_pre(),
            self.bi.country_pre(),
            self.bi.emai_pre())
        time.sleep(2)

        if fh_num_val == self.bi.fl_hn_num_pre():
            assert True
        else:
            assert False

        if hb_num_val == self.bi.ho_bu_name_pre():
            assert True
        else:
            assert False

        if street_val == self.bi.street_pre():
            assert True
        else:
            assert False

        if email_val == self.bi.emai_pre():
            assert True
        else:
            assert False

        if city_val == self.bi.cty_pre():
            assert True
        else:
            assert False

        if drp_contry_val == self.bi.country_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_maxlength(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_max_50())
        hb_num.send_keys(random_string_generator_max_50())
        street.send_keys(random_string_generator_max_50())
        email.send_keys(generate_random_email())
        city.send_keys(random_string_generator_max_30())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_10()+random_string_generator_numbers_10())

        fh_num_max = int(fh_num.get_attribute('maxlength'))
        hb_num_max = int(hb_num.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        email_max = int(email.get_attribute('maxlength'))
        city_max = int(city.get_attribute('maxlength'))
        phone_max = int(phone.get_attribute('maxlength'))

        print(f"fh_num_max: {fh_num_max}, hb_num_max: {hb_num_max}, street_max: {street_max}, email_max: {email_max}, city_max: {city_max}, phone_max: {phone_max}")

        fh_num_val = len(fh_num.get_attribute('value'))
        hb_num_val = len(hb_num.get_attribute('value'))
        street_val = len(street.get_attribute('value'))
        email_val = len(email.get_attribute('value'))
        city_val = len(city.get_attribute('value'))
        phone_val = len(phone.get_attribute('maxlength'))

        print(f"fh_num_val: {fh_num_val}, hb_num_val: {hb_num_val}, street_val: {street_val}, email_val: {email_val}, city_val: {city_val}, phone_val:{phone_val}")

        if fh_num_val == fh_num_max:
            assert True
        else:
            assert False

        if hb_num_val == hb_num_max:
            assert True
        else:
            assert False

        if street_val == street_max:
            assert True
        else:
            assert False

        # if email_val == email_max:
        #     assert True
        # else:
        #     assert False

        if city_val == city_max:
            assert True
        else:
            assert False

        # if phone_val == phone_max:
        #     assert True
        # else:
        #     assert False

        self.ci.btn_next()

        self.driver.quit()

    def test_validating_maxlength_lessthen(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_max_48())
        hb_num.send_keys(random_string_generator_max_48())
        street.send_keys(random_string_generator_max_48())
        email.send_keys(generate_random_email())
        city.send_keys(random_string_generator_max_28())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers())

        fh_num_max = int(fh_num.get_attribute('maxlength'))
        hb_num_max = int(hb_num.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        email_max = int(email.get_attribute('maxlength'))
        city_max = int(city.get_attribute('maxlength'))
        phone_max = int(phone.get_attribute('maxlength'))

        print(f"fh_num_max: {fh_num_max}, hb_num_max: {hb_num_max}, street_max: {street_max}, email_max: {email_max}, city_max: {city_max}, phone_max: {phone_max}")

        fh_num_val = len(fh_num.get_attribute('value'))
        hb_num_val = len(hb_num.get_attribute('value'))
        street_val = len(street.get_attribute('value'))
        email_val = len(email.get_attribute('value'))
        city_val = len(city.get_attribute('value'))
        phone_val = len(phone.get_attribute('maxlength'))

        print(f"fh_num_val: {fh_num_val}, hb_num_val: {hb_num_val}, street_val: {street_val}, email_val: {email_val}, city_val: {city_val}, phone_val:{phone_val}")

        if fh_num_val < fh_num_max:
            assert True
        else:
            assert False

        if hb_num_val < hb_num_max:
            assert True
        else:
            assert False

        if street_val < street_max:
            assert True
        else:
            assert False

        if email_val < email_max:
            assert True
        else:
            assert False

        if city_val < city_max:
            assert True
        else:
            assert False

        if phone_val < phone_max:
            assert True
        else:
            assert False

        self.ci.btn_next()

        self.driver.quit()

    def test_validating_maxlength_graterthen(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_max_48()+random_string_generator_max_48())
        hb_num.send_keys(random_string_generator_max_48()+random_string_generator_max_48())
        street.send_keys(random_string_generator_max_48()+random_string_generator_max_48())
        email.send_keys(generate_random_email()+generate_random_email())
        city.send_keys(random_string_generator_max_28()+random_string_generator_max_28())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers())

        fh_num_max = int(fh_num.get_attribute('maxlength'))
        hb_num_max = int(hb_num.get_attribute('maxlength'))
        street_max = int(street.get_attribute('maxlength'))
        email_max = int(email.get_attribute('maxlength'))
        city_max = int(city.get_attribute('maxlength'))
        phone_max = int(phone.get_attribute('maxlength'))

        print(f"fh_num_max: {fh_num_max}, hb_num_max: {hb_num_max}, street_max: {street_max}, email_max: {email_max}, city_max: {city_max}, phone_max: {phone_max}")

        fh_num_val = len(fh_num.get_attribute('value'))
        hb_num_val = len(hb_num.get_attribute('value'))
        street_val = len(street.get_attribute('value'))
        email_val = len(email.get_attribute('value'))
        city_val = len(city.get_attribute('value'))
        phone_val = len(phone.get_attribute('maxlength'))

        print(f"fh_num_val: {fh_num_val}, hb_num_val: {hb_num_val}, street_val: {street_val}, email_val: {email_val}, city_val: {city_val}, phone_val:{phone_val}")

        if fh_num_val == fh_num_max:
            assert True
        else:
            assert False

        if hb_num_val == hb_num_max:
            assert True
        else:
            assert False

        if street_val == street_max:
            assert True
        else:
            assert False

        if email_val == email_max:
            assert True
        else:
            assert False

        if city_val == city_max:
            assert True
        else:
            assert False
        #
        # if phone_val == phone_max:
        #     assert True
        # else:
        #     assert False

        self.ci.btn_next()

        self.driver.quit()

    def test_with_clear_phonenum(self, setup):
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
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        phone_bf = drp_phone.first_selected_option.text
        print(f"Phone: {phone_bf}")

        self.ci.btn_next()
        time.sleep(2)
        self.bi.btn_back()

        drp_phone = Select(self.ci.drp_phone())
        phone_af = self.ci.phone()
        phone_af.clear()

        phone_af = drp_phone.first_selected_option.text
        print(f"phone_af: {phone_af}")

        time.sleep(2)

        if phone_bf != phone_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CI_test_with_clear_phonenum.png")
            assert False

        self.driver.quit()