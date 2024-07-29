import os
import time

from selenium.webdriver.common.by import By

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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

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
        time.sleep(5)

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

        # perform customer registration actions for id verification
        self.cur = Persomal_Information(self.driver)

        self.cur.btnnext()
        time.sleep(2)

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_without_data.png")
            assert True
        self.driver.quit()

    def test_personal_info_with_bulk_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername("hello")
        self.lp.setPassword("pass")
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()

        self.cur = Persomal_Information(self.driver)
        self.cui = Contact_Information(self.driver)

        # Dropdowns
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
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

        self.cur.dobpicker_required(11022000)

        # Bulk data for personal information
        firstnames = ["Ahmed", "Fatima", "Ali", "Sara", "Omar", "Aisha", "Hassan", "Layla", "Mohammed", "Noor"]
        middlenames = ["Hussein", "Khalid", "Mariam", "Abdullah", "Youssef", "Ibrahim", "Zainab", "Fahad", "Hala","Tariq"]
        arabicnames = ["Ahmed", "Fatima", "Ali", "Sara", "Omar", "Aisha", "Hassan", "Layla", "Mohammed","boom"]
        lastnames = ["Al-Farsi", "Ibrahim", "Al-Hashimi", "Nasser", "Al-Turki", "Al-Salem", "Al-Jabri", "Darwish","Al-Rashid", "Al-Habib"]
        shortnames = ["Ahm", "Fat", "Ali", "Sar", "Oma", "Ais", "Has", "Lay", "Moh", "Noo"]
        maidennames = ["Al-Turki", "Al-Salem", "Al-Jabri", "Darwish", "Al-Amin", "Al-Ghamdi", "Al-Hassan", "Al-Sharif","Al-Mansoori", "Al-Khalifa"]

        for i in range(len(firstnames)):
            fr_name = firstnames[i]
            mid_name = middlenames[i]
            la_name = lastnames[i]
            arb_name = arabicnames[i]
            sho_name = shortnames[i]
            ma_name = maidennames[i]

            # Perform personal information
            self.cur.firstNameField_required(fr_name)
            self.cur.middleNameField_not_required(mid_name)
            self.cur.lastNameField_required(la_name)
            self.cur.arabicNameFiels_required(arb_name)
            self.cur.shortNameField_not_required(sho_name)
            self.cur.maidenNameFiels_not_required(ma_name)

            self.error = self.cur.errorMessage()

            if self.error == "Required":
                assert False
            else:
                self.driver.save_screenshot(screenShort.screen_short() + f"test_personal_info_bulk_data_success_{i}.png")
                assert True

            # Click the next button after each iteration
            self.cur.btnnext()

            # Come back to the previous page
            self.cui.btn_back()

            # Clear the fields for the next iteration
            self.cur.first_clear()
            self.cur.middle_clear()
            self.cur.last_clear()
            self.cur.arabic_clear()
            self.cur.short_clear()
            self.cur.maiden_clear()

        self.driver.quit()

    def test_personal_info_with_special_char(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.cur.middleNameField_not_required("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.cur.lastNameField_required("!@#$%^&*(_+*)/{}|]""-[:;',.?")
        self.cur.arabicNameFiels_required("!@#$%^&)*(_+*/{}|]""-[:;',.?")
        self.cur.shortNameField_not_required("!@#$%^)&*(_+*/{}|]""-[:;',.?")
        self.cur.maidenNameFiels_not_required("!@#$%^&*(_+*/{}|]"")-[:;',.?")

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

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_special_char.png")
            assert True
        self.driver.quit()

    def test_personal_info_with_special_num_char_char(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        self.cur.middleNameField_not_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        self.cur.lastNameField_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        self.cur.arabicNameFiels_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        self.cur.shortNameField_not_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        self.cur.maidenNameFiels_not_required("1!@#$%^&*()_+*/{}|]""-[:;',.?a")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_special_num_char_char.png")
            # assert True
        self.driver.quit()


    def test_personal_info_with_numbers(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("1234567890")
        self.cur.middleNameField_not_required("1234567890")
        self.cur.lastNameField_required("1234567890")
        self.cur.arabicNameFiels_required("1234567890")
        self.cur.shortNameField_not_required("1234567890")
        self.cur.maidenNameFiels_not_required("1234567890")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers.png")
            assert True
        self.driver.quit()


    def test_personal_info_with_text(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("qwertus")
        self.cur.middleNameField_not_required("qwertus")
        self.cur.lastNameField_required("qwertus")
        self.cur.arabicNameFiels_required("qwertus")
        self.cur.shortNameField_not_required("qwertus")
        self.cur.maidenNameFiels_not_required("qwertus")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers.png")
            # assert True
        self.driver.quit()

    def test_personal_info_with_text_required(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("qwertus")
        self.cur.lastNameField_required("qwertus")
        self.cur.arabicNameFiels_required("qwertus")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers.png")
            # assert True
        self.driver.quit()

    def test_personal_info_with_numbers_required(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("123456789")
        self.cur.lastNameField_required("123456789")
        self.cur.arabicNameFiels_required("1234567")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers_required.png")
            assert True
        self.driver.quit()


    def test_personal_info_with_specialchar_required(self, setup):
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
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.cur.lastNameField_required("1!@#$%^&*()_+*/{}|]""-[:;',.?")
        self.cur.arabicNameFiels_required("!@#$%^&*()_+*/{}|]""-[:;',.?")

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

        time.sleep(5)
        self.cur.btnnext()


        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_specialchar_required.png")
            assert True
        self.driver.quit()

    def test_personal_info_with_previewpage(self,setup):
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
        self.ci = Contact_Information(self.driver)
        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

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

    # getting data for preview validation

        # for tittle dropdown
        self.title = self.drp.first_selected_option
        self.title_text = self.title.text

        # for cob
        self.cob = self.cob.first_selected_option
        self.cunofbir = self.cob.text

        # for nationality
        self.text = self.nationality.first_selected_option
        self.nat = self.text.text

        # for citizenship
        self.text = self.citizenship.first_selected_option
        self.citiz = self.text.text

        # for country of residence
        self.text = self.country_of_residence.first_selected_option
        self.cor = self.text.text

        # for residential status
        self.text = self.residential_status.first_selected_option
        self.res = self.text.text

        # for gender
        self.text = self.gender.first_selected_option
        self.gen = self.text.text

        # for marital status
        self.text = self.mrg.first_selected_option
        self.mrgs = self.text.text

        # for profession
        self.text = self.profession.first_selected_option
        self.profs = self.text.text

        # btns
        self.cur.btnnext()
        self.ci.click_preview()

        # print input data
        print(self.title_text)
        print(self.cunofbir)
        print(self.nat)
        print(self.citiz)
        print(self.cor)
        print(self.res)
        print(self.gen)
        print(self.mrgs)
        print(self.profs)

        # print previe values

        print("Title:", self.ci.title())
        print("First Name:", self.ci.firstname())
        print("Last Name:", self.ci.lastname())
        print("Middle Name:", self.ci.middlename())
        print("Arabic Name:", self.ci.arabicname())
        print("Short Name:", self.ci.shortname())
        print("Maiden Name:", self.ci.maidenname())
        print("Date of Birth:", self.ci.dob())
        print("Nationality:", self.ci.natinality())
        print("Citizen:", self.ci.citizen())
        print("Country of Residence:", self.ci.cor())
        print("Country of Birth:", self.ci.cob())
        print("Residency Status:", self.ci.res())
        print("Gender:", self.ci.gender())
        print("Marital Status:", self.ci.marristatus())
        print("Profession:", self.ci.profesion())

        if self.title_text == self.ci.title():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_title.png")
            assert False

        if self.ci.firstname() == "Test":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_first.png")
            assert False

        if self.ci.lastname() == "User":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_last.png")
            assert False

        if self.ci.middlename() == "Middle":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_middle.png")
            assert False

        if self.ci.arabicname() == "name":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_arabic.png")
            assert False

        if self.ci.shortname() == "Short":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_short.png")
            assert False

        if self.ci.maidenname() == "Maiden":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_maidname.png")
            assert False

        if self.ci.dob() == "11-02-2000":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_dob.png")
            assert False

        if self.ci.natinality() == self.nat:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_nationality.png")
            assert False

        if self.ci.citizen() == self.citiz:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_citizen.png")
            assert False

        if self.ci.cor() == self.cor:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_cor.png")
            assert False

        if self.ci.res() == self.res:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_res.png")
            assert False

        if self.ci.gender() == self.gen:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_gender.png")
            assert False

        if self.ci.marristatus() == self.mrgs:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_mrgstatus.png")
            assert False

        if self.ci.profesion() == self.profs:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_previewpage_profision.png")
            assert False













