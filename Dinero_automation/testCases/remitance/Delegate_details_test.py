import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Delegate_details, Beneficiary_details
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_delegate_details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    #
    # def test_sending_valid_data_name(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #
    #     self.dd = Delegate_details(self.driver)
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transcation_mode.select_by_index(2)
    #
    #     delegate_name = self.dd.delegate_searchbar()
    #     delegate_name.send_keys("hild")
    #     self.dd.delegate_select_bar()
    #
    #     delegate_name_value = delegate_name.get_attribute('value')
    #     print("Delegate Name: ", delegate_name_value)
    #
    #     time.sleep(3)
    #     self.dd.btn_nexte()
    #
    #     if delegate_name_value == "hilda dada dadad":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "Remi_dd_with_valid_data.png")
    #         assert False
    #     #test passed
    #     # last tested on built 19/09/2024
    #
    # def test_sendin_without_data(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #
    #     self.dd = Delegate_details(self.driver)
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transcation_mode.select_by_index(2)
    #
    #     delegate_name = self.dd.delegate_searchbar()
    #     #delegate_name.send_keys("hild")
    #     #self.dd.delegate_select_bar()
    #
    #     delegate_name_value = delegate_name.get_attribute('value')
    #     print("Delegate Name: ", delegate_name_value)
    #     self.dd.btn_verify()
    #
    #     time.sleep(3)
    #     self.dd.btn_nexte()
    #     time.sleep(2)
    #
    #     # test failed (  we can go next without adding delegate )
    #     # last tested on built 19/09/2024
    #
    # def test_maximum_length(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #
    #     self.dd = Delegate_details(self.driver)
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transcation_mode.select_by_index(2)
    #
    #     delegate_name = self.dd.delegate_searchbar()
    #     delegate_name.send_keys(random_string_generator_max_50())
    #     #self.dd.delegate_select_bar()
    #
    #     delegate_name_value = delegate_name.get_attribute('value')
    #     print("Delegate Name: ", delegate_name_value)
    #
    #     max_length = delegate_name.get_attribute('maxlength')
    #
    #     # Check if maxlength is None and handle accordingly
    #
    #     if max_length is None:
    #         print("The field does not have a maxlength attribute.")
    #     else:
    #         print(f"The maximum length of the field is: {max_length}")
    #     time.sleep(3)
    #     self.dd.btn_nexte()
    #
    # def test_sdending_invalid_data(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #
    #     self.dd = Delegate_details(self.driver)
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transcation_mode.select_by_index(2)
    #
    #     delegate_name = self.dd.delegate_searchbar()
    #     delegate_name.send_keys(random_string_generator_max_50())
    #     #self.dd.delegate_select_bar()
    #
    #     delegate_name_value = delegate_name.get_attribute('value')
    #     print("Delegate Name: ", delegate_name_value)
    #
    #     time.sleep(3)
    #     self.dd.btn_verify()
    #     self.dd.btn_nexte()
    #     time.sleep(2)
    #
    #     # if delegate_name_value == "hilda dada dadad":
    #     #     assert True
    #     # else:
    #     #     self.driver.save_screenshot(screenShort.screen_short() + "Remi_dd_with_valid_data.png")
    #     #     assert False
    #
    # def test_validating_cancel(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #
    #     self.dd = Delegate_details(self.driver)
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transcation_mode.select_by_index(2)
    #
    #     delegate_name = self.dd.delegate_searchbar()
    #     delegate_name.send_keys("hild")
    #     self.dd.delegate_select_bar()
    #     self.dd.btn_verify()
    #
    #     delegate_name_value_bef = delegate_name.get_attribute('value')
    #     print("Delegate Name before: ", delegate_name_value_bef)
    #
    #     transc_mode_val = transcation_mode.first_selected_option.text
    #     print("transc_mode_value_before:", transc_mode_val)
    #
    #     time.sleep(3)
    #     self.dd.btn_nexte()
    #     time.sleep(2)
    #     self.bd = Beneficiary_details(self.driver)
    #
    #     self.bd.btn_backe()
    #     time.sleep(2)
    #     self.dd.btn_cancel()
    #     self.dd.btn_cancel_yes()
    #     time.sleep(2)
    #
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # delegate_name = self.dd.delegate_searchbar()
    #     # delegate_name_value_aft = delegate_name.get_attribute('value')
    #     # print("Delegate Name after: ", delegate_name_value_aft)
    #
    #     transcation_mode = Select(self.dd.drp_transaction_mode())
    #     transc_mode_val_af = transcation_mode.first_selected_option.text
    #     print("transc_mode_value_after:", transc_mode_val_af)
    #
    #     if transc_mode_val_af != transc_mode_val:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "Remi_dd_with_valid_data.png")
    #         assert False
    #
    #     # test passed
    #     # last tested on built 18/09/2024
    #
    # def test_bulk_data(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer details
    #     self.nav.click_remitance()
    #     self.cd = Customer_Details(self.driver)
    #     self.drp_transn_typ = Select(self.cd.drp_transcation_type())
    #     self.drp_transn_typ.select_by_index(1)
    #     self.custom_name = self.cd.customer_search_bar()
    #
    #     self.custom_name.send_keys("Kar")
    #     time.sleep(2)
    #     self.cd.custom_select1()
    #     self.cd.verify_btn()
    #     time.sleep(2)
    #     self.cd.btn_next()
    #     time.sleep(2)
    #
    #     # click action for Delegate details
    #     delegate_names_bulk = ['Karunakar middle last', 'Messi Marie Brown', ' Pele Marie Jones', 'babu Marie Williams']
    #
    #     for i in range(3):
    #         self.dd = Delegate_details(self.driver)
    #         transcation_mode = Select(self.dd.drp_transaction_mode())
    #         transcation_mode.select_by_index(2)
    #
    #         delegate_name = self.dd.delegate_searchbar()
    #         delegate_name.send_keys(delegate_names_bulk[i])
    #         self.dd.delegate_select_bar()
    #
    #         delegate_name_value = delegate_name.get_attribute('value')
    #         print("Delegate Name: ", delegate_name_value)
    #
    #         time.sleep(3)
    #         self.dd.btn_nexte()
    #
    #         # # test passed
    #         # # last tested on built 19/09/2024

    def test_delegate_value_undefined(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        # time.sleep(2)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer details
        self.nav.click_remitance()
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)
        self.custom_name = self.cd.customer_search_bar()

        self.custom_name.send_keys("Kar")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(2)

        delegate_name = self.dd.delegate_searchbar()
        delegate_name.send_keys("hild")
        self.dd.delegate_select_bar()
        self.dd.btn_verify()

        del_name_pg = self.dd.delegate_values_on_page_name()
        del_arabic_name_pg = self.dd.delegate_values_on_page_arabic_name()
        del_gendder_pg = self.dd.delegat_val_gender()

        del_name_pg_val = self.dd.delegate_values_on_page_name().text  # Get the visible text
        del_arabic_name_pg_val = self.dd.delegate_values_on_page_arabic_name().text  # Get the visible text
        del_gendder_pg_val = self.dd.delegat_val_gender().text  # Get the visible text

        print(f" del_name_pg_val: {del_name_pg_val}, del_arabic_name_pg_val: { del_arabic_name_pg_val}, del_gendder_pg_val: {del_gendder_pg_val}" )

        time.sleep(2)
        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)
        self.bd.btn_backe()
        time.sleep(2)
        self.dd.btn_verify()
        self.dd.btn_nexte()
        time.sleep(2)
        self.bd.btn_backe()
        time.sleep(5)

        # del_name_pg_val_af = self.dd.delegate_values_on_page_name().text  # Get the visible text
        # del_arabic_name_pg_val_af = self.dd.delegate_values_on_page_arabic_name().text  # Get the visible text
        # del_gendder_pg_val_af = self.dd.delegat_val_gender().text  # Get the visible text
        #
        # print(
        #     f" del_name_pg_val_af: {del_name_pg_val_af}, del_arabic_name_pg_val_af: {del_arabic_name_pg_val_af}, del_gendder_pg_val_af: {del_gendder_pg_val_af}")

        # del_name_pg_val_aft = self.dd.delegate_values_on_page_name().text  # Get the visible text
        # del_arabic_name_pg_val_aft = self.dd.delegate_values_on_page_arabic_name().text  # Get the visible text
        # del_gendder_pg_val_aft = self.dd.delegat_val_gender().text

        # if del_name_pg_val == del_name_pg_val_aft:
        #     assert True
        # else:
        #     assert False

        try:
            # Check if the element exists after clicking cancel
            del_name_pg_val_aft = self.dd.delegate_values_on_page_name()

            # If the element exists, retrieve its text
            del_name_pg_val_aft_text = del_name_pg_val_aft.text

            # Assert if the text is "undefined"
            if not del_name_pg_val_aft_text.lower() == "undefined undefined":
                assert True

            else:
                self.driver.save_screenshot(screenShort.screen_short() + "test_delegate_value_undefined.png")

                assert False

        except NoSuchElementException:
            self.driver.save_screenshot(screenShort.screen_short() + "test_delegate_value_undefined.png")
            assert False







