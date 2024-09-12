import time
import pytest
import controller
import pyautogui
import self
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import Dinero_automation
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.service_provider import General_Information, Agreement_Details, Upload_document
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Controller
from Dinero_automation.utilities.randomString import random_string_generator_max_30, random_string_generator_max_50, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51, random_string_generator_numbers_18
from Dinero_automation.utilities import screenShort


class Test_upload_document:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # def test_sending_docs(self, setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(8)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #
    #     # click action for general information
    #
    #     self.nav.click_service_provider()
    #
    #     # time.sleep(2)
    #     self.gi = General_Information(self.driver)
    #     self.ad = Agreement_Details(self.driver)
    #     self.ud = Upload_document(self.driver)
    #
    #     drp_category = Select(self.gi.drp_category())
    #     name = self.gi.name()
    #     arabic_name = self.gi.arabic_name()
    #     address_1 = self.gi.adress_1()
    #     address_2 = self.gi.adress_2()
    #     address_3 = self.gi.adress_3()
    #     postal_code = self.gi.postal_code()
    #     city = self.gi.city()
    #     drp_count_of_Incorp = Select(self.gi.drp_country_of_incorporation())
    #     drp_country_code = Select(self.gi.drp_country_code())
    #     mob_no = self.gi.mobile_number()
    #     email = self.gi.email()
    #     btn_next = self.gi.btn_nxt()
    #
    #     drp_category.select_by_index(2)
    #     time.sleep(2)
    #     name.send_keys("adrstsgs")
    #     arabic_name.send_keys("hfsdjgfd")
    #     address_1.send_keys("dgjhafdhja")
    #     address_2.send_keys("gdhgfhjfg")
    #     address_3.send_keys("hkjgfkhgfkh")
    #     postal_code.send_keys("346714684")
    #     city.send_keys("hgdhkdgfkh")
    #     drp_country = Select(self.gi.drp_country())
    #     drp_country.select_by_index(3)
    #     drp_count_of_Incorp.select_by_index(5)
    #     drp_country_code.select_by_index(8)
    #     mob_no.send_keys("654546445454")
    #     email.send_keys("njuyg@gm.vom")
    #     btn_next.click()
    #     time.sleep(2)
    #
    #     # click action for agreement details
    #
    #     dpick_agreement_star_date = self.ad.dpick_agreement_start_details()
    #     dpick_agreement_end_date = self.ad.dpick_agreement_end_details()
    #     registration_number = self.ad.registration_number()
    #     dpick_reg_exp_date = self.ad.dpick_registration_exp_date()
    #     trade_lic_num = self.ad.trade_license_number()
    #     license_number = self.ad.license_number()
    #     trade_lic_expiry = self.ad.dpick_trade_exp_date()
    #     license_authority = self.ad.licensing_authority()
    #     auth_pers_name = self.ad.authoritzed_person_name()
    #     drp_gender = Select(self.ad.drp_gender())
    #     dpick_dob = self.ad.dpick_date_of_birth()
    #     drp_country_birth = Select(self.ad.drp_country_of_birh())
    #     drp_nation = Select(self.ad.drp_nationality())
    #
    #     dpick_agreement_star_date.send_keys("12081999")
    #     dpick_agreement_end_date.send_keys("12012066")
    #     registration_number.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_18())
    #     dpick_reg_exp_date.send_keys("12112055")
    #     trade_lic_num.send_keys(random_string_generator_numbers_18())
    #     trade_lic_expiry.send_keys("12082026")
    #     license_number.send_keys(random_string_generator_numbers_18())
    #     license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
    #     auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
    #     drp_gender.select_by_index(2)
    #     dpick_dob.send_keys("12-08-1978")
    #     drp_country_birth.select_by_index(15)
    #     drp_nation.select_by_index(55)
    #     btn_new = self.ad.fund_btn_new()
    #     btn_new.click()
    #     time.sleep(2)
    #     drp_fund_curr = Select(self.ad.drp_fund_curency())
    #     drp_fund_curr.select_by_index(2)
    #     rate = self.ad.rate()
    #     rate.send_keys("3234")
    #     settlement_rate = self.ad.settlement_rate()
    #     settlement_rate.send_keys("2311")
    #     pay_settle_rate = self.ad.pay_settelement_rate()
    #     pay_settle_rate.send_keys("1222")
    #     balance_trigg = self.ad.balance_trigger()
    #     balance_trigg.send_keys(random_string_generator_numbers_18())
    #     btn_add = self.ad.btn_add()
    #     btn_add.click()
    #     time.sleep(2)
    #
    #     btn_nxt = self.ad.btn_nxt()
    #     btn_nxt.click()
    #
    #
    #     # click action for upload document
    #
    #     self.ud.doc_selector().click()
    #     time.sleep(5)
    #     keyword = controller
    #
    #     #
    #     #os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
    #     base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
    #     file_name = "Screenshot 2024-07-22 162441.png"
    #     full_path = os.path.join(base_dir, file_name)
    #     time.sleep(2)
    #
    #
    #     #screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
    #     pyautogui.click()
    #     time.sleep(4)
    #     pyautogui.write(full_path)
    #     time.sleep(2)
    #     pyautogui.press("enter")
    #
    #     time.sleep(5)
    #
    #     # test passed
    #     # last tested on built 03/09/2024

    def test_adding_same_docmt_again(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Click action for nav bar arrow and service provider
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_service_provider()

        # Filling general information form
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

        # Fill form fields
        drp_category.select_by_index(2)
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
        btn_next.click()

        time.sleep(2)

        # Filling agreement details form
        self.ad = Agreement_Details(self.driver)
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

        # Select fund currency
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

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # Click action for uploading document
        self.ud = Upload_document(self.driver)
        self.ud.doc_selector().click()
        time.sleep(5)

        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)

        pyautogui.click()
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        btn_nexte = self.ud.btn_nexte()
        btn_nexte.click()
        time.sleep(5)

        btn_backe = self.ud.btn_backe()
        btn_backe.click()
        time.sleep(2)

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        pyautogui.click()
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(4)

        li = []
        doc_container = self.ud.doc_container().text
        li.append(doc_container)

        documents_str = ''.join(li)

        # Split the string by newlines
        lines = documents_str.split('\n')

        # Filter the lines to only get the ones with ".png" (file names)
        png_files = [line for line in lines if '.png' in line]

        # Create a dictionary to store the file names and their cumulative counts
        file_counts = {}

        # Total count of PNG files
        total_count = 0

        # Iterate through the file names and calculate the cumulative count
        for file in png_files:
            total_count += 1
            file_counts[file] = total_count

        # Print file names with their respective cumulative counts
        for file, count in file_counts.items():
            print(f"{file}: {count}")

    def test_without_documents_go_next(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

        # Login

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Click action for nav bar arrow and service provider

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_service_provider()

        # Filling general information form

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

        # Fill form fields

        drp_category.select_by_index(2)
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
        btn_next.click()

        time.sleep(2)

        # Filling agreement details form

        self.ad = Agreement_Details(self.driver)
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

        # Select fund currency
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

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # Click action for uploading document

        self.ud = Upload_document(self.driver)

        time.sleep(2)
        btn_nexte = self.ud.btn_nexte()
        btn_nexte.click()
        error_msg = self.ud.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ud_without_doc.png")
            assert False

        time.sleep(2)

        ### test case failed ( we can go next without upload document)
        ## last tested on built 03/09/2024

    def test_upload_delet_same(self, setup):

        #### testing on manual Reports###

        # not able to add same documents after deleting one time

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Click action for nav bar arrow and service provider
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_service_provider()

        # Filling general information form
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

        # Fill form fields
        drp_category.select_by_index(2)
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
        btn_next.click()

        time.sleep(2)

        # Filling agreement details form
        self.ad = Agreement_Details(self.driver)
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

        # Select fund currency
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

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # Click action for uploading document
        self.ud = Upload_document(self.driver)
        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        pyautogui.click()
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        delete = self.ud.doc_delte()
        delete.click()

        doc_select = self.ud.doc_selector()
        doc_select.click()
        time.sleep(5)
        #keyword = controller

        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(4)

        pyautogui.click()
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(4)
        pyautogui.press("enter")
        time.sleep(4)
        error_message = self.ud.error_message()

        if error_message != "NoSuchElementException":
            assert True
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ud_same_doc.png")
            assert False
        time.sleep(2)

        ### test case failed ( same document cant add twice after deleting
        ### last tested on built 03/09/2024
