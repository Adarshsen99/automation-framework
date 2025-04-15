import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.deal_manger import To_be_approved
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_to_be_approved:
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
        # time.sleep(2)

        # click action for customer details
        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("CR Enterprises")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        #self.tba.request_for_approval()
        time.sleep(2)

        self.tba.click_new_deal().click()
        time.sleep(1)
        deal_mode = Select(self.tba.drp_dealmode())
        deal_mode.select_by_index(1)

        self.tba.deal_amount().send_keys("5000")
        self.tba.deal_rate().send_keys("2.5")
        time.sleep(2)




        self.tba.request_for_approval().click()

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
        # time.sleep(2)

        # click action for customer details
        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)

        # ser_pro = Select(self.tba.drp_service_pro())
        # ser_pro.select_by_visible_text("Phenomenal Money")
        #
        # country = Select(self.tba.drp_country())
        # currency = Select(self.tba.drp_currency())
        #
        # country.select_by_index(1)
        # currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.click_new_deal().click()
        time.sleep(1)
        deal_mode = Select(self.tba.drp_dealmode())
        deal_mode.select_by_index(1)

        self.tba.deal_amount().send_keys("500")
        self.tba.deal_rate().send_keys("0.0125")
        time.sleep(2)

        self.tba.request_for_approval().click()

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
        # time.sleep(2)

        # click action for customer details
        self.nav.click_deal_manger()
        time.sleep(2)

        self.tba = To_be_approved(self.driver)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.click_new_deal().click()
        time.sleep(1)
        deal_mode = Select(self.tba.drp_dealmode())
        deal_mode.select_by_index(1)

        self.tba.deal_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.tba.deal_rate().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        time.sleep(2)

        self.tba.request_for_approval().click()

    def test_sending_spl_char_num(self, setup):
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

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.click_new_deal().click()
        time.sleep(1)
        deal_mode = Select(self.tba.drp_dealmode())
        deal_mode.select_by_index(1)

        self.tba.deal_amount().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?aevzx")
        self.tba.deal_rate().send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?aezx")
        time.sleep(2)

        self.tba.request_for_approval().click()

    def test_data_have_spaces(self, setup):
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

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.click_new_deal().click()
        time.sleep(1)
        deal_mode = Select(self.tba.drp_dealmode())
        deal_mode.select_by_index(1)

        self.tba.deal_amount().send_keys("2 2 52 5 5 22  ")
        self.tba.deal_rate().send_keys("2 2 52 5 5 22 ")
        time.sleep(2)

        self.tba.request_for_approval().click()

    def test_refresh_inside_deal_date(self, setup):
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

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.date_from_field().send_keys(12022022)
        time.sleep(2)
        # self.tba.date_to_field().send_keys(12082025)
        # time.sleep(2)

        self.tba.refresh_insd()
        time.sleep(3)
        self.tba.date_from_field().send_keys(12022022)
        time.sleep(2)
        self.tba.date_to_field().send_keys(12082025)
        # time.sleep(2)
        self.tba.refresh_insd()
        time.sleep(3)
        self.tba.date_from_field().send_keys(12022022)
        time.sleep(2)
        # self.tba.date_to_field().send_keys(12082025)
        # time.sleep(2)

        # self.tba.click_new_deal().click()
        # time.sleep(1)
        # deal_mode = Select(self.tba.drp_dealmode())
        # deal_mode.select_by_index(1)
        #
        # self.tba.deal_amount().send_keys("797979")
        # self.tba.deal_rate().send_keys("4")
        # time.sleep(2)
        #
        # self.tba.request_for_approval().click()

    def test_refresh_outside_ser_pro(self, setup):
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

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        time.sleep(2)
        self.tba.refresh_out()
        time.sleep(3)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        time.sleep(2)
        self.tba.refresh_out()
        time.sleep(3)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        time.sleep(2)
        self.tba.refresh_out()
        time.sleep(3)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        time.sleep(2)
        self.tba.refresh_out()
        time.sleep(3)

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

    def test_date_field_working(self, setup):
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

        ser_pro = Select(self.tba.drp_service_pro())
        ser_pro.select_by_visible_text("Phenomenal Money")

        country = Select(self.tba.drp_country())
        currency = Select(self.tba.drp_currency())

        country.select_by_index(1)
        currency.select_by_index(1)

        self.tba.select().click()

        # self.tba.request_for_approval()
        time.sleep(2)

        self.tba.date_from_field().send_keys(18102024)
        time.sleep(2)
        # self.tba.date_to_field().send_keys(18102024)
        # time.sleep(2)

        self.tba.refresh_insd()
        time.sleep(3)
        self.tba.date_from_field().send_keys(18102024)
        time.sleep(2)
        # self.tba.date_to_field().send_keys(18102024)
        # time.sleep(2)
        self.tba.refresh_insd()
        time.sleep(3)
        self.tba.date_from_field().send_keys(18102024)
        time.sleep(2)
        # self.tba.date_to_field().send_keys(12082025)
        # time.sleep(2)
