import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.currencytrade import SelectCustomer, Selectdelegate, Transaction_review, \
    Transaction_details, Payment_details
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Delegate_Selector:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_purchase(self, setup):
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
        self.nav.click_currency_trade()

        self.sc = SelectCustomer(self.driver)
        self.dc = Selectdelegate(self.driver)

        customer_type = self.sc.customersearching()
        customer_type.send_keys("Adam Edge")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        transc_mode = Select(self.dc.Drptransction())
        transc_mode.select_by_index(1)
        time.sleep(2)
        delegate = self.dc.delegate_search()
        delegate.send_keys("John Cena")

        time.sleep(1)
        delegate_selecer_element = self.dc.delegate_selecer()
        delegate_selecer_element.click()

        self.dc.nextbtn()
        time.sleep(4)

        self.tdr = Transaction_details(self.driver)

        trans_purpose = Select(self.tdr.transaction_purpose())
        trans_purpose.select_by_index(2)
        source_of_income = Select(self.tdr.source_of_income())
        source_of_income.select_by_index(2)
        self.tdr.add_row_click().click()
        time.sleep(2)

        drp_transtyp1 = Select(self.tdr.transc_type1())
        drp_transtyp1.select_by_index(2)
        time.sleep(1)
        drp_currency1 = Select(self.tdr.drp_currency1())
        drp_currency1.select_by_index(1)
        time.sleep(2)
        fc_amount1 = self.tdr.fc_amount1().send_keys("200")
        rate1 = self.tdr.rate1().send_keys("1.5")
        service_charge1 = self.tdr.service_charge1().send_keys("30")
        self.tdr.close_button_click().click()
        time.sleep(2)

        # self.tdr.pos_click().click()
        self.tdr.cash_click().click()
        # self.tdr.online_click().click()
        self.tdr.cheque_click().click()
        # self.tdr.digital_click().click()
        time.sleep(1)

        self.tdr.click_next().click()
        time.sleep(2)

        self.trv = Transaction_review(self.driver)

        self.trv.click_confirm().click()

        self.pd = Payment_details(self.driver)

        self.pd.enter_cash().send_keys("200")
        self.pd.cheque_amount().send_keys("70")
        self.pd.cheque_number().send_keys("65665")
        self.pd.cheque_bank().send_keys("Bank")
        time.sleep(2)
        self.pd.cheque_date().click()
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[23]").click()

        self.pd.savebtn().click()

    def test_valid_data_sales(self, setup):
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
        self.nav.click_currency_trade()

        self.sc = SelectCustomer(self.driver)
        self.dc = Selectdelegate(self.driver)

        customer_type = self.sc.customersearching()
        customer_type.send_keys("Adam Edge")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        transc_mode = Select(self.dc.Drptransction())
        transc_mode.select_by_index(1)
        time.sleep(2)
        delegate = self.dc.delegate_search()
        delegate.send_keys("John Cena")

        time.sleep(1)
        delegate_selecer_element = self.dc.delegate_selecer()
        delegate_selecer_element.click()

        self.dc.nextbtn()
        time.sleep(4)

        self.tdr = Transaction_details(self.driver)

        trans_purpose = Select(self.tdr.transaction_purpose())
        trans_purpose.select_by_index(2)
        source_of_income = Select(self.tdr.source_of_income())
        source_of_income.select_by_index(2)
        self.tdr.add_row_click().click()
        time.sleep(2)

        drp_transtyp1 = Select(self.tdr.transc_type1())
        drp_transtyp1.select_by_index(1)
        time.sleep(1)
        drp_currency1 = Select(self.tdr.drp_currency1())
        drp_currency1.select_by_index(1)
        time.sleep(2)
        fc_amount1 = self.tdr.fc_amount1().send_keys("200")
        rate1 = self.tdr.rate1().send_keys("1.5")
        service_charge1 = self.tdr.service_charge1().send_keys("30")
        self.tdr.close_button_click().click()
        time.sleep(2)

        self.tdr.pos_click().click()
        self.tdr.cash_click().click()
        self.tdr.online_click().click()
        self.tdr.cheque_click().click()
        self.tdr.digital_click().click()
        pos_typ = Select(self.tdr.pos_type())
        pos_typ.select_by_index(1)
        time.sleep(1)

        self.tdr.click_next().click()
        time.sleep(2)

        self.trv = Transaction_review(self.driver)

        self.trv.click_confirm().click()

        self.pd = Payment_details(self.driver)

        self.pd.enter_cash().send_keys("200")
        self.pd.enter_pos_amount().send_keys("50")
        self.pd.pos_code().send_keys("adas")
        pos_bnk = Select(self.pd.drp_pos_bank())
        pos_bnk.select_by_index(3)

        screen = self.driver.find_element(By.XPATH,
                                          "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView(0,10);", screen)

        self.pd.cheque_amount().send_keys("50")
        self.pd.cheque_number().send_keys("65665")
        self.pd.cheque_bank().send_keys("Bank")

        self.pd.cheque_date().click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//abbr[contains(@aria-label,'February 21, 2025')]").click()

        self.pd.online_amount().send_keys("10")
        self.pd.digital_pay().send_keys("20")

        time.sleep(2)

        self.pd.savebtn().click()
