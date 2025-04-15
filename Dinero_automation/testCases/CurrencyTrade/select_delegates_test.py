import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.currencytrade import SelectCustomer, Selectdelegate
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Delegate_Selector:
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
        self.nav.click_currency_trade()

        self.sc = SelectCustomer(self.driver)
        self.dc = Selectdelegate(self.driver)

        customer_type = self.sc.customersearching()
        customer_type.send_keys("Adarsh")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        transc_mode = Select(self.dc.Drptransction())
        transc_mode.select_by_index(2)
        time.sleep(2)
        delegate = self.dc.delegate_search()
        delegate.send_keys("akash p")

        time.sleep(1)
        delegate_selecer_element = self.dc.delegate_selecer()
        delegate_selecer_element.click()
        #

        # self.dc.nextbtn()
        time.sleep(4)

    def test_with_invalid_data(self, setup):
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
        customer_type.send_keys("Adarsh")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        transc_mode = Select(self.dc.Drptransction())
        transc_mode.select_by_index(2)
        time.sleep(2)
        # delegate = self.dc.delegate_search()
        # delegate.send_keys("akash p")
        #
        # time.sleep(1)
        # delegate_selecer_element = self.dc.delegate_selecer()
        # delegate_selecer_element.click()
        #

        # self.dc.nextbtn()
        time.sleep(4)

    def test_validating_cancel(self, setup):
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
        customer_type.send_keys("Adarsh")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        transc_mode = Select(self.dc.Drptransction())
        transc_mode.select_by_index(2)
        time.sleep(2)
        delegate = self.dc.delegate_search()
        delegate.send_keys("akash p")

        time.sleep(1)
        delegate_selecer_element = self.dc.delegate_selecer()
        delegate_selecer_element.click()

        self.dc.cancelbtn()
        self.dc.cancelyes()
        time.sleep(2)

        customer_type = self.sc.customersearching()
        customer_type.send_keys("Adarsh")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)
