import os
import random
import string

import pyautogui
import self
from controller import controller

from DineroQa.Dinero_automation.utilities.randomString import random_string_generator_numbers_18
from Dinero_automation.utilities import screenShort
from selenium.webdriver.support.ui import WebDriverWait, Select
from Dinero_automation.pageObjects.service_provider_edit import General_Information, Agreement_Details, PayoutProfile, \
    Upload_document
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key

from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


class Test_General_info_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # return_url = None

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_email(self):
        return generate_random_string(5) + "@example.com"

    # def test_going_to_editmode(self, setup):
    #     responce = []
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(20)
    #
    #     # Initialize page objects
    #
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # Navigate to Remittance
    #     self.nav.click_navbar()
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
    #     name.send_keys("Celtic Warrior")
    #     arabic_name.send_keys("Celtic Warrior")
    #     address_1.send_keys("United states of Africa")
    #     address_2.send_keys("United states of Africa")
    #     address_3.send_keys("United states of Africa")
    #     postal_code.send_keys("35155544")
    #     city.send_keys("New york")
    #     drp_country = Select(self.gi.drp_country())
    #     drp_country.select_by_index(3)
    #     drp_count_of_Incorp.select_by_index(5)
    #     drp_country_code.select_by_index(8)
    #     mob_no.send_keys("6545416445454")
    #     email.send_keys("celtic99@yahhoo.in")
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
    #     registration_number.send_keys("2584461564")
    #     dpick_reg_exp_date.send_keys("12112055")
    #     trade_lic_num.send_keys("45145454")
    #     trade_lic_expiry.send_keys("12082026")
    #     license_number.send_keys("797997197")
    #     license_authority.send_keys("78799895")
    #     auth_pers_name.send_keys("Randy Orton")
    #     drp_gender.select_by_index(2)
    #     dpick_dob.send_keys("12-08-1978")
    #     drp_country_birth.select_by_index(15)
    #     drp_nation.select_by_index(55)
    #     btn_new = self.ad.fund_btn_new()
    #     btn_new.click()
    #     time.sleep(2)
    #     drp_fund_curr = Select(self.ad.drp_fund_curency())
    #     drp_fund_curr.select_by_index(3)
    #     rate = self.ad.rate()
    #     rate.send_keys("3234")
    #     settlement_rate = self.ad.settlement_rate()
    #     settlement_rate.send_keys("2311")
    #     pay_settle_rate = self.ad.pay_settelement_rate()
    #     pay_settle_rate.send_keys("1222")
    #     balance_trigg = self.ad.balance_trigger()
    #     balance_trigg.send_keys("78988")
    #     btn_add = self.ad.btn_add()
    #     btn_add.click()
    #     time.sleep(2)
    #
    #     btn_nxt = self.ad.btn_nxt()
    #     btn_nxt.click()
    #
    #     # click action for upload document
    #
    #     self.ud.doc_selector().click()
    #     time.sleep(5)
    #     keyword = controller
    #
    #     #
    #     # os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\adars\\PycharmProjects\\pythonProject5\\customer_reg_ ind\\sample.py")))
    #     base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
    #     file_name = "Screenshot 2024-07-22 162441.png"
    #     full_path = os.path.join(base_dir, file_name)
    #     time.sleep(2)
    #
    #     # screenshot_path = os.path.abspath("C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-07-22 162441.png")
    #     pyautogui.click(50, 50)
    #     time.sleep(4)
    #     pyautogui.write(full_path)
    #     time.sleep(2)
    #     pyautogui.press("enter")
    #
    #     time.sleep(2)
    #
    #     self.ud.btn_nexte().click()
    #     time.sleep(2)
    #
    #     self.pp = PayoutProfile(self.driver)
    #
    #     self.pp.click_payout_profile().click()
    #     time.sleep(2)
    #
    #     country = Select(self.pp.drp_country())
    #     country.select_by_index(11)
    #     currency = Select(self.pp.drp_currency())
    #     currency.select_by_index(3)
    #     date_for = Select(self.pp.drp_date_formatt())
    #     date_for.select_by_index(1)
    #     cost_rate_source = Select(self.pp.drp_cost_rate_source())
    #     cost_rate_source.select_by_index(2)
    #     fund_curr = Select(self.pp.drp_fund_currency())
    #     fund_curr.select_by_index(1)
    #     time.sleep(2)
    #
    #     self.pp.click_bank_transfer().click()
    #     #self.pp.click_fast_cash().click()
    #     time.sleep(2)
    #
    #     self.pp.click_api_available().click()
    #     self.pp.deal_balance_alert().send_keys("8745445")
    #     self.pp.click_overdraft_allowed().click()
    #     time.sleep(2)
    #     self.pp.overdraft_limit().send_keys("5998989898")
    #     self.pp.over_draft_limitalert().send_keys("599989")
    #
    #     self.pp.click_ind_to_ind().click()
    #     self.pp.ind_to_indtrancs_limit().send_keys("1000000")
    #     ind_ind_transc_curren = Select(self.pp.ind_to_inddrptransc_lim_currenc())
    #     ind_ind_transc_curren.select_by_index(2)
    #
    #     self.pp.click_ind_to_corp().click()
    #     self.pp.indcop_trans_limit().send_keys("10000000")
    #     ind_cop_transc_curr = Select(self.pp.indcorp_drp_trans_currency())
    #     ind_cop_transc_curr.select_by_index(1)
    #
    #     bank_trsn_down = self.pp.ban_transfer_down_select()
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", bank_trsn_down)
    #     time.sleep(2)
    #     bank_trsn_down.click()
    #     time.sleep(2)
    #
    #     self.pp.click_service_charges().click()
    #     time.sleep(2)
    #     self.pp.click_sc_from_api().click()
    #     sc_currency = Select(self.pp.drp_sc_currency())
    #     sc_share_mode = Select(self.pp.drp_sc_share_mode())
    #
    #     sc_currency.select_by_index(1)
    #     sc_share_mode.select_by_index(1)
    #     self.pp.share_factor().send_keys("1522")
    #     time.sleep(2)
    #
    #     self.pp.payout_save_btn().click()
    #     time.sleep(2)
    #
    #     self.pp.click_final_save_button().click()
    #
    #     document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
    #
    #     if self.pp.editmode_message() == "You're in edit mode":
    #         responce.append(document)
    #         self.return_url = document['root']['baseURL']
    #
    #         print(self.return_url)
    #         # Test_General_info_Editmode.return_url = self.return_url  # Store the URL for reuse
    #         assert True

    def test_other_category_value_remain(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        time.sleep(2)

        self.driver.get("http://www.dinero.local/serviceprovider/658")
        time.sleep(2)

        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)
        self.pp = PayoutProfile(self.driver)
        other_cat = self.gi.catego_other_field()
        other_cat.send_keys("Gunther")
        other_cat_val = other_cat.get_attribute("value")

        print("other_cat_val:", other_cat_val)

        self.gi.btn_nxt().click()
        time.sleep(2)

        self.ad.btn_nxt().click()
        time.sleep(2)

        self.ud.btn_nexte().click()
        time.sleep(2)

        self.pp.click_final_save_button().click()
        time.sleep(2)

        other_cat_aft = self.gi.catego_other_field()
        other_cat_aft_val = other_cat_aft.get_attribute("value")

        print("other_cat_aft_val:", other_cat_aft_val)

        if other_cat_val == other_cat_aft_val:
            assert True
        else:
            assert False
