import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Delegate_details, Beneficiary_details, \
    Remittance_details, Transaction_Review, Payment_details
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50, random_string_generator_numbers
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Payment_Details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_on_all_payment_mode(self, setup):
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
        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView();", sidebar)
        time.sleep(2)
        # click action for customer details
        self.nav.click_remitance()
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)
        self.custom_name = self.cd.customer_search_bar()

        self.custom_name.send_keys("adarsh")
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
        benefiary_name.send_keys("mangalath")
        self.bd.beneficiary_selectbar_man()
        time.sleep(2)
        loc_selct = Select(self.bd.drp_location())
        loc_selct.select_by_index(1)
        time.sleep(1)
        self.bd.btn_nexte()
        time.sleep(2)
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy = Select(self.rd.drp_currency())

        currecncy.select_by_index(2)
        service_pro = Select(self.rd.drp_service_provider())
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("10000")
        rate = self.rd.rate_type_area()
        rate.send_keys("2.6")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()
        time.sleep(2)

        # Set values for thousand, hundred, and ten notes
        self.pd.cash500().send_keys("4")
        time.sleep(2)
        self.pd.cash20().send_keys("2")
        #self.pd.cash1().send_keys("2")

        time.sleep(2)

        self.pd.submit()
        self.pd.pos_amount().send_keys("2040")
        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)
        self.pd.pos_code().send_keys("2002")
        time.sleep(2)

        self.pd.cheque_amount().send_keys("2040")
        self.pd.cheque_number().send_keys("4548348")
        self.pd.cheque_bank().send_keys("ICICI")
        self.pd.cheque_date().send_keys("12092024")
        time.sleep(2)

        self.pd.online_amount().send_keys("2040")
        self.pd.digital_pay().send_keys("2040")
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(15)

    def test_sending_without_data(self, setup):
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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("100000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        # cash_element.click()
        #
        # # Set values for thousand, hundred, and ten notes
        # self.pd.cash1000().send_keys("20")
        # self.pd.cash100().send_keys("2")
        #
        # # Use cash10 values from the list
        #
        # self.pd.cash10().send_keys("4")
        # self.pd.cash1().send_keys("3")
        #
        # time.sleep(2)
        #
        # self.pd.submit()
        # self.pd.pos_amount().send_keys("20243")
        # pos_bank = Select(self.pd.drp_pos_bank())
        # pos_bank.select_by_index(1)
        # self.pd.pos_code().send_keys("2002")
        # time.sleep(2)
        #
        # self.pd.cheque_amount().send_keys("20243")
        # self.pd.cheque_number().send_keys("4548348")
        # self.pd.cheque_bank().send_keys("ICICI")
        # self.pd.cheque_date().send_keys("12092024")
        # time.sleep(2)
        #
        # self.pd.online_amount().send_keys("20243")
        # self.pd.digital_pay().send_keys("20243")
        # self.pd.generate_qr_code()
        #
        self.pd.save_remittance()
        time.sleep(2)
        error_message_element = self.pd.error_messge()

        # Get the error message text
        error_message_text = error_message_element.text

        actual_error_message = error_message_text.split("\n")[0]

        # Assert that the error message is what we expect
        expected_error_message = "Some of the required fields are empty"
        assert actual_error_message == expected_error_message, f"Expected: {expected_error_message}, but got: {actual_error_message}"

        print(f"Assertion passed: Error message is '{actual_error_message}'")

        #test passed

    def test_with_spl_char(self, setup):
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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("100000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()

        # Set values for thousand, hundred, and ten notes
        self.pd.cash1000().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.cash100().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        # Use cash10 values from the list

        self.pd.cash10().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.cash1().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        time.sleep(2)

        self.pd.submit()
        self.pd.pos_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)
        self.pd.pos_code().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        time.sleep(2)

        self.pd.cheque_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.cheque_number().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.cheque_bank().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.cheque_date().send_keys("12092024")
        time.sleep(2)

        self.pd.online_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.digital_pay().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(15)

        # test failed
        # some fields in cash accepts +, - and e

    def test_sending_spl_char_num(self, setup):
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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("100000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()

        # Set values for thousand, hundred, and ten notes
        self.pd.cash1000().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.cash100().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")

        # Use cash10 values from the list

        self.pd.cash10().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.cash1().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")

        time.sleep(2)

        self.pd.submit()
        self.pd.pos_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)
        self.pd.pos_code().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        time.sleep(2)

        self.pd.cheque_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.cheque_number().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.cheque_bank().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.cheque_date().send_keys("12092024")
        time.sleep(2)

        self.pd.online_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.digital_pay().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(15)

        # test failed
        # some fields in cash accepts +, - and e

    def test_sending_numbers(self, setup):
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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("100000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()

        # Set values for thousand, hundred, and ten notes
        self.pd.cash1000().send_keys("1234567890")
        self.pd.cash100().send_keys("1234567890")

        # Use cash10 values from the list

        self.pd.cash10().send_keys("1234567890")
        self.pd.cash1().send_keys("1234567890")

        time.sleep(2)

        self.pd.submit()
        self.pd.pos_amount().send_keys("1234567890")
        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)
        self.pd.pos_code().send_keys("1234567890")
        time.sleep(2)

        self.pd.cheque_amount().send_keys("1234567890")
        self.pd.cheque_number().send_keys("1234567890")
        self.pd.cheque_bank().send_keys("1234567890")
        self.pd.cheque_date().send_keys("12092024")
        time.sleep(2)

        self.pd.online_amount().send_keys("1234567890")
        self.pd.digital_pay().send_keys("1234567890")
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(15)

        # test failed
        # some fields in cash accepts +, - and e

    def test_maximum_length(self, setup):
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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("100000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()

        # Set values for thousand, hundred, and ten notes

        cash1000 = self.pd.cash1000()
        cash1000_len = cash1000.get_attribute("maxlength")
        print("cash1000_len:", cash1000_len)
        cash1000.send_keys(random_string_generator_numbers())

        cash1000_val = len(self.pd.cash1000().get_attribute("value"))
        print("cash1000_val:", cash1000_val)
        cash1000_val_data = self.pd.cash1000().get_attribute("value")
        print("cash1000_val_data:", cash1000_val_data)

        cash100 = self.pd.cash100()
        cash100_len = cash100.get_attribute("maxlength")
        print("cash100_len:", cash100_len)
        cash100.send_keys(random_string_generator_numbers())

        cash100_val = len(self.pd.cash100().get_attribute("value"))
        print("cash100_val:", cash100_val)
        cash100_val_data = self.pd.cash100().get_attribute("value")
        print("cash100_val_data:", cash100_val_data)

        cash10 = self.pd.cash10()
        cash10_len = cash10.get_attribute("maxlength")
        print("cash10_len:", cash10_len)
        cash10.send_keys(random_string_generator_numbers())

        cash10_val = len(self.pd.cash10().get_attribute("value"))
        print("cash10_val:", cash10_val)
        cash10_val_data = self.pd.cash10().get_attribute("value")
        print("cash10_val_data:", cash10_val_data)

        cash1 = self.pd.cash1()
        cash1_len = cash1.get_attribute("maxlength")
        print("cash10_len:", cash10_len)
        cash1.send_keys(random_string_generator_numbers())

        cash1_val = len(self.pd.cash1().get_attribute("value"))
        print("cash1_val:", cash1_val)
        cash1_val_data = self.pd.cash1().get_attribute("value")
        print("cash1_val_data:", cash1_val_data)

        time.sleep(2)

        self.pd.submit()

        pos_amount = self.pd.pos_amount()
        pos_amount_len = pos_amount.get_attribute("maxlength")
        print("pos_amount_len:", pos_amount_len)

        pos_amount.send_keys(random_string_generator_numbers())
        pos_amount_val = self.pd.pos_amount().get_attribute("value")
        print("pos_amount_val:", pos_amount_val)

        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)

        poscode = self.pd.pos_code()
        poscode_len = poscode.get_attribute("maxlength")
        print('poscode_len:', poscode_len)
        time.sleep(2)
        poscode.send_keys(random_string_generator_numbers())

        poscode_val = self.pd.pos_code().get_attribute("value")
        print("poscode_val:", poscode_val)

        self.pd.cheque_amount().send_keys(random_string_generator_numbers())
        self.pd.cheque_number().send_keys(random_string_generator_numbers())
        self.pd.cheque_bank().send_keys(random_string_generator_numbers())
        self.pd.cheque_date().send_keys(random_string_generator_numbers())
        time.sleep(2)

        self.pd.online_amount().send_keys(random_string_generator_numbers())
        self.pd.digital_pay().send_keys(random_string_generator_numbers())
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(15)

    def test_pos_code_limit(self, setup):
        ## TESTING BASED ON MANUAL REPORTS
        ## iF POS VALUE GREATER THAN TEN REMITTANCE WONT SAVE

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
        self.rd = Remittance_details(self.driver)

        transc_pin = self.rd.transaction_pin()
        remi_pur = Select(self.rd.drp_remittance_purpose())
        source_income = Select(self.rd.drp_source_of_income())
        currecncy = Select(self.rd.drp_currency())
        service_pro = Select(self.rd.drp_service_provider())

        transc_pin.send_keys("76212")
        remi_pur.select_by_index(2)
        source_income.select_by_index(2)
        currecncy.select_by_index(1)
        service_pro.select_by_index(1)

        self.rd.click_cash()
        self.rd.click_pos()
        self.rd.click_cheque()
        self.rd.click_online()
        self.rd.click_digital_pay()

        lc = self.rd.lc_type_area()
        lc.send_keys("1000")
        rate = self.rd.rate_type_area()
        rate.send_keys("10")  # Integer value from the list
        tax = self.rd.tax_typing()
        tax.send_keys("2")  # Random tax value between 5 and 15
        time.sleep(3)
        self.rd.btn_nxtee()
        time.sleep(2)

        self.tr = Transaction_Review(self.driver)

        self.tr.btn_confrm()
        self.tr.confirm_yes_btn()
        time.sleep(2)
        self.pd = Payment_details(self.driver)

        # Scroll to the bottom of the page

        cash_element = self.pd.cash_ampunt()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cash_element)
        time.sleep(2)  # Allow time for scrolling to finish
        cash_element.click()

        # Set values for thousand, hundred, and ten notes
        # self.pd.cash1000().send_keys("20")
        self.pd.cash100().send_keys("4")

        # Use cash10 values from the list

        self.pd.cash10().send_keys("4")
        self.pd.cash1().send_keys("3")

        time.sleep(2)

        self.pd.submit()
        self.pd.pos_amount().send_keys("443")
        pos_bank = Select(self.pd.drp_pos_bank())
        pos_bank.select_by_index(1)
        self.pd.pos_code().send_keys("200212212121215151515")
        time.sleep(2)

        self.pd.cheque_amount().send_keys("443")
        self.pd.cheque_number().send_keys("4548348")
        self.pd.cheque_bank().send_keys("ICICI")
        self.pd.cheque_date().send_keys("12092024")
        time.sleep(2)

        self.pd.online_amount().send_keys("443")
        self.pd.digital_pay().send_keys("443")
        self.pd.generate_qr_code()

        self.pd.save_remittance()
        time.sleep(5)
        # self.pd.pos_code().send_keys("200212212121215151515")  # More than 10 digits
        # time.sleep(2)
        #
        # self.pd.save_remittance()
        # time.sleep(15)

        # Capture the error message that appears
        error_message_element = self.pd.error_messsge_notrecord()  # Ensure this locator method is correct

        # Get the text of the error message
        error_message_text = error_message_element.text.strip()

        # Now you can assert the error message
        if "Failed to record remittance." in error_message_text:
            print("Error message detected: 'Failed to record remittance.'")

            # Correct the POS code (set to less than 10 digits)
            self.pd.pos_code().clear()
            self.pd.pos_code().send_keys("123456789")  # Valid POS code (less than 10 digits)
            time.sleep(2)

            # Retry saving the remittance
            self.pd.save_remittance()
            time.sleep(5)

        ## test failed
        ## if pos code is less than 10 it will only save remittance
