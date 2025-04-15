import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Remitance import Customer_Details, Delegate_details
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Customer_detals:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_name(self, setup):
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
        time.sleep(2)

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

        self.custom_name.send_keys("Adarsh")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        ### test passed
        ### last tested on 15/10/2024

    def test_sending_valid_data_id_no(self, setup):
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
        self.nav.click_remitance()
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)
        self.custom_name = self.cd.customer_search_bar()
        self.custom_name.clear()
        self.custom_name.send_keys("242412412")

        time.sleep(4)
        self.cd.customer_selector_adarshid()
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        ### test passed
        ### last tested on 15/10/2024

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
        # self.custom_name.clear()
        # self.custom_name.send_keys("")

        time.sleep(4)
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        ## test failed
        ## last tested on built 19/09/2024

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
        self.custom_name.clear()
        self.custom_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        time.sleep(4)
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        ## test failed

    def test_with_validating_mx_length(self, setup):
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
        time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView();", sidebar)
        time.sleep(2)
        # click action for customer details
        self.nav.click_remitance()
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)

        max_50 = random_string_generator_max_50()

        def get_max_length(element):
            if element is not None:
                return element.get_attribute('maxlength')
            return None

        self.custom_name = self.cd.customer_search_bar()
        self.custom_name.clear()

        custom_len_ele = self.cd.customer_search_bar()

        custom_len_max = get_max_length(custom_len_ele)

        print(f"Max length for customer : {type(custom_len_max)}")

        customer_name_number = max_50

        self.cd.customer_search_bar().send_keys(customer_name_number)

        cus_val = custom_len_ele.get_attribute('value')
        cus_val_len = len(cus_val)

        print("custom value", type(cus_val_len))

        #self.custom_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        time.sleep(4)
        self.cd.verify_btn()
        time.sleep(2)
        self.cd.btn_next()
        time.sleep(2)

        # if cus_val_len == custom_len_max:
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "CI_test_validating_max_len_fh.png")
        #     assert False

    def test_validating_cancel(self, setup):
        def get_dropdown_text(select_element):
            return select_element.first_selected_option.text

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to the customer details page
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView();", sidebar)
        time.sleep(2)
        # click action for customer details
        self.nav.click_remitance()

        # Select a transaction type
        self.cd = Customer_Details(self.driver)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ.select_by_index(1)

        # Search for a customer
        custom_name = self.cd.customer_search_bar()
        custom_name.send_keys("adarsh")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)
        customer_val = custom_name.get_attribute('value')

        # Print the selected transaction type before clearing
        print("Getting data for customer details info before clear")
        self.transcationtyp_text_before = get_dropdown_text(self.drp_transn_typ)
        print("Transfer type before clear:", self.transcationtyp_text_before)

        print(f"customer_val:{customer_val}")
        # Perform cancel operation
        self.cd.cancel_btm()
        time.sleep(2)
        self.cd.cancel_confirm()
        time.sleep(3)

        # Print the selected transaction type after clearing
        print("Getting data for customer details info after clear")
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())
        self.drp_transn_typ_after = Select(self.cd.drp_transcation_type())

        self.transcationtyp_text_after = get_dropdown_text(self.drp_transn_typ)
        print("Transfer type after clear:", self.transcationtyp_text_after)
        custom_name = self.cd.customer_search_bar()
        customer_val_aft = custom_name.get_attribute('value')
        print(f"customer_val_aft:{customer_val_aft}")

        if self.transcationtyp_text_after != self.transcationtyp_text_before:

            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_remi.cd.png")
            assert False

        if customer_val_aft != customer_val:

            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_remi.cd.png")
            assert False

    def test_transctn_mode_not_clearing(self, setup):
        def get_dropdown_text(select_element):
            return select_element.first_selected_option.text

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
        self.drp_transn_typ.select_by_index(2)
        self.custom_name = self.cd.customer_search_bar()

        self.custom_name.send_keys("adarsh")
        time.sleep(2)
        self.cd.custom_select1()
        self.cd.verify_btn()
        time.sleep(2)

        self.transcationtyp_text_before = get_dropdown_text(self.drp_transn_typ)
        print("Transfer type before cancel:", self.transcationtyp_text_before)

        self.cd.btn_next()
        time.sleep(2)

        self.dd = Delegate_details(self.driver)
        self.dd.btn_back()
        time.sleep(2)
        self.drp_transn_typ = Select(self.cd.drp_transcation_type())

        self.transcationtyp_text_after = get_dropdown_text(self.drp_transn_typ)
        print("Transfer type after cancel:", self.transcationtyp_text_after)

        if self.transcationtyp_text_after == self.transcationtyp_text_before:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "remittance.png")
            assert False
            time.sleep(2)

            # test failed( values are remaining same)
            # last tested onb built 19/09/2024
