import os
import random
import string
import time

import controller
import pyautogui
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib3.exceptions import MaxRetryError

from DineroQa.Dinero_automation.utilities import screenShort
from DineroQa.Dinero_automation.utilities.randomString import random_string_generator_numbers_18, \
    random_string_generator_max_28, random_string_generator_max_31, random_string_generator_numbers
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.service_provider import Agreement_Details, General_Information, Upload_document, \
    PayoutProfile
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
from selenium import webdriver


class Test_PayoutProfile:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(50, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        #
        self.pp.click_fast_cash().click()
        self.pp.click_bank_transfer().click()
        self.pp.click_ewallet()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges_bank().click()
        time.sleep(2)
        self.pp.click_sc_from_api_bank().click()
        sc_currency = Select(self.pp.drp_sc_currency_bank_bank())
        sc_share_mode = Select(self.pp.drp_sc_share_mode_bank())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor_bank().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive_bank().click()
        time.sleep(2)
        self.pp.click_incentive_slecter_bank().click()
        incentive_mode = Select(self.pp.drp_incentive_mode_bank())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle_bank())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency_bank())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing_bank().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos_fastcash().click()
        time.sleep(2)

        third_party = self.pp.click_third_party_fastcash()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency_bank())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin_fastcash().send_keys("154")

        # self.pp.payout_save_btn().click()
        time.sleep(2)

    def test_without_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        # self.pp.click_bank_transfer().click()
        self.pp.click_bank_transfer().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        #self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        #self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        #self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        #self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        #self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges_bank().click()
        time.sleep(2)
        self.pp.click_sc_from_api_bank().click()
        sc_currency = Select(self.pp.drp_sc_currency_bank_bank())
        sc_share_mode = Select(self.pp.drp_sc_share_mode_bank())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        #self.pp.share_factor_bank().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive_bank().click()
        time.sleep(2)
        self.pp.click_incentive_slecter_bank().click()
        incentive_mode = Select(self.pp.drp_incentive_mode_bank())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle_bank())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency_bank())
        incentve_currency.select_by_index(1)
        #self.pp.incentive_data_typing_bank().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos_bank().click()
        time.sleep(2)

        third_party = self.pp.click_third_party_bank()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency_bank())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        #self.pp.other_bank_data_typin_fastcash().send_keys("154")

        self.pp.payout_save_btn().click()
        time.sleep(5)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_withoutdata.png")
            assert False

    def test_with_spl_characters(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(50, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        #
        self.pp.click_fast_cash().click()
        self.pp.click_bank_transfer().click()
        self.pp.click_ewallet()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        self.pp.over_draft_limitalert().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges_bank().click()
        time.sleep(2)
        self.pp.click_sc_from_api_bank().click()
        sc_currency = Select(self.pp.drp_sc_currency_bank_bank())
        sc_share_mode = Select(self.pp.drp_sc_share_mode_bank())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor_bank().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        time.sleep(2)

        self.pp.click_incentive_bank().click()
        time.sleep(2)
        self.pp.click_incentive_slecter_bank().click()
        incentive_mode = Select(self.pp.drp_incentive_mode_bank())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle_bank())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency_bank())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing_bank().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")
        time.sleep(2)

        self.pp.click_other_bank_depos_fastcash().click()
        time.sleep(2)

        third_party = self.pp.click_third_party_fastcash()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency_bank())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin_fastcash().send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?aev")

        # self.pp.payout_save_btn().click()
        time.sleep(2)
        time.sleep(2)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_with_spl_character.png")
            assert False

    def test_spl_char_num(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.pp.over_draft_limitalert().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(1)
        time.sleep(2)
        self.pp.other_bank_data_typin().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?abe")

        self.pp.payout_save_btn().click()
        time.sleep(2)
        error_msg = self.gi.error_message()
        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Ser_Pro_ad_with_spl_character.png")
            assert False

    def test_sending_bulk_data(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        deal_balance_alert = [3124124, 2314412, 23214124]
        over_draft_limit = [2432423532, 2442114124, 21414124]
        over_draft_limit_alert = [4211324, 241432, 241245]
        ind_ind_trans_limit = [231444, 414124, 214124124]
        ind_cop_tran_limit = [44646, 454564654, 654654654]
        share_factor = [4454, 4654, 5454]
        incentive = [454, 564, 454]
        other_bank = [646, 544, 545]

        for i in range(3):
            self.pp.click_api_available().click()
            self.pp.deal_balance_alert().send_keys(deal_balance_alert[i])
            self.pp.click_overdraft_allowed().click()
            time.sleep(2)
            self.pp.overdraft_limit().send_keys(over_draft_limit[i])
            self.pp.over_draft_limitalert().send_keys(over_draft_limit_alert[i])

            if i == 0:  # Only click on the first iteration
                self.pp.click_ind_to_ind().click()
                self.pp.click_ind_to_corp().click()
                self.pp.click_sc_from_api().click()
                self.pp.click_incentive().click()
                self.pp.click_incentive_slecter().click()
                third_party = self.pp.click_third_party()

            #self.pp.click_ind_to_ind().click()
            self.pp.ind_to_indtrancs_limit().send_keys(ind_ind_trans_limit[i])
            ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
            ind_ind_transc_curren.select_by_index(2)

            #self.pp.click_ind_to_corp().click()
            self.pp.indcop_trans_limit().send_keys(ind_cop_tran_limit[i])
            ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
            ind_cop_transc_curr.select_by_index(1)

            bank_trsn_down = self.pp.ban_transfer_down_select()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
            time.sleep(2)
            bank_trsn_down.click()
            time.sleep(2)

            self.pp.click_service_charges().click()
            time.sleep(2)

            sc_currency = Select(self.pp.drp_sc_currency())
            sc_share_mode = Select(self.pp.drp_sc_share_mode())

            sc_currency.select_by_index(1)
            sc_share_mode.select_by_index(1)
            self.pp.share_factor().send_keys(share_factor[i])
            time.sleep(2)

            time.sleep(2)

            incentive_mode = Select(self.pp.drp_incentive_mode())
            incentive_mode.select_by_index(1)
            settlemet_cycle = Select(self.pp.drp_settlement_cycle())
            settlemet_cycle.select_by_index(1)
            incentve_currency = Select(self.pp.incentive_curency())
            incentve_currency.select_by_index(1)
            self.pp.incentive_data_typing().send_keys(incentive[i])
            time.sleep(2)

            self.pp.click_other_bank_depos().click()
            time.sleep(2)

            self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
            third_party.click()
            other_bank_currency = Select(self.pp.drp_other_bank_currency())
            other_bank_currency.select_by_index(1)
            time.sleep(2)
            self.pp.other_bank_data_typin().send_keys(other_bank[i])
            time.sleep(3)

            self.pp.deal_balance_alert().clear()
            time.sleep(5)
            self.pp.overdraft_limit().clear()
            time.sleep(5)
            self.pp.over_draft_limitalert().clear()
            time.sleep(5)
            self.pp.ind_to_indtrancs_limit().clear()
            time.sleep(5)
            self.pp.indcop_trans_limit().clear()
            time.sleep(5)
            self.pp.share_factor().clear()
            time.sleep(5)
            self.pp.share_factor().clear()
            time.sleep(5)
            self.pp.incentive_data_typing().clear()
            time.sleep(5)
            self.pp.other_bank_data_typin().clear()
            time.sleep(5)

            #self.pp.payout_save_btn().click()
            time.sleep(2)

    def test_data_with_spaces(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        deal_balance_alert = ["3 1 24de d    12 3 4"]
        over_draft_limit = ["3 1 24de d    12 3 4"]
        over_draft_limit_alert = ["3 1 24de d    12 3 4"]
        ind_ind_trans_limit = ["3 1 24de d    12 3 4"]
        ind_cop_tran_limit = ["3 1 24de d    12 3 4"]
        share_factor = ["3 1 24de d    12 3 4"]
        incentive = ["3 1 24de d    12 3 4"]
        other_bank = ["3 1 24de d    12 3 4"]

        for i in range(1):
            self.pp.click_api_available().click()
            self.pp.deal_balance_alert().send_keys(deal_balance_alert[i])
            self.pp.click_overdraft_allowed().click()
            time.sleep(2)
            self.pp.overdraft_limit().send_keys(over_draft_limit[i])
            self.pp.over_draft_limitalert().send_keys(over_draft_limit_alert[i])

            # self.pp.click_ind_to_ind().click()
            self.pp.click_ind_to_ind().click()
            self.pp.ind_to_indtrancs_limit().send_keys(ind_ind_trans_limit[i])
            ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
            ind_ind_transc_curren.select_by_index(2)

            # self.pp.click_ind_to_corp().click()
            self.pp.click_ind_to_corp().click()
            self.pp.indcop_trans_limit().send_keys(ind_cop_tran_limit[i])
            ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
            ind_cop_transc_curr.select_by_index(1)

            bank_trsn_down = self.pp.ban_transfer_down_select()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
            time.sleep(2)
            bank_trsn_down.click()
            time.sleep(2)

            self.pp.click_service_charges().click()
            time.sleep(2)
            self.pp.click_sc_from_api().click()

            sc_currency = Select(self.pp.drp_sc_currency())
            sc_share_mode = Select(self.pp.drp_sc_share_mode())

            sc_currency.select_by_index(1)
            sc_share_mode.select_by_index(1)
            self.pp.share_factor().send_keys(share_factor[i])
            time.sleep(2)

            time.sleep(2)

            self.pp.click_incentive().click()
            self.pp.click_incentive_slecter().click()
            incentive_mode = Select(self.pp.drp_incentive_mode())
            incentive_mode.select_by_index(1)
            settlemet_cycle = Select(self.pp.drp_settlement_cycle())
            settlemet_cycle.select_by_index(1)
            incentve_currency = Select(self.pp.incentive_curency())
            incentve_currency.select_by_index(1)
            self.pp.incentive_data_typing().send_keys(incentive[i])
            time.sleep(2)

            self.pp.click_other_bank_depos().click()
            time.sleep(2)
            third_party = self.pp.click_third_party()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
            third_party.click()
            other_bank_currency = Select(self.pp.drp_other_bank_currency())
            other_bank_currency.select_by_index(1)
            time.sleep(2)
            self.pp.other_bank_data_typin().send_keys(other_bank[i])
            time.sleep(3)

            self.pp.payout_save_btn().click()
            time.sleep(2)

    def test_over_draft_limit_remains(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        over_draft_limit = self.pp.overdraft_limit()
        over_draft_limit_val = over_draft_limit.get_attribute("value")

        print("over_draft_limit_val:", over_draft_limit_val)

        time.sleep(3)

        self.pp.click_none().click()

        over_draft_limit = self.pp.overdraft_limit()
        over_draft_limit_val_aft = over_draft_limit.get_attribute("value")
        print("over_draft_limit_val_aft:", over_draft_limit_val_aft)

        time.sleep(2)

        if over_draft_limit_val != over_draft_limit_val_aft:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "service_pro_balanc_bug.png")
            assert False

        # self.pp.click_ind_to_ind().click()
        # self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        # ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        # ind_ind_transc_curren.select_by_index(2)
        #
        # self.pp.click_ind_to_corp().click()
        # self.pp.indcop_trans_limit().send_keys("10000000")
        # ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        # ind_cop_transc_curr.select_by_index(1)
        #
        # bank_trsn_down = self.pp.ban_transfer_down_select()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        # time.sleep(2)
        # bank_trsn_down.click()
        # time.sleep(2)
        #
        # self.pp.click_service_charges().click()
        # time.sleep(2)
        # self.pp.click_sc_from_api().click()
        # sc_currency = Select(self.pp.drp_sc_currency())
        # sc_share_mode = Select(self.pp.drp_sc_share_mode())
        #
        # sc_currency.select_by_index(1)
        # sc_share_mode.select_by_index(1)
        # self.pp.share_factor().send_keys("1522")
        # time.sleep(2)

        # self.pp.click_incentive().click()
        # time.sleep(2)
        # self.pp.click_incentive_slecter().click()
        # incentive_mode = Select(self.pp.drp_incentive_mode())
        # incentive_mode.select_by_index(1)
        # settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        # settlemet_cycle.select_by_index(1)
        # incentve_currency = Select(self.pp.incentive_curency())
        # incentve_currency.select_by_index(1)
        # self.pp.incentive_data_typing().send_keys("652")
        # time.sleep(2)
        #
        # self.pp.click_other_bank_depos().click()
        # time.sleep(2)
        #
        # third_party = self.pp.click_third_party()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        # third_party.click()
        # other_bank_currency = Select(self.pp.drp_other_bank_currency())
        # other_bank_currency.select_by_index(1)
        # time.sleep(2)
        # self.pp.other_bank_data_typin().send_keys("154")
        #
        # self.pp.payout_save_btn().click()
        # time.sleep(2)

    def test_saving_without_selecting_incentive_values(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        #self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        time.sleep(2)
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin().send_keys("154")
        time.sleep(2)

        self.pp.payout_save_btn().click()
        time.sleep(5)

    def test_over_draft_limit_alert_less_than_limit(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)

        over_draft_limit = self.pp.overdraft_limit()
        over_draft_limit_alert = self.pp.over_draft_limitalert()

        self.pp.overdraft_limit().send_keys("664616")
        self.pp.over_draft_limitalert().send_keys("26565656565")

        over_draft_limit_val = int(over_draft_limit.get_attribute("value"))
        over_draft_limit_alert_val = int(over_draft_limit_alert.get_attribute("value"))

        print("over_draft_limit_val:", over_draft_limit_val)
        print("over_draft_limit_alert_val:", over_draft_limit_alert_val)

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)

        self.pp.other_bank_data_typin().send_keys("154")

        self.pp.payout_save_btn().click()
        time.sleep(2)

        if over_draft_limit_val > over_draft_limit_alert_val:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "ser_pro_overdraft.png")
            assert False

    def test_without_other_bank_deposit_value(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        time.sleep(2)
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        #self.pp.other_bank_data_typin().send_keys("154")
        time.sleep(2)

        self.pp.payout_save_btn().click()
        time.sleep(5)

    def test_saving_without_sc_api_or_slab(self, setup, ):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        #self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        time.sleep(2)
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin().send_keys("154")
        time.sleep(2)

        self.pp.payout_save_btn().click()
        time.sleep(5)

        error_messege = self.pp.error_message()

        if error_messege == "required":
            assert True
        else:
            assert False

    def test_try_selecting_sc_without_transfer_types(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        #self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        # bank_trsn_down = self.pp.ban_transfer_down_select()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        # time.sleep(2)
        # bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)

        erro_transfer = self.pp.transfer_type_error()

        erro_transfer_org = erro_transfer.split('/0')[0].replace("Dismiss", "").strip()

        print(erro_transfer_org)

        if erro_transfer_org == "Please select a transfer type before proceeding.":
            assert True
        else:
            assert False

    def test_other_bank_deposit_already_selected(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        # cost_rate_source = Select(self.pp.drp_cost_rate_source())
        # cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        # self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency()).first_selected_option.text
        #other_bank_currency.select_by_index(2)

        print(other_bank_currency)

        if other_bank_currency == "":
            assert True
        else:
            assert False

    def test_with_adding_only_bank_or_fast_byselecting_both(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys("652")
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin().send_keys("154")

        self.pp.payout_save_btn().click()
        time.sleep(2)
        error_mess = self.pp.error_message()

        if error_mess == "required":
            assert True
        else:
            assert False

    def test_after_adding_new_branch_sc_the_old_value_remains(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        #self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys("1522")
        time.sleep(4)
        new_sc = self.pp.click_sc_branch_new()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", new_sc)
        new_sc.click()

        branch_id_1 = Select(self.pp.click_drp_branch_id())
        branch_id_1.select_by_index(1)
        branch_id_text = branch_id_1.first_selected_option.text

        print("branch_id_text:", branch_id_text)

        time.sleep(2)

        self.pp.sc_data().send_keys("454")
        self.pp.sc_add_and_close().click()
        time.sleep(2)

        self.pp.sc_new2nd_click().click()
        branch_id_2 = Select(self.pp.click_new_branch_id2nd())
        branch_id_2_text = branch_id_2.first_selected_option.text

        print("branch_id_2_text:", branch_id_2_text)

        if branch_id_2_text == "":

            assert True
        else:
            assert False

    def test_maximum_length(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(100, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        self.pp.click_bank_transfer().click()
        # self.pp.click_fast_cash().click()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys(random_string_generator_numbers())
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys(random_string_generator_numbers())
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges().click()
        time.sleep(2)
        #self.pp.click_sc_from_api().click()
        sc_currency = Select(self.pp.drp_sc_currency())
        sc_share_mode = Select(self.pp.drp_sc_share_mode())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor().send_keys(random_string_generator_numbers())
        time.sleep(2)

        self.pp.click_incentive().click()
        time.sleep(2)
        self.pp.click_incentive_slecter().click()
        incentive_mode = Select(self.pp.drp_incentive_mode())
        incentive_mode.select_by_index(1)
        settlemet_cycle = Select(self.pp.drp_settlement_cycle())
        settlemet_cycle.select_by_index(1)
        incentve_currency = Select(self.pp.incentive_curency())
        incentve_currency.select_by_index(1)
        self.pp.incentive_data_typing().send_keys(random_string_generator_numbers())
        time.sleep(2)

        self.pp.click_other_bank_depos().click()
        time.sleep(2)

        third_party = self.pp.click_third_party()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", third_party)
        third_party.click()
        other_bank_currency = Select(self.pp.drp_other_bank_currency())
        other_bank_currency.select_by_index(2)
        time.sleep(2)
        self.pp.other_bank_data_typin().send_keys(random_string_generator_numbers())

        deal_required = self.pp.deal_balance_alert().get_attribute("maxlength")
        overdraft_limit = self.pp.overdraft_limit().get_attribute("maxlength")
        overdraft_limit_alert = self.pp.over_draft_limitalert().get_attribute("maxlength")
        incentive_data = self.pp.incentive_data_typing().get_attribute("maxlength")
        other_bank_data = self.pp.other_bank_data_typin().get_attribute("maxlength")
        share_factor = self.pp.share_factor().get_attribute("maxlength")

        # Print out the maxlength values
        print("Deal Required Max Length:", deal_required)
        print("Overdraft Limit Max Length:", overdraft_limit)
        print("Overdraft Limit Alert Max Length:", overdraft_limit_alert)
        print("Incentive Data Max Length:", incentive_data)
        print("Other Bank Data Max Length:", other_bank_data)
        print("Share Factor Max Length:", share_factor)

        # Additionally, you can also retrieve the current value in each field using get_attribute('value')
        deal_value = self.pp.deal_balance_alert().get_attribute("value")
        overdraft_limit_value = self.pp.overdraft_limit().get_attribute("value")
        overdraft_limit_alert_value = self.pp.over_draft_limitalert().get_attribute("value")
        incentive_data_value = self.pp.incentive_data_typing().get_attribute("value")
        other_bank_data_value = self.pp.other_bank_data_typin().get_attribute("value")
        share_factor_value = self.pp.share_factor().get_attribute("value")

        # Print out the current values
        print("Deal Required Value:", deal_value)
        print("Overdraft Limit Value:", overdraft_limit_value)
        print("Overdraft Limit Alert Value:", overdraft_limit_alert_value)
        print("Incentive Data Value:", incentive_data_value)
        print("Other Bank Data Value:", other_bank_data_value)
        print("Share Factor Value:", share_factor_value)

        self.pp.payout_save_btn().click()
        time.sleep(2)

    def test_delete_1st_branch_if_selected_more(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # Initialize page objects

        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Remittance
        self.nav.click_navbar()

        self.nav.click_service_provider()

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)

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
        name.send_keys(random_string_generator_max_28())
        arabic_name.send_keys(random_string_generator_max_28())
        address_1.send_keys(random_string_generator_max_28())
        address_2.send_keys("gdhgfhjfg")
        address_3.send_keys("hkjgfkhgfkh")
        postal_code.send_keys(random_string_generator_numbers(4))
        city.send_keys(random_string_generator_max_28())
        drp_country = Select(self.gi.drp_country())
        drp_country.select_by_index(3)
        drp_count_of_Incorp.select_by_index(5)
        drp_country_code.select_by_index(7)
        mob_no.send_keys(random_string_generator_numbers(10))
        email.send_keys("sgdagsh@fhj.fdgd")
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
        drp_fund_curr.select_by_index(8)
        rate = self.ad.rate()
        rate.send_keys(random_string_generator_numbers(4))
        settlement_rate = self.ad.settlement_rate()
        settlement_rate.send_keys("2311")
        pay_settle_rate = self.ad.pay_settelement_rate()
        pay_settle_rate.send_keys("1222")
        balance_trigg = self.ad.balance_trigger()
        balance_trigg.send_keys(random_string_generator_numbers(5))
        btn_add = self.ad.btn_add()
        btn_add.click()
        time.sleep(2)

        btn_nxt = self.ad.btn_nxt()
        btn_nxt.click()

        # click action for upload document

        self.ud.doc_selector().click()
        time.sleep(5)
        keyword = controller

        #
        # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
        base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
        file_name = "Screenshot 2024-07-22 162441.png"
        full_path = os.path.join(base_dir, file_name)
        time.sleep(2)

        # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
        pyautogui.click(50, 50)
        time.sleep(4)
        pyautogui.write(full_path)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)
        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp = PayoutProfile(self.driver)

        self.pp.click_payout_profile().click()
        time.sleep(2)

        country = Select(self.pp.drp_country())
        country.select_by_index(12)
        currency = Select(self.pp.drp_currency())
        currency.select_by_index(3)
        date_for = Select(self.pp.drp_date_formatt())
        date_for.select_by_index(1)
        cost_rate_source = Select(self.pp.drp_cost_rate_source())
        cost_rate_source.select_by_index(2)
        fund_curr = Select(self.pp.drp_fund_currency())
        fund_curr.select_by_index(1)
        time.sleep(2)

        #
        #self.pp.click_fast_cash().click()
        self.pp.click_bank_transfer().click()
        self.pp.click_ewallet()
        time.sleep(2)

        self.pp.click_api_available().click()
        self.pp.deal_balance_alert().send_keys(random_string_generator_numbers())
        self.pp.click_overdraft_allowed().click()
        time.sleep(2)
        self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
        self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

        self.pp.click_ind_to_ind().click()
        self.pp.ind_to_indtrancs_limit().send_keys("1000000")
        ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
        ind_ind_transc_curren.select_by_index(2)

        self.pp.click_ind_to_corp().click()
        self.pp.indcop_trans_limit().send_keys("10000000")
        ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
        ind_cop_transc_curr.select_by_index(1)

        bank_trsn_down = self.pp.ban_transfer_down_select()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
        time.sleep(2)
        bank_trsn_down.click()
        time.sleep(2)

        self.pp.click_service_charges_bank().click()
        time.sleep(2)
        #self.pp.click_sc_from_api_bank().click()
        sc_currency = Select(self.pp.drp_sc_currency_bank_bank())
        sc_share_mode = Select(self.pp.drp_sc_share_mode_bank())

        sc_currency.select_by_index(1)
        sc_share_mode.select_by_index(1)
        self.pp.share_factor_bank().send_keys("1522")
        time.sleep(3)

        self.pp.click_sc_branch_new_bank().click()
        time.sleep(2)
        sc_branch = Select(self.pp.click_drp_branch_id_bank())
        sc_branch.select_by_index(1)
        time.sleep(2)
        self.pp.sc_data_bank().send_keys("55")
        self.pp.sc_add_and_close_bank().click()
        time.sleep(2)

        time.sleep(2)
        self.pp.click_sc_branch_new_bank().click()
        sc_branch = Select(self.pp.click_drp_branch_id_bank())
        sc_branch.select_by_index(2)
        time.sleep(2)
        self.pp.sc_data_bank().send_keys("55")
        self.pp.sc_add_and_close_bank().click()
        time.sleep(2)
        self.pp.click_sc_branch_new_bank().click()
        sc_branch = Select(self.pp.click_drp_branch_id_bank())
        sc_branch.select_by_index(3)
        time.sleep(2)
        self.pp.sc_data_bank().send_keys("55")
        self.pp.sc_add_and_close_bank().click()

        self.pp.delete_first_branch().click()







