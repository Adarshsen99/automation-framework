import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Fastcash_Location,Bank_Information,Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Fastcash_Location:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    # def test_adding_without_adding_fastcash(self,setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.fi = Fastcash_Location(self.driver)
    #     self.fp = Final_Preview(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Bumble")
    #     mname.send_keys("Boom")
    #     lname.send_keys("bee")
    #     sname.send_keys("boo Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("12412563erdfvgy")
    #     trans_type.select_by_index(1)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("12345678291")
    #     hb_num.send_keys("12345678291")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal6@gmail.com")
    #     city.send_keys("Ernak44amm")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("98765436623210")
    #
    #     self.ci.btn_next()
    #
    #     # self.fi.click_payout_anywhere()
    #     # drp_cont = Select(self.fi.drp_country())
    #     # drp_country_code = Select(self.fi.drp_num_country())
    #     # mo_num = self.fi.mobile_number()
    #     #
    #     # drp_cont.select_by_index(5)
    #     # drp_country_code.select_by_index(15)
    #     # mo_num.send_keys("9876543210")
    #     #
    #     # # Buttons for anywhare location
    #     # self.fi.btn_add_location()
    #     time.sleep(3)
    #
    #     self.fi.btn_next()
    #     self.fp.btn_save().click()
    #     time.sleep(2)
    #     print(self.fp.editmode_message())
    #
    #     if not self.fp.editmode_message() == "You're in edit mode":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "FP_test_adding_without_adding_fastcash.png")
    #         assert False

    def test_adding_without_adding_bankinfo(self,setup):
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
        fname.send_keys("Bumble")
        mname.send_keys("Boom")
        lname.send_keys("bee")
        sname.send_keys("boo Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("12412563erdffvgy")
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

        fh_num.send_keys("123456783291")
        hb_num.send_keys("123456782951")
        street.send_keys("Kochi")
        email.send_keys("personal8@gmail.com")
        city.send_keys("Ernak44amm")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("987654436623210")

        self.ci.btn_next()

        # self.fi.click_payout_anywhere()
        # drp_cont = Select(self.fi.drp_country())
        # drp_country_code = Select(self.fi.drp_num_country())
        # mo_num = self.fi.mobile_number()
        #
        # drp_cont.select_by_index(5)
        # drp_country_code.select_by_index(15)
        # mo_num.send_keys("9876543210")
        #
        # # Buttons for anywhare location
        # self.fi.btn_add_location()
        time.sleep(3)

        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(2)

        if not self.fp.editmode_message() == "You're in edit mode":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "FP_test_adding_without_adding_fastcash.png")
            assert False

    def test_adding_without_adding_bankinfo_and_fastcash(self,setup):
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
        self.fl = Fastcash_Location(self.driver)
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
        fname.send_keys("Bumble")
        mname.send_keys("Boom")
        lname.send_keys("bee")
        sname.send_keys("boo Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("12412563erdfvgy")
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

        fh_num.send_keys("12345678291")
        hb_num.send_keys("12345678291")
        street.send_keys("Kochi")
        email.send_keys("personal6@gmail.com")
        city.send_keys("Ernak44amm")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("98765436623210")

        self.ci.btn_next()

        # self.fi.click_payout_anywhere()
        # drp_cont = Select(self.fi.drp_country())
        # drp_country_code = Select(self.fi.drp_num_country())
        # mo_num = self.fi.mobile_number()
        #
        # drp_cont.select_by_index(5)
        # drp_country_code.select_by_index(15)
        # mo_num.send_keys("9876543210")
        #
        # # Buttons for anywhare location
        # self.fi.btn_add_location()
        time.sleep(3)

        self.bi.btn_next()
        self.fp.btn_save().click()
        time.sleep(2)

        if not self.fp.editmode_message() == "You're in edit mode":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "FP_test_adding_without_adding_bankinfo_and_fastcash.png")
            assert False