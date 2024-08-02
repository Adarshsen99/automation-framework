from selenium.webdriver.support.wait import WebDriverWait

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from selenium.webdriver.support import expected_conditions as EC
import time
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Contact_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

#     def test_sending_valid_data(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#         time.sleep(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = "Kerala"
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#
#         val = self.id.visible_id()
#
#         if val == True:
#             assert True
#         else:
#             assert False
#
#     def test_sending_without_data(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#         time.sleep(2)
#
#         self.cur.btnnext()
#
#         self.ci.btn_next()
#
#         # val = self.id.visible_id()
#
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert False
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "test_sending_without_data.png")
#             assert True
#
#         self.driver.quit()
#
#     def test_sending_special_char(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         hb_name = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         stre = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         cit_dis = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         emi_sta = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         mob = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#         email = "!@#$%^&*()_+*/{}|]""-[:;',.?"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert False
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_sending_special_char.png")
#             assert True
#
#     def test_sending_numbers_char(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "1234567890"
#         hb_name = "1234567890"
#         stre = "1234567890"
#         cit_dis = "1234567890"
#         emi_sta = "1234567890"
#         mob = "1234567890"
#         email = "1234567890"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert False
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_sending_numbers_char.png")
#             assert True
#
#     def test_sending_char(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "abcdefghijk"
#         hb_name = "abcdefghijk"
#         stre = "abcdefghijk"
#         cit_dis = "abcdefghijk"
#         emi_sta = "abcdefghijk"
#         mob = "abcdefghijk"
#         email = "abcdefghijk"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert False
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_sending_char.png")
#             assert True
#
#     def test_sending_speci_char_num(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         hb_name = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         stre = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         cit_dis = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         emi_sta = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         mob = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#         email = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert False
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_sending_speci_char_num.png")
#             assert True
#
    # def test_sending_bulk_data(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #
    #     # assigning the page objects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #
    #     # assign data into the fields
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
    #
    #     self.cur.btnnext()
    #
    #     # Bulk data for personal information
    #     flat_house_numbers = ["102", "B-203", "305", "A-406", "110"]
    #     house_building_names = ["Green View Apartments", "Maple Heights", "Sunset Villas", "Cedar Residency",
    #                             "Oakwood Estates"]
    #     streets = ["Oak Street", "Pine Avenue", "Maple Boulevard", "Elm Street", "Birch Road"]
    #     city_districts = ["Springfield", "Albany", "Riverside", "Greenville", "Lakewood"]
    #     emirate_states = ["Illinois", "New York", "California", "Texas", "Florida"]
    #     mobiles = ["15551234567", "15552345678", "15553456789", "15554567890", "15555678901"]
    #     emails = ["john.doe@example.com", "jane.smith@example.com", "robert.brown@example.com",
    #               "linda.jones@example.com", "michael.johnson@example.com"]
    #
    #     for i in range(len(flat_house_numbers)):
    #         fh_number = flat_house_numbers[i]
    #         hb_name = house_building_names[i]
    #         stre = streets[i]
    #         cit_dis = city_districts[i]
    #         emi_sta = emirate_states[i]
    #         mob = mobiles[i]
    #         email = emails[i]
    #
    #         # Perform personal information
    #         self.ci.field_fh_num_required(fh_number)
    #         self.ci.field_hb_name_required(hb_name)
    #         self.ci.field_street_required(stre)
    #         self.ci.field_city_dist_required(cit_dis)
    #         self.ci.field_emin_dist(emi_sta)
    #         # dropdowns
    #         self.con = Select(self.ci.drp_country_required())
    #         self.con.select_by_visible_text("India")
    #         self.mob = Select(self.ci.drp_mobile_required())
    #         self.mob.select_by_index(69)
    #         self.ci.field_mobile_required(mob)
    #         self.ci.field_email_required(email)
    #
    #         self.error = self.cur.errorMessage()
    #
    #         if self.error == "Required":
    #             assert False
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + f"CI_test_sending_bulk_data_{i}.png")
    #             assert True
    #
    #         # Click the next button after each iteration
    #         self.ci.btn_next()
    #
    #         self.id.btn_back_id()
    #
    #         # Clear the fields for the next iteration
    #         self.ci.field_fh_num_required_clear()
    #         self.ci.field_hb_name_required_clear()
    #         self.ci.field_street_required_clear()
    #         self.ci.field_city_dist_required_clear()
    #         self.ci.field_emin_state_clear()
    #         self.ci.field_mobile_required_clear()
    #         self.ci.field_email_required_clear()
    #
    #     self.driver.quit()

