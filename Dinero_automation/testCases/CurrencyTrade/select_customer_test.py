import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.currencytrade import SelectCustomer, Selectdelegate
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Customer_Selector:
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

        customer_type = self.sc.customersearching()
        customer_type.send_keys("Adarsh")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        #test passed

    def test_send_valid_id_no(self, setup):
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

        customer_type = self.sc.customersearching()
        customer_type.send_keys("242412412")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        #test passed

    def test_send_without_data(self, setup):
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

        # customer_type = self.sc.customersearching()
        # customer_type.send_keys("242412412")
        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

        # test passed

    def test_spl_char(self, setup):
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

        customer_type = self.sc.customersearching()
        customer_type.send_keys("!@#$%^&*()_++{}:/.,.;;/")

        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.nextbtn()
        time.sleep(2)

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

        customer_type = self.sc.customersearching()
        customer_type.send_keys("adarsh")

        time.sleep(2)
        self.sc.customerselect()
        time.sleep(2)

        self.sc.verifybtn()
        self.sc.cancelbtn()

        self.sc.cancelyes()

        self.sc.nextbtn()
        time.sleep(2)



