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

    # def test_sending_valid_data(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #
    #     # send data
    #     place_of_id_send = "Kochi"
    #     id_num_send = "5678999"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "KTYUOA9761"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "MYNATAXT"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if not self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_valid_data.png")
    #         assert False
    #     self.driver.quit()

    # def test_sending_spcialchar_data(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #     # send data
    #     place_of_id_send = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     id_num_send = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_spcialchar_data.png")
    #         assert True
    #     # time.sleep(5)
    #     self.driver.quit()

    # def test_sending_numbers_data(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #     # send data
    #     place_of_id_send = "1234567890"
    #     id_num_send = "1234567890"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "1234567890"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "1234567890"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_numbers_data.png")
    #         assert True
    #     # time.sleep(5)
    #     self.driver.quit()

    # def test_sending_onlychar_data(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #     # send data
    #     place_of_id_send = "qwertyuiop"
    #     id_num_send = "qwertyuiop"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "qwertyuiop"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "qwertyuiop"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_onlychar_data.png")
    #         assert True
    #     # time.sleep(5)
    #     self.driver.quit()

    # def test_sending_spchar_num_char_data(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #     # send data
    #     place_of_id_send = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     id_num_send = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_spchar_num_char_data.png")
    #         assert True
    #     # time.sleep(5)
    #     self.driver.quit()

    # def test_sending_data_have_spaces(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     id_type_drp = Select(self.id.id_type_field_req())
    #     place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     id_num_field = self.id.id_number_field_req()
    #     date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     passport_numb = self.id.passport_numb_field_req()
    #     passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #     # send data
    #     place_of_id_send = "abcd efgh"
    #     id_num_send = "12345 67890"
    #     date_of_id_issue_send = "30042004"
    #     date_of_id_expaire_send = "30042025"
    #     passport_numb_send = "123456 78901"
    #     passport_issue_date_send = "30042010"
    #     passport_expi_date_send = "30052025"
    #
    #     # Dual nation
    #     passport_num_req_send = "12345 6789"
    #     passport_issue_date_dual_send = "30042011"
    #     passport_expai_date_dual_send = "30052025"
    #
    #     id_type_drp.select_by_index(1)
    #     place_of_id_iss.send_keys(place_of_id_send)
    #     id_num_field.send_keys(id_num_send)
    #     date_of_id_issue.send_keys(date_of_id_issue_send)
    #     date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #     place_of_passport_isse_drp.select_by_index(1)
    #     passport_numb.send_keys(passport_numb_send)
    #     passport_issue_date.send_keys(passport_issue_date_send)
    #     passport_expi_date.send_keys(passport_expi_date_send)
    #     self.driver.implicitly_wait(2)
    #     #
    #     toggle = self.id.toggle()
    #     toggle.click()
    #
    #     time.sleep(2)
    #     #
    #     nationality_drp = Select(self.id.nationality_drp_req_dual())
    #     place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #     passport_num_req = self.id.passport_num_req_dual()
    #     passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #     passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #
    #     nationality_drp.select_by_index(3)
    #     place_of_pass_issue.select_by_index(2)
    #     passport_num_req.send_keys(passport_num_req_send)
    #     passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #     passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #     self.id.btn_next()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "ID_test_sending_data_have_spaces.png")
    #         assert True
    #     self.driver.quit()

    # def test_sending_bulk_data(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     # time.sleep(2)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #     # time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #
    #     # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
    #     # self.cu_status.select_by_index(1)
    #     # self.cur.idNoField_not_required("7")
    #     # self.cur.dateofexpiry_not_required(12102024)
    #     # self.cur.btnverify()
    #     # time.sleep(2)
    #
    #     # assign data in to the fields
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # perform personal information
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #
    #     # Select date of birth using the custom method
    #     self.cur.dobpicker_required(dob)
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
    #     self.residential_status.select_by_index(1)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #     time.sleep(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = "Kerala"
    #     mob = "9505123743"
    #     email = "finnesttechnology@zooker.com"
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("India")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #
    #     # Assening the elements
    #     # ID Detaials
    #     # id_type_drp = Select(self.id.id_type_field_req())
    #     # place_of_id_iss = self.id.place_of_id_issue_field_req()
    #     # id_num_field = self.id.id_number_field_req()
    #     # date_of_id_issue = self.id.id_issue_date_dpick_req()
    #     # date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #     # place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #     # passport_numb = self.id.passport_numb_field_req()
    #     # passport_issue_date = self.id.passport_issue_date_dpick_req()
    #     # passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #     # Dual Nation
    #     #
    #
    #     places_of_id = [
    #         "Kochi", "Mumbai", "Delhi", "Chennai", "Bangalore",
    #         "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Surat"
    #     ]
    #
    #     id_numbers = [
    #         "5678999", "1234567", "2345678", "3456789", "4567890",
    #         "6789012", "7890123", "8901234", "9012345", "0123456"
    #     ]
    #
    #     passport_numbers = [
    #         "KTYUOA9761", "ABCD1234", "XYZ9876", "PQR4567", "LMN7890",
    #         "MNOP1234", "QRST5678", "UVWX9012", "YZA3456", "BCD7890"
    #     ]
    #
    #     passport_num_dual = [
    #         "MYNATAXT", "OTHERS123", "DUAL9876", "SECONDARY1", "DUPLICATE1",
    #         "ADDL1234", "EXTRA5678", "NEWNUM9012", "SECOND7890", "SUPPL3456"
    #     ]
    #
    #     for i in range(len(places_of_id)):
    #         place_of_id_send = places_of_id[i]
    #         id_num_send = id_numbers[i]
    #         passport_numb_send = passport_numbers[i]
    #         passport_num_req_send = passport_num_dual[i]
    #
    #         # Static dates
    #         date_of_id_issue_send = "30042004"
    #         date_of_id_expaire_send = "30042025"
    #         passport_issue_date_send = "30042010"
    #         passport_expi_date_send = "30052025"
    #         passport_issue_date_dual_send = "30042011"
    #         passport_expai_date_dual_send = "30052025"
    #
    #         # Re-fetch elements in each iteration
    #         id_type_drp = Select(self.id.id_type_field_req())
    #         place_of_id_iss = self.id.place_of_id_issue_field_req()
    #         id_num_field = self.id.id_number_field_req()
    #         date_of_id_issue = self.id.id_issue_date_dpick_req()
    #         date_of_id_expaire = self.id.id_expaire_date_dpick_req()
    #         place_of_passport_isse_drp = Select(self.id.place_of_passport_isse_drp_req())
    #         passport_numb = self.id.passport_numb_field_req()
    #         passport_issue_date = self.id.passport_issue_date_dpick_req()
    #         passport_expi_date = self.id.passport_expi_date_dpick_req()
    #
    #         # Send data
    #         id_type_drp.select_by_index(1)
    #         place_of_id_iss.send_keys(place_of_id_send)
    #         id_num_field.send_keys(id_num_send)
    #         date_of_id_issue.send_keys(date_of_id_issue_send)
    #         date_of_id_expaire.send_keys(date_of_id_expaire_send)
    #         place_of_passport_isse_drp.select_by_index(1)
    #         passport_numb.send_keys(passport_numb_send)
    #         passport_issue_date.send_keys(passport_issue_date_send)
    #         passport_expi_date.send_keys(passport_expi_date_send)
    #
    #         self.driver.implicitly_wait(2)
    #
    #         # Click toggle only on the first iteration
    #         if i == 0:
    #             toggle = self.id.toggle()
    #             toggle.click()
    #
    #         time.sleep(2)
    #
    #         nationality_drp = Select(self.id.nationality_drp_req_dual())
    #         place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
    #         passport_num_req = self.id.passport_num_req_dual()
    #         passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
    #         passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()
    #
    #         nationality_drp.select_by_index(3)
    #         place_of_pass_issue.select_by_index(2)
    #         passport_num_req.send_keys(passport_num_req_send)
    #         passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
    #         passport_expai_date_dual.send_keys(passport_expai_date_dual_send)
    #
    #         self.error = self.cur.errorMessage()
    #
    #         if self.error == "Required":
    #             assert False
    #         else:
    #             self.driver.save_screenshot(screenShort.screen_short() + f"ID_test_sending_bulk_data_{i}.png")
    #             assert True
    #
    #         self.id.btn_next()
    #         self.oi.btn_back()
    #
    #         # Re-fetch the elements for clearing in each iteration
    #         place_of_id_iss = self.id.place_of_id_issue_field_req()
    #         id_num_field = self.id.id_number_field_req()
    #         passport_numb = self.id.passport_numb_field_req()
    #         passport_num_req = self.id.passport_num_req_dual()
    #
    #         # Clear the fields for the next iteration
    #         place_of_id_iss.clear()
    #         id_num_field.clear()
    #         passport_numb.clear()
    #         passport_num_req.clear()

    def test_validating_preview(self, setup):
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
        self.driver.implicitly_wait(2)
        #
        toggle = self.id.toggle()
        toggle.click()

        time.sleep(2)
        #
        nationality_drp = Select(self.id.nationality_drp_req_dual())
        place_of_pass_issue = Select(self.id.place_of_pass_issue_drp_req_dual())
        passport_num_req = self.id.passport_num_req_dual()
        passport_issue_date_dual = self.id.passport_issue_date_dpick_req_dual()
        passport_expai_date_dual = self.id.passport_expai_date_dpick_req_dual()

        nationality_drp.select_by_index(3)
        place_of_pass_issue.select_by_index(2)
        passport_num_req.send_keys(passport_num_req_send)
        passport_issue_date_dual.send_keys(passport_issue_date_dual_send)
        passport_expai_date_dual.send_keys(passport_expai_date_dual_send)

        # Getting data from the fields
        id_type_val = id_type_drp.first_selected_option.text
        place_of_id_iss_val = place_of_id_iss.get_attribute('value')
        id_num_val = id_num_field.get_attribute('value')
        date_of_id_issue_val = date_of_id_issue.get_attribute('value')
        date_of_id_exp_val = date_of_id_expaire.get_attribute('value')
        place_of_passport_isse_val = place_of_passport_isse_drp.first_selected_option.text
        passport_numb_val = passport_numb.get_attribute('value')
        passport_issue_date_val = passport_issue_date.get_attribute('value')
        passport_expi_date_val = passport_expi_date.get_attribute('value')

        print(f"ID Type: {id_type_val}\n"
              f"Place of ID Issuance: {place_of_id_iss_val}\n"
              f"ID Number: {id_num_val}\n"
              f"Date of ID Issue: {date_of_id_issue_val}\n"
              f"Date of ID Expiry: {date_of_id_exp_val}\n"  # Note: This seems to be the same as the issue date; check if this is correct
              f"Place of Passport Issuance: {place_of_passport_isse_val}\n"
              f"Passport Number: {passport_numb_val}\n"
              f"Passport Issue Date: {passport_issue_date_val}\n"
              f"Passport Expiry Date: {passport_expi_date_val}")

        self.id.btn_next()
        time.sleep(5)
        self.oi.click_id_details_drp()
        time.sleep(5)

        num_pre = self.oi.passport_num_pre()
        place_of_passport_issue_pre = self.oi.place_of_passport_issue_pre()
        passport_issue_date_pre = self.oi.passport_issue_date_pre()
        passport_expaire_date_pre = self.oi.passport_expaire_date_pre()
        id_type_pre = self.oi.id_type_pre()
        id_num_pre = self.oi.id_num_pre()
        place_of_id_issue_pre = self.oi.place_of_id_issue_pre()
        id_issue_date_pre = self.oi.id_issue_date_pre()
        id_expaire_date_pre = self.oi.id_expaire_date_pre()
        nationality_pre = self.oi.nationality_pre()
        place_of_passport_issue_dual_pre = self.oi.place_of_passport_issue_dual_pre()
        passport_num_dual_pre = self.oi.passport_num_dual_pre()
        passport_issue_date_dual_pre = self.oi.passport_issue_date_dual_pre()
        passport_expaire_date_dual_pre = self.oi.passport_expaire_date_dual_pre()

        print(f"""
        num_pre: {num_pre}
        place_of_passport_issue_pre: {place_of_passport_issue_pre}
        passport_issue_date_pre: {passport_issue_date_pre}
        passport_expaire_date_pre: {passport_expaire_date_pre}
        id_type_pre: {id_type_pre}
        id_num_pre: {id_num_pre}
        place_of_id_issue_pre: {place_of_id_issue_pre}
        id_issue_date_pre: {id_issue_date_pre}
        id_expaire_date_pre: {id_expaire_date_pre}
        nationality_pre: {nationality_pre}
        place_of_passport_issue_dual_pre: {place_of_passport_issue_dual_pre}
        passport_num_dual_pre: {passport_num_dual_pre}
        passport_issue_date_dual_pre: {passport_issue_date_dual_pre}
        passport_expaire_date_dual_pre: {passport_expaire_date_dual_pre}
        """)

        #
        # self.error = self.cur.errorMessage()
        #
        # if not self.error == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "ID_test_validating_preview.png")
        #     assert False
        self.driver.quit()






