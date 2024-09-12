import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Fastcash_Location,Final_Preview
from Dinero_automation.utilities.randomString import generate_random_email_new,random_string_generator,random_string_generator_numbers_new,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Fastcash_Location:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    def test_adding_payout_anywhere(self,setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_payout_anywhere()
        drp_cont = Select(self.fi.drp_country())
        drp_country_code = Select(self.fi.drp_num_country())
        mo_num = self.fi.mobile_number()

        drp_cont.select_by_index(5)
        drp_country_code.select_by_index(15)
        mo_num.send_keys(random_string_generator_numbers_new())

        # Buttons for anywhare location
        self.fi.btn_add_location()
        time.sleep(3)
        # self.fi.btn_clear()

    def test_adding_payout_anywhere_witoutdata(self,setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_payout_anywhere()
        # drp_cont = Select(self.fi.drp_country())
        # drp_country_code = Select(self.fi.drp_num_country())
        # mo_num = self.fi.mobile_number()
        #
        # drp_cont.select_by_index(5)
        # drp_country_code.select_by_index(15)
        # mo_num.send_keys("9876543210")

        # Buttons for anywhare location
        self.fi.btn_add_location()
        time.sleep(3)
        # self.fi.btn_clear()

    def test_adding_payout_anywhere_withoutnumber(self, setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_payout_anywhere()
        drp_cont = Select(self.fi.drp_country())
        drp_country_code = Select(self.fi.drp_num_country())
        mo_num = self.fi.mobile_number()

        drp_cont.select_by_index(5)
        drp_country_code.select_by_index(15)
        # mo_num.send_keys("9876543210")

        before_count = drp_cont.first_selected_option.text

        print("before number:",before_count)


        # Buttons for anywhare location
        self.fi.btn_add_location()
        self.fi.fastcash_1().click()

        if not before_count == self.fi.fastcash_1().text:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "fc_test_adding_payout_anywhere_withoutnumber.png")
            assert False
        time.sleep(3)

    def test_adding_payout_anywhere_clearing_mobilenum(self, setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_payout_anywhere()
        drp_cont = Select(self.fi.drp_country())
        drp_country_code = Select(self.fi.drp_num_country())
        mo_num = self.fi.mobile_number()

        drp_cont.select_by_index(5)
        drp_country_code.select_by_index(15)
        mo_num.send_keys(random_string_generator_numbers_new())

        before_count = mo_num.get_attribute("value")
        print("before number:",before_count)

        country_before = drp_country_code.first_selected_option.text

        print("country_before",country_before)


        # Buttons for anywhare location
        self.fi.btn_add_location()
        self.fi.fastcash_1().click()

        mo_num = self.fi.mobile_number()
        mo_num.clear()

        after_count = mo_num.get_attribute("value")

        print("after_count:", after_count)

        country_after = drp_country_code.first_selected_option.text

        print("country_after", country_after)

        if not country_before == country_after:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "FC_test_adding_payout_anywhere_clearing_mobilenum.png")
            assert False
        time.sleep(3)

    def test_validating_payout_anywhere_preview(self, setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_payout_anywhere().click()
        drp_cont = Select(self.fi.drp_country())
        drp_country_code = Select(self.fi.drp_num_country())
        mo_num = self.fi.mobile_number()

        drp_cont.select_by_index(5)
        drp_country_code.select_by_index(15)
        mo_num.send_keys(random_string_generator_numbers_new())

        before_count = mo_num.get_attribute("value")
        print("before number:",before_count)

        count = drp_cont.first_selected_option.text
        print("count_before_val", count)


        # Buttons for anywhare location
        self.fi.btn_add_location()
        self.fi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)
        self.fi.click_fastcash_location()
        time.sleep(2)

        if count == self.fi.country_pre():
            assert True
        else:
            assert False

        if before_count == self.fi.mobile_pre():
            assert True
        else:
            assert False
        time.sleep(3)

    def test_validating_payout_anywhere_previeww(self, setup):
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
        self.fi = Fastcash_Location(self.driver)
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()

        self.fi.click_specific_location()
        counrty = Select(self.fi.drp_country_splocation())
        countrt_num = Select(self.fi.drp_num_country_splocation())
        number = self.fi.mobile_number_splocation()
        addr_1 = self.fi.address_1_splocation()
        addr_2 = self.fi.address_2_splocation()
        addr_3 = self.fi.address_3_splocation()
        city = self.fi.city_splocation()

        counrty.select_by_index(2)
        countrt_num.select_by_index(4)
        number.send_keys("9876543210")
        addr_1.send_keys("kochi")
        addr_2.send_keys("ernakulam")
        addr_3.send_keys("habbel")
        city.send_keys("ernakulam")

        counrty_val = counrty.first_selected_option.text
        number_val = number.get_attribute("value")
        addr_1_val = addr_1.get_attribute("value")
        addr_2_val = addr_2.get_attribute("value")
        addr_3_val = addr_3.get_attribute("value")
        city_val = city.get_attribute("value")

        print(counrty_val, number_val, addr_1_val, addr_2_val,addr_3_val,city_val)

        self.fi.btn_add_location_splocation()
        # self.fi.btn_clear_splocation()

        # Buttons for anywhare location
        self.fi.btn_add_location()
        self.fi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)
        self.fi.click_fastcash_location()
        time.sleep(2)

        print(self.fi.country_sp_location_pre(),self.fi.mobile_sp_location_pre(),self.fi.address_1_sp_location_pre(),self.fi.address_2_sp_location_pre(),self.fi.address_3_sp_location_pre(),self.fi.city_sp_location_pre())

        if counrty_val == self.fi.country_sp_location_pre():
            assert True
        else:
            assert False

        if number_val == self.fi.mobile_sp_location_pre():
            assert True
        else:
            assert False

        if addr_1_val == self.fi.address_1_sp_location_pre():
            assert True
        else:
            assert False

        if addr_2_val == self.fi.address_2_sp_location_pre():
            assert True
        else:
            assert False

        if addr_3_val == self.fi.address_3_sp_location_pre():
            assert True
        else:
            assert False

        if city_val == self.fi.city_sp_location_pre():
            assert True
        else:
            assert False
        time.sleep(3)
        self.driver.quit()





