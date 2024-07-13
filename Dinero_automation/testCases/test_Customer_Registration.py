import os
import time

from Dinero_automation.utilities.readProperties import ReadConfig
from ..pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Customer_Registration:
    url = ReadConfig.getApplicationURL()
    def test_personal_info_with_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        # time.sleep(2)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer registration
        self.nav.click_customer_registration()
        # time.sleep(2)

    #     # perform customer registration actions for id verification
        self.cur = Persomal_Information(self.driver)
        self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        self.cu_status.select_by_index(1)
        self.cur.idNoField_not_required("7")
        self.cur.dateofexpiry_not_required(12102024)
        self.cur.btnverify()
        time.sleep(2)
    #
        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Test")
        self.cur.middleNameField_not_required("Middle")
        self.cur.lastNameField_required("User")
        self.cur.arabicNameFiels_required("name")
        self.cur.shortNameField_not_required("Short")
        self.cur.maidenNameFiels_not_required("Maiden")

        # Select date of birth using the custom method
        self.cur.dobpicker_required(11022000)
        # dropdowns
        self.cob = Select(self.cur.cobDropdown_required())
        self.cob.select_by_index(2)
        self.nationality = Select(self.cur.nationality())
        self.nationality.select_by_index(2)
        self.citizenship = Select(self.cur.citizenship())
        self.citizenship.select_by_index(2)
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.country_of_residence.select_by_index(2)
        self.residential_status = Select(self.cur.residentialstatus())
        self.residential_status.select_by_index(2)
        self.gender = Select(self.cur.gender())
        self.gender.select_by_index(2)
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_index(2)
        self.profession = Select(self.cur.profession())
        self.profession.select_by_index(2)
        time.sleep(2)

        self.cur.btnnext()
        time.sleep(2)

        self.error = self.cur.errorMessage()

        if not self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_valid_data.png")
            assert False
        self.driver.quit()


    def test_personal_info_without_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        time.sleep(2)

        # click action for customer registration
        self.nav.click_customer_registration()
        time.sleep(2)

    #     # perform customer registration actions for id verification
        self.cur = Persomal_Information(self.driver)

        self.cur.btnnext()
        time.sleep(2)

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_without_data.png")
            assert False
        self.driver.quit()

    # def test_personal_info_with_bulk_data(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(20)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername("hello")
    #     self.lp.setPassword("pass")
    #     time.sleep(2)
    #     self.lp.clickLogin()
    #     time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     time.sleep(2)
    #
    #     #     # perform customer registration actions for id verification
    #     self.cur = Persomal_Information(self.driver)
    #     self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     self.cu_status.select_by_index(1)
    #     self.cur.idNoField_not_required("7")
    #     self.cur.dateofexpiry_not_required(12102024)
    #     self.cur.btnverify()
    #     time.sleep(2)
    #     #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     firstnames = ["Ahmed", "Fatima", "Ali", "Sara", "Mohammed", "Aisha", "Omar", "Yasmin", "Hassan", "Layla"]
    #     middlenames = ["Hussein", "Khalid", "Mariam", "Abdullah", "Youssef", "Nour", "Salim", "Samira", "Ibrahim","Mona"]
    #     lastnames = ["Al-Farsi", "Ibrahim", "Al-Hashimi", "Nasser", "Yazid", "Abbas", "Khan", "Aziz", "Mahmoud","Hassan"]
    #     arabicnames = ["أحمد", "فاطمة", "علي", "سارة", "محمد", "عائشة", "عمر", "ياسمين", "حسن", "ليلى"]
    #     shortnames = ["Ahm", "Fat", "Ali", "Sar", "Moh", "Ais", "Omr", "Yas", "Has", "Lay"]
    #     maidennames = ["Al-Turki", "Al-Salem", "Al-Jabri", "Naguib", "Salam", "Al-Muhandis", "Hakim", "Al-Badawi", "Shakir", "Darwish"]
    #
    #     for fr_name in firstnames:
    #         for mid_name in middlenames:
    #             for la_name in lastnames:
    #                 for arb_name in arabicnames:
    #                     for sho_name in shortnames:
    #                         for ma_name in maidennames:
    #                             self.cur.firstNameField_required(fr_name)
    #                             self.cur.middleNameField_required(mid_name)
    #                             self.cur.lastNameField_required(la_name)
    #                             self.cur.arabicNameFiels_required(arb_name)
    #                             self.cur.shortNameField_required(sho_name)
    #                             self.cur.maidenNameFiels_required(ma_name)
    #
    #                             # Select date of birth using the custom method
    #                             self.cur.dobpicker_required(11022000)
    #                             # dropdowns
    #                             self.cob = Select(self.cur.cobDropdown_required())
    #                             self.cob.select_by_index(2)
    #                             self.nationality = Select(self.cur.nationality())
    #                             self.nationality.select_by_index(2)
    #                             self.citizen
    #
    #
    #         self.cur.firstNameField_required("Test")
    #     self.cur.middleNameField_not_required("Middle")
    #     self.cur.lastNameField_required("User")
    #     self.cur.arabicNameFiels_required("name")
    #     self.cur.shortNameField_not_required("Short")
    #     self.cur.maidenNameFiels_not_required("Maiden")
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(11022000)
    #     # dropdowns
    #     self.cob = Select(self.cur.cobDropdown_required())
    #     self.cob.select_by_index(2)
    #     self.nationality = Select(self.cur.nationality())
    #     self.nationality.select_by_index(2)
    #     self.citizenship = Select(self.cur.citizenship())
    #     self.citizenship.select_by_index(2)
    #     self.country_of_residence = Select(self.cur.countryofresidence())
    #     self.country_of_residence.select_by_index(2)
    #     self.residential_status = Select(self.cur.residentialstatus())
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #     time.sleep(2)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if not self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_wit_bulk_data.png")
    #         assert False
    #     self.driver.quit()









