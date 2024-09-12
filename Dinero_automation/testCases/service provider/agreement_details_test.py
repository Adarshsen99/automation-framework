import time
from selenium.webdriver import Keys
from selenium.common.exceptions import WebDriverException
import self

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.service_provider import General_Information, Agreement_Details, Upload_document
from Dinero_automation.utilities.randomString import random_string_generator_max_30, random_string_generator_max_50, \
     random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
     random_string_generator_max_51, random_string_generator_numbers_18
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_agreement_details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_with_valid_data(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # entering values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        #trade_lic_num = self.ad.registration_number()
        dpik_trade_exp_date = self.ad.dpick_trade_exp_date()
        license_number = self.ad.license_number()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        #dpick_country_birth = self.ad.drp_country_of_birh()
        drp_nation = Select(self.ad.drp_nationality())

        # entering values

        dpick_agreement_star_date.send_keys("12081999")
        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys("sdsafadfds")
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num = self.ad.trade_license_number()
        trade_lic_num.send_keys("5656656")
        dpik_trade_exp_date.send_keys("051228")
        license_number.send_keys("15451514")
        license_authority.send_keys("adsfasffasf")
        auth_pers_name.send_keys("dgesdgdsgs")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("12-08-1978")
        drp_country_of_birth = Select(self.ad.drp_country_of_birh())
        drp_country_of_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("3234")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys("557485524")
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)
        btn_next = self.ad.btn_nxt()
        btn_next.click()
        time.sleep(2)

        # test passed
        # last tested on built - 3/9/2024- Adarsh Sen Madhu


    def test_without_data(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)


        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # assigning values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        #dpick_country_birth = self.ad.drp_country_of_birh()
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("")
        dpick_agreement_end_date.send_keys("")
        registration_number.send_keys("")
        dpick_reg_exp_date.send_keys("")
        trade_lic_num.send_keys("")
        license_number.send_keys("")
        license_authority.send_keys("")
        auth_pers_name.send_keys("")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("")
        drp_country_of_birth = Select(self.ad.drp_country_of_birh())
        drp_country_of_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        # btn_new.click()
        # time.sleep(2)
        # drp_fund_curr = Select(self.ad.drp_fund_curency())
        # drp_fund_curr.select_by_index(2)
        # rate = self.ad.rate()
        # rate.send_keys("")
        # settlement_rate = self.ad.settlement_rate()
        # settlement_rate.send_keys("")
        # pay_settle_rate = self.ad.pay_settelement_rate()
        # pay_settle_rate.send_keys("")
        # balance_trigg = self.ad.balance_trigger()
        # balance_trigg.send_keys("")
        # btn_add = self.ad.btn_add()
        # btn_add.click()
        # time.sleep(2)
        btn_next = self.ad.btn_nxt()
        btn_next.click()
        time.sleep(5)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
         assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_without_valid_data.png")
            assert False

         # test case passed
        # last tested - 3/09/2024

    def test_with_special_char_data(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # assigning values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        #dpick_country_birth = self.ad.drp_country_of_birh()
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        dpick_agreement_end_date.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        registration_number.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        dpick_reg_exp_date.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        license_number.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        license_authority.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        auth_pers_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_country_of_birth = Select(self.ad.drp_country_of_birh())
        drp_country_of_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)

        # fund currency

        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(5)
        btn_next = self.ad.btn_nxt()
        btn_next.click()
        time.sleep(2)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_with_spl_character.png")
            assert False

        time.sleep(5)

        # test case failed ( fund currency fields accepting +, - values and saving )
        # last tested on built 03/09/2024


    def test_with_sending_numbers(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # assigning values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        license_authority = self.ad.licensing_authority()
        dpick_trade_lic_num = self.ad.dpick_trade_exp_date()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        dpick_country_birth = self.ad.drp_country_of_birh()
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("11082021")
        dpick_agreement_end_date.send_keys("15122055")
        registration_number.send_keys("0123456789")
        dpick_reg_exp_date.send_keys("11081988")
        trade_lic_num.send_keys("4544612921")
        license_number.send_keys("0123456789")
        license_authority.send_keys("0123456789")
        dpick_trade_lic_num.send_keys("15032027")
        auth_pers_name.send_keys("0123456789")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("11121988")
        drp_country_of_birth = Select(self.ad.drp_country_of_birh())
        drp_country_of_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("0123456789")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("0123456789")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("0123456789")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys("0123456789")
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(5)
        btn_next = self.ad.btn_nxt()
        btn_next.click()
        time.sleep(12)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_with_numbers.png")
            assert False

        time.sleep(10)

        # test case passed
        # last tested on built 03/09/2024 - Adarsh Sen Madhu

    def test_with_only_char(self, setup):

        # log in

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)

        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        license_authority = self.ad.licensing_authority()
        dpick_trade_lic_num = self.ad.dpick_trade_exp_date()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        dpick_country_birth = self.ad.drp_country_of_birh()
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("abcdefghijklmnopqrstuvwxyz")
        dpick_agreement_end_date.send_keys("abcdefghijklmnopqrstuvwxyz")
        registration_number.send_keys("abcdefghijklmnopqrstuvwxyz")
        dpick_reg_exp_date.send_keys("abcdefghijklmnopqrstuvwxyz")
        trade_lic_num.send_keys("abcdefghijklmnopqrstuvwxyz")
        license_number.send_keys("abcdefghijklmnopqrstuvwxyz")
        license_authority.send_keys("abcdefghijklmnopqrstuvwxyz")
        dpick_trade_lic_num.send_keys("abcdefghijklmnopqrstuvwxyz")
        auth_pers_name.send_keys("abcdefghijklmnopqrstuvwxyz")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("abcdefghijklmnopqrstuvwxyz")
        drp_country_of_birth = Select(self.ad.drp_country_of_birh())
        drp_country_of_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("abcdefghijklmnopqrstuvwxyz")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("abcdefghijklmnopqrstuvwxyz")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("abcdefghijklmnopqrstuvwxyz")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys("abcdefghijklmnopqrstuvwxyz")
        btn_add = self.ad.btn_add()
        btn_add.click()
        # time.sleep(5)
        btn_next = self.ad.btn_nxt()
        btn_next.click()
        time.sleep(12)
        error_msg = self.ad.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_with_chaaractr.png")
            assert False
        #  test case passed ( but fund currency values accepting the letter e ; )
        # last tested on built 3/9/2024 - Adarsh Sen Madhu
    #
    def test_with_bulk_data(self, setup):

        # Initialize WebDriver and open the URL
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Service Provider
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_service_provider()

        # General Information
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

        # Fill General Information form
        drp_category = Select(self.gi.drp_category())
        drp_category.select_by_index(2)
        time.sleep(2)
        self.gi.name().send_keys("adrstsgs")
        self.gi.arabic_name().send_keys("hfsdjgfd")
        self.gi.adress_1().send_keys("dgjhafdhja")
        self.gi.adress_2().send_keys("gdhgfhjfg")
        self.gi.adress_3().send_keys("hkjgfkhgfkh")
        self.gi.postal_code().send_keys("346714684")
        self.gi.city().send_keys("hgdhkdgfkh")

        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)

        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_count_of_Incorp.select_by_index(5)

        drp_country_code = Select(self.gi.drp_country_code())
        drp_country_code.select_by_index(8)

        self.gi.mobile_number().send_keys("654546445454")
        self.gi.email().send_keys("njuyg@gm.vom")
        self.gi.btn_nxt().click()
        time.sleep(2)

        # Bulk data
        registration_numbers = [12545545, 4154161545, 6451516516, ]
        trade_licenses = [64646464, 485659, 454545454,]
        license_numbers = [59444, 44524465, 4542597797, ]
        licensing_authorities = ['dfdsfgfsg', 'dsdgdsgds', 'dsgsdgdfsg']
        authorized_persons = ['dggdgfgre', 'dsgdsgdgs', 'dsgdgdsgdg']


        for i in range(3):

            # Fill Agreement Details
            self.ad.dpick_agreement_start_details().send_keys("12051999")
            self.ad.dpick_agreement_end_details().send_keys("12052022")
            self.ad.registration_number().send_keys(registration_numbers[i])
            self.ad.dpick_registration_exp_date().send_keys("22112055")
            self.ad.trade_license_number().send_keys(trade_licenses[i])
            self.ad.license_number().send_keys(license_numbers[i])
            self.ad.licensing_authority().send_keys(licensing_authorities[i])
            self.ad.dpick_trade_exp_date().send_keys("20122022")
            self.ad.authoritzed_person_name().send_keys(authorized_persons[i])

            drp_gender = Select(self.ad.drp_gender())
            drp_gender.select_by_index(2)

            self.ad.dpick_date_of_birth().send_keys("15121988")

            drp_country_birth = Select(self.ad.drp_country_of_birh())
            drp_country_birth.select_by_index(15)

            drp_nation = Select(self.ad.drp_nationality())
            drp_nation.select_by_index(55)

            self.ad.fund_btn_new().click()
            time.sleep(2)

            # Fill Fund details
            drp_fund_curr = Select(self.ad.drp_fund_curency())
            drp_fund_curr.select_by_index(2)

            self.ad.rate().send_keys("1511")
            self.ad.settlement_rate().send_keys("1448")
            self.ad.pay_settelement_rate().send_keys("48754")
            self.ad.balance_trigger().send_keys("1515121")
            self.ad.btn_add().click()

            # Move to the next entry
            self.ad.btn_nxt().click()

            # Navigate back and clear fields for the next iteration
            self.ud.btn_backe().click()

            self.ad.registration_number().clear()
            self.ad.authoritzed_person_name().clear()
            self.ad.trade_license_number().clear()
            self.ad.license_number().clear()
            self.ad.licensing_authority().clear()
            time.sleep(2)
            self.ad.fundcurr_table()
            time.sleep(2)
            self.ad.delete().click()
            time.sleep(5)

        # Check for any error messages
        error_msg = self.ad.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(f"Ser_Pro_ad_with_bulkdata_success_{i}.png")
            assert False
          # test case passed
          # last tested on built 03/09/2024 - Adarsh Sen Madhu



    def test_with_spaces(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

         # assigning values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        trade_lic_expiry = self.ad.dpick_trade_exp_date()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        drp_country_birth = Select(self.ad.drp_country_of_birh())
        drp_nation = Select(self.ad.drp_nationality())

         # assigning values

        dpick_agreement_star_date.send_keys("12081999")
        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys("2646 6 45 45454 ")
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num.send_keys("4 44544 54 ")
        trade_lic_expiry.send_keys("12082026")
        license_number.send_keys("15 45 15 14")
        license_authority.send_keys("ads  fa sff asf")
        auth_pers_name.send_keys("dges dgd  d c sgs")
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("12-08-1978")
        drp_country_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("3 2 34")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("23 11")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("122 2")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys("55 7 485 524")
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)
        # btn_next = self.ad.btn_nxt()
        # btn_next.click()
        time.sleep(10)

        # test case failed ( liscense authority is not accepting spaces)
        # tesst on last built 3/09/2024 - Adarsh Sen Madhu

    def test_with_maximum_length(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        trade_lic_expiry = self.ad.dpick_trade_exp_date()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        drp_country_birth = Select(self.ad.drp_country_of_birh())
        drp_nation = Select(self.ad.drp_nationality())

        registration_number_len = int(registration_number.get_attribute("maxlength"))
        print("registration_number", registration_number_len)
        trade_lic_num_len = int(trade_lic_num.get_attribute("maxlength"))
        print("trade_license_number", trade_lic_num_len)
        license_number_len = int(license_number.get_attribute("maxlength"))
        print("license_number", license_number_len)
        license_authority_len = int(license_authority.get_attribute("maxlength"))
        print("license_athority", license_authority_len)
        auth_pers_name_len = int(auth_pers_name.get_attribute("maxlength"))
        print("auth_pers_name_len", auth_pers_name_len)

        # assigning values


        dpick_agreement_star_date.send_keys("12081999")
        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num.send_keys(random_string_generator_numbers_18())
        trade_lic_expiry.send_keys("12082026")
        license_number.send_keys(random_string_generator_numbers_18())
        license_authority.send_keys(random_string_generator_max_50()+ random_string_generator_max_28())
        auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("12-08-1978")
        drp_country_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("3234")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers_18())
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        reg_num_val = len(self.ad.registration_number().get_attribute("value"))
        trade_lic_num_val = len(self.ad.trade_license_number().get_attribute("value"))
        lisence_num_val = len(self.ad.license_number().get_attribute("value"))
        lisc_auth_val = len(self.ad.licensing_authority().get_attribute("value"))
        auth_pers_val = len(self.ad.authoritzed_person_name().get_attribute("value"))

        print("reg_num_val:", reg_num_val)
        print("trade_lic_num_val:",trade_lic_num_val)
        print("lisence_num_val:", lisence_num_val)
        print("lisc_auth_val:", lisc_auth_val)
        print("auth_pers_val:", auth_pers_val)

        btn_next = self.ad.btn_nxt()
        btn_next.click()

        if reg_num_val <= registration_number_len:
           assert True
        else:
           self.driver.save_screenshot(screenShort.screen_short() + "ad_test_max_length.png")
           assert False


        if trade_lic_num_val <= trade_lic_num_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "ad_test_max_length.png")
            assert False

        if lisence_num_val <= license_number_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "ad_test_max_length.png")
            assert False

        if lisc_auth_val <= license_number_len:
            assert True
        else:
            self.driver.save_screenshot((screenShort.screen_short() + "ad_test_max_length.png"))
            assert False

        if auth_pers_val <= auth_pers_name_len:
            assert True
        else:
            self.driver.save_screenshot((screenShort.screen_short() + "ad_test_max_length.png"))
            assert False

        time.sleep(10)

        # test case passed
        # last tested on built 03/09/2024

    def test_validating_cancel(self, setup):

            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
            self.lp = LoginPage(self.driver)
            self.lp.setUsername(self.uname)
            self.lp.setPassword(self.upass)
            self.lp.clickLogin()

            # click action for nav bar arrow
            self.nav = Navigation_Page(self.driver)
            self.nav.click_navbar()

            # click action for general information

            self.nav.click_service_provider()

            # time.sleep(2)
            self.gi = General_Information(self.driver)
            self.ad = Agreement_Details(self.driver)

            drp_category = Select(self.gi.drp_category())
            ##bank_name = self.gi.bank_name()
            name = self.gi.name()
            arabic_name = self.gi.arabic_name()
            address_1 = self.gi.adress_1()
            address_2 = self.gi.adress_2()
            address_3 = self.gi.adress_3()
            postal_code = self.gi.postal_code()
            city = self.gi.city()
            drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
            drp_country_code = Select(self.gi.drp_country_code())
            mob_no = self.gi.mobile_number()
            email = self.gi.email()
            btn_next = self.gi.btn_nxt()

            drp_category.select_by_index(2)
            # bank_name.send_keys("fed")
            time.sleep(2)
            # click_bank = self.gi.click_bank_name()
            # click_bank.click()
            name.send_keys("adrstsgs")
            arabic_name.send_keys("hfsdjgfd")
            address_1.send_keys("dgjhafdhja")
            address_2.send_keys("gdhgfhjfg")
            address_3.send_keys("hkjgfkhgfkh")
            postal_code.send_keys("346714684")
            city.send_keys("hgdhkdgfkh")
            drp_country = Select(self.gi.drp_country())
            drp_country.select_by_index(3)
            drp_count_of_Incorp.select_by_index(5)
            drp_country_code.select_by_index(8)
            mob_no.send_keys("654546445454")
            email.send_keys("njuyg@gm.vom")
            btn_next.click()
            time.sleep(2)

            # click action for agreement details
            dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
            dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
            registration_number = self.ad.registration_number()
            dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
            trade_lic_num = self.ad.trade_license_number()
            license_number = self.ad.license_number()
            trade_lic_expiry = self.ad.dpick_trade_exp_date()
            license_authority = self.ad.licensing_authority()
            auth_pers_name = self.ad.authoritzed_person_name()
            drp_gender = Select(self.ad.drp_gender())
            dpick_dob = self.ad.dpick_date_of_birth()
            drp_country_birth = Select(self.ad.drp_country_of_birh())
            drp_nation = Select(self.ad.drp_nationality())

            dpick_agreement_star_date.send_keys("12081999")
            dpick_agreement_end_date.send_keys("12012066")
            registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
            dpick_reg_exp_date.send_keys("12112055")
            trade_lic_num.send_keys(random_string_generator_numbers_18())
            trade_lic_expiry.send_keys("12082026")
            license_number.send_keys(random_string_generator_numbers_18())
            license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
            auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
            drp_gender.select_by_index(2)
            dpick_dob.send_keys("12-08-1978")
            drp_country_birth.select_by_index(15)
            drp_nation.select_by_index(55)
            btn_new = self.ad.fund_btn_new()
            btn_new.click()
            time.sleep(2)
            drp_fund_curr = Select(self.ad.drp_fund_curency())
            drp_fund_curr.select_by_index(2)
            rate = self.ad.rate()
            rate.send_keys("3234")
            settlement_rate = self.ad.settlement_rate()
            settlement_rate.send_keys("2311")
            pay_settle_rate = self.ad.pay_settelement_rate()
            pay_settle_rate.send_keys("1222")
            balance_trigg = self.ad.balance_trigger()
            balance_trigg.send_keys(random_string_generator_numbers_18())

            rate_val = rate.get_attribute('value')
            settlement_rate = self.ad.settlement_rate()
            settlement_rate_val = settlement_rate.get_attribute("value")
            drp_fund_curr = Select(self.ad.drp_fund_curency())
            drp_fund_curr_val = drp_fund_curr.first_selected_option.text
            pay_settle_rate = self.ad.pay_settelement_rate()
            pay_settle_rate_val = pay_settle_rate.get_attribute('value')
            balance_trigg_val = balance_trigg.get_attribute('value')

            btn_add = self.ad.btn_add()
            btn_add.click()
            time.sleep(2)


            dpick_agreement_star_date_val = dpick_agreement_star_date.get_attribute('value')
            dpick_agreement_end_date_val = dpick_agreement_end_date.get_attribute('value')
            registration_number_val = registration_number.get_attribute('value')
            dpick_reg_exp_date_val = dpick_reg_exp_date.get_attribute('value')
            trade_lic_num_val = trade_lic_num.get_attribute('value')
            trade_lic_expiry_val = trade_lic_expiry.get_attribute('value')
            license_number_val = license_number.get_attribute('value')
            license_authority_val = license_authority.get_attribute('value')
            auth_pers_name_val = auth_pers_name.get_attribute('value')
            drp_gender_val = drp_gender.first_selected_option.text
            dpick_dob_val = dpick_dob.get_attribute('value')
            drp_country_birth_val = drp_country_birth.first_selected_option.text
            drp_nation_val = drp_nation.first_selected_option.text


            print(
                "values before cancel"
                
                f"dpick_agreement_star_date_val: {dpick_agreement_star_date_val}  "
                f"dpick_agreement_end_date_val: {dpick_agreement_end_date_val}"
                f"registration_number_val: {registration_number_val}"
                f"dpick_reg_exp_date_val: {dpick_reg_exp_date_val}"
                f"trade_lic_num_val: {trade_lic_num_val}"
                f"trade_lic_expiry_val: {trade_lic_expiry_val}"
                f"license_number_val: {license_number_val}"
                f"license_authority_val: {license_authority_val }"
                f"auth_pers_name_val: {auth_pers_name_val}"
                f"drp_gender_val:{drp_gender_val}"
                f"dpick_dob_val:{dpick_dob_val}"
                f"drp_country_birth_val:{drp_country_birth_val}"
                f"drp_nation_val:{drp_nation_val}"
                f"rate_val:{rate_val}"
                f"settlement_rate_val:{settlement_rate_val}"
                f"drp_fund_curr_val:{drp_fund_curr_val}"
                f"pay_settle_rate_val:{pay_settle_rate_val}"
                f"balance_trigg_val:{balance_trigg_val}"

                )
            self.ad.btn_cancel().click()
            time.sleep(2)
            self.ad.btn_cancl_confm().click()


            drp_category = Select(self.gi.drp_category())
            name = self.gi.name()
            arabic_name = self.gi.arabic_name()
            address_1 = self.gi.adress_1()
            address_2 = self.gi.adress_2()
            address_3 = self.gi.adress_3()
            postal_code = self.gi.postal_code()
            city = self.gi.city()
            drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
            drp_country_code = Select(self.gi.drp_country_code())
            mob_no = self.gi.mobile_number()
            email = self.gi.email()
            btn_next = self.gi.btn_nxt()

            drp_category.select_by_index(2)
            time.sleep(2)
            name.send_keys("adrstsgs")
            arabic_name.send_keys("hfsdjgfd")
            address_1.send_keys("dgjhafdhja")
            address_2.send_keys("gdhgfhjfg")
            address_3.send_keys("hkjgfkhgfkh")
            postal_code.send_keys("346714684")
            city.send_keys("hgdhkdgfkh")
            drp_country = Select(self.gi.drp_country())
            drp_country.select_by_index(3)
            drp_count_of_Incorp.select_by_index(5)
            drp_country_code.select_by_index(8)
            mob_no.send_keys("654546445454")
            email.send_keys("njuyg@gm.vom")
            btn_next.click()
            time.sleep(2)

            dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
            dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
            registration_number = self.ad.registration_number()
            dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
            trade_lic_num = self.ad.trade_license_number()
            license_number = self.ad.license_number()
            trade_lic_expiry = self.ad.dpick_trade_exp_date()
            license_authority = self.ad.licensing_authority()
            auth_pers_name = self.ad.authoritzed_person_name()
            drp_gender = Select(self.ad.drp_gender())
            dpick_dob = self.ad.dpick_date_of_birth()
            drp_country_birth = Select(self.ad.drp_country_of_birh())
            drp_nation = Select(self.ad.drp_nationality())

            dpick_agreement_star_date_af = dpick_agreement_star_date.get_attribute('value')
            dpick_agreement_end_date_af = dpick_agreement_end_date.get_attribute('value')
            registration_number_af = registration_number.get_attribute('value')
            dpick_reg_exp_date_af = dpick_reg_exp_date.get_attribute('value')
            trade_lic_num_af = trade_lic_num.get_attribute('value')
            trade_lic_expiry_af = trade_lic_expiry.get_attribute('value')
            license_number_af = license_number.get_attribute('value')
            license_authority_af = license_authority.get_attribute('value')
            auth_pers_name_af = auth_pers_name.get_attribute('value')
            drp_gender_af = drp_gender.first_selected_option.text
            dpick_dob_af = dpick_dob.get_attribute('value')
            drp_country_birth_af = drp_country_birth.first_selected_option.text
            drp_nation_af = drp_nation.first_selected_option.text


            print(
                "values after cancel"

                f"dpick_agreement_star_date_af: {dpick_agreement_star_date_af}  "
                f"dpick_agreement_end_date_af: {dpick_agreement_end_date_af}"
                f"registration_number_af: {registration_number_af}"
                f"dpick_reg_exp_date_af: {dpick_reg_exp_date_af}"
                f"trade_lic_num_af: {trade_lic_num_af}"
                f"trade_lic_expiry_af: {trade_lic_expiry_af}"
                f"license_number_af: {license_number_af}"
                f"license_authority_af: {license_authority_af}"
                f"auth_pers_name_af: {auth_pers_name_af}"
                f"drp_gender_af:{drp_gender_af}"
                f"dpick_dob_af:{dpick_dob_af}"
                f"drp_country_birth_af:{drp_country_birth_af}"
                f"drp_nation_af:{drp_nation_af}"

            )

            if registration_number_val != registration_number_af:
                assert True
            if trade_lic_num_val != trade_lic_num_af:
                assert True
            if auth_pers_name_val != auth_pers_name:
                assert True

            self.driver.quit()

            # test passed
            # last tested of built 03/09/2024

    def test_balance_alert_val_remn(self, setup):

        ### Testing based on manual reports###

        # (Fund currency>>When new currency is trying to be added,
        # balance alert trigger shows value as that of the currency added first, if the previous one has updated)



        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        trade_lic_expiry = self.ad.dpick_trade_exp_date()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        drp_country_birth = Select(self.ad.drp_country_of_birh())
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("12081999")
        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num.send_keys(random_string_generator_numbers_18())
        trade_lic_expiry.send_keys("12082026")
        license_number.send_keys(random_string_generator_numbers_18())
        license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
        auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("12-08-1978")
        drp_country_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("3234")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")

        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers_18())
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        self.ad.fundcurr_table()
        time.sleep(2)

        balance_trigg = self.ad.balance_trigger()

        balance_trigg_val_afterup = balance_trigg.get_attribute("value")

        btn_update = self.ad.btn_updte()
        btn_update.click()
        time.sleep(3)



        print(
            "Values after update:\n"
            
            f"values after update: balance_trigg_val_afterup: {balance_trigg_val_afterup}"
        )

        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)

        balance_trigg = self.ad.balance_trigger()
        balance_trigg_val_new = balance_trigg.get_attribute("value")

        print(
            "Values after adding new :\n"

            f"values after adding new :    balance_trigg_val_new: {balance_trigg_val_new}"
        )

        if balance_trigg_val_new != balance_trigg_val_afterup:
            assert True
        else:
            self.driver.save_screenshot((screenShort.screen_short() + "ad_balance_val_err0r_.png"))
            assert False

        time.sleep(5)

        ### test case passed ( values are not showing )
        ### tested on last built 03/09/2024 - Adarsh Sen Madhu


    def test_validating_req_field_date(self, setup):

        ### Testing based on manual reports###

        # Most of the fields including calender widgets shows required even after entering values


        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        #dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        trade_lic_expiry = self.ad.dpick_trade_exp_date()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        #dpick_dob = self.ad.dpick_date_of_birth()
        drp_country_birth = Select(self.ad.drp_country_of_birh())
        drp_nation = Select(self.ad.drp_nationality())
        btn_nxt = self.ad.btn_nxt()

        #dpick_agreement_star_date.send_keys("12081999")
        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num.send_keys(random_string_generator_numbers_18())
        trade_lic_expiry.send_keys("12082026")
        license_number.send_keys(random_string_generator_numbers_18())
        license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
        auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_gender.select_by_index(2)
        #dpick_dob.send_keys("12-08-1978")
        drp_country_birth.select_by_index(15)
        drp_nation.select_by_index(55)
        btn_new = self.ad.fund_btn_new()
        btn_new.click()
        time.sleep(2)
        drp_fund_curr = Select(self.ad.drp_fund_curency())
        drp_fund_curr.select_by_index(2)
        rate = self.ad.rate()
        rate.send_keys("3234")
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers_18())
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)
        btn_nxt.click()
        time.sleep(2)

        dpick_dob = self.ad.dpick_date_of_birth()
        dpick_dob.send_keys("12-08-1978")

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_star_date.send_keys("12081999")

        time.sleep(3)
        btn_nxt.click()

        ### test passed
        ### last tested on built 03/09/2024 - Adarsh Sen Madhu

    def test_double_calndr_widget(self, setup):

        ### testing of manual bugs
        ##2 calender widgets are coming for date fields

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for general information

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        btn_next.click()
        time.sleep(2)

        # click action for agreement details

        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
        registration_number = self.ad.registration_number()
        dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
        trade_lic_num = self.ad.trade_license_number()
        license_number = self.ad.license_number()
        trade_lic_expiry = self.ad.dpick_trade_exp_date()
        license_authority = self.ad.licensing_authority()
        auth_pers_name = self.ad.authoritzed_person_name()
        drp_gender = Select(self.ad.drp_gender())
        dpick_dob = self.ad.dpick_date_of_birth()
        drp_country_birth = Select(self.ad.drp_country_of_birh())
        drp_nation = Select(self.ad.drp_nationality())

        dpick_agreement_star_date.send_keys("12081999")

        dpick_agreement_end_date.send_keys("12012066")
        registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
        dpick_reg_exp_date.send_keys("12112055")
        trade_lic_num.send_keys(random_string_generator_numbers_18())
        trade_lic_expiry.send_keys("12082026")
        license_number.send_keys(random_string_generator_numbers_18())
        license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
        auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_gender.select_by_index(2)
        dpick_dob.send_keys("12-08-1978")
        drp_country_birth.select_by_index(15)
        drp_nation.select_by_index(55)

        # Locating the input field - date of agreement


        dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
        dpick_agreement_star_date.send_keys("12081999")

        # Press backspace 5 times
        for _ in range(1):
         dpick_agreement_star_date.send_keys(Keys.SPACE)

         time.sleep(5)

         print(
             "Refer to the test case documentation here: https://docs.google.com/spreadsheets/d/1KCGKeeg6HNDSpMQggRA00OUgte7jRhg7XqUQPkMqc10/edit?usp=sharing")

         # test failed (2 widgets are coming)
         # last tested on built 03/09/2024




