#     def test_sending_required_fields(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = ""
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         val = self.id.visible_id()
#
#         if val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                             screenShort.screen_short() + "CI_test_sending_required_fields.png")
#             assert False
#
#         self.driver.quit()
#
#     def test_sending_not_required_fields(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         fh_number = ""
#         hb_name = ""
#         stre = ""
#         cit_dis = ""
#         emi_sta = "Dubai"
#         mob = ""
#         email = ""
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.error = self.cur.errorMessage()
#
#         if self.error == "Required":
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_sending_not_required_fields.png")
#             assert True
#
#         self.driver.quit()
#
#     def test_validation_preview_page(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = "Kerala"
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
# #       Getting data from the dropdowns
#         self.coun = self.con.first_selected_option.text
#
#         self.mobil = self.mob.first_selected_option
#         self.monil_pre = self.mobil.text
#
#         self.ci.btn_next()
#         self.id.drp_ci_pre()
#
#         print("Actual Data from the system")
#         print(self.coun)
#         print(self.monil_pre)
#
#
#         print(" ")
#         print("Data from the Preview")
#         print(self.id.fh_pre())
#         print(self.id.hb_pre())
#         print(self.id.stre_pre())
#         print(self.id.cidi_pre())
#         print(self.id.emist_pre())
#         print(self.id.con_pre())
#         print(self.id.mob_pre())
#         print(self.id.email_pre())
#
#         if fh_number == self.id.fh_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_fh.png")
#             assert False
#
#         if hb_name == self.id.hb_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_hb.png")
#             assert False
#
#         if stre == self.id.stre_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_stre.png")
#             assert False
#
#         if cit_dis == self.id.cidi_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_cit_dis.png")
#             assert False
#
#         if emi_sta == self.id.emist_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_emi_sta.png")
#             assert False
#
#         # if mob == self.id.mob_pre():
#         #     assert True
#         # else:
#         #     self.driver.save_screenshot(
#         #         screenShort.screen_short() + "CI_test_validation_preview_page_mob.png")
#         #     assert False
#
#         if email == self.id.email_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_preview_page_email.png")
#             assert False
#
#     def test_validating_max_len(self, setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#
#         # Login actions
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         self.lp.clickLogin()
#
#         # Navigation actions
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         self.nav.click_customer_registration()
#
#         # Assigning page objects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # Personal information data
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#         # Fill personal information fields
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#         self.cur.dobpicker_required(dob)
#
#         # Dropdown selections
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         def get_max_length(element):
#             if element is not None:
#                 return element.get_attribute('maxlength')
#             return None
#
#         # Fetching elements
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         stree_elem = self.ci.field_street_required_val()
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         emin_elem = self.ci.field_emin_dist_val()
#         mob_elem = self.ci.field_mobile_required_val()
#         email_elem = self.ci.field_email_required_val()
#
#         # Get and print max lengths
#         fh_len_max = get_max_length(fh_len_elem)
#         fh_len_max_int = int(fh_len_max)
#         print(f"Max length for flat/house number: {type(fh_len_max_int)}")
#
#         hb_len_max = int(get_max_length(hb_len_elem))
#         print(f"Max length for house/building name: {hb_len_max}")
#
#         stree_max = int(get_max_length(stree_elem))
#         print(f"Max length for street: {stree_max}")
#
#         ci_di_max = int(get_max_length(ci_di_elem))
#         print(f"Max length for city/district: {ci_di_max}")
#
#         emin_max = int(get_max_length(emin_elem))
#         print(f"Max length for emirate/state: {emin_max}")
#
#         mob_max = int(get_max_length(mob_elem))
#         print(f"Max length for mobile: {mob_max}")
#
#         email_max = int(get_max_length(email_elem))
#         print(f"Max length for email: {email_max}")
#
#         email = generate_random_email()
#         print("email:",email)
#         num = random_string_generator_numbers()
#         print("numbers", num)
#         max_20 = random_string_generator_max_20()
#         print("maxlenght_20:", max_20)
#         max_30 = random_string_generator_max_30()
#         print("maxlenght_30:", max_30)
#         max_50 = random_string_generator_max_50()
#         print("maxlenght_50:", max_50)
#
#         fh_number = max_50
#         hb_name = max_50
#         stre = max_50
#         cit_dis = max_30
#         emi_sta = max_20
#         mob_val = num
#         email_val = email
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#
#         # Dropdown selections
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob_val)
#         self.ci.field_email_required(email_val)
#
#         fh_val = fh_len_elem.get_attribute('value')
#         fh_val_len = len(fh_val)
#         print("fhvalue", type(fh_val_len))
#         hb_val = hb_len_elem.get_attribute('value')
#         hb_val_len = len(hb_val)
#         print("hbval:", hb_val_len)
#         stree_val = stree_elem.get_attribute('value')
#         stree_val_len = len(stree_val)
#         print("stree:", stree_val_len)
#         cidi_val = ci_di_elem.get_attribute('value')
#         cidi_val_len = len(cidi_val)
#         print("cidi_val:", cidi_val_len)
#         emin_val = emin_elem.get_attribute('value')
#         emin_val_len =len(emin_val)
#         print("emin_val:", emin_val_len)
#         mob_val = mob_elem.get_attribute('value')
#         mob_val_len = len(mob_val)
#         print("mob_val",mob_val_len)
#         email_val = email_elem.get_attribute('value')
#         email_val_len = len(email_val)
#         print("email_val:", email_val_len)
#
#         self.ci.btn_next()
#         # time.sleep(4)
#
#         val = self.id.visible_id()
#         print(val)
#
#         if fh_val_len == fh_len_max_int and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                             screenShort.screen_short() + "CI_test_validating_max_len_fh.png")
#             assert False
#
#         if hb_val_len == hb_len_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_hb.png")
#             assert False
#
#         if stree_val_len == stree_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_stre.png")
#             assert False
#
#         if cidi_val_len == ci_di_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_cidi.png")
#             assert False
#
#         if emin_val_len == emin_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_emin.png")
#             assert False
#
#         if mob_val_len == mob_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_mob.png")
#             assert False
#
#         if email_val_len == email_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_max_len_emai.png")
#             assert False
#
#         self.driver.quit()
#
#     def test_validating_lessthen_max_len(self, setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#
#         # Login actions
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         self.lp.clickLogin()
#
#         # Navigation actions
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         self.nav.click_customer_registration()
#
#         # Assigning page objects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # Personal information data
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#         # Fill personal information fields
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#         self.cur.dobpicker_required(dob)
#
#         # Dropdown selections
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         # def get_max_length(element):
#         #     if element is not None:
#         #         return element.get_attribute('maxlength')
#         #     return None
#
#         # Fetching elements
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         stree_elem = self.ci.field_street_required_val()
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         emin_elem = self.ci.field_emin_dist_val()
#         mob_elem = self.ci.field_mobile_required_val()
#         email_elem = self.ci.field_email_required_val()
#
#         # Get and print max lengths
#         fh_len_max = fh_len_elem.get_attribute('maxlength')
#         fh_len_max_int = int(fh_len_max)
#         print(f"Max length for flat/house number: {fh_len_max_int}")
#
#         hb_len_max = int(hb_len_elem.get_attribute('maxlength'))
#         print(f"Max length for house/building name: {hb_len_max}")
#
#         stree_max = int(stree_elem.get_attribute('maxlength'))
#         print(f"Max length for street: {stree_max}")
#
#         ci_di_max = int(ci_di_elem.get_attribute('maxlength'))
#         print(f"Max length for city/district: {ci_di_max}")
#
#         emin_max = int(emin_elem.get_attribute('maxlength'))
#         print(f"Max length for emirate/state: {emin_max}")
#
#         mob_max = int(mob_elem.get_attribute('maxlength'))
#         print(f"Max length for mobile: {mob_max}")
#
#         email_max = int(email_elem.get_attribute('maxlength'))
#         print(f"Max length for email: {email_max}")
#
#         email = generate_random_email_lessthen_45()
#         print("email:",email)
#         num = random_string_generator_numbers_max_10()
#         print("numbers", num)
#         max_18 = random_string_generator_max_18()
#         print("maxlenght_20:", max_18)
#         max_28 = random_string_generator_max_28()
#         print("maxlenght_30:", max_28)
#         max_48 = random_string_generator_max_48()
#         print("maxlenght_50:", max_48)
#         #
#         fh_number = max_48
#         hb_name = max_48
#         stre = max_48
#         cit_dis = max_28
#         emi_sta = max_18
#         mob_val = num
#         email_val = email
#         #
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#
#         # Dropdown selections
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob_val)
#         self.ci.field_email_required(email_val)
#
#         fh_val = fh_len_elem.get_attribute('value')
#         fh_val_len = len(fh_val)
#         print("fhvalue", type(fh_val_len))
#         hb_val = hb_len_elem.get_attribute('value')
#         hb_val_len = len(hb_val)
#         print("hbval:", hb_val_len)
#         stree_val = stree_elem.get_attribute('value')
#         stree_val_len = len(stree_val)
#         print("stree:", stree_val_len)
#         cidi_val = ci_di_elem.get_attribute('value')
#         cidi_val_len = len(cidi_val)
#         print("cidi_val:", cidi_val_len)
#         emin_val = emin_elem.get_attribute('value')
#         emin_val_len =len(emin_val)
#         print("emin_val:", emin_val_len)
#         mob_val = mob_elem.get_attribute('value')
#         mob_val_len = len(mob_val)
#         print("mob_val",mob_val_len)
#         email_val = email_elem.get_attribute('value')
#         email_val_len = len(email_val)
#         print("email_val:", email_val_len)
#
#         self.ci.btn_next()
#         # time.sleep(4)
#         #
#         val = self.id.visible_id()
#         print(val)
#
#         if fh_val_len <= fh_len_max_int and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_fh.png")
#             assert False
#
#         if hb_val_len < hb_len_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_hb.png")
#             assert False
#
#         if stree_val_len < stree_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_stre.png")
#             assert False
#
#         if cidi_val_len < ci_di_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_cidi.png")
#             assert False
#         if emin_val_len < emin_max and val == True:
#
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_emin.png")
#             assert False
#
#         if mob_val_len < mob_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_mob.png")
#             assert False
#
#         if email_val_len < email_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_lessthen_max_len_emai.png")
#             assert False
#
#         self.driver.quit()
#
#     def test_validating_greaterthen_max_len(self, setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#
#         # Login actions
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         self.lp.clickLogin()
#
#         # Navigation actions
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         self.nav.click_customer_registration()
#
#         # Assigning page objects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # Personal information data
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#         # Fill personal information fields
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#         self.cur.dobpicker_required(dob)
#
#         # Dropdown selections
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#
#         # Fetching elements
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         stree_elem = self.ci.field_street_required_val()
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         emin_elem = self.ci.field_emin_dist_val()
#         mob_elem = self.ci.field_mobile_required_val()
#         email_elem = self.ci.field_email_required_val()
#
#         # Get and print max lengths
#         fh_len_max = fh_len_elem.get_attribute('maxlength')
#         fh_len_max_int = int(fh_len_max)
#         print(f"Max length for flat/house number: {fh_len_max_int}")
#
#         hb_len_max = int(hb_len_elem.get_attribute('maxlength'))
#         print(f"Max length for house/building name: {hb_len_max}")
#
#         stree_max = int(stree_elem.get_attribute('maxlength'))
#         print(f"Max length for street: {stree_max}")
#
#         ci_di_max = int(ci_di_elem.get_attribute('maxlength'))
#         print(f"Max length for city/district: {ci_di_max}")
#
#         emin_max = int(emin_elem.get_attribute('maxlength'))
#         print(f"Max length for emirate/state: {emin_max}")
#
#         mob_max = int(mob_elem.get_attribute('maxlength'))
#         print(f"Max length for mobile: {mob_max}")
#
#         email_max = int(email_elem.get_attribute('maxlength'))
#         print(f"Max length for email: {email_max}")
#
#         email = generate_random_email_lessthen_52()
#         print("email:",email)
#         num = random_string_generator_numbers_18()
#         print("numbers", num)
#         max_22 = random_string_generator_max_22()
#         print("maxlenght_20:", max_22)
#         max_32 = random_string_generator_max_32()
#         print("maxlenght_30:", max_32)
#         max_52 = random_string_generator_max_52()
#         print("maxlenght_50:", max_52)
#         #
#         fh_number = max_52
#         hb_name = max_52
#         stre = max_52
#         cit_dis = max_32
#         emi_sta = max_22
#         mob_val = num
#         email_val = email
#         #
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#
#         # Dropdown selections
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob_val)
#         self.ci.field_email_required(email_val)
#
#         fh_val = fh_len_elem.get_attribute('value')
#         fh_val_len = len(fh_val)
#         print("fhvalue", type(fh_val_len))
#         hb_val = hb_len_elem.get_attribute('value')
#         hb_val_len = len(hb_val)
#         print("hbval:", hb_val_len)
#         stree_val = stree_elem.get_attribute('value')
#         stree_val_len = len(stree_val)
#         print("stree:", stree_val_len)
#         cidi_val = ci_di_elem.get_attribute('value')
#         cidi_val_len = len(cidi_val)
#         print("cidi_val:", cidi_val_len)
#         emin_val = emin_elem.get_attribute('value')
#         emin_val_len =len(emin_val)
#         print("emin_val:", emin_val_len)
#         mob_val = mob_elem.get_attribute('value')
#         mob_val_len = len(mob_val)
#         print("mob_val",mob_val_len)
#         email_val = email_elem.get_attribute('value')
#         email_val_len = len(email_val)
#         print("email_val:", email_val_len)
#
#         self.ci.btn_next()
#         # time.sleep(4)
#         #
#         val = self.id.visible_id()
#         print(val)
#
#         if fh_val_len == fh_len_max_int and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_fh.png")
#             assert False
#
#         if hb_val_len == hb_len_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_hb.png")
#             assert False
#
#         if stree_val_len == stree_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_stre.png")
#             assert False
#
#         if cidi_val_len == ci_di_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_cidi.png")
#             assert False
#         if emin_val_len == emin_max and val == True:
#
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_emin.png")
#             assert False
#
#         if mob_val_len == mob_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_mob.png")
#             assert False
#
#         if email_val_len == email_max and val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_emai.png")
#             assert False
#
#         self.driver.quit()
#
#     def test_validating_cancel(self, setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#         time.sleep(2)
#
#         def get_dropdown_text(select_element):
#             return select_element.first_selected_option.text
#
#         print("Getting data from the dropdowns before personal info")
#         self.title_text = get_dropdown_text(self.drp)
#         self.cunofbir = get_dropdown_text(self.cob)
#         self.nat = get_dropdown_text(self.nationality)
#         self.citiz = get_dropdown_text(self.citizenship)
#         self.cor = get_dropdown_text(self.country_of_residence)
#         self.res = get_dropdown_text(self.residential_status)
#         self.gen = get_dropdown_text(self.gender)
#         self.mrgs = get_dropdown_text(self.mrg)
#         self.profs = get_dropdown_text(self.profession)
#
#         print(self.title_text)
#         print(self.cunofbir)
#         print(self.nat)
#         print(self.citiz)
#         print(self.cor)
#         print(self.res)
#         print(self.gen)
#         print(self.mrgs)
#         print(self.profs)
#
#         self.cur.btnnext()
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = "Kerala"
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(1)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         stree_elem = self.ci.field_street_required_val()
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         emin_elem = self.ci.field_emin_dist_val()
#         mob_elem = self.ci.field_mobile_required_val()
#         email_elem = self.ci.field_email_required_val()
#
#         print("getting data for contact info before clear")
#     #       Getting data from
#         self.coun = self.con.first_selected_option.text
#         print("contry:",self.coun)
#
#         self.mobil = self.mob.first_selected_option
#         self.monil_pre = self.mobil.text
#         print("monile:",self.monil_pre)
#
#         fh_val = fh_len_elem.get_attribute('value')
#         print("fhvalue", fh_val)
#
#         hb_val = hb_len_elem.get_attribute('value')
#         print("hbval:", hb_val)
#
#         stree_val = stree_elem.get_attribute('value')
#         print("stree:", stree_val)
#
#         cidi_val = ci_di_elem.get_attribute('value')
#         print("cidi_val:", cidi_val)
#
#         emin_val = emin_elem.get_attribute('value')
#         print("emin_val:", emin_val)
#
#         mob_val = mob_elem.get_attribute('value')
#         print("mob_val", mob_val)
#
#         email_val = email_elem.get_attribute('value')
#         print("email_val:", email_val)
#
#         self.ci.btn_cancel()
#         self.ci.btn_cancel_cfirm()
#
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.nationality = Select(self.cur.nationality())
#         self.citizenship = Select(self.cur.citizenship())
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.gender = Select(self.cur.gender())
#         self.mrg = Select(self.cur.maritalstatus())
#         self.profession = Select(self.cur.profession())
#
#         print("Getting data from the dropdowns after clearing person info")
#         self.title_text_af = get_dropdown_text(self.drp)
#         self.cunofbir_af = get_dropdown_text(self.cob)
#         self.nat_af = get_dropdown_text(self.nationality)
#         self.citiz_af = get_dropdown_text(self.citizenship)
#         self.cor_af = get_dropdown_text(self.country_of_residence)
#         self.res_af = get_dropdown_text(self.residential_status)
#         self.gen_af = get_dropdown_text(self.gender)
#         self.mrgs_af = get_dropdown_text(self.mrg)
#         self.profs_af = get_dropdown_text(self.profession)
#
#         print(self.title_text_af)
#         print(self.cunofbir_af)
#         print(self.nat_af)
#         print(self.citiz_af)
#         print(self.cor_af)
#         print(self.res_af)
#         print(self.gen_af)
#         print(self.mrgs_af)
#         print(self.profs_af)
#
#         if (self.title_text != self.title_text_af and self.cunofbir != self.cunofbir_af and self.nat != self.nat_af and
#                 self.citiz != self.citiz_af and self.cor != self.cor_af and self.res != self.res_af and self.gen != self.gen_af and
#                 self.mrgs != self.mrgs_af and self.profs != self.profs_af):
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_cancel_PI.png")
#             assert False
#
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#         time.sleep(5)
#
#         print("getting data for contact info after clear")
#
#         # After clearing the form, reinitialize the required elements
#         self.con = Select(self.ci.drp_country_required())
#         self.mob = Select(self.ci.drp_mobile_required())
#
#         # Continue with the data extraction
#         print("Getting data for contact info after clear")
#         self.coun_cl = self.con.first_selected_option.text
#         self.monil_pre_cl = self.mob.first_selected_option.text
#
#         print("Country after clear:", self.coun_cl)
#         print("Mobile after clear:", self.monil_pre_cl)
#
#         fh_val_cl = self.ci.field_fh_num_required_val().get_attribute('value')
#         hb_val_cl = self.ci.field_hb_name_required_val().get_attribute('value')
#         stree_val_cl = self.ci.field_street_required_val().get_attribute('value')
#         cidi_val_cl = self.ci.field_city_dist_required_val().get_attribute('value')
#         emin_val_cl = self.ci.field_emin_dist_val().get_attribute('value')
#         mob_val_cl = self.ci.field_mobile_required_val().get_attribute('value')
#         email_val_cl = self.ci.field_email_required_val().get_attribute('value')
#
#         print("FH Number after clear:", fh_val_cl)
#         print("House/Building Name after clear:", hb_val_cl)
#         print("Street after clear:", stree_val_cl)
#         print("City/District after clear:", cidi_val_cl)
#         print("Emirate/State after clear:", emin_val_cl)
#         print("Mobile after clear:", mob_val_cl)
#         print("Email after clear:", email_val_cl)
#         #
#         if (self.coun != self.coun_cl and self.monil_pre != self.monil_pre_cl and fh_val != fh_val_cl and hb_val != hb_val_cl and stree_val != stree_val_cl
#             and cidi_val != cidi_val_cl and emin_val != emin_val_cl and mob_val != mob_val_cl and email_val != email_val_cl):
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validating_cancel_PI.png")
#             assert False
#
#         self.driver.quit()
#
#     def test_validation_modification_page(self, setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = "30032000"
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = "Kerala"
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#         self.id.btn_back_id()
#         time.sleep(5)
#
#         fh_number = "4BH"
#         hb_name = "Monlash"
#         stre = "Main road"
#         cit_dis = "Kochi"
#         emi_sta = "Kerala"
#         mob = "9505123743"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_index(3)
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#
#         self.ci.btn_next()
#         self.id.drp_ci_pre()
#
#         #       Getting data from the dropdowns
#         self.coun = self.con.first_selected_option.text
#
#         self.mobil = self.mob.first_selected_option
#         self.monil_pre = self.mobil.text
#
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         stree_elem = self.ci.field_street_required_val()
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         emin_elem = self.ci.field_emin_dist_val()
#         mob_elem = self.ci.field_mobile_required_val()
#         email_elem = self.ci.field_email_required_val()
#
#         print("Actual Data from the system")
#         print(self.coun)
#         print(self.monil_pre)
#
#         print("getting data for contact info before clear")
#         #       Getting data from
#         self.coun = self.con.first_selected_option.text
#         print("contry:", self.coun)
#
#         self.mobil = self.mob.first_selected_option
#         self.monil_pre = self.mobil.text
#         print("monile:", self.monil_pre)
#
#         fh_val = fh_len_elem.get_attribute('value')
#         print("fhvalue", fh_val)
#
#         hb_val = hb_len_elem.get_attribute('value')
#         print("hbval:", hb_val)
#
#         stree_val = stree_elem.get_attribute('value')
#         print("stree:", stree_val)
#
#         cidi_val = ci_di_elem.get_attribute('value')
#         print("cidi_val:", cidi_val)
#
#         emin_val = emin_elem.get_attribute('value')
#         print("emin_val:", emin_val)
#
#         mob_val = mob_elem.get_attribute('value')
#         print("mob_val", mob_val)
#
#         email_val = email_elem.get_attribute('value')
#         print("email_val:", email_val)
#
#
#         print(" ")
#         print("Data from the Preview")
#         print(self.id.fh_pre())
#         print(self.id.hb_pre())
#         print(self.id.stre_pre())
#         print(self.id.cidi_pre())
#         print(self.id.emist_pre())
#         print(self.id.con_pre())
#         print(self.id.mob_pre())
#         print(self.id.email_pre())
#
#         if fh_val == self.id.fh_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_fh.png")
#             assert False
#
#         if hb_val == self.id.hb_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_hb.png")
#             assert False
#
#         if stree_val == self.id.stre_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_stre.png")
#             assert False
#
#         if cidi_val == self.id.cidi_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_dis.png")
#             assert False
#
#         if emin_val == self.id.emist_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_sta.png")
#             assert False
#
#         # if mob == self.id.mob_pre():
#         #     assert True
#         # else:
#         #     self.driver.save_screenshot(
#         #         screenShort.screen_short() + "CI_test_validation_modification_page_mob.png")
#         #     assert False
#
#         if email_val == self.id.email_pre():
#             assert True
#         else:
#             self.driver.save_screenshot(
#                 screenShort.screen_short() + "CI_test_validation_modification_page_email.png")
#             assert False
#
#     def test_getting_fieldsize(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = "30032000"
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#
#         self.cur.btnnext()
#
#         fh_len_elem = self.ci.field_fh_num_required_val()
#         print("fh_len_elem:",fh_len_elem.size)
#         hb_len_elem = self.ci.field_hb_name_required_val()
#         print("hb_len_elem:",hb_len_elem.size)
#         stree_elem = self.ci.field_street_required_val()
#         print("stree_elem:",stree_elem.size)
#         ci_di_elem = self.ci.field_city_dist_required_val()
#         print("ci_di_elem:",ci_di_elem.size)
#         emin_elem = self.ci.field_emin_dist_val()
#         print("emin_elem:",emin_elem.size)
#         mob_elem = self.ci.field_mobile_required_val()
#         print("mob_elem:",mob_elem.size)
#         email_elem = self.ci.field_email_required_val()
#         print("email_elem:",email_elem.size)
#         con = self.ci.drp_country_required()
#         print("cob:",con.size)
#         mob = self.ci.drp_mobile_required()
#         print("mob:",mob.size)
#         self.driver.quit()
#
#     def test_sending_data_havespaces(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.uname)
#         self.lp.setPassword(self.upass)
#         # time.sleep(2)
#         self.lp.clickLogin()
#         # time.sleep(2)
#
#         # click action for nav bar arrow
#         self.nav = Navigation_Page(self.driver)
#         self.nav.click_navbar()
#         # time.sleep(2)
#
#         # click action for customer registration
#         self.nav.click_customer_registration()
#         # time.sleep(2)
#
#         # assining the pageobjects
#         self.cur = Persomal_Information(self.driver)
#         self.ci = Contact_Information(self.driver)
#         self.id = Id_details(self.driver)
#
#
#         # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
#         # self.cu_status.select_by_index(1)
#         # self.cur.idNoField_not_required("7")
#         # self.cur.dateofexpiry_not_required(12102024)
#         # self.cur.btnverify()
#         # time.sleep(2)
#
#         # assign data in to the fields
#         fname = "QA"
#         mname = "Automation"
#         lname = "Tester"
#         arbname = "Khan"
#         shname = "QA Automation"
#         mainame = "Nayana"
#         dob = 30032000
#
#
#         # perform personal information
#         self.drp = Select(self.cur.titleDropdown_required())
#         self.drp.select_by_index(1)
#         self.cur.firstNameField_required(fname)
#         self.cur.middleNameField_not_required(mname)
#         self.cur.lastNameField_required(lname)
#         self.cur.arabicNameFiels_required(arbname)
#         self.cur.shortNameField_not_required(shname)
#         self.cur.maidenNameFiels_not_required(mainame)
#
#         # Select date of birth using the custom method
#         self.cur.dobpicker_required(dob)
#         # dropdowns
#         self.cob = Select(self.cur.cobDropdown_required())
#         self.cob.select_by_index(2)
#         self.nationality = Select(self.cur.nationality())
#         self.nationality.select_by_index(2)
#         self.citizenship = Select(self.cur.citizenship())
#         self.citizenship.select_by_index(2)
#         self.country_of_residence = Select(self.cur.countryofresidence())
#         self.country_of_residence.select_by_index(2)
#         self.residential_status = Select(self.cur.residentialstatus())
#         self.residential_status.select_by_index(1)
#         self.gender = Select(self.cur.gender())
#         self.gender.select_by_index(2)
#         self.mrg = Select(self.cur.maritalstatus())
#         self.mrg.select_by_index(2)
#         self.profession = Select(self.cur.profession())
#         self.profession.select_by_index(2)
#         time.sleep(2)
#
#         self.cur.btnnext()
#
#
#         fh_number = "4BH BKM"
#         hb_name = "Monlash Building"
#         stre = "Main road"
#         cit_dis = "Kochi Kerala"
#         emi_sta = "Kerala Kochi"
#         mob = "9505123743 34"
#         email = "finnesttechnology@zooker.com"
#
#         self.ci.field_fh_num_required(fh_number)
#         self.ci.field_hb_name_required(hb_name)
#         self.ci.field_street_required(stre)
#         self.ci.field_city_dist_required(cit_dis)
#         self.ci.field_emin_dist(emi_sta)
#         # dropdowns
#         self.con = Select(self.ci.drp_country_required())
#         self.con.select_by_visible_text("India")
#         self.mob = Select(self.ci.drp_mobile_required())
#         self.mob.select_by_index(69)
#         self.ci.field_mobile_required(mob)
#         self.ci.field_email_required(email)
#
#         self.ci.btn_next()
#
#         val = self.id.visible_id()
#
#         if val == True:
#             assert True
#         else:
#             self.driver.save_screenshot(
#                         screenShort.screen_short() + "CI_test_sending_data_havespaces.png")
#             assert False

    # def test_printing_text_drps(self, setup):
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
    #     con = Select(self.ci.drp_country_required())
    #     options = con.options
    #     print(f"Number of options in the dropdown: {len(options)}")
    #
    #     mob = Select(self.ci.drp_mobile_required())
    #     options = mob.options
    #     # Print the number of options
    #     print(f"Number of options in the dropdown: {len(options)}")

