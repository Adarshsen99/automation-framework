import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Delegate_details, Beneficiary_details, \
    Remittance_details, Transaction_Review
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50, random_string_generator_numbers
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Beneficiary_details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_banktransfer(self, setup):
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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("ronaldo")
        self.bd.beneficiary_selectbar()
        time.sleep(2)
        bank_selct = Select(self.bd.drp_bank())
        bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

        ## test passed

    def test_adding_without_data(self, setup):
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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        # benefiary_name = self.bd.beneficiary_search_bar()
        # benefiary_name.send_keys("ronaldo")
        # self.bd.beneficiary_selectbar()
        # time.sleep(2)
        # bank_selct = Select(self.bd.drp_bank())
        # bank_selct.select_by_index(1)
        # time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

    def test_sending_invalid_data(self, setup):
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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("bdvashdvashdvsahd")
        # self.bd.beneficiary_selectbar()
        time.sleep(3)
        # bank_selct = Select(self.bd.drp_bank())
        # bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

    def test_validating_maxlength(self, setup):
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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()

        benefiary_name_len = (benefiary_name.get_attribute("maxlength"))
        print("benefiary_name_len:", benefiary_name_len)

        benefiary_name.send_keys("ronaldo")
        self.bd.beneficiary_selectbar()
        time.sleep(2)
        bank_selct = Select(self.bd.drp_bank())
        bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

    def test_sending_spl_char(self, setup):
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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        #
        time.sleep(5)
        # bank_selct = Select(self.bd.drp_bank())
        # bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

    def test_bank_details_remain_after_coming_next(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_remitance()

        # Customer Details
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)
        self.custom_name = self.cd.customer_search_bar()
        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        self.cd.btn_next()

        # Delegate Details
        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)
        self.dd.btn_nexte()

        # Beneficiary Details
        self.bd = Beneficiary_details(self.driver)
        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("ronaldo")
        time.sleep(3)
        self.bd.beneficiary_selectbar_ronaldo()
        time.sleep(2)

        # Select a bank
        bank_select = Select(self.bd.drp_bank())
        bank_select.select_by_index(1)
        bank_name = bank_select.first_selected_option.text
        print("Bank Name Selected:", bank_name)

        self.bd.btn_nexte()
        time.sleep(2)

        # Navigate back
        self.rd = Remittance_details(self.driver)
        self.rd.btn_bck()
        time.sleep(5)

        # Check if the bank selection is retained after going back
        bank_select_after = Select(self.bd.drp_bank())

        try:
            bank_name_after = bank_select_after.first_selected_option.text
            print("Bank Name After Back:", bank_name_after)

            # Assert that the bank name after coming back is the same as initially selected
            assert bank_name == bank_name_after, f"Bank name mismatch! Expected '{bank_name}', but got '{bank_name_after}'"

        except Exception as e:
            # This will catch any issue if the dropdown is empty or no selection is found
            print(f"Error: {str(e)}")
            assert False, "Bank name is not retained after going back!"

        # test failed
        # bank name not remains

    def test_adding_benenficiaries_with_fast_cash(self, setup):
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
        self.drp_transn_typ.select_by_index(2)
        self.custom_name = self.cd.customer_search_bar()

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("pisha")
        self.bd.beneficiary_select_bar_pisharadi()
        location = Select(self.bd.drp_location())
        location.select_by_index(2)

        time.sleep(2)
        bank_selct = Select(self.bd.drp_bank())
        bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

    def test_bank_location_erases_after_coming_back(self, setup):

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
        self.drp_transn_typ.select_by_index(2)
        self.custom_name = self.cd.customer_search_bar()

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("pisha")
        self.bd.beneficiary_select_bar_pisharadi()

        time.sleep(3)
        location = Select(self.bd.drp_location())
        location.select_by_index(1)
        time.sleep(2)

        location_name = location.first_selected_option.text
        print("location_name:", location_name)

        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)

        self.rd = Remittance_details(self.driver)

        self.rd.btn_bck()
        time.sleep(2)

        location_name_after = Select(self.bd.drp_location())

        try:
            location_name_after = location_name_after.first_selected_option.text
            print("location_name_after:", location_name_after)

            assert location_name == location_name_after, f"location name mismatch! Expected '{location_name}', but got '{location_name_after}'"

        except Exception as e:
            # This will catch any issue if the dropdown is empty or no selection is found
            print(f"Error: {str(e)}")
            assert False, "location name is not retained after going back!"

        # test failed
        # location is not retained after coming back

    def test_beneficiary_details_undefined_on_preview(self, setup):

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

        self.custom_name.send_keys("Messi Marie Brown")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        transcation_mode = Select(self.dd.drp_transaction_mode())
        transcation_mode.select_by_index(1)

        self.dd.btn_nexte()
        time.sleep(2)

        self.bd = Beneficiary_details(self.driver)

        benefiary_name = self.bd.beneficiary_search_bar()
        benefiary_name.send_keys("ronaldo")
        self.bd.beneficiary_selectbar_ronaldo()
        time.sleep(2)
        bank_selct = Select(self.bd.drp_bank())
        bank_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(4)

        self.rd = Remittance_details(self.driver)
        self.rd.click_beneficiary_preview()
        time.sleep(2)

        bank_preview = self.rd.bank_preview()
        print("bank_preview:", bank_preview)

        bank_code_preview = self.rd.bank_code_preview()
        print("bank_code_preview:", bank_code_preview)

        branch_code_pre = self.rd.branch_code_preview()
        print("branch_code_pre:", branch_code_pre)

        branch_country_pre = self.rd.branch_country_preview()
        print("branch_country_pre:", branch_country_pre)

        branch_address_pre = self.rd.branch_address_preview()
        print("branch_address_pre:", branch_address_pre)

        self.rd.btn_bck()
        time.sleep(3)
        self.bd.btn_nexte()
        time.sleep(5)

        #self.rd.click_beneficiary_preview()
        time.sleep(3)

        bank_preview_aft = self.rd.bank_preview()
        print("bank_preview_aft:", bank_preview_aft)

        bank_code_preview_aft = self.rd.bank_code_preview()
        print("bank_code_preview_af:", bank_code_preview_aft)

        branch_code_pre_aft = self.rd.branch_code_preview()
        print("branch_code_pre_aft:", branch_code_pre_aft)

        branch_country_pre_aft = self.rd.branch_country_preview()
        print("branch_country_pre_aft:",branch_country_pre_aft)

        branch_address_pre_aft = self.rd.branch_address_preview()
        print("branch_address_pre_aft:", branch_address_pre_aft)

        if bank_preview_aft == bank_preview and bank_code_preview_aft == bank_code_preview and branch_code_pre_aft == branch_code_pre:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "bene_pre_undefined.png")
            assert False






