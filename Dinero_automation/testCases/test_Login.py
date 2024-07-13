import os
import time

from Dinero_automation.utilities.readProperties import ReadConfig
from ..pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import Select


class Test_Login:
    url = ReadConfig.getApplicationURL()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)

    def test_ar_lang_dropdown_validation(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.lp = LoginPage(self.driver)
        self.element = self.lp.clickDropdown()
        time.sleep(2)
        self.drp = Select(self.element)
        # for ar
        self.drp.select_by_index(1)
        time.sleep(2)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.quit()

    def test_es_lang_dropdown_validation(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.lp = LoginPage(self.driver)
        self.element = self.lp.clickDropdown()
        time.sleep(2)
        self.drp = Select(self.element)
        # for ar
        self.drp.select_by_index(2)
        time.sleep(2)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.quit()

    def test_fr_lang_dropdown_validation(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.lp = LoginPage(self.driver)
        self.element = self.lp.clickDropdown()
        time.sleep(2)
        self.drp = Select(self.element)
        # for ar
        self.drp.select_by_index(3)
        time.sleep(2)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.quit()

    def test_hi_lang_dropdown_validation(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.lp = LoginPage(self.driver)
        self.element = self.lp.clickDropdown()
        time.sleep(2)
        self.drp = Select(self.element)
        # for ar
        self.drp.select_by_index(4)
        time.sleep(2)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.quit()

    def test_te_lang_dropdown_validation(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.lp = LoginPage(self.driver)
        self.element = self.lp.clickDropdown()
        time.sleep(2)
        self.drp = Select(self.element)
        # for ar
        self.drp.select_by_index(5)
        time.sleep(2)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.quit()