# // ---------------------------Non Resident-------------------------------------//

    # def test_sending_valid_data_nonres(self, setup):
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
        # #Non resident
        # fh_number_non = "4BH"
        # hb_name_non = "Monlash"
        # stre_non = "Main road"
        # cit_dis_non = "Kochi"
        # emi_sta_non = "Kerala"
        # visa_num_non = "BVUXP1033V"
        # visa_issue_non = "04052004"
        # visa_exp_non = "04062014"
        # remarks = "No remarks"
        #
        # self.ci.non_field_fh_num_required(fh_number_non)
        # self.ci.non_field_hb_name_required(hb_name_non)
        # self.ci.non_field_street_required(stre_non)
        # self.ci.non_field_city_dist_required(cit_dis_non)
        # self.ci.non_field_emin_dist(emi_sta_non)
        # self.non_coun = Select(self.ci.non_drp_country_required())
        # self.non_coun.select_by_index(6)
        # self.non_visa = Select(self.ci.non_residen_visa_type_drp())
        # self.non_visa.select_by_index(1)
        # self.ci.non_residen_visa_number(visa_num_non)
        # self.ci.non_residen_visa_issu_date(visa_issue_non)
        # self.ci.non_residen_visa_expair_date(visa_exp_non)
        # self.ci.remarks(remarks)
    #
    #     # time.sleep(4)
    #     self.ci.btn_next()
    #
    #     val = self.id.visible_id()
    #
    #     if val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "test_sending_valid_data_nonres.png")
    #         assert False

    # def test_sending_without_data_non_res(self, setup):
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
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.5
    #
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #
    #     time.sleep(5)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_without_data_non_res.png")
    #         assert True
    #
    #     self.driver.quit()
    #
    # def test_sending_special_char_non(self, setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     hb_name = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     stre = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     cit_dis = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     emi_sta = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     mob = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     email = "!@#$%^&*()_+*/{}|]""-[:;',.?"
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
    #     # Non resident
    #     fh_number_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     hb_name_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     stre_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     cit_dis_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     emi_sta_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     visa_num_non = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #     visa_issue_non = "04052004"
    #     visa_exp_non = "04062014"
    #     remarks = "!@#$%^&*()_+*/{}|]""-[:;',.?"
    #
    #     self.ci.non_field_fh_num_required(fh_number_non)
    #     self.ci.non_field_hb_name_required(hb_name_non)
    #     self.ci.non_field_street_required(stre_non)
    #     self.ci.non_field_city_dist_required(cit_dis_non)
    #     self.ci.non_field_emin_dist(emi_sta_non)
    #     self.non_coun = Select(self.ci.non_drp_country_required())
    #     self.non_coun.select_by_index(6)
    #     self.non_visa = Select(self.ci.non_residen_visa_type_drp())
    #     self.non_visa.select_by_index(1)
    #     self.ci.non_residen_visa_number(visa_num_non)
    #     self.ci.non_residen_visa_issu_date(visa_issue_non)
    #     self.ci.non_residen_visa_expair_date(visa_exp_non)
    #     self.ci.remarks(remarks)
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.5
    #
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_special_char_non.png")
    #         assert True

    # def test_sending_numbers_char_non(self, setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "1234567890"
    #     hb_name = "1234567890"
    #     stre = "1234567890"
    #     cit_dis = "1234567890"
    #     emi_sta = "1234567890"
    #     mob = "1234567890"
    #     email = "1234567890"
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
    #     # Non resident
    #     fh_number_non = "1234567890"
    #     hb_name_non = "1234567890"
    #     stre_non = "1234567890"
    #     cit_dis_non = "1234567890"
    #     emi_sta_non = "1234567890"
    #     visa_num_non = "1234567890"
    #     visa_issue_non = "04052004"
    #     visa_exp_non = "04062014"
    #     remarks = "1234567890"
    #
    #     self.ci.non_field_fh_num_required(fh_number_non)
    #     self.ci.non_field_hb_name_required(hb_name_non)
    #     self.ci.non_field_street_required(stre_non)
    #     self.ci.non_field_city_dist_required(cit_dis_non)
    #     self.ci.non_field_emin_dist(emi_sta_non)
    #     self.non_coun = Select(self.ci.non_drp_country_required())
    #     self.non_coun.select_by_index(6)
    #     self.non_visa = Select(self.ci.non_residen_visa_type_drp())
    #     self.non_visa.select_by_index(1)
    #     self.ci.non_residen_visa_number(visa_num_non)
    #     self.ci.non_residen_visa_issu_date(visa_issue_non)
    #     self.ci.non_residen_visa_expair_date(visa_exp_non)
    #     self.ci.remarks(remarks)
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.5
    #
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_numbers_char_non.png")
    #         assert True

    # def test_sending_char_non(self,setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "abcdefghijk"
    #     hb_name = "abcdefghijk"
    #     stre = "abcdefghijk"
    #     cit_dis = "abcdefghijk"
    #     emi_sta = "abcdefghijk"
    #     mob = "abcdefghijk"
    #     email = "abcdefghijk"
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
    #     # Non resident
    #     fh_number_non = "abcdefghijk"
    #     hb_name_non = "abcdefghijk"
    #     stre_non = "abcdefghijk"
    #     cit_dis_non = "abcdefghijk"
    #     emi_sta_non = "abcdefghijk"
    #     visa_num_non = "abcdefghijk"
    #     visa_issue_non = "04052004"
    #     visa_exp_non = "04062014"
    #     remarks = "abcdefghijk"
    #
    #     self.ci.non_field_fh_num_required(fh_number_non)
    #     self.ci.non_field_hb_name_required(hb_name_non)
    #     self.ci.non_field_street_required(stre_non)
    #     self.ci.non_field_city_dist_required(cit_dis_non)
    #     self.ci.non_field_emin_dist(emi_sta_non)
    #     self.non_coun = Select(self.ci.non_drp_country_required())
    #     self.non_coun.select_by_index(6)
    #     self.non_visa = Select(self.ci.non_residen_visa_type_drp())
    #     self.non_visa.select_by_index(1)
    #     self.ci.non_residen_visa_number(visa_num_non)
    #     self.ci.non_residen_visa_issu_date(visa_issue_non)
    #     self.ci.non_residen_visa_expair_date(visa_exp_non)
    #     self.ci.remarks(remarks)
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.5
    #
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_char_non.png")
    #         assert True

    # def test_sending_speci_char_num_non(self, setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     hb_name = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     stre = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     cit_dis = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     emi_sta = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     mob = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
    #     email = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
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
        # # Non resident
        # fh_number_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # hb_name_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # stre_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # cit_dis_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # emi_sta_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # visa_num_non = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        # visa_issue_non = "04052004"
        # visa_exp_non = "04062014"
        # remarks = "1!@#$%^&*()_+*/{}|]""-[:;',.?a"
        #
        # self.ci.non_field_fh_num_required(fh_number_non)
        # self.ci.non_field_hb_name_required(hb_name_non)
        # self.ci.non_field_street_required(stre_non)
        # self.ci.non_field_city_dist_required(cit_dis_non)
        # self.ci.non_field_emin_dist(emi_sta_non)
        # self.non_coun = Select(self.ci.non_drp_country_required())
        # self.non_coun.select_by_index(6)
        # self.non_visa = Select(self.ci.non_residen_visa_type_drp())
        # self.non_visa.select_by_index(1)
        # self.ci.non_residen_visa_number(visa_num_non)
        # self.ci.non_residen_visa_issu_date(visa_issue_non)
        # self.ci.non_residen_visa_expair_date(visa_exp_non)
        # self.ci.remarks(remarks)
        #
        # self.ci.btn_next()
        # # For scrool down
        # SCROLL_PAUSE_TIME = 0.4
        #
        # # Get scroll height
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_speci_char_num_non.png")
    #         assert True

    # def test_sending_bulk_data_non(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration()
    #
    #     # assigning the page objects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #
    #     # assign data into the fields
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
    #
    #     self.cur.btnnext()
    #
    #     # Bulk data for personal information
    #     flat_house_numbers = ["102", "B-203", "305", "A-406", "110"]
    #     house_building_names = ["Green View Apartments", "Maple Heights", "Sunset Villas", "Cedar Residency",
    #                             "Oakwood Estates"]
    #     streets = ["Oak Street", "Pine Avenue", "Maple Boulevard", "Elm Street", "Birch Road"]
    #     city_districts = ["Springfield", "Albany", "Riverside", "Greenville", "Lakewood"]
    #     emirate_states = ["Illinois", "New York", "California", "Texas", "Florida"]
    #     mobiles = ["15551234567", "15552345678", "15553456789", "15554567890", "15555678901"]
    #     emails = ["john.doe@example.com", "jane.smith@example.com", "robert.brown@example.com",
    #               "linda.jones@example.com", "michael.johnson@example.com"]
    #
    #     for i in range(len(flat_house_numbers)):
    #         fh_number = flat_house_numbers[i]
    #         hb_name = house_building_names[i]
    #         stre = streets[i]
    #         cit_dis = city_districts[i]
    #         emi_sta = emirate_states[i]
    #         mob = mobiles[i]
    #         email = emails[i]
    #
    #         # Perform personal information
    #         self.ci.field_fh_num_required(fh_number)
    #         self.ci.field_hb_name_required(hb_name)
    #         self.ci.field_street_required(stre)
    #         self.ci.field_city_dist_required(cit_dis)
    #         self.ci.field_emin_dist(emi_sta)
    #         # dropdowns
    #         self.con = Select(self.ci.drp_country_required())
    #         self.con.select_by_visible_text("India")
    #         self.mob = Select(self.ci.drp_mobile_required())
    #         self.mob.select_by_index(69)
    #         self.ci.field_mobile_required(mob)
    #         self.ci.field_email_required(email)
    #
    #         self.error = self.cur.errorMessage()
    #
    #         if self.error == "Required":
    #             assert False
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + f"CI_test_sending_bulk_data_{i}.png")
    #             assert True
    #
    #         # Click the next button after each iteration
    #         self.ci.btn_next()
    #
    #         self.id.btn_back()
    #
    #         # Clear the fields for the next iteration
    #         self.ci.field_fh_num_required_clear()
    #         self.ci.field_hb_name_required_clear()
    #         self.ci.field_street_required_clear()
    #         self.ci.field_city_dist_required_clear()
    #         self.ci.field_emin_state_clear()
    #         self.ci.field_mobile_required_clear()
    #         self.ci.field_email_required_clear()
    #
    #     self.driver.quit()
    #
    # def test_sending_required_fields_non(self, setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = "4BH"
    #     hb_name = "Monlash"
    #     stre = "Main road"
    #     cit_dis = "Kochi"
    #     emi_sta = ""
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
    #     # Non resident
    #     visa_num_non = "BRST314168H"
    #     visa_issue_non = "04052004"
    #     visa_exp_non = "04062014"
    #     self.non_visa = Select(self.ci.non_residen_visa_type_drp())
    #     self.non_visa.select_by_index(1)
    #     self.ci.non_residen_visa_number(visa_num_non)
    #     self.ci.non_residen_visa_issu_date(visa_issue_non)
    #     self.ci.non_residen_visa_expair_date(visa_exp_non)
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.4
    #
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #     self.error = self.cur.errorMessage()
    #
    #     val = self.id.visible_id()
    #
    #     if val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_required_fields_non.png")
    #         assert False
    #
    #     self.driver.quit()

    # def test_sending_not_required_fields_non(self, setup):
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
    #     self.residential_status.select_by_index(2)
    #     self.gender = Select(self.cur.gender())
    #     self.gender.select_by_index(2)
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.mrg.select_by_index(2)
    #     self.profession = Select(self.cur.profession())
    #     self.profession.select_by_index(2)
    #
    #     self.cur.btnnext()
    #
    #     fh_number = ""
    #     hb_name = ""
    #     stre = ""
    #     cit_dis = ""
    #     emi_sta = "Dubai"
    #     mob = ""
    #     email = ""
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #     # dropdowns
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_visible_text("")
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     # Non resident
    #     fh_number_non = "F516"
    #     hb_name_non = "HY614"
    #     stre_non = "Kochi"
    #     cit_dis_non = "Ernakulam"
    #     emi_sta_non = "Bhai Bhai"
    #
    #     remarks = "Remarks"
    #
    #     self.ci.non_field_fh_num_required(fh_number_non)
    #     self.ci.non_field_hb_name_required(hb_name_non)
    #     self.ci.non_field_street_required(stre_non)
    #     self.ci.non_field_city_dist_required(cit_dis_non)
    #     self.ci.non_field_emin_dist(emi_sta_non)
    #     self.non_coun = Select(self.ci.non_drp_country_required())
    #     self.non_coun.select_by_index(6)
    #
    #     self.ci.remarks(remarks)
    #
    #     self.ci.btn_next()
    #     # For scrool down
    #     SCROLL_PAUSE_TIME = 0.9
    #     # Get scroll height
    #     last_height = self.driver.execute_script("return document.body.scrollHeight")
    #
    #     while True:
    #         # Scroll down to bottom
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #         # Wait to load page
    #         time.sleep(SCROLL_PAUSE_TIME)
    #
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = self.driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_not_required_fields_non.png")
    #         assert True
    #
    #     self.driver.quit()

    def test_validation_preview_page_non(self, setup):
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
        self.residential_status.select_by_index(2)
        self.gender = Select(self.cur.gender())
        self.gender.select_by_index(2)
        self.mrg = Select(self.cur.maritalstatus())
        self.mrg.select_by_index(2)
        self.profession = Select(self.cur.profession())
        self.profession.select_by_index(2)

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
        self.con.select_by_index(3)
        self.mob = Select(self.ci.drp_mobile_required())
        self.mob.select_by_index(69)
        self.ci.field_mobile_required(mob)
        self.ci.field_email_required(email)

        #       Getting data from the dropdowns
        self.coun = self.con.first_selected_option.text

        self.mobil = self.mob.first_selected_option
        self.monil_pre = self.mobil.text

        # Non resident
        fh_number_non = "6BK"
        hb_name_non = "Twin towers"
        stre_non = "Aluva"
        cit_dis_non = "Kochi"
        emi_sta_non = "Kerala"
        visa_num_non = "BVUXP1033V"
        visa_issue_non = "04052004"
        visa_exp_non = "04062014"
        remarks = "No remarks"

        self.ci.non_field_fh_num_required(fh_number_non)
        self.ci.non_field_hb_name_required(hb_name_non)
        self.ci.non_field_street_required(stre_non)
        self.ci.non_field_city_dist_required(cit_dis_non)
        self.ci.non_field_emin_dist(emi_sta_non)
        self.non_coun = Select(self.ci.non_drp_country_required())
        self.non_coun.select_by_index(6)
        self.non_visa = Select(self.ci.non_residen_visa_type_drp())
        self.non_visa.select_by_index(1)
        self.ci.non_residen_visa_number(visa_num_non)
        self.ci.non_residen_visa_issu_date(visa_issue_non)
        self.ci.non_residen_visa_expair_date(visa_exp_non)
        self.ci.remarks(remarks)
        self.coun_drp = self.non_coun.first_selected_option.text
        self.non_visa_get = self.non_visa.first_selected_option.text

        self.ci.btn_next()
        self.id.drp_ci_pre()



        print("Actual Data from the system")
        print(self.coun)
        print(self.monil_pre)

        print("Actual Data from the system non res")
        print(self.coun_drp)
        print(self.non_visa_get)

        print(" ")
        print("Data from the Preview")
        print(self.id.fh_pre())
        print(self.id.hb_pre())
        print(self.id.stre_pre())
        print(self.id.cidi_pre())
        print(self.id.emist_pre())
        print(self.id.con_pre())
        print(self.id.mob_pre())
        print(self.id.email_pre())

        print(" ")
        # Non resident
        print("Data from the Preview non res")
        print(self.id.fh_non_pre())
        print(self.id.hb_non_pre())
        print(self.id.stre_non_pre())
        print(self.id.cidi_non_pre())
        print(self.id.emist_non_pre())
        print(self.id.con_non_pre())
        print(self.id.vtype_non_pre())
        print(self.id.v_isdat_non_pre())
        print(self.id.v_exdat_non_pre())
        print(self.id.remar_isdat_non_pre())

        # assertion for non resident
        if fh_number_non == self.id.fh_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_fh.png")
            assert False

        if hb_name_non == self.id.hb_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_hb.png")
            assert False

        if stre_non == self.id.stre_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_stre.png")
            assert False

        if cit_dis_non == self.id.cidi_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_citidist.png")
            assert False

        if emi_sta_non == self.id.emist_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_emi.png")
            assert False

        if self.coun_drp == self.id.con_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_cont.png")
            assert False

        if self.non_visa_get == self.id.vtype_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_count.png")
            assert False


        if "04-05-2004" == self.id.v_isdat_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_visa_issue.png")
            assert False

        if '04-06-2014' == self.id.v_exdat_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_visa_exp.png")
            assert False

        if remarks == self.id.remar_isdat_non_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_nonres_remark.png")
            assert False

        # assertion for resident
        if fh_number == self.id.fh_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_non_fh.png")
            assert False

        if hb_name == self.id.hb_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_non_hb.png")
            assert False

        if stre == self.id.stre_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_non_stre.png")
            assert False

        if cit_dis == self.id.cidi_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_cit_non_dis.png")
            assert False

        if emi_sta == self.id.emist_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_emi_non_sta.png")
            assert False

        # if mob == self.id.mob_pre():
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "CI_test_validation_preview_page_non_mob.png")
        #     assert False

        if email == self.id.email_pre():
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "CI_test_validation_preview_page_non_email.png")
            assert False

    # def test_validating_max_len(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Login actions
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # Navigation actions
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     self.nav.click_customer_registration()
    #
    #     # Assigning page objects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #
    #     # Personal information data
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # Fill personal information fields
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #     self.cur.dobpicker_required(dob)
    #
    #     # Dropdown selections
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
    #
    #     self.cur.btnnext()
    #
    #     def get_max_length(element):
    #         if element is not None:
    #             return element.get_attribute('maxlength')
    #         return None
    #
    #     # Fetching elements
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     stree_elem = self.ci.field_street_required_val()
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     emin_elem = self.ci.field_emin_dist_val()
    #     mob_elem = self.ci.field_mobile_required_val()
    #     email_elem = self.ci.field_email_required_val()
    #
    #     # Get and print max lengths
    #     fh_len_max = get_max_length(fh_len_elem)
    #     fh_len_max_int = int(fh_len_max)
    #     print(f"Max length for flat/house number: {type(fh_len_max_int)}")
    #
    #     hb_len_max = int(get_max_length(hb_len_elem))
    #     print(f"Max length for house/building name: {hb_len_max}")
    #
    #     stree_max = int(get_max_length(stree_elem))
    #     print(f"Max length for street: {stree_max}")
    #
    #     ci_di_max = int(get_max_length(ci_di_elem))
    #     print(f"Max length for city/district: {ci_di_max}")
    #
    #     emin_max = int(get_max_length(emin_elem))
    #     print(f"Max length for emirate/state: {emin_max}")
    #
    #     mob_max = int(get_max_length(mob_elem))
    #     print(f"Max length for mobile: {mob_max}")
    #
    #     email_max = int(get_max_length(email_elem))
    #     print(f"Max length for email: {email_max}")
    #
    #     email = generate_random_email()
    #     print("email:", email)
    #     num = random_string_generator_numbers()
    #     print("numbers", num)
    #     max_20 = random_string_generator_max_20()
    #     print("maxlenght_20:", max_20)
    #     max_30 = random_string_generator_max_30()
    #     print("maxlenght_30:", max_30)
    #     max_50 = random_string_generator_max_50()
    #     print("maxlenght_50:", max_50)
    #
    #     fh_number = max_50
    #     hb_name = max_50
    #     stre = max_50
    #     cit_dis = max_30
    #     emi_sta = max_20
    #     mob_val = num
    #     email_val = email
    #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #
    #     # Dropdown selections
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_index(3)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob_val)
    #     self.ci.field_email_required(email_val)
    #
    #     fh_val = fh_len_elem.get_attribute('value')
    #     fh_val_len = len(fh_val)
    #     print("fhvalue", type(fh_val_len))
    #     hb_val = hb_len_elem.get_attribute('value')
    #     hb_val_len = len(hb_val)
    #     print("hbval:", hb_val_len)
    #     stree_val = stree_elem.get_attribute('value')
    #     stree_val_len = len(stree_val)
    #     print("stree:", stree_val_len)
    #     cidi_val = ci_di_elem.get_attribute('value')
    #     cidi_val_len = len(cidi_val)
    #     print("cidi_val:", cidi_val_len)
    #     emin_val = emin_elem.get_attribute('value')
    #     emin_val_len = len(emin_val)
    #     print("emin_val:", emin_val_len)
    #     mob_val = mob_elem.get_attribute('value')
    #     mob_val_len = len(mob_val)
    #     print("mob_val", mob_val_len)
    #     email_val = email_elem.get_attribute('value')
    #     email_val_len = len(email_val)
    #     print("email_val:", email_val_len)
    #
    #     self.ci.btn_next()
    #     # time.sleep(4)
    #
    #     val = self.id.visible_id()
    #     print(val)
    #
    #     if fh_val_len == fh_len_max_int and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_fh.png")
    #         assert False
    #
    #     if hb_val_len == hb_len_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_hb.png")
    #         assert False
    #
    #     if stree_val_len == stree_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_stre.png")
    #         assert False
    #
    #     if cidi_val_len == ci_di_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_cidi.png")
    #         assert False
    #
    #     if emin_val_len == emin_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_emin.png")
    #         assert False
    #
    #     if mob_val_len == mob_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_mob.png")
    #         assert False
    #
    #     if email_val_len == email_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_max_len_emai.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_validating_lessthen_max_len(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Login actions
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # Navigation actions
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     self.nav.click_customer_registration()
    #
    #     # Assigning page objects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #
    #     # Personal information data
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # Fill personal information fields
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #     self.cur.dobpicker_required(dob)
    #
    #     # Dropdown selections
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
    #
    #     self.cur.btnnext()
    #
    #     # def get_max_length(element):
    #     #     if element is not None:
    #     #         return element.get_attribute('maxlength')
    #     #     return None
    #
    #     # Fetching elements
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     stree_elem = self.ci.field_street_required_val()
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     emin_elem = self.ci.field_emin_dist_val()
    #     mob_elem = self.ci.field_mobile_required_val()
    #     email_elem = self.ci.field_email_required_val()
    #
    #     # Get and print max lengths
    #     fh_len_max = fh_len_elem.get_attribute('maxlength')
    #     fh_len_max_int = int(fh_len_max)
    #     print(f"Max length for flat/house number: {fh_len_max_int}")
    #
    #     hb_len_max = int(hb_len_elem.get_attribute('maxlength'))
    #     print(f"Max length for house/building name: {hb_len_max}")
    #
    #     stree_max = int(stree_elem.get_attribute('maxlength'))
    #     print(f"Max length for street: {stree_max}")
    #
    #     ci_di_max = int(ci_di_elem.get_attribute('maxlength'))
    #     print(f"Max length for city/district: {ci_di_max}")
    #
    #     emin_max = int(emin_elem.get_attribute('maxlength'))
    #     print(f"Max length for emirate/state: {emin_max}")
    #
    #     mob_max = int(mob_elem.get_attribute('maxlength'))
    #     print(f"Max length for mobile: {mob_max}")
    #
    #     email_max = int(email_elem.get_attribute('maxlength'))
    #     print(f"Max length for email: {email_max}")
    #
    #     email = generate_random_email_lessthen_45()
    #     print("email:", email)
    #     num = random_string_generator_numbers_max_10()
    #     print("numbers", num)
    #     max_18 = random_string_generator_max_18()
    #     print("maxlenght_20:", max_18)
    #     max_28 = random_string_generator_max_28()
    #     print("maxlenght_30:", max_28)
    #     max_48 = random_string_generator_max_48()
    #     print("maxlenght_50:", max_48)
    #     #
    #     fh_number = max_48
    #     hb_name = max_48
    #     stre = max_48
    #     cit_dis = max_28
    #     emi_sta = max_18
    #     mob_val = num
    #     email_val = email
    #     #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #
    #     # Dropdown selections
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_index(3)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob_val)
    #     self.ci.field_email_required(email_val)
    #
    #     fh_val = fh_len_elem.get_attribute('value')
    #     fh_val_len = len(fh_val)
    #     print("fhvalue", type(fh_val_len))
    #     hb_val = hb_len_elem.get_attribute('value')
    #     hb_val_len = len(hb_val)
    #     print("hbval:", hb_val_len)
    #     stree_val = stree_elem.get_attribute('value')
    #     stree_val_len = len(stree_val)
    #     print("stree:", stree_val_len)
    #     cidi_val = ci_di_elem.get_attribute('value')
    #     cidi_val_len = len(cidi_val)
    #     print("cidi_val:", cidi_val_len)
    #     emin_val = emin_elem.get_attribute('value')
    #     emin_val_len = len(emin_val)
    #     print("emin_val:", emin_val_len)
    #     mob_val = mob_elem.get_attribute('value')
    #     mob_val_len = len(mob_val)
    #     print("mob_val", mob_val_len)
    #     email_val = email_elem.get_attribute('value')
    #     email_val_len = len(email_val)
    #     print("email_val:", email_val_len)
    #
    #     self.ci.btn_next()
    #     # time.sleep(4)
    #     #
    #     val = self.id.visible_id()
    #     print(val)
    #
    #     if fh_val_len <= fh_len_max_int and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_fh.png")
    #         assert False
    #
    #     if hb_val_len < hb_len_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_hb.png")
    #         assert False
    #
    #     if stree_val_len < stree_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_stre.png")
    #         assert False
    #
    #     if cidi_val_len < ci_di_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_cidi.png")
    #         assert False
    #     if emin_val_len < emin_max and val == True:
    #
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_emin.png")
    #         assert False
    #
    #     if mob_val_len < mob_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_mob.png")
    #         assert False
    #
    #     if email_val_len < email_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_lessthen_max_len_emai.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_validating_greaterthen_max_len(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Login actions
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # Navigation actions
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     self.nav.click_customer_registration()
    #
    #     # Assigning page objects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #
    #     # Personal information data
    #     fname = "QA"
    #     mname = "Automation"
    #     lname = "Tester"
    #     arbname = "Khan"
    #     shname = "QA Automation"
    #     mainame = "Nayana"
    #     dob = 30032000
    #
    #     # Fill personal information fields
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.drp.select_by_index(1)
    #     self.cur.firstNameField_required(fname)
    #     self.cur.middleNameField_not_required(mname)
    #     self.cur.lastNameField_required(lname)
    #     self.cur.arabicNameFiels_required(arbname)
    #     self.cur.shortNameField_not_required(shname)
    #     self.cur.maidenNameFiels_not_required(mainame)
    #     self.cur.dobpicker_required(dob)
    #
    #     # Dropdown selections
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
    #
    #     self.cur.btnnext()
    #
    #     # Fetching elements
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     stree_elem = self.ci.field_street_required_val()
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     emin_elem = self.ci.field_emin_dist_val()
    #     mob_elem = self.ci.field_mobile_required_val()
    #     email_elem = self.ci.field_email_required_val()
    #
    #     # Get and print max lengths
    #     fh_len_max = fh_len_elem.get_attribute('maxlength')
    #     fh_len_max_int = int(fh_len_max)
    #     print(f"Max length for flat/house number: {fh_len_max_int}")
    #
    #     hb_len_max = int(hb_len_elem.get_attribute('maxlength'))
    #     print(f"Max length for house/building name: {hb_len_max}")
    #
    #     stree_max = int(stree_elem.get_attribute('maxlength'))
    #     print(f"Max length for street: {stree_max}")
    #
    #     ci_di_max = int(ci_di_elem.get_attribute('maxlength'))
    #     print(f"Max length for city/district: {ci_di_max}")
    #
    #     emin_max = int(emin_elem.get_attribute('maxlength'))
    #     print(f"Max length for emirate/state: {emin_max}")
    #
    #     mob_max = int(mob_elem.get_attribute('maxlength'))
    #     print(f"Max length for mobile: {mob_max}")
    #
    #     email_max = int(email_elem.get_attribute('maxlength'))
    #     print(f"Max length for email: {email_max}")
    #
    #     email = generate_random_email_lessthen_52()
    #     print("email:", email)
    #     num = random_string_generator_numbers_18()
    #     print("numbers", num)
    #     max_22 = random_string_generator_max_22()
    #     print("maxlenght_20:", max_22)
    #     max_32 = random_string_generator_max_32()
    #     print("maxlenght_30:", max_32)
    #     max_52 = random_string_generator_max_52()
    #     print("maxlenght_50:", max_52)
    #     #
    #     fh_number = max_52
    #     hb_name = max_52
    #     stre = max_52
    #     cit_dis = max_32
    #     emi_sta = max_22
    #     mob_val = num
    #     email_val = email
    #     #
    #     self.ci.field_fh_num_required(fh_number)
    #     self.ci.field_hb_name_required(hb_name)
    #     self.ci.field_street_required(stre)
    #     self.ci.field_city_dist_required(cit_dis)
    #     self.ci.field_emin_dist(emi_sta)
    #
    #     # Dropdown selections
    #     self.con = Select(self.ci.drp_country_required())
    #     self.con.select_by_index(3)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob_val)
    #     self.ci.field_email_required(email_val)
    #
    #     fh_val = fh_len_elem.get_attribute('value')
    #     fh_val_len = len(fh_val)
    #     print("fhvalue", type(fh_val_len))
    #     hb_val = hb_len_elem.get_attribute('value')
    #     hb_val_len = len(hb_val)
    #     print("hbval:", hb_val_len)
    #     stree_val = stree_elem.get_attribute('value')
    #     stree_val_len = len(stree_val)
    #     print("stree:", stree_val_len)
    #     cidi_val = ci_di_elem.get_attribute('value')
    #     cidi_val_len = len(cidi_val)
    #     print("cidi_val:", cidi_val_len)
    #     emin_val = emin_elem.get_attribute('value')
    #     emin_val_len = len(emin_val)
    #     print("emin_val:", emin_val_len)
    #     mob_val = mob_elem.get_attribute('value')
    #     mob_val_len = len(mob_val)
    #     print("mob_val", mob_val_len)
    #     email_val = email_elem.get_attribute('value')
    #     email_val_len = len(email_val)
    #     print("email_val:", email_val_len)
    #
    #     self.ci.btn_next()
    #     # time.sleep(4)
    #     #
    #     val = self.id.visible_id()
    #     print(val)
    #
    #     if fh_val_len == fh_len_max_int and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_fh.png")
    #         assert False
    #
    #     if hb_val_len == hb_len_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_hb.png")
    #         assert False
    #
    #     if stree_val_len == stree_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_stre.png")
    #         assert False
    #
    #     if cidi_val_len == ci_di_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_cidi.png")
    #         assert False
    #     if emin_val_len == emin_max and val == True:
    #
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_emin.png")
    #         assert False
    #
    #     if mob_val_len == mob_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_mob.png")
    #         assert False
    #
    #     if email_val_len == email_max and val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_greaterthen_max_len_emai.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_validating_cancel(self, setup):
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
    #     def get_dropdown_text(select_element):
    #         return select_element.first_selected_option.text
    #
    #     print("Getting data from the dropdowns before personal info")
    #     self.title_text = get_dropdown_text(self.drp)
    #     self.cunofbir = get_dropdown_text(self.cob)
    #     self.nat = get_dropdown_text(self.nationality)
    #     self.citiz = get_dropdown_text(self.citizenship)
    #     self.cor = get_dropdown_text(self.country_of_residence)
    #     self.res = get_dropdown_text(self.residential_status)
    #     self.gen = get_dropdown_text(self.gender)
    #     self.mrgs = get_dropdown_text(self.mrg)
    #     self.profs = get_dropdown_text(self.profession)
    #
    #     print(self.title_text)
    #     print(self.cunofbir)
    #     print(self.nat)
    #     print(self.citiz)
    #     print(self.cor)
    #     print(self.res)
    #     print(self.gen)
    #     print(self.mrgs)
    #     print(self.profs)
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
    #     self.con.select_by_index(1)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     stree_elem = self.ci.field_street_required_val()
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     emin_elem = self.ci.field_emin_dist_val()
    #     mob_elem = self.ci.field_mobile_required_val()
    #     email_elem = self.ci.field_email_required_val()
    #
    #     print("getting data for contact info before clear")
    #     #       Getting data from
    #     self.coun = self.con.first_selected_option.text
    #     print("contry:", self.coun)
    #
    #     self.mobil = self.mob.first_selected_option
    #     self.monil_pre = self.mobil.text
    #     print("monile:", self.monil_pre)
    #
    #     fh_val = fh_len_elem.get_attribute('value')
    #     print("fhvalue", fh_val)
    #
    #     hb_val = hb_len_elem.get_attribute('value')
    #     print("hbval:", hb_val)
    #
    #     stree_val = stree_elem.get_attribute('value')
    #     print("stree:", stree_val)
    #
    #     cidi_val = ci_di_elem.get_attribute('value')
    #     print("cidi_val:", cidi_val)
    #
    #     emin_val = emin_elem.get_attribute('value')
    #     print("emin_val:", emin_val)
    #
    #     mob_val = mob_elem.get_attribute('value')
    #     print("mob_val", mob_val)
    #
    #     email_val = email_elem.get_attribute('value')
    #     print("email_val:", email_val)
    #
    #     self.ci.btn_cancel()
    #     self.ci.btn_cancel_cfirm()
    #
    #     self.drp = Select(self.cur.titleDropdown_required())
    #     self.cob = Select(self.cur.cobDropdown_required())
    #     self.nationality = Select(self.cur.nationality())
    #     self.citizenship = Select(self.cur.citizenship())
    #     self.country_of_residence = Select(self.cur.countryofresidence())
    #     self.residential_status = Select(self.cur.residentialstatus())
    #     self.gender = Select(self.cur.gender())
    #     self.mrg = Select(self.cur.maritalstatus())
    #     self.profession = Select(self.cur.profession())
    #
    #     print("Getting data from the dropdowns after clearing person info")
    #     self.title_text_af = get_dropdown_text(self.drp)
    #     self.cunofbir_af = get_dropdown_text(self.cob)
    #     self.nat_af = get_dropdown_text(self.nationality)
    #     self.citiz_af = get_dropdown_text(self.citizenship)
    #     self.cor_af = get_dropdown_text(self.country_of_residence)
    #     self.res_af = get_dropdown_text(self.residential_status)
    #     self.gen_af = get_dropdown_text(self.gender)
    #     self.mrgs_af = get_dropdown_text(self.mrg)
    #     self.profs_af = get_dropdown_text(self.profession)
    #
    #     print(self.title_text_af)
    #     print(self.cunofbir_af)
    #     print(self.nat_af)
    #     print(self.citiz_af)
    #     print(self.cor_af)
    #     print(self.res_af)
    #     print(self.gen_af)
    #     print(self.mrgs_af)
    #     print(self.profs_af)
    #
    #     if (
    #             self.title_text != self.title_text_af and self.cunofbir != self.cunofbir_af and self.nat != self.nat_af and
    #             self.citiz != self.citiz_af and self.cor != self.cor_af and self.res != self.res_af and self.gen != self.gen_af and
    #             self.mrgs != self.mrgs_af and self.profs != self.profs_af):
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_cancel_PI.png")
    #         assert False
    #
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
    #
    #     self.cur.btnnext()
    #     time.sleep(5)
    #
    #     print("getting data for contact info after clear")
    #
    #     # After clearing the form, reinitialize the required elements
    #     self.con = Select(self.ci.drp_country_required())
    #     self.mob = Select(self.ci.drp_mobile_required())
    #
    #     # Continue with the data extraction
    #     print("Getting data for contact info after clear")
    #     self.coun_cl = self.con.first_selected_option.text
    #     self.monil_pre_cl = self.mob.first_selected_option.text
    #
    #     print("Country after clear:", self.coun_cl)
    #     print("Mobile after clear:", self.monil_pre_cl)
    #
    #     fh_val_cl = self.ci.field_fh_num_required_val().get_attribute('value')
    #     hb_val_cl = self.ci.field_hb_name_required_val().get_attribute('value')
    #     stree_val_cl = self.ci.field_street_required_val().get_attribute('value')
    #     cidi_val_cl = self.ci.field_city_dist_required_val().get_attribute('value')
    #     emin_val_cl = self.ci.field_emin_dist_val().get_attribute('value')
    #     mob_val_cl = self.ci.field_mobile_required_val().get_attribute('value')
    #     email_val_cl = self.ci.field_email_required_val().get_attribute('value')
    #
    #     print("FH Number after clear:", fh_val_cl)
    #     print("House/Building Name after clear:", hb_val_cl)
    #     print("Street after clear:", stree_val_cl)
    #     print("City/District after clear:", cidi_val_cl)
    #     print("Emirate/State after clear:", emin_val_cl)
    #     print("Mobile after clear:", mob_val_cl)
    #     print("Email after clear:", email_val_cl)
    #     #
    #     if (
    #             self.coun != self.coun_cl and self.monil_pre != self.monil_pre_cl and fh_val != fh_val_cl and hb_val != hb_val_cl and stree_val != stree_val_cl
    #             and cidi_val != cidi_val_cl and emin_val != emin_val_cl and mob_val != mob_val_cl and email_val != email_val_cl):
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validating_cancel_PI.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_validation_modification_page(self, setup):
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
    #     dob = "30032000"
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
    #     self.con.select_by_index(3)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #     self.id.btn_back_id()
    #     time.sleep(5)
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
    #     self.con.select_by_index(3)
    #     self.mob = Select(self.ci.drp_mobile_required())
    #     self.mob.select_by_index(69)
    #     self.ci.field_mobile_required(mob)
    #     self.ci.field_email_required(email)
    #
    #     self.ci.btn_next()
    #     self.id.drp_ci_pre()
    #
    #     #       Getting data from the dropdowns
    #     self.coun = self.con.first_selected_option.text
    #
    #     self.mobil = self.mob.first_selected_option
    #     self.monil_pre = self.mobil.text
    #
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     stree_elem = self.ci.field_street_required_val()
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     emin_elem = self.ci.field_emin_dist_val()
    #     mob_elem = self.ci.field_mobile_required_val()
    #     email_elem = self.ci.field_email_required_val()
    #
    #     print("Actual Data from the system")
    #     print(self.coun)
    #     print(self.monil_pre)
    #
    #     print("getting data for contact info before clear")
    #     #       Getting data from
    #     self.coun = self.con.first_selected_option.text
    #     print("contry:", self.coun)
    #
    #     self.mobil = self.mob.first_selected_option
    #     self.monil_pre = self.mobil.text
    #     print("monile:", self.monil_pre)
    #
    #     fh_val = fh_len_elem.get_attribute('value')
    #     print("fhvalue", fh_val)
    #
    #     hb_val = hb_len_elem.get_attribute('value')
    #     print("hbval:", hb_val)
    #
    #     stree_val = stree_elem.get_attribute('value')
    #     print("stree:", stree_val)
    #
    #     cidi_val = ci_di_elem.get_attribute('value')
    #     print("cidi_val:", cidi_val)
    #
    #     emin_val = emin_elem.get_attribute('value')
    #     print("emin_val:", emin_val)
    #
    #     mob_val = mob_elem.get_attribute('value')
    #     print("mob_val", mob_val)
    #
    #     email_val = email_elem.get_attribute('value')
    #     print("email_val:", email_val)
    #
    #     print(" ")
    #     print("Data from the Preview")
    #     print(self.id.fh_pre())
    #     print(self.id.hb_pre())
    #     print(self.id.stre_pre())
    #     print(self.id.cidi_pre())
    #     print(self.id.emist_pre())
    #     print(self.id.con_pre())
    #     print(self.id.mob_pre())
    #     print(self.id.email_pre())
    #
    #     if fh_val == self.id.fh_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_fh.png")
    #         assert False
    #
    #     if hb_val == self.id.hb_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_hb.png")
    #         assert False
    #
    #     if stree_val == self.id.stre_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_stre.png")
    #         assert False
    #
    #     if cidi_val == self.id.cidi_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_dis.png")
    #         assert False
    #
    #     if emin_val == self.id.emist_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_sta.png")
    #         assert False
    #
    #     # if mob == self.id.mob_pre():
    #     #     assert True
    #     # else:
    #     #     self.driver.save_screenshot(
    #     #         screenShort.screen_short() + "CI_test_validation_modification_page_mob.png")
    #     #     assert False
    #
    #     if email_val == self.id.email_pre():
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_validation_modification_page_email.png")
    #         assert False
    #
    # def test_getting_fieldsize(self, setup):
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
    #     dob = "30032000"
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
    #
    #     self.cur.btnnext()
    #
    #     fh_len_elem = self.ci.field_fh_num_required_val()
    #     print("fh_len_elem:", fh_len_elem.size)
    #     hb_len_elem = self.ci.field_hb_name_required_val()
    #     print("hb_len_elem:", hb_len_elem.size)
    #     stree_elem = self.ci.field_street_required_val()
    #     print("stree_elem:", stree_elem.size)
    #     ci_di_elem = self.ci.field_city_dist_required_val()
    #     print("ci_di_elem:", ci_di_elem.size)
    #     emin_elem = self.ci.field_emin_dist_val()
    #     print("emin_elem:", emin_elem.size)
    #     mob_elem = self.ci.field_mobile_required_val()
    #     print("mob_elem:", mob_elem.size)
    #     email_elem = self.ci.field_email_required_val()
    #     print("email_elem:", email_elem.size)
    #     con = self.ci.drp_country_required()
    #     print("cob:", con.size)
    #     mob = self.ci.drp_mobile_required()
    #     print("mob:", mob.size)
    #     self.driver.quit()

    # def test_sending_data_havespaces(self, setup):
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
    #     fh_number = "4BH BKM"
    #     hb_name = "Monlash Building"
    #     stre = "Main road"
    #     cit_dis = "Kochi Kerala"
    #     emi_sta = "Kerala Kochi"
    #     mob = "9505123743 34"
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
    #     val = self.id.visible_id()
    #
    #     if val == True:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "CI_test_sending_data_havespaces.png")
    #         assert False





