import time

import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.service_provider import General_Information, Agreement_Details
from Dinero_automation.utilities.randomString import random_string_generator_max_30, random_string_generator_max_50, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51, random_string_generator_numbers_18
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_General_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_with_valid_data(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(4)

        #click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # entering fields for general information

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        time.sleep(2)
        btn_next.click()

        error_msg = self.gi.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_Gi_with_valid_data.png")
            assert False
        self.driver.quit()

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
        time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("")
        arabic_name.send_keys("")
        address_1.send_keys("")
        address_2.send_keys("")
        address_3.send_keys("")
        postal_code.send_keys("")
        city.send_keys("")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("")
        email.send_keys("")
        btn_next.click()

        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_Gi_withot_data.png")
            assert False

    def test_with_spchar(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        time.sleep(4)
        self.gi = General_Information(self.driver)

        # Assigning the fields

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # Sending the data

        drp_category.select_by_index(1)
        time.sleep(4)
        # other_cat = self.gi.catego_other_field()
        # other_cat.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        arabic_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        address_1.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        address_2.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        address_3.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        postal_code.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        city.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        email.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        btn_next.click()

        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_Gi_with_spl_char_data.png")
            assert False

        time.sleep(10)

        #test case failed , ( other category accept special characters like " ^_][` " )
        # test on last build - 3/09/2024- Adarsh Sen Madhu

    def test_with_spchar_nums_char(self, setup):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        left_side_element = self.driver.find_element(By.XPATH,
                                                     "//div[@class='sideBarRoutesContainer ']")  # Use appropriate locator for your page

        # Scroll the left side element using JavaScript
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 300;", left_side_element)
        # click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(1)
        time.sleep(2)
        # other_cat = self.gi.catego_other_field()
        # other_cat.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        arabic_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        address_1.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        address_2.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        address_3.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        postal_code.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        city.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        email.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        btn_next.click()

        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_Gi_with_spl_char_mum_data.png")
            assert False
        time.sleep(10)

        #test case failed , ( other category accept special characters like " ^_][` " )
        # test on last build - 3/09/2024 - Adarsh Sen Madhu

    def test_with_data_have_spaces(self, setup):
        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("asad fgv  xfv")
        arabic_name.send_keys("dfdsg dfgdf dfc dfb ")
        address_1.send_keys("vdv dfvc fvcx ")
        address_2.send_keys("vdf fvcvc fv ")
        address_3.send_keys("gdgb gvcb dfv ")
        postal_code.send_keys("2454 54 45 ")
        city.send_keys("srgv fv v fv")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys("6545 46445 454")
        email.send_keys("nj  uyg@ gm.vom")
        time.sleep(2)
        btn_next.click()
        time.sleep(2)

        error_msg = self.gi.error_message()
        if not error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_Gi_with_space_data.png")
            assert False
        time.sleep(5)

        # test case passed
        # tested on last built 3/09/2024 - Adarsh Sen Madhu

    def test_with_validating_maxlen(self, setup, ):

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        self.gi = General_Information(self.driver)
        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # for getting maimum length

        name_len = int(name.get_attribute('maxlength'))
        print("Name:", name_len)
        arabic_name_len = int(arabic_name.get_attribute("maxlength"))
        print("arabic_name:", arabic_name_len)
        address_1_len = int(address_1.get_attribute("maxlength"))
        print("address_1:", address_1_len)
        address_2_len = int(address_2.get_attribute("maxlength"))
        print("address_2:", address_2_len)
        address_3_len = int(address_3.get_attribute("maxlength"))
        print("address_2:", address_3_len)
        postal_code_len = int(postal_code.get_attribute("maxlength"))
        print("postal_code:", postal_code_len)
        city_len = int(city.get_attribute("maxlength"))
        print("city:", city_len)
        mob_no_len = int(mob_no.get_attribute("maxlength"))
        print("mob_no:", mob_no_len)
        email_len = int(email.get_attribute("maxlength"))
        print("email:", email_len)

        # assingning length and value

        name_val = len(self.gi.name().get_attribute("value"))
        arabic_name_val = len(self.gi.arabic_name().get_attribute("value"))
        address_1_val = len(self.gi.adress_1().get_attribute("value"))
        address_2_val = len(self.gi.adress_2().get_attribute("value"))
        address_3_val = len(self.gi.adress_3().get_attribute("value"))
        postal_code_val = len(self.gi.postal_code().get_attribute("value"))
        city_val = len(self.gi.city().get_attribute("value"))
        mob_no_val = len(self.gi.mobile_number().get_attribute("value"))

        # assigning values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        arabic_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_1.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_2.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_3.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        postal_code.send_keys("24548282 ")
        city.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys(random_string_generator_numbers_18())
        email.send_keys("njuyg@gm.vom")
        time.sleep(2)
        btn_next.click()
        time.sleep(2)

        # assertion

        if name_val <= name_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False

        if arabic_name_val <= arabic_name_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False

        if address_1_val <= address_1_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False
        if address_2_val <= address_2_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False
        if address_3_val <= address_3_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")

        if postal_code_val <= postal_code_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False

        if city_val <= city_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False

        if mob_no_val <= mob_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Gi_test_validity_max_length.png")
            assert False

            time.sleep(5)

        # test case passed
        # tested on last build - 3/09/2024 - Adarsh Sen Madhu

    def test_validating_cancel(self, setup, ):
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

        # Assigning and entering values

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()

        # Set values

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        arabic_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_1.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_2.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_3.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        postal_code.send_keys("24548282 ")
        city.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys(random_string_generator_numbers_18())
        email.send_keys("njuyg@gm.vom")

        # Store the values before cancel

        name_val = len(self.gi.name().get_attribute("value"))
        arabic_name_val = len(self.gi.arabic_name().get_attribute("value"))
        address_1_val = len(self.gi.adress_1().get_attribute("value"))
        address_2_val = len(self.gi.adress_2().get_attribute("value"))
        address_3_val = len(self.gi.adress_3().get_attribute("value"))
        postal_code_val = len(self.gi.postal_code().get_attribute("value"))
        city_val = len(self.gi.city().get_attribute("value"))
        mob_no_val = len(self.gi.mobile_number().get_attribute("value"))

        print(f"name_val: {name_val}, arabic_name_val: {arabic_name_val}, "
              f"address_1_val: {address_1_val}, address_2_val: {address_2_val}, "
              f"address_3_val: {address_3_val}, postal_code_val: {postal_code_val}, "
              f"city_val: {city_val}, mob_no_val: {mob_no_val}")

        self.gi.btn_nxt().click()
        time.sleep(2)
        self.ad.btn_back().click()

        # # Perform cancel operation

        self.gi.btn_cancel().click()
        time.sleep(2)
        self.gi.btn_cancelconfirm().click()

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        arabic_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_1.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_2.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        address_3.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        postal_code.send_keys("24548282 ")
        city.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        mob_no.send_keys(random_string_generator_numbers_18())
        email.send_keys("njuyg@gm.vom")

        self.gi.btn_nxt().click()
        time.sleep(2)
        self.ad.btn_back().click()

        # # Perform cancel operation
        self.gi.btn_cancel().click()  # Assuming there's a cancel button method in General_Information
        self.gi.btn_cancelconfirm().click()

        # Re-assign and check values after cancel

        name_af = len(self.gi.name().get_attribute("value"))
        arabic_name_af = len(self.gi.arabic_name().get_attribute("value"))
        address_1_af = len(self.gi.adress_1().get_attribute("value"))
        address_2_af = len(self.gi.adress_2().get_attribute("value"))
        address_3_af = len(self.gi.adress_3().get_attribute("value"))
        postal_code_af = len(self.gi.postal_code().get_attribute("value"))
        city_af = len(self.gi.city().get_attribute("value"))
        mob_no_af = len(self.gi.mobile_number().get_attribute("value"))

        print(f"name_af: {name_af}, arabic_name_af: {arabic_name_af}, "
              f"address_1_af: {address_1_af}, address_2_af: {address_2_af}, "
              f"address_3_af: {address_3_af}, postal_code_af: {postal_code_af}, "
              f"city_af: {city_af}, mob_no_af: {mob_no_af}")

        time.sleep(5)

        # test case passed
        # last tested - 03/09/2024 - Adarsh Sen Madhu

    def test_mobile_num_req_remain(self, setup):

        #### Test cases according to Manual test reports ###

        # test case =  Mobile num>> If not added and goes next, Required shows and upon adding Required highlight remains ##

        # login setup

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # entering fields for general information

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        #mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        time.sleep(2)
        btn_next.click()
        mob_no.send_keys("654546445454")
        time.sleep(2)

        # test case passed, status: closed
        #last tested-built - 3/09/2024 - Adarsh Sen Madhu

    def test_moble_num_bckspace_clear(self, setup):

        #### Test cases according to Manual test reports ###

        # test case = Mobile num>>Upon backspacing, entire mobile data vanishes ##

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(2)

        # click action for general information

        self.nav.click_service_provider()
        time.sleep(2)
        self.gi = General_Information(self.driver)

        drp_category = Select(self.gi.drp_category())
        name = self.gi.name()
        arabic_name = self.gi.arabic_name()
        address_1 = self.gi.adress_1()
        address_2 = self.gi.adress_2()
        address_3 = self.gi.adress_3()
        postal_code = self.gi.postal_code()
        city = self.gi.city()
        drp_country = Select(self.gi.drp_country())
        drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
        drp_country_code = Select(self.gi.drp_country_code())
        mob_no = self.gi.mobile_number()
        email = self.gi.email()
        btn_next = self.gi.btn_nxt()

        # entering fields for general information

        drp_category.select_by_index(2)
        time.sleep(2)
        name.send_keys("adrstsgs")
        arabic_name.send_keys("hfsdjgfd")
        address_1.send_keys("dgjhafdhja")
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys("346714684")
        city.send_keys("hgdhkdgfkh")
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(8)
        # mob_no.send_keys("654546445454")
        email.send_keys("njuyg@gm.vom")
        time.sleep(2)

        # Locating the input field - mobile number

        mob_no = self.gi.mobile_number()

        # Type some text into the field
        mob_no.send_keys("4564656")

        # Press backspace 5 times
        for _ in range(8):
            mob_no.send_keys(Keys.BACKSPACE)

        # Assert the final value of the field, if needed
        assert mob_no.get_attribute("value") == ""

        time.sleep(2)

        # test case failed, status - open
        # test on last built-3/9/2024- Adarsh Sen Madhu
