from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details, Other_Information
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_ID_Details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self,setup):
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

        # click action for customer registration
        self.nav.click_customer_registration()
        # time.sleep(2)

        # assining the pageobjects
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)
        self.id = Id_details(self.driver)
        self.oi = Other_Information(self.driver)

        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # assign data in to the fields
        fname = "QA"
        mname = "Automation"
        lname = "Tester"
        arbname = "Khan"
        shname = "QA Automation"
        mainame = "Nayana"
        dob = 30032000

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        self.drp.select_by_index(1)
        self.cur.firstNameField_required(fname)
        self.cur.middleNameField_not_required(mname)
        self.cur.lastNameField_required(lname)
        self.cur.arabicNameFiels_required(arbname)
        self.cur.shortNameField_not_required(shname)
        self.cur.maidenNameFiels_not_required(mainame)

        # Select date of birth using the custom method
        self.cur.dobpicker_required(dob)
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
        self.residential_status.select_by_index(1)
        self.gender = Select(self.cur.gender())
        self.gender.select_by_index(2)
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_index(2)
        self.profession = Select(self.cur.profession())
        self.profession.select_by_index(2)
        time.sleep(2)

        self.cur.btnnext()

        fh_number = "4BH"
        hb_name = "Monlash"
        stre = "Main road"
        cit_dis = "Kochi"
        emi_sta = "Kerala"
        mob = "9505123743"
        email = "finnesttechnology@zooker.com"

        self.ci.field_fh_num_required(fh_number)
        self.ci.field_hb_name_required(hb_name)
        self.ci.field_street_required(stre)
        self.ci.field_city_dist_required(cit_dis)
        self.ci.field_emin_dist(emi_sta)
        # dropdowns
        self.con = Select(self.ci.drp_country_required())
        self.con.select_by_visible_text("India")
        self.mob = Select(self.ci.drp_mobile_required())
        self.mob.select_by_index(69)
        self.ci.field_mobile_required(mob)
        self.ci.field_email_required(email)

        self.ci.btn_next()

        # Assening the elements
        # ID Detaials
        id_type_drp = Select(self.id.id_type_field_req())
        place_of_id_iss = self.id.place_of_id_issue_field_req()
        id_num_field = self.id.id_number_field_req()
        date_of_id_issue = self.id.id_issue_date_dpick_req()
        date_of_id_expaire = self.id.id_expaire_date_dpick_req()
        place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
        passport_numb = self.id.passport_numb_field_req()
        passport_issue_date = self.id.passport_issue_date_dpick_req()
        passport_expi_date = self.id.passport_expi_date_dpick_req()

        # Dual Nation
        #
        nationality_drp = Select(self.id.nationality_drp_req_dual())
        place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
        passport_num_req = self.id.passport_num_req_dual()
        passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
        passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()

        # send data
        place_of_id_send = "Kochi"
        id_num_send = "5678999"
        date_of_id_issue_send = "30042004"
        date_of_id_expaire_send = "30042025"
        passport_numb_send = "KTYUOA9761"
        passport_issue_date_send = "30042010"
        passport_expi_date_send = "30052025"

        # Dual nation
        passport_num_req_send = "MYNATAXT"
        passport_issue_date_dual_send = "30042011"
        passport_expai_date_dual_send = "30052025"

        id_type_drp.select_by_index(1)
        place_of_id_iss.send_keys(place_of_id_send)
        id_num_field.send_keys(id_num_send)
        date_of_id_issue.send_keys(date_of_id_issue_send)
        date_of_id_expaire.send_keys(date_of_id_expaire_send)
        place_of_passport_isse_drp.select_by_index(1)
        passport_numb.send_keys(passport_numb_send)
        passport_issue_date.send_keys(passport_issue_date_send)
        passport_expi_date.send_keys(passport_expi_date_send)
        self.driver.implicitly_wait(10)
        #
        self.id.toggle()
        #
        nationality_drp.select_by_index(3)
        place_of_pass_issue.select_by_index(1)
        passport_num_req.send_keys(passport_num_req_send)
        passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
        passport_expai_date_dual.send_keys(passport_expai_date_dual_send)

        self.id.btn_next()

        if self.oi.btn_next.is_displayed():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "ID_test_sending_valid_data.png")
            assert False
        time.sleep(2)
        # Submit the form
        self.driver.quit()
