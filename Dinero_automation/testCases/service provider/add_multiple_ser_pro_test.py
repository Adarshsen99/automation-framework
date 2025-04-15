import os
import random
import string
import time

import controller
import pyautogui
import self
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib3.exceptions import MaxRetryError

from DineroQa.Dinero_automation.utilities.randomString import random_string_generator_numbers_18, \
    random_string_generator_max_28, random_string_generator_max_31, random_string_generator_numbers
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.service_provider import Agreement_Details, General_Information, Upload_document, \
    PayoutProfile
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
from selenium import webdriver


def generate_random_digits(length=8):
    return ''.join(random.choices(string.digits, k=length))


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_email():
    return generate_random_string(5) + "@example.com"


class TestSendingDocs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)

        # Navigate to Remittance

        # time.sleep(2)
        self.gi = General_Information(self.driver)
        self.ad = Agreement_Details(self.driver)
        self.ud = Upload_document(self.driver)
        Treasury_pull_element = self.driver.find_element(By.XPATH,
                                                         "//div[normalize-space()='Treasury']")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Treasury_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        service_pro_element = self.driver.find_element(By.XPATH,
                                                       "//div[normalize-space()='Service Provider']")
        service_pro_element.click()
        time.sleep(2)

        for i in range(10):
            service_provider_names = [

                "rupee Services",
                "WaveCom Technologies",
                "Quantum Web Systems",
                "GlobalNet IT Support",
                "BlueWave Digital Services",
                "Apex Cloud Solutions",
                "SecureLink Consultings"
            ]

            short_names = ["Nexus", "WaveCom", "Quantum", "GlobalNet", "BlueWave", "Apex", "SecureLink"]

            address_1_names = [
                "Maplewood",
                "Silverbrook",
                "Ridgeview",
                "Eastwood",
                "Brightwater",
                "Greenfield",
                "Stonebridge",
                "Westvale",
                "Clearwater",
                "Sunset Bay"
            ]

            cities = [
                "Rivertown",
                "Crestwood",
                "Maple Valley",
                "Oceanview",
                "Silver Springs",
                "Pinehill",
                "Amberfield",
                "Sunridge",
                "Greenleaf",
                "Willow Creek"
            ]

            self.gi.new_btn().click()
            time.sleep(2)
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
            name.send_keys(service_provider_names[i])
            arabic_name.send_keys(service_provider_names[i])
            short_name = self.gi.short_name()
            short_name.send_keys(short_names[i])

            address_1.send_keys(address_1_names[i])
            address_2.send_keys(address_1_names[i] + "road")
            address_3.send_keys(address_1_names[i] + "way")
            postal_code.send_keys(random_string_generator_numbers(4))
            city.send_keys(cities[i])
            drp_country = Select(self.gi.drp_country())
            drp_country.select_by_index(17 + i)
            drp_count_of_Incorp.select_by_index(17 + i)
            drp_country_code.select_by_index(17 + i)
            mob_no.send_keys(random_string_generator_numbers(10))
            email.send_keys(generate_random_email())
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
            registration_number.send_keys(random_string_generator_numbers_18())
            dpick_reg_exp_date.send_keys("12112055")
            trade_lic_num.send_keys(random_string_generator_numbers_18())
            trade_lic_expiry.send_keys("12082026")
            license_number.send_keys(random_string_generator_numbers_18())
            license_authority.send_keys(random_string_generator_max_50() + random_string_generator_max_28())
            auth_pers_name.send_keys(random_string_generator_max_50() + random_string_generator_max_31())
            drp_gender.select_by_index(2)
            dpick_dob.send_keys("12-08-1978")
            drp_country_birth.select_by_index(17 + i)
            drp_nation.select_by_index(17 + i)
            btn_new = self.ad.fund_btn_new()
            btn_new.click()
            # time.sleep()
            drp_fund_curr = Select(self.ad.drp_fund_curency())
            #     time.sleep(2)
            #     time.sleep(2)
            drp_fund_curr.select_by_index(17 + i)
            rate = self.ad.rate()

            rate.send_keys("3.23")
            settlement_rate = self.ad.settlement_rate()
            settlement_rate.send_keys("3.23")
            pay_settle_rate = self.ad.pay_settelement_rate()
            pay_settle_rate.send_keys("3.23")
            balance_trigg = self.ad.balance_trigger()
            balance_trigg.send_keys(random_string_generator_numbers(5))
            od_lim = self.ad.od_limit()
            od_lim.send_keys("90000")
            od_lim_alert = self.ad.od_limit_alert()
            od_lim_alert.send_keys("89999")
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
            country.select_by_index(17 + i)
            currency = Select(self.pp.drp_currency())
            currency.select_by_index(17 + i)
            date_for = Select(self.pp.drp_date_formatt())
            date_for.select_by_index(1)
            cost_rate_source = Select(self.pp.drp_cost_rate_source())
            cost_rate_source.select_by_index(3)
            fund_curr = Select(self.pp.drp_fund_currency())
            fund_curr.select_by_index(1)
            time.sleep(2)

            self.pp.click_bank_transfer().click()
            #self.pp.click_fast_cash().click()
            time.sleep(2)

            self.pp.click_api_available().click()
            self.pp.deal_balance_alert().send_keys("500000")
            # self.pp.click_overdraft_allowed().click()
            # time.sleep(2)
            # self.pp.overdraft_limit().send_keys(random_string_generator_numbers())
            # self.pp.over_draft_limitalert().send_keys(random_string_generator_numbers())

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
            self.pp.click_sc_from_api_bank()
            sc_currency = Select(self.pp.drp_sc_currency_bank_bank())


            sc_currency.select_by_index(1)
            sc_share_mode = Select(self.pp.drp_sc_share_mode_bank())
            sc_share_mode.select_by_index(1)
            self.pp.click_new_branch_bank().click()
            drp_branch = Select(self.pp.click_drp_branch_id_bank())
            drp_branch.select_by_index(1)
            self.pp.sc_bank_our().send_keys("50")
            self.pp.sc_sp_bank().send_keys("50")
            self.pp.sc_add_and_close_bank().click()

            time.sleep(2)

            self.pp.payout_done_btn().click()
            time.sleep(25)

            self.pp.click_final_save_button().click()
            time.sleep(3)
