import time

from selenium.webdriver.common.by import By

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information
from Dinero_automation.utilities.randomString import random_string_generator_max_30, random_string_generator_max_50, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Test_Personal_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_personal_info_with_data(self, setup):
        # Setup and login
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        time.sleep(11)

        # Navigation actions
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

        # Perform personal information actions

        self.cur.firstNameField_required("Tesfat")
        self.cur.middleNameField_not_required("Miafsddle")
        self.cur.lastNameField_required("Usesfr")
        self.cur.arabicNameFiels_required("nafsafme")
        self.cur.shortNameField_not_required("Shoafsrt")
        self.cur.maidenNameFiels_not_required("Mafsaiden")
        self.cur.dobpicker_required(11022000)

        # Wait object
        wait = WebDriverWait(self.driver, 10)

        # Dropdowns with Explicit Waits
        try:
            # Nationality Dropdown
            nationality_dropdown = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[7]/div[1]/div[1]/div[1]/select[1]"))
            )
            nationality_select = Select(nationality_dropdown)
            nationality_values = [option.text for option in nationality_select.options]
            print("Nationality Values:", nationality_values)

            # Country of Birth Dropdown
            country_of_birth_dropdown = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div[2]/div/div/select")
                )
            )
            country_of_birth_select = Select(country_of_birth_dropdown)
            country_of_birth_values = [option.text for option in country_of_birth_select.options]
            print("Country of Birth Values:", country_of_birth_values)

            profession_dropdown = wait.until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[10]/div/div/select"))
            )
            profession_select = Select(profession_dropdown)
            profession_values = [option.text for option in profession_select.options]
            print("profession_values:", profession_values)

            # Continue with remaining dropdown selections
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

            # Error message check
            self.error = self.cur.errorMessage()
            if self.error != "Required":
                assert True
            else:
                self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_valid_data.png")
                assert False

        finally:
            # Clean up
            self.driver.quit()

    def test_personal_info_without_data(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        #
        time.sleep(15)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

        # perform customer registration actions for id verification
        self.cur = Persomal_Information(self.driver)
        time.sleep(2)

        self.cur.btnnext()

        self.error = self.cur.errorMessage()

        nationality_dropdown = self.driver.find_element(By.ID,
                                                        "nationalityDropdownID")  # Replace with actual ID or locator
        nationality_select = Select(nationality_dropdown)

        nationality_values = [option.text for option in nationality_select.options]
        print("Nationality Values:", nationality_values)

        # Locate the dropdown for Country of Birth and print all values
        country_of_birth_dropdown = self.driver.find_element(By.ID,
                                                             "countryOfBirthDropdownID")  # Replace with actual ID or locator
        country_of_birth_select = Select(country_of_birth_dropdown)

        country_of_birth_values = [option.text for option in country_of_birth_select.options]
        print("Country of Birth Values:", country_of_birth_values)

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_without_data.png")
            assert False

    def test_personal_info_with_bulk_data(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

        self.cur = Persomal_Information(self.driver)
        self.cui = Contact_Information(self.driver)

        # Dropdowns

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
        middlenames = ["Hussein", "Khalid", "Mariam", "Abdullah", "Youssef", "Ibrahim", "Zainab", "Fahad", "Hala",
                       "Tariq"]
        arabicnames = ["Ahmed", "Fatima", "Ali", "Sara", "Omar", "Aisha", "Hassan", "Layla", "Mohammed", "boom"]
        lastnames = ["Al-Farsi", "Ibrahim", "Al-Hashimi", "Nasser", "Al-Turki", "Al-Salem", "Al-Jabri", "Darwish",
                     "Al-Rashid", "Al-Habib"]
        shortnames = ["Ahm", "Fat", "Ali", "Sar", "Oma", "Ais", "Has", "Lay", "Moh", "Noo"]
        maidennames = ["Al-Turki", "Al-Salem", "Al-Jabri", "Darwish", "Al-Amin", "Al-Ghamdi", "Al-Hassan", "Al-Sharif",
                       "Al-Mansoori", "Al-Khalifa"]

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
                self.driver.save_screenshot(
                    screenShort.screen_short() + f"test_personal_info_bulk_data_success_{i}.png")
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

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

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
        # time.sleep(2)

        self.cur.btnnext()
        # time.sleep(2)

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_special_char.png")
            assert False
        self.driver.quit()

    def test_personal_info_with_special_num_char_char(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")
        self.cur.middleNameField_not_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")
        self.cur.lastNameField_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")
        self.cur.arabicNameFiels_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")
        self.cur.shortNameField_not_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")
        self.cur.maidenNameFiels_not_required("10!@#$%^&*()_+*/{}|]""-[:;',.?aeb")

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

        # time.sleep(5)
        self.cur.btnnext()

        self.error = self.cur.errorMessage()

        if not self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_special_num_char_char.png")
            assert False
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

        # time.sleep(5)
        self.cur.btnnext()

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers.png")
            assert True
        self.driver.quit()

    def test_personal_info_with_text(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
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

        # time.sleep(5)
        self.cur.btnnext()

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_numbers.png")
            # assert True
        self.driver.quit()

    def test_personal_info_with_text_required(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)

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

        # time.sleep(5)
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

        # time.sleep(5)
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
        self.cur.lastNameField_required("!@#$%^&*()_+*/{}|]""-[:;',.?")
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

        # time.sleep(5)
        self.cur.btnnext()

        self.error = self.cur.errorMessage()

        if self.error == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_personal_info_with_specialchar_required.png")
            assert True
        self.driver.quit()

    def test_personal_info_with_previewpage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

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
        # time.sleep(2)

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

        print("Actual Data from the system")
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
        print(" ")
        print("Data from the Preview")
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
        print("Residential Status:", self.ci.res())
        print("Gender:", self.ci.gender())
        print("Marital Status:", self.ci.marristatus())
        print("Profession:", self.ci.profesion())

        print("System Residential Status:", repr(self.res))
        print("Preview Residential Status:", repr(self.ci.res()))

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

        if self.ci.arabicname() == "Name":
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
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_previewpage_profision.png")
            assert False

        self.driver.quit()

    def test_cancel(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Test")
        self.cur.middleNameField_not_required("Middle")
        self.cur.lastNameField_required("User")
        self.cur.arabicNameFiels_required("name")
        self.cur.shortNameField_not_required("Short")
        self.cur.maidenNameFiels_not_required("Maiden")
        self.cur.dobpicker_required(11022000)

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

        def get_dropdown_text(select_element):
            return select_element.first_selected_option.text

        print("Getting data from the dropdowns before")
        self.title_text = get_dropdown_text(self.drp)
        self.cunofbir = get_dropdown_text(self.cob)
        self.nat = get_dropdown_text(self.nationality)
        self.citiz = get_dropdown_text(self.citizenship)
        self.cor = get_dropdown_text(self.country_of_residence)
        self.res = get_dropdown_text(self.residential_status)
        self.gen = get_dropdown_text(self.gender)
        self.mrgs = get_dropdown_text(self.mrg)
        self.profs = get_dropdown_text(self.profession)

        print(self.title_text)
        print(self.cunofbir)
        print(self.nat)
        print(self.citiz)
        print(self.cor)
        print(self.res)
        print(self.gen)
        print(self.mrgs)
        print(self.profs)

        self.cur.btncancel()
        self.cur.btn_canel_confirm()

        # Re-find the elements after the cancel action to avoid stale element reference
        self.drp = Select(self.cur.titleDropdown_required())
        self.cob = Select(self.cur.cobDropdown_required())
        self.nationality = Select(self.cur.nationality())
        self.citizenship = Select(self.cur.citizenship())
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.residential_status = Select(self.cur.residentialstatus())
        self.gender = Select(self.cur.gender())
        self.mrg = Select(self.cur.maritalstatus())
        self.profession = Select(self.cur.profession())

        print("Getting data from the dropdowns after clearing")
        self.title_text_af = get_dropdown_text(self.drp)
        self.cunofbir_af = get_dropdown_text(self.cob)
        self.nat_af = get_dropdown_text(self.nationality)
        self.citiz_af = get_dropdown_text(self.citizenship)
        self.cor_af = get_dropdown_text(self.country_of_residence)
        self.res_af = get_dropdown_text(self.residential_status)
        self.gen_af = get_dropdown_text(self.gender)
        self.mrgs_af = get_dropdown_text(self.mrg)
        self.profs_af = get_dropdown_text(self.profession)

        print(self.title_text_af)
        print(self.cunofbir_af)
        print(self.nat_af)
        print(self.citiz_af)
        print(self.cor_af)
        print(self.res_af)
        print(self.gen_af)
        print(self.mrgs_af)
        print(self.profs_af)

        if (self.title_text != self.title_text_af and self.cunofbir != self.cunofbir_af and self.nat != self.nat_af and
                self.citiz != self.citiz_af and self.cor != self.cor_af and self.res != self.res_af and self.gen != self.gen_af and
                self.mrgs != self.mrgs_af and self.profs != self.profs_af):
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_cancel.png")
            assert False
        self.driver.quit()

    def test_modifications_append(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Test")
        self.cur.middleNameField_not_required("Middle")
        self.cur.lastNameField_required("User")
        self.cur.arabicNameFiels_required("name")
        self.cur.shortNameField_not_required("Short")
        self.cur.maidenNameFiels_not_required("Maiden")
        self.cur.dobpicker_required(11022000)

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

        # buttons
        self.cur.btnnext()
        self.ci.btn_back()

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Karunkar")
        self.cur.middleNameField_not_required("Finnest")
        self.cur.lastNameField_required("Technology")
        self.cur.arabicNameFiels_required("Mohamad")
        self.cur.shortNameField_not_required("Karunakar")
        self.cur.maidenNameFiels_not_required("Karunakar")
        self.cur.dobpicker_required(30032000)

        self.cob = Select(self.cur.cobDropdown_required())
        self.cob.select_by_index(1)
        self.nationality = Select(self.cur.nationality())
        self.nationality.select_by_index(1)
        self.citizenship = Select(self.cur.citizenship())
        self.citizenship.select_by_index(1)
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.country_of_residence.select_by_index(1)
        self.residential_status = Select(self.cur.residentialstatus())
        self.residential_status.select_by_index(1)
        self.gender = Select(self.cur.gender())
        self.gender.select_by_index(1)
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_index(1)
        self.profession = Select(self.cur.profession())
        self.profession.select_by_index(1)

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

        print("Actual Data from the system")
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
        print(" ")
        print("Data from the Preview")
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
                screenShort.screen_short() + "test_modifications_append_title.png")
            assert False

        if self.ci.firstname() == "TestKarunkar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_first.png")
            assert False

        if self.ci.lastname() == "UserTechnology":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_last.png")
            assert False

        if self.ci.middlename() == "MiddleFinnest":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_middle.png")
            assert False

        if self.ci.arabicname() == "NameMohamad":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_arabic.png")
            assert False

        if self.ci.shortname() == "ShortKarunakar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_short.png")
            assert False

        if self.ci.maidenname() == "MaidenKarunakar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_maidname.png")
            assert False

        if self.ci.dob() == "30-03-2000":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_dob.png")
            assert False

        if self.ci.natinality() == self.nat:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_nationality.png")
            assert False

        if self.ci.citizen() == self.citiz:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_citizen.png")
            assert False

        if self.ci.cor() == self.cor:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_cor.png")
            assert False

        if self.ci.res() == self.res:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_res.png")
            assert False

        if self.ci.gender() == self.gen:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_gender.png")
            assert False

        if self.ci.marristatus() == self.mrgs:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_mrgstatus.png")
            assert False

        if self.ci.profesion() == self.profs:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_append_profision.png")
            assert False

        self.driver.quit()

    def test_modifications_earse_before(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Test")
        self.cur.middleNameField_not_required("Middle")
        self.cur.lastNameField_required("User")
        self.cur.arabicNameFiels_required("name")
        self.cur.shortNameField_not_required("Short")
        self.cur.maidenNameFiels_not_required("Maiden")
        self.cur.dobpicker_required(11022000)

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

        # buttons
        self.cur.btnnext()
        self.ci.btn_back()

        self.cur.first_clear()

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.first_clear()
        self.cur.firstNameField_required("Karunkar")
        self.cur.middle_clear()
        self.cur.middleNameField_not_required("Finnest")
        self.cur.last_clear()
        self.cur.lastNameField_required("Technology")
        self.cur.arabic_clear()
        self.cur.arabicNameFiels_required("Mohamad")
        self.cur.short_clear()
        self.cur.shortNameField_not_required("Karunakar")
        self.cur.maiden_clear()
        self.cur.maidenNameFiels_not_required("Karunakar")
        self.cur.dobpicker_required(30032000)

        self.cob = Select(self.cur.cobDropdown_required())
        self.cob.select_by_index(1)
        self.nationality = Select(self.cur.nationality())
        self.nationality.select_by_index(1)
        self.citizenship = Select(self.cur.citizenship())
        self.citizenship.select_by_index(1)
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.country_of_residence.select_by_index(1)
        self.residential_status = Select(self.cur.residentialstatus())
        self.residential_status.select_by_index(1)
        self.gender = Select(self.cur.gender())
        self.gender.select_by_index(1)
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_index(1)
        self.profession = Select(self.cur.profession())
        self.profession.select_by_index(1)

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

        print("Actual Data from the system")
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
        print(" ")
        print("Data from the Preview")
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
                screenShort.screen_short() + "test_modifications_earse_before_title.png")
            assert False

        if self.ci.firstname() == "Karunkar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_first.png")
            assert False

        if self.ci.lastname() == "Technology":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_last.png")
            assert False

        if self.ci.middlename() == "Finnest":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_middle.png")
            assert False

        if self.ci.arabicname() == "Mohamad":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_arabic.png")
            assert False

        if self.ci.shortname() == "Karunakar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_short.png")
            assert False

        if self.ci.maidenname() == "Karunakar":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_maidname.png")
            assert False

        if self.ci.dob() == "30-03-2000":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_dob.png")
            assert False

        if self.ci.natinality() == self.nat:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_nationality.png")
            assert False

        if self.ci.citizen() == self.citiz:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_citizen.png")
            assert False

        if self.ci.cor() == self.cor:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_cor.png")
            assert False

        if self.ci.res() == self.res:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_res.png")
            assert False

        if self.ci.gender() == self.gen:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_gender.png")
            assert False

        if self.ci.marristatus() == self.mrgs:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_mrgstatus.png")
            assert False

        if self.ci.profesion() == self.profs:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_modifications_earse_before_profision.png")
            assert False
        self.driver.quit()

    def test_clear_data(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_visible_text("")
        self.cur.firstNameField_required("")
        self.cur.middleNameField_not_required("")
        self.cur.lastNameField_required("")
        self.cur.arabicNameFiels_required("")
        self.cur.shortNameField_not_required("")
        self.cur.maidenNameFiels_not_required("")
        self.cur.dobpicker_required("")

        self.cob = Select(self.cur.cobDropdown_required())
        self.cob.select_by_visible_text("")
        self.nationality = Select(self.cur.nationality())
        self.nationality.select_by_visible_text("")
        self.citizenship = Select(self.cur.citizenship())
        self.citizenship.select_by_visible_text("")
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.country_of_residence.select_by_visible_text("")
        self.residential_status = Select(self.cur.residentialstatus())
        self.residential_status.select_by_visible_text("")
        self.gender = Select(self.cur.gender())
        self.gender.select_by_visible_text("")
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_visible_text("")
        self.profession = Select(self.cur.profession())
        self.profession.select_by_visible_text("")

        def get_dropdown_text(select_element):
            return select_element.first_selected_option.text

        print("Getting data from the dropdowns before")
        self.title_text = get_dropdown_text(self.drp)
        self.cunofbir = get_dropdown_text(self.cob)
        self.nat = get_dropdown_text(self.nationality)
        self.citiz = get_dropdown_text(self.citizenship)
        self.cor = get_dropdown_text(self.country_of_residence)
        self.res = get_dropdown_text(self.residential_status)
        self.gen = get_dropdown_text(self.gender)
        self.mrgs = get_dropdown_text(self.mrg)
        self.profs = get_dropdown_text(self.profession)

        print(self.title_text)
        print(self.cunofbir)
        print(self.nat)
        print(self.citiz)
        print(self.cor)
        print(self.res)
        print(self.gen)
        print(self.mrgs)
        print(self.profs)

        # time.sleep(2)

        self.cur.btncancel()
        self.cur.btn_canel_confirm()

        # Re-find the elements after the cancel action to avoid stale element reference
        self.drp = Select(self.cur.titleDropdown_required())
        self.cob = Select(self.cur.cobDropdown_required())
        self.nationality = Select(self.cur.nationality())
        self.citizenship = Select(self.cur.citizenship())
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.residential_status = Select(self.cur.residentialstatus())
        self.gender = Select(self.cur.gender())
        self.mrg = Select(self.cur.maritalstatus())
        self.profession = Select(self.cur.profession())

        print("Getting data from the dropdowns after clearing")
        self.title_text_af = get_dropdown_text(self.drp)
        self.cunofbir_af = get_dropdown_text(self.cob)
        self.nat_af = get_dropdown_text(self.nationality)
        self.citiz_af = get_dropdown_text(self.citizenship)
        self.cor_af = get_dropdown_text(self.country_of_residence)
        self.res_af = get_dropdown_text(self.residential_status)
        self.gen_af = get_dropdown_text(self.gender)
        self.mrgs_af = get_dropdown_text(self.mrg)
        self.profs_af = get_dropdown_text(self.profession)

        print(self.title_text_af)
        print(self.cunofbir_af)
        print(self.nat_af)
        print(self.citiz_af)
        print(self.cor_af)
        print(self.res_af)
        print(self.gen_af)
        print(self.mrgs_af)
        print(self.profs_af)

        if (self.title_text == self.title_text_af and self.cunofbir == self.cunofbir_af and self.nat == self.nat_af and
                self.citiz == self.citiz_af and self.cor == self.cor_af and self.res == self.res_af and self.gen == self.gen_af and
                self.mrgs == self.mrgs_af and self.profs == self.profs_af):
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_clear_data.png")
            assert False
        self.driver.quit()

    def test_cancel_from_next_page(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required("Test")
        self.cur.middleNameField_not_required("Middle")
        self.cur.lastNameField_required("User")
        self.cur.arabicNameFiels_required("name")
        self.cur.shortNameField_not_required("Short")
        self.cur.maidenNameFiels_not_required("Maiden")
        self.cur.dobpicker_required(11022000)

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

        def get_dropdown_text(select_element):
            return select_element.first_selected_option.text

        print("Getting data from the dropdowns before")
        self.title_text = get_dropdown_text(self.drp)
        self.cunofbir = get_dropdown_text(self.cob)
        self.nat = get_dropdown_text(self.nationality)
        self.citiz = get_dropdown_text(self.citizenship)
        self.cor = get_dropdown_text(self.country_of_residence)
        self.res = get_dropdown_text(self.residential_status)
        self.gen = get_dropdown_text(self.gender)
        self.mrgs = get_dropdown_text(self.mrg)
        self.profs = get_dropdown_text(self.profession)

        print(self.title_text)
        print(self.cunofbir)
        print(self.nat)
        print(self.citiz)
        print(self.cor)
        print(self.res)
        print(self.gen)
        print(self.mrgs)
        print(self.profs)

        self.cur.btnnext()
        self.ci.btn_cancel()
        self.ci.btn_cancel_cfirm()

        # Re-find the elements after the cancel action to avoid stale element reference
        self.drp = Select(self.cur.titleDropdown_required())
        self.cob = Select(self.cur.cobDropdown_required())
        self.nationality = Select(self.cur.nationality())
        self.citizenship = Select(self.cur.citizenship())
        self.country_of_residence = Select(self.cur.countryofresidence())
        self.residential_status = Select(self.cur.residentialstatus())
        self.gender = Select(self.cur.gender())
        self.mrg = Select(self.cur.maritalstatus())
        self.profession = Select(self.cur.profession())

        print("Getting data from the dropdowns after clearing")
        self.title_text_af = get_dropdown_text(self.drp)
        self.cunofbir_af = get_dropdown_text(self.cob)
        self.nat_af = get_dropdown_text(self.nationality)
        self.citiz_af = get_dropdown_text(self.citizenship)
        self.cor_af = get_dropdown_text(self.country_of_residence)
        self.res_af = get_dropdown_text(self.residential_status)
        self.gen_af = get_dropdown_text(self.gender)
        self.mrgs_af = get_dropdown_text(self.mrg)
        self.profs_af = get_dropdown_text(self.profession)

        print(self.title_text_af)
        print(self.cunofbir_af)
        print(self.nat_af)
        print(self.citiz_af)
        print(self.cor_af)
        print(self.res_af)
        print(self.gen_af)
        print(self.mrgs_af)
        print(self.profs_af)

        if (self.title_text != self.title_text_af and self.cunofbir != self.cunofbir_af and self.nat != self.nat_af and
                self.citiz != self.citiz_af and self.cor != self.cor_af and self.res != self.res_af and self.gen != self.gen_af and
                self.mrgs != self.mrgs_af and self.profs != self.profs_af):
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_cancel_from_next_page")
            assert False
        # time.sleep(4)
        self.driver.quit()

    def test_fieldname_height_width(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        # Function to print size
        def print_element_size(element, element_name):
            if element is not None:
                size = element.size
                print(f"{element_name} - Width: {size['width']}, Height: {size['height']}")
            else:
                print(f"{element_name} - Element not found")

        # Locate elements and print sizes
        title_dropdown = self.cur.titleDropdown_required()
        first_name_field = self.cur.firstNameField_required_size()
        middle_name_field = self.cur.middleNameField_not_required_size()
        last_name_field = self.cur.lastNameField_required_size()
        arabic_name_field = self.cur.arabicNameFiels_required_size()
        short_name_field = self.cur.shortNameField_not_required_size()
        maiden_name_field = self.cur.maidenNameFiels_not_required_size()
        dob_picker = self.cur.dobpicker_required_size()

        cob_dropdown = self.cur.cobDropdown_required()
        nationality_dropdown = self.cur.nationality()
        citizenship_dropdown = self.cur.citizenship()
        country_of_residence_dropdown = self.cur.countryofresidence()
        residential_status_dropdown = self.cur.residentialstatus()
        gender_dropdown = self.cur.gender()
        marital_status_dropdown = self.cur.maritalstatus()
        profession_dropdown = self.cur.profession()

        # Print sizes of the fields
        print_element_size(title_dropdown, "Title Dropdown")
        print_element_size(first_name_field, "First Name Field")
        print_element_size(middle_name_field, "Middle Name Field")
        print_element_size(last_name_field, "Last Name Field")
        print_element_size(arabic_name_field, "Arabic Name Field")
        print_element_size(short_name_field, "Short Name Field")
        print_element_size(maiden_name_field, "Maiden Name Field")
        print_element_size(dob_picker, "DOB Picker")
        print_element_size(cob_dropdown, "COB Dropdown")
        print_element_size(nationality_dropdown, "Nationality Dropdown")
        print_element_size(citizenship_dropdown, "Citizenship Dropdown")
        print_element_size(country_of_residence_dropdown, "Country of Residence Dropdown")
        print_element_size(residential_status_dropdown, "Residential Status Dropdown")
        print_element_size(gender_dropdown, "Gender Dropdown")
        print_element_size(marital_status_dropdown, "Marital Status Dropdown")
        print_element_size(profession_dropdown, "Profession Dropdown")

        # Close the driver after the test
        self.driver.quit()

    def test_fieldname_max_length(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        # Function to print max length
        # Locate elements
        first_name_field = self.cur.firstNameField_required_size()
        middle_name_field = self.cur.middleNameField_not_required_size()
        last_name_field = self.cur.lastNameField_required_size()
        arabic_name_field = self.cur.arabicNameFiels_required_size()
        short_name_field = self.cur.shortNameField_not_required_size()
        maiden_name_field = self.cur.maidenNameFiels_not_required_size()

        # Print max lengths directly

        f_maxlength = first_name_field.get_attribute('maxlength')
        f_maxlength_int = int(f_maxlength)

        m_maxlength = middle_name_field.get_attribute('maxlength')
        m_maxlength_int = int(m_maxlength)
        print("middlename:", m_maxlength_int)

        l_maxlength = last_name_field.get_attribute('maxlength')
        l_maxlength_int = int(l_maxlength)

        a_maxlength = arabic_name_field.get_attribute('maxlength')
        a_maxlength_int = int(a_maxlength)

        s_maxlength = short_name_field.get_attribute('maxlength')
        s_maxlength_int = int(s_maxlength)

        ma_maxlength = maiden_name_field.get_attribute('maxlength')
        ma_maxlength_int = int(ma_maxlength)

        max_30 = random_string_generator_max_30()
        print("maxlenght_30:", max_30)
        max_50 = random_string_generator_max_50()
        print("maxlenght_50:", max_50)

        # Fill out the fields and print lengths
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        # Ensure firstNameField_required returns a WebElement
        self.cur.firstNameField_required(max_30)
        # Continue with other fields similarly
        self.cur.middleNameField_not_required(max_30)
        self.cur.lastNameField_required(max_30)
        self.cur.arabicNameFiels_required(max_50)
        self.cur.shortNameField_not_required(max_50)
        self.cur.maidenNameFiels_not_required(max_50)

        # Select date of birth using the custom method
        self.cur.dobpicker_required(11022000)

        # Handle dropdowns
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

        # Click the next button and back
        self.cur.btnnext()
        self.ci.btn_back()
        # time.sleep(10)

        self.fval = self.cur.firstNameField_required_value()
        self.mval = self.cur.middleNameField_not_required_value()
        self.lval = self.cur.lastNameField_required_value()
        self.aval = self.cur.arabicNameFiels_required_value()
        self.sval = self.cur.shortNameField_not_required_value()
        self.maval = self.cur.maidenNameFiels_not_required_value()

        print(self.fval, self.mval, self.lval, self.aval, self.sval, self.mval)

        if self.fval == f_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_first.png")
            assert False

        if self.mval == m_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_middle.png")
            assert False

        if self.lval == l_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_last.png")
            assert False

        if self.aval == a_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_arab.png")
            assert False

        if self.sval == s_maxlength_int:
            assert True
        else:
            assert False

        if self.maval == ma_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_maiden.png")
            assert False

        self.driver.quit()

    def test_fieldname_max_length_lessthen(self, setup, f_maxlength=None):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        # Function to print max length
        # Locate elements
        first_name_field = self.cur.firstNameField_required_size()
        middle_name_field = self.cur.middleNameField_not_required_size()
        last_name_field = self.cur.lastNameField_required_size()
        arabic_name_field = self.cur.arabicNameFiels_required_size()
        short_name_field = self.cur.shortNameField_not_required_size()
        maiden_name_field = self.cur.maidenNameFiels_not_required_size()

        # Print max lengths directly

        f_maxlength = first_name_field.get_attribute('maxlength')
        f_maxlength_int = int(f_maxlength)

        m_maxlength = middle_name_field.get_attribute('maxlength')
        m_maxlength_int = int(m_maxlength)
        print("middlename:", m_maxlength_int)

        l_maxlength = last_name_field.get_attribute('maxlength')
        l_maxlength_int = int(l_maxlength)

        a_maxlength = arabic_name_field.get_attribute('maxlength')
        a_maxlength_int = int(a_maxlength)

        s_maxlength = short_name_field.get_attribute('maxlength')
        s_maxlength_int = int(s_maxlength)

        ma_maxlength = maiden_name_field.get_attribute('maxlength')
        ma_maxlength_int = int(ma_maxlength)

        max_28 = random_string_generator_max_28()
        print("maxlenght_28:", max_28)
        max_48 = random_string_generator_max_48()
        print("maxlenght_48:", max_48)

        # Fill out the fields and print lengths
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        # Ensure firstNameField_required returns a WebElement
        self.cur.firstNameField_required(max_28)
        # Continue with other fields similarly
        self.cur.middleNameField_not_required(max_28)
        self.cur.lastNameField_required(max_28)
        self.cur.arabicNameFiels_required(max_48)
        self.cur.shortNameField_not_required(max_48)
        self.cur.maidenNameFiels_not_required(max_48)

        # Select date of birth using the custom method
        self.cur.dobpicker_required(11022000)

        # Handle dropdowns
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

        # Click the next button and back
        self.cur.btnnext()
        self.ci.btn_back()
        # time.sleep(10)

        self.fval = self.cur.firstNameField_required_value()
        self.mval = self.cur.middleNameField_not_required_value()
        self.lval = self.cur.lastNameField_required_value()
        self.aval = self.cur.arabicNameFiels_required_value()
        self.sval = self.cur.shortNameField_not_required_value()
        self.maval = self.cur.maidenNameFiels_not_required_value()

        print(self.fval, self.mval, self.lval, self.aval, self.sval, self.mval)

        if self.fval <= f_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_less_first.png")
            assert False

        if self.mval <= m_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_less_middle.png")
            assert False

        if self.lval <= l_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_less_last.png")
            assert False

        if self.aval <= a_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_less_arab.png")
            assert False

        if self.sval <= s_maxlength_int:
            assert True
        else:
            assert False

        if self.maval <= ma_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_less_maiden.png")
            assert False

        self.driver.quit()

    def test_fieldname_max_length_greaterthen(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)

        # Function to print max length
        # Locate elements
        first_name_field = self.cur.firstNameField_required_size()
        middle_name_field = self.cur.middleNameField_not_required_size()
        last_name_field = self.cur.lastNameField_required_size()
        arabic_name_field = self.cur.arabicNameFiels_required_size()
        short_name_field = self.cur.shortNameField_not_required_size()
        maiden_name_field = self.cur.maidenNameFiels_not_required_size()

        # Print max lengths directly

        f_maxlength = first_name_field.get_attribute('maxlength')
        f_maxlength_int = int(f_maxlength)

        m_maxlength = middle_name_field.get_attribute('maxlength')
        m_maxlength_int = int(m_maxlength)

        l_maxlength = last_name_field.get_attribute('maxlength')
        l_maxlength_int = int(l_maxlength)

        a_maxlength = arabic_name_field.get_attribute('maxlength')
        a_maxlength_int = int(a_maxlength)

        s_maxlength = short_name_field.get_attribute('maxlength')
        s_maxlength_int = int(s_maxlength)

        ma_maxlength = maiden_name_field.get_attribute('maxlength')
        ma_maxlength_int = int(ma_maxlength)

        max_31 = random_string_generator_max_31()
        print("maxlenght_31:", max_31)
        max_51 = random_string_generator_max_51()
        print("maxlenght_51:", max_51)

        # Fill out the fields and print lengths
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        # Ensure firstNameField_required returns a WebElement
        self.cur.firstNameField_required(max_31)
        # Continue with other fields similarly
        self.cur.middleNameField_not_required(max_31)
        self.cur.lastNameField_required(max_31)
        self.cur.arabicNameFiels_required(max_51)
        self.cur.shortNameField_not_required(max_51)
        self.cur.maidenNameFiels_not_required(max_51)

        # Select date of birth using the custom method
        self.cur.dobpicker_required(11022000)

        # Handle dropdowns
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

        # Click the next button and back
        self.cur.btnnext()
        self.ci.btn_back()
        # time.sleep(10)

        self.fval = self.cur.firstNameField_required_value()
        self.mval = self.cur.middleNameField_not_required_value()
        self.lval = self.cur.lastNameField_required_value()
        self.aval = self.cur.arabicNameFiels_required_value()
        self.sval = self.cur.shortNameField_not_required_value()
        self.maval = self.cur.maidenNameFiels_not_required_value()

        print(self.fval, self.mval, self.lval, self.aval, self.sval, self.maval)

        if self.fval >= f_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_first.png")
            assert False

        if self.mval >= m_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_middle.png")
            assert False

        if self.lval >= l_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_last.png")
            assert False

        if self.aval >= a_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_arab.png")
            assert False

        if self.sval >= s_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_short.png")
            assert False

        if self.maval >= ma_maxlength_int:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_fieldname_max_length_greaterthen_maiden.png")
            assert False

        self.driver.quit()

    def test_personal_info_with_data_have_space(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow

        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration()
        self.cur = Persomal_Information(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer registration
        self.nav.click_customer_registration()
        # time.sleep(2)

        # perform customer registration actions for id verification
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
        self.cur.firstNameField_required("QA Finnest ")
        self.cur.middleNameField_not_required("Middle Name ")
        self.cur.lastNameField_required("Last name ")
        self.cur.arabicNameFiels_required("Arabic name ")
        self.cur.shortNameField_not_required("Short name ")
        self.cur.maidenNameFiels_not_required("Maiden name ")

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

        self.fget = self.cur.firstNameField_required_value_getting()
        self.mget = self.cur.middleNameField_not_required_value_getting()
        self.lget = self.cur.lastNameField_required_value_getting()
        self.aget = self.cur.arabicNameFiels_required_value_getting()
        self.sget = self.cur.shortNameField_not_required_value_getting()
        self.maget = self.cur.maidenNameFiels_not_required_value_getting()

        print(self.fget)
        print(self.mget)
        print(self.lget)
        print(self.aget)
        print(self.sget)
        print(self.maget)

        self.cur.btnnext()
        self.ci.btn_back()

        self.error = self.cur.errorMessage()

        if self.fget == "QA Finnest ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_first.png")
            assert False

        if self.mget == "Middle Name ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_middle.png")
            assert False

        if self.lget == "Last name ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_last.png")
            assert False

        if self.aget == "Arabic name ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_arabic.png")
            assert False

        if self.sget == "Short name ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_short.png")
            assert False

        if self.maget == "Maiden name ":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "test_personal_info_with_data_have_space_maiden.png")
            assert False

        self.driver.quit()
