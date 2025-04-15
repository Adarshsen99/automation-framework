import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.deal_manger import To_be_approved, Approved
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
import math


class Test_approved_and_reject:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_approve_click_and_calculations(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)
        self.apd = Approved(self.driver)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("CR Enterprises")

        country = Select(self.tba.drp_country())
        country.select_by_index(1)

        currency = Select(self.tba.drp_currency())
        currency.select_by_index(1)

        self.tba.select().click()
        time.sleep(3)
        self.tba.to_be_approved().click()

        self.apd.select_first_Deal_phenom()
        time.sleep(3)

        # Fetching values from UI
        deal_rate = float(self.tba.deal_rate().get_attribute("value"))
        deal_rev_rate = float(self.tba.deal_reverse_rate().get_attribute("value"))
        fund_ded = float(self.tba.fund_deduction().get_attribute("value"))
        deal_cost_rate = float(self.tba.deal_cost_rate().get_attribute("value"))
        cost_rev_rate = float(self.tba.cost_reverse_rate().get_attribute("value"))
        equilant_lc = float(self.tba.equilant_lc().get_attribute("value"))
        fund_rate = float(self.tba.fund_rate().text.split("\n")[-1].strip())
        new_deal_pos = float(self.tba.new_deal_position().get_attribute("value"))
        update_cost_rate = float(self.tba.updated_cost_rate().get_attribute("value"))
        equilant_lc2 = float(self.tba.equilant_lc2().get_attribute("value"))

        # Assume deal_amount is fetched or predefined
        deal_amount = float(self.tba.deal_amount().get_attribute("value"))

        # Tolerance for floating-point comparison
        tolerance = 1e-5  # Allow small precision differences

        # Performing calculations and assertions with tolerance
        if math.isclose(deal_amount * deal_cost_rate, equilant_lc, rel_tol=tolerance):
            print("✅ deal_amount * deal_cost_rate = equilant_lc is correct")
        else:
            assert False, f"❌ Mismatch: {deal_amount * deal_cost_rate} != {equilant_lc}"

        if math.isclose(deal_amount * deal_rate, fund_ded, rel_tol=tolerance):
            print("✅ deal_amount * deal_rate = fund_deduction is correct")
        else:
            assert False, f"❌ Mismatch: {deal_amount * deal_rate} != {fund_ded}"

        if math.isclose(fund_ded * deal_rev_rate, deal_amount, rel_tol=tolerance):
            print("✅ fund_deduction * deal_reverse_rate = deal_amount is correct")
        else:
            assert False, f"❌ Mismatch: {fund_ded * deal_rev_rate} != {deal_amount}"

        if math.isclose(fund_rate * deal_rate, deal_cost_rate, rel_tol=tolerance):
            print("✅ fund_rate * deal_rate = deal_cost_rate is correct")
        else:
            assert False, f"❌ Mismatch: {fund_rate * deal_rate} != {deal_cost_rate}"

        if math.isclose(1 / deal_cost_rate, cost_rev_rate, rel_tol=tolerance):
            print("✅ 1 / deal_cost_rate = deal_reverse_rate is correct")
        else:
            assert False, f"❌ Mismatch: {1 / deal_cost_rate} != {cost_rev_rate}"

        if math.isclose(equilant_lc2 / new_deal_pos, update_cost_rate, rel_tol=tolerance):
            print("✅ equilant_lc / new_deal_pos = updated_cost_rate is correct")
        else:
            assert False, f"❌ Mismatch: {equilant_lc2 / new_deal_pos} != {update_cost_rate}"

        self.apd.click_approve()
        time.sleep(2)

    def test_check_values_before_approved_and_after_are_same(self, setup):
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
        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)
        self.apd = Approved(self.driver)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()
        time.sleep(2)

        self.apd.select_first_Deal_phenom()
        time.sleep(5)

        ser_pro_bef = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/form/div/div[2]/div[1]/div[2]/div[1]/div/select")
        select = Select(ser_pro_bef)

        # Get the selected option's text
        ser_pro_bef_text = select.first_selected_option.text
        print("ser_pro_bef_text:", ser_pro_bef_text)

        deal_reference = self.driver.find_element(By.XPATH, "//input[@id='Deal Reference']").get_attribute("value")
        print("deal_reference:", deal_reference)

        deal_bef = self.driver.find_element(By.XPATH, "//select[@id='Deal Mode']")
        select = Select(deal_bef)
        deal_text = select.first_selected_option.text
        print("deal_text:", deal_text)

        value_date_field = self.driver.find_element(By.XPATH,
                                                    "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]").text
        print("value_date_field:", value_date_field)

        apply_date = self.driver.find_element(By.XPATH,
                                              "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]").text
        print("apply_date:", apply_date)

        deal_amount_bef = self.driver.find_element(By.XPATH, "//input[@id='Deal Amount']").get_attribute("value")
        print("deal_amount_bef:", deal_amount_bef)

        deal_rate = self.driver.find_element(By.XPATH, "//input[@id='dealRate']").get_attribute("value")
        print("deal_rate:", deal_rate)

        deal_reverse_rate = self.driver.find_element(By.XPATH, "//input[@id='dealReverseRate']").get_attribute("value")
        print("deal_reverse_rate:", deal_reverse_rate)

        fund_deduction = self.driver.find_element(By.XPATH, "//input[@id='fundDeduction']").get_attribute("value")
        print("fund_deduction:", fund_deduction)

        deal_cost_rate = self.driver.find_element(By.XPATH, "//input[@id='dealCostRate']").get_attribute("value")
        print("deal_cost_rate:", deal_cost_rate)

        cost_reverse_rate = self.driver.find_element(By.XPATH, "//input[@id='costReverseRate']").get_attribute("value")
        print("cost_reverse_rate:", cost_reverse_rate)

        equivalent_lc = self.driver.find_element(By.XPATH, "//input[@id='equivalentLC']").get_attribute("value")
        print("equivalent_lc:", equivalent_lc)

        self.apd.click_approve()
        time.sleep(2)

        self.apd.click_approved()
        time.sleep(3)

        approve_list = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[2]/div[34]")
        self.driver.execute_script("arguments[0].scrollIntoView();", approve_list)

        # Optionally, interact with the element after scrolling
        time.sleep(2)
        approve_list.click()

        print("after values")

        ser_pro_bef = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/form/div/div[2]/div[1]/div[2]/div[1]/div/select")
        select = Select(ser_pro_bef)

        # Get the selected option's text
        ser_pro_bef_text = select.first_selected_option.text
        print("ser_pro_bef_text:", ser_pro_bef_text)

        deal_reference = self.driver.find_element(By.XPATH, "//input[@id='Deal Reference']").get_attribute("value")
        print("deal_reference:", deal_reference)

        deal_bef = self.driver.find_element(By.XPATH, "//select[@id='Deal Mode']")
        select = Select(deal_bef)
        deal_text = select.first_selected_option.text
        print("deal_text:", deal_text)

        value_date_field = self.driver.find_element(By.XPATH,
                                                    "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]").text
        print("value_date_field:", value_date_field)

        apply_date = self.driver.find_element(By.XPATH,
                                              "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]").text
        print("apply_date:", apply_date)

        deal_amount_bef = self.driver.find_element(By.XPATH, "//input[@id='Deal Amount']").get_attribute("value")
        print("deal_amount_bef:", deal_amount_bef)

        deal_rate = self.driver.find_element(By.XPATH, "//input[@id='dealRate']").get_attribute("value")
        print("deal_rate:", deal_rate)

        deal_reverse_rate = self.driver.find_element(By.XPATH, "//input[@id='dealReverseRate']").get_attribute("value")
        print("deal_reverse_rate:", deal_reverse_rate)

        fund_deduction = self.driver.find_element(By.XPATH, "//input[@id='fundDeduction']").get_attribute("value")
        print("fund_deduction:", fund_deduction)

        deal_cost_rate = self.driver.find_element(By.XPATH, "//input[@id='dealCostRate']").get_attribute("value")
        print("deal_cost_rate:", deal_cost_rate)

        cost_reverse_rate = self.driver.find_element(By.XPATH, "//input[@id='costReverseRate']").get_attribute("value")
        print("cost_reverse_rate:", cost_reverse_rate)

        equivalent_lc = self.driver.find_element(By.XPATH, "//input[@id='equivalentLC']").get_attribute("value")
        print("equivalent_lc:", equivalent_lc)

    def test_valid_data_reject(self, setup):
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
        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)
        self.apd = Approved(self.driver)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())

        country.select_by_index(1)
        currency = Select(self.tba.drp_currency())
        currency.select_by_index(1)

        self.tba.select().click()
        time.sleep(2)

        self.apd.select_first_Deal_phenom()
        time.sleep(5)
        self.apd.click_Reject()
        time.sleep(2)
