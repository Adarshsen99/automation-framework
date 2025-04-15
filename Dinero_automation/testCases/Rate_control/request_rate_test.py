import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.rate_control import Request_rate
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_Request_rate:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self, setup):

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
        self.nav.click_rate_control()
        time.sleep(2)

        self.rr = Request_rate(self.driver)

        ser_pro = Select(self.rr.drp_service_provider())
        time.sleep(1)
        # ser_pro.select_by_index(12)
        ser_pro.select_by_visible_text("CRISTIANO FOUNDATIONS")

        country = Select(self.rr.drp_country())
        country.select_by_visible_text("India")

        self.rr.click_filter().click()

        marg_contro = Select(self.rr.drp_margin_control())
        marg_contro.select_by_index(1)
        time.sleep(2)

        self.rr.issue_rate_input().send_keys("0.1")

        self.rr.slab_selector().click()

        self.rr.best_rate_perc().send_keys("2")

        req_click = self.rr.click_req_for_apprvl()

        # Scroll the element into view using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", req_click)
        time.sleep(2)

        req_click.click()

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
        time.sleep(2)
        self.nav.click_rate_control()
        time.sleep(2)

        self.rr = Request_rate(self.driver)

        ser_pro = Select(self.rr.drp_service_provider())
        ser_pro.select_by_index(12)
        # ser_pro.select_by_visible_text("CRISTIANO")

        country = Select(self.rr.drp_country())
        country.select_by_index(1)

        self.rr.click_filter().click()

        marg_contro = Select(self.rr.drp_margin_control())
        marg_contro.select_by_index(1)
        time.sleep(2)

        self.rr.issue_rate_input().send_keys("")

        self.rr.slab_selector().click()

        self.rr.best_rate_perc().send_keys("")

        req_click = self.rr.click_req_for_apprvl()

        # Scroll the element into view using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", req_click)
        time.sleep(2)

        req_click.click()

    def test_sending_invalid_data(self, setup):
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
        self.nav.click_rate_control()
        time.sleep(2)

        self.rr = Request_rate(self.driver)

        ser_pro = Select(self.rr.drp_service_provider())
        ser_pro.select_by_index(12)
        # ser_pro.select_by_visible_text("Phenomenal")

        country = Select(self.rr.drp_country())
        country.select_by_index(1)

        self.rr.click_filter().click()

        marg_contro = Select(self.rr.drp_margin_control())
        marg_contro.select_by_index(1)
        time.sleep(2)

        self.rr.issue_rate_input().send_keys("0")

        self.rr.slab_selector().click()

        self.rr.best_rate_perc().send_keys("0")

        req_click = self.rr.click_req_for_apprvl()

        # Scroll the element into view using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", req_click)
        time.sleep(2)

        req_click.click()

    def test_sendimg_spl_char_Alp(self, setup):
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
        self.nav.click_rate_control()
        time.sleep(2)

        self.rr = Request_rate(self.driver)

        ser_pro = Select(self.rr.drp_service_provider())
        ser_pro.select_by_index(12)
        # ser_pro.select_by_visible_text("Phenomenal")

        country = Select(self.rr.drp_country())
        country.select_by_index(1)

        self.rr.click_filter().click()

        marg_contro = Select(self.rr.drp_margin_control())
        marg_contro.select_by_index(1)
        time.sleep(2)

        self.rr.issue_rate_input().send_keys("!@##$%$%^&*()_+{}|:?""[]=-evax")

        self.rr.slab_selector().click()

        self.rr.best_rate_perc().send_keys("!@##$%$%^&*()_+{}|:?""[]=-")

        req_click = self.rr.click_req_for_apprvl()

        # Scroll the element into view using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", req_click)
        time.sleep(2)

        req_click.click()

    def test_calculating_margin_factor(self, setup):
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
        self.nav.click_rate_control()
        time.sleep(2)

        self.rr = Request_rate(self.driver)

        ser_pro = Select(self.rr.drp_service_provider())
        ser_pro.select_by_index(12)
        # ser_pro.select_by_visible_text("Phenomenal")

        country = Select(self.rr.drp_country())
        country.select_by_index(1)

        self.rr.click_filter().click()

        marg_contro = Select(self.rr.drp_margin_control())
        marg_contro.select_by_index(1)
        time.sleep(2)

        issue_rate = self.rr.issue_rate_input()

        issue_rate.send_keys("9.5")

        issue_rate_value = float(issue_rate.get_attribute('value'))

        cost_rate = self.driver.find_element(By.XPATH,
                                             "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/span[7]")
        cost_rate_value_str = cost_rate.get_attribute('value')

        if cost_rate_value_str is None:
            cost_rate_value_str = cost_rate.text

        cost_rate_value = float(cost_rate_value_str)

        margin_factor = self.driver.find_element(By.XPATH,
                                                 "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/span[11]")

        margin_factor_value = margin_factor.get_attribute('value')

        if margin_factor_value is None:
            margin_factor_value = margin_factor.text

        margin_factor_value1 = float(margin_factor_value)

        print("cost_rate_value:", cost_rate_value)
        print("issue_rate_value:", issue_rate_value)
        print("margin_factor_value1:", margin_factor_value1)

        field1 = (cost_rate_value - issue_rate_value)
        print(field1)

        expected_margin_factor = field1 / cost_rate_value

        print("expected_margin_factor:", expected_margin_factor)

        if expected_margin_factor == margin_factor_value:
            assert True
        else:
            assert False
