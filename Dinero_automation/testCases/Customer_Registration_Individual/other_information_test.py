from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details, Other_Information,Upload_documents
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Other_Information:
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     toggle_other_source_of.click()
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     drp_org_cate.select_by_index(2)
    #     drp_designation.select_by_index(2)
    #     employer.send_keys("Karunakar")
    #     emploer_description.send_keys("Tester")
    #     drp_source_of_income.select_by_index(1)
    #     drp_slary_range.select_by_index(2)
    #     anaul_incom.send_keys("100000")
    #     drp_purpose.select_by_index(2)
    #     loyalty_card_no.send_keys("1245789654")
    #     drp_category.select_by_index(2)
    #     points.send_keys("100")
    #
    #     drp_second_income_source.select_by_index(1)
    #     drp_second_income_range.select_by_index(2)
    #     drp_demographics.select_by_index(1)
    #     drp_industry_type.select_by_index(2)
    #     drp_employemnt.select_by_index(1)
    #     drp_employee_type.select_by_index(2)
    #     email.send_keys("tester@gmail.com")
    #     drp_cb_purpose.select_by_index(2)
    #     drp_nearest_airport.select_by_index(1)
    #     fax.send_keys("212344")
    #     drp_customer_segment.select_by_index(2)
    #     drp_role.select_by_index(1)
    #     additional_remark.send_keys("No remarks for role")
    #     speci_need.click()
    #     drp_sp_needs.select_by_index(2)
    #     # sp_needs.send_keys("No remarks for special needs")
    #     toogle_is_pef.click()
    #     pep_remarks.send_keys("No remarks for PEP")
    #     check_remit_product.click()
    #     check_forex.click()
    #     check_utility.click()
    #     drp_relation_type.select_by_index(2)
    #     search_customer.send_keys("karunakar")
    #     time.sleep(2)
    #     # select_custom.click()
    #     company_name.send_keys("Finnest Tech")
    #     location.send_keys("Kerala")
    #     drp_percent_holding.select_by_index(12)
    #     drp_annual_inc_curre.select_by_index(7)
    #     drp_annual_inc_freq.send_keys("200000")
    #     line_of_bussiness.send_keys("Technology Business")
    #     # btn_clear.click()
    #     btn_add.click()
    #     drp_applica_prority.select_by_index(2)
    #     wsapp.send_keys("9854217")
    #     fb.send_keys("finnestfb")
    #     x.send_keys("finnestx")
    #     insta.send_keys("finnestx")
    #     linked_in.send_keys("finnestlinked")
    #     website.send_keys("https://chatgpt.com/")
    #     insti_name.send_keys("Institute Me")
    #     drp_insti_type.select_by_index(2)
    #     drp_membership.select_by_index(2)
    #     check_email.click()
    #     check_sms.click()
    #     check_wapp.click()
    #     check_phone.click()
    #     check_fax.click()
    #     check_postid.click()
    #     # check_promtion.click()
    #     check_privacy.click()
    #     select_custom = self.oi.select_customer()
    #     select_custom.click()
    #     time.sleep(5)
    #     btn_next.click()
    #     time.sleep(5)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if not self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_valid_data.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_sending_without_data(self,setup):
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     time.sleep(4)
    #     btn_next = self.oi.btn_next()
    #     btn_next.click()
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_without_data.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_sending_spchar(self,setup):
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     toggle_other_source_of.click()
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     drp_org_cate.select_by_index(2)
    #     drp_designation.select_by_index(2)
    #     employer.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     emploer_description.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_source_of_income.select_by_index(1)
    #     drp_slary_range.select_by_index(2)
    #     anaul_incom.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_purpose.select_by_index(2)
    #     loyalty_card_no.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_category.select_by_index(2)
    #     points.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #
    #     drp_second_income_source.select_by_index(1)
    #     drp_second_income_range.select_by_index(2)
    #     drp_demographics.select_by_index(1)
    #     drp_industry_type.select_by_index(2)
    #     drp_employemnt.select_by_index(1)
    #     drp_employee_type.select_by_index(2)
    #     email.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_cb_purpose.select_by_index(2)
    #     drp_nearest_airport.select_by_index(1)
    #     fax.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_customer_segment.select_by_index(2)
    #     drp_role.select_by_index(1)
    #     additional_remark.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     speci_need.click()
    #     drp_sp_needs.select_by_index(2)
    #     # sp_needs.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     toogle_is_pef.click()
    #     pep_remarks.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     check_remit_product.click()
    #     check_forex.click()
    #     check_utility.click()
    #     drp_relation_type.select_by_index(2)
    #     search_customer.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     time.sleep(2)
    #     # select_custom.click()
    #     company_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     location.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_percent_holding.select_by_index(12)
    #     drp_annual_inc_curre.select_by_index(7)
    #     drp_annual_inc_freq.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     line_of_bussiness.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     # btn_clear.click()
    #     btn_add.click()
    #     drp_applica_prority.select_by_index(2)
    #     wsapp.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     fb.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     x.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     insta.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     linked_in.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     website.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     insti_name.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     drp_insti_type.select_by_index(2)
    #     drp_membership.select_by_index(2)
    #     check_email.click()
    #     check_sms.click()
    #     check_wapp.click()
    #     check_phone.click()
    #     check_fax.click()
    #     check_postid.click()
    #     # check_promtion.click()
    #     check_privacy.click()
    #     # select_custom = self.oi.select_customer()
    #     # select_custom.click()
    #     time.sleep(7)
    #     btn_next.click()
    #     time.sleep(5)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if not self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_spchar.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_sending_number(self,setup):
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     toggle_other_source_of.click()
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     drp_org_cate.select_by_index(2)
    #     drp_designation.select_by_index(2)
    #     employer.send_keys("123456789")
    #     emploer_description.send_keys("123456789")
    #     drp_source_of_income.select_by_index(1)
    #     drp_slary_range.select_by_index(2)
    #     anaul_incom.send_keys("123456789")
    #     drp_purpose.select_by_index(2)
    #     loyalty_card_no.send_keys("123456789")
    #     drp_category.select_by_index(2)
    #     points.send_keys("123456789")
    #
    #     drp_second_income_source.select_by_index(1)
    #     drp_second_income_range.select_by_index(2)
    #     drp_demographics.select_by_index(1)
    #     drp_industry_type.select_by_index(2)
    #     drp_employemnt.select_by_index(1)
    #     drp_employee_type.select_by_index(2)
    #     email.send_keys("123456789")
    #     drp_cb_purpose.select_by_index(2)
    #     drp_nearest_airport.select_by_index(1)
    #     fax.send_keys("123456789")
    #     drp_customer_segment.select_by_index(2)
    #     drp_role.select_by_index(1)
    #     additional_remark.send_keys("123456789")
    #     speci_need.click()
    #     drp_sp_needs.select_by_index(2)
    #     # sp_needs.send_keys("123456789")
    #     toogle_is_pef.click()
    #     pep_remarks.send_keys("123456789")
    #     check_remit_product.click()
    #     check_forex.click()
    #     check_utility.click()
    #     drp_relation_type.select_by_index(2)
    #     search_customer.send_keys("123456789")
    #     time.sleep(2)
    #     # select_custom.click()
    #     company_name.send_keys("123456789")
    #     location.send_keys("123456789")
    #     drp_percent_holding.select_by_index(12)
    #     drp_annual_inc_curre.select_by_index(7)
    #     drp_annual_inc_freq.send_keys("123456789")
    #     line_of_bussiness.send_keys("123456789")
    #     # btn_clear.click()
    #     btn_add.click()
    #     drp_applica_prority.select_by_index(2)
    #     wsapp.send_keys("123456789")
    #     fb.send_keys("123456789")
    #     x.send_keys("123456789")
    #     insta.send_keys("123456789")
    #     linked_in.send_keys("123456789")
    #     website.send_keys("123456789")
    #     insti_name.send_keys("123456789")
    #     drp_insti_type.select_by_index(2)
    #     drp_membership.select_by_index(2)
    #     time.sleep(2)
    #     check_email.click()
    #     time.sleep(2)
    #     check_sms.click()
    #     time.sleep(2)
    #     check_wapp.click()
    #     time.sleep(2)
    #     check_phone.click()
    #     time.sleep(2)
    #     check_fax.click()
    #     time.sleep(2)
    #     check_postid.click()
    #     time.sleep(2)
    #     # check_promtion.click()
    #     check_privacy.click()
    #     select_custom = self.oi.select_customer()
    #     select_custom.click()
    #     time.sleep(5)
    #     btn_next.click()
    #     time.sleep(5)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if not self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_number.png")
    #         assert False
    #
    #     self.driver.quit()
    #
    # def test_sending_char(self,setup):
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     toggle_other_source_of.click()
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     drp_org_cate.select_by_index(2)
    #     drp_designation.select_by_index(2)
    #     employer.send_keys("qwertyuiop")
    #     emploer_description.send_keys("qwertyuiop")
    #     drp_source_of_income.select_by_index(1)
    #     drp_slary_range.select_by_index(2)
    #     anaul_incom.send_keys("qwertyuiop")
    #     drp_purpose.select_by_index(2)
    #     loyalty_card_no.send_keys("qwertyuiop")
    #     drp_category.select_by_index(2)
    #     points.send_keys("qwertyuiop")
    #
    #     drp_second_income_source.select_by_index(1)
    #     drp_second_income_range.select_by_index(2)
    #     drp_demographics.select_by_index(1)
    #     drp_industry_type.select_by_index(2)
    #     drp_employemnt.select_by_index(1)
    #     drp_employee_type.select_by_index(2)
    #     email.send_keys("qwertyuiop")
    #     drp_cb_purpose.select_by_index(2)
    #     drp_nearest_airport.select_by_index(1)
    #     fax.send_keys("qwertyuiop")
    #     drp_customer_segment.select_by_index(2)
    #     drp_role.select_by_index(1)
    #     additional_remark.send_keys("qwertyuiop")
    #     speci_need.click()
    #     drp_sp_needs.select_by_index(2)
    #     # sp_needs.send_keys("qwertyuiop")
    #     toogle_is_pef.click()
    #     pep_remarks.send_keys("qwertyuiop")
    #     check_remit_product.click()
    #     time.sleep(2)
    #     check_forex.click()
    #     time.sleep(2)
    #     check_utility.click()
    #     drp_relation_type.select_by_index(2)
    #     search_customer.send_keys("qwertyuiop")
    #     time.sleep(2)
    #     # select_custom.click()
    #     company_name.send_keys("qwertyuiop")
    #     location.send_keys("qwertyuiop")
    #     drp_percent_holding.select_by_index(12)
    #     drp_annual_inc_curre.select_by_index(7)
    #     drp_annual_inc_freq.send_keys("qwertyuiop")
    #     line_of_bussiness.send_keys("qwertyuiop")
    #     # btn_clear.click()
    #     btn_add.click()
    #     drp_applica_prority.select_by_index(2)
    #     wsapp.send_keys("qwertyuiop")
    #     fb.send_keys("qwertyuiop")
    #     x.send_keys("qwertyuiop")
    #     insta.send_keys("qwertyuiop")
    #     linked_in.send_keys("qwertyuiop")
    #     website.send_keys("qwertyuiop")
    #     insti_name.send_keys("qwertyuiop")
    #     drp_insti_type.select_by_index(2)
    #     drp_membership.select_by_index(2)
    #     time.sleep(2)
    #     check_email.click()
    #     time.sleep(2)
    #     check_sms.click()
    #     time.sleep(2)
    #     check_wapp.click()
    #     time.sleep(2)
    #     check_phone.click()
    #     time.sleep(2)
    #     check_fax.click()
    #     time.sleep(2)
    #     check_postid.click()
    #     time.sleep(2)
    #     # check_promtion.click()
    #     check_privacy.click()
    #     # select_custom = self.oi.select_customer()
    #     # select_custom.click()
    #     time.sleep(2)
    #     btn_next.click()
    #     time.sleep(2)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_char.png")
    #         assert False
    #
    #     self.driver.quit()

    # def test_sending_spchar_num_char(self,setup):
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
    #     time.sleep(2)
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #     toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     toggle_other_source_of.click()
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     drp_org_cate.select_by_index(2)
    #     drp_designation.select_by_index(2)
    #     employer.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     emploer_description.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_source_of_income.select_by_index(1)
    #     drp_slary_range.select_by_index(2)
    #     anaul_incom.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_purpose.select_by_index(2)
    #     loyalty_card_no.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_category.select_by_index(2)
    #     points.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #
    #     drp_second_income_source.select_by_index(1)
    #     drp_second_income_range.select_by_index(2)
    #     drp_demographics.select_by_index(1)
    #     drp_industry_type.select_by_index(2)
    #     drp_employemnt.select_by_index(1)
    #     drp_employee_type.select_by_index(2)
    #     email.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_cb_purpose.select_by_index(2)
    #     drp_nearest_airport.select_by_index(1)
    #     fax.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_customer_segment.select_by_index(2)
    #     drp_role.select_by_index(1)
    #     additional_remark.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     speci_need.click()
    #     drp_sp_needs.select_by_index(2)
    #     # sp_needs.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     toogle_is_pef.click()
    #     pep_remarks.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     check_remit_product.click()
    #     time.sleep(2)
    #     check_forex.click()
    #     time.sleep(2)
    #     check_utility.click()
    #     drp_relation_type.select_by_index(2)
    #     search_customer.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     time.sleep(2)
    #     # select_custom.click()
    #     company_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     location.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_percent_holding.select_by_index(12)
    #     drp_annual_inc_curre.select_by_index(7)
    #     drp_annual_inc_freq.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     line_of_bussiness.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     # btn_clear.click()
    #     btn_add.click()
    #     drp_applica_prority.select_by_index(2)
    #     wsapp.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     fb.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     x.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     insta.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     linked_in.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     website.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     insti_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
    #     drp_insti_type.select_by_index(2)
    #     drp_membership.select_by_index(2)
    #     time.sleep(2)
    #     check_email.click()
    #     time.sleep(2)
    #     check_sms.click()
    #     time.sleep(2)
    #     check_wapp.click()
    #     time.sleep(2)
    #     check_phone.click()
    #     time.sleep(2)
    #     check_fax.click()
    #     time.sleep(2)
    #     check_postid.click()
    #     time.sleep(2)
    #     check_privacy.click()
    #     time.sleep(2)
    #     btn_next.click()
    #     time.sleep(2)
    #
    #     self.error = self.cur.errorMessage()
    #
    #     if self.error == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "OI_test_sending_spchar_num_char.png")
    #         assert True
    #
    #     self.driver.quit()
# TODO: Need to modify this
    # def test_sending_bulk_data(self,setup):
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
    #     time.sleep(2)
    #
    #     # assining the pageobjects
    #     self.cur = Persomal_Information(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.id = Id_details(self.driver)
    #     self.oi = Other_Information(self.driver)
    #     self.ud = Upload_documents(self.driver)
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
    #     toggle = self.id.toggle()
    #     toggle.click()
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
    #     # Other information
    #
    #     drp_org_cate = Select(self.oi.req_drp_organzation_category())
    #     drp_designation = Select(self.oi.drp_designation())
    #     employer = self.oi.employer()
    #     emploer_description = self.oi.employer_description()
    #     drp_source_of_income = Select(self.oi.drp_source_of_income())
    #     drp_slary_range = Select(self.oi.drp_salary_range())
    #     anaul_incom = self.oi.annual_income()
    #     drp_purpose = Select(self.oi.drp_purpose())
    #     loyalty_card_no = self.oi.loyalty_card_no()
    #     drp_category = Select(self.oi.drp_categoty())
    #     points = self.oi.req_points()
    #     # toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #     # toggle_other_source_of.click()
    #     drp_second_income_source = Select(self.oi.drp_secondary_income_source())
    #     drp_second_income_range = Select(self.oi.drp_secondary_income_range())
    #     drp_demographics = Select(self.oi.drp_demographics())
    #     drp_industry_type = Select(self.oi.drp_industry_type())
    #     drp_employemnt = Select(self.oi.drp_employment())
    #     drp_employee_type = Select(self.oi.drp_employee_type())
    #     email = self.oi.professional_email()
    #     drp_cb_purpose = Select(self.oi.drp_cb_purpose())
    #     drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
    #     fax = self.oi.fax()
    #     drp_customer_segment = Select(self.oi.drp_cusomer_segment())
    #     drp_role = Select(self.oi.drp_role())
    #     additional_remark = self.oi.additional_remarks()
    #     speci_need = self.oi.check_special_needs()
    #     drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
    #     # sp_needs_remark = self.oi.remarks_of_sp_needs()
    #     toogle_is_pef = self.oi.toggle_is_pef()
    #     pep_remarks = self.oi.pep_remarks()
    #     check_remit_product = self.oi.checkbox_remittance_products()
    #     check_forex = self.oi.checkbox_forex()
    #     check_utility = self.oi.checkbox_utility()
    #     drp_relation_type = Select(self.oi.drp_relationship_type())
    #     search_customer = self.oi.search_customer()
    #     company_name = self.oi.company_name()
    #     location = self.oi.location()
    #     drp_percent_holding = Select(self.oi.drp_percentage_holding())
    #     drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
    #     drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
    #     line_of_bussiness = self.oi.line_of_bussiness()
    #     # btn_clear = self.oi.btn_clear()
    #     btn_add = self.oi.btn_add()
    #     drp_applica_prority = Select(self.oi.drp_application_priority())
    #     wsapp = self.oi.whatsapp()
    #     fb = self.oi.facebook()
    #     x = self.oi.x()
    #     insta = self.oi.insta()
    #     linked_in = self.oi.linkedin()
    #     website = self.oi.website()
    #     insti_name = self.oi.institution_name()
    #     drp_insti_type = Select(self.oi.drp_institution_type())
    #     drp_membership = Select(self.oi.drp_mebmership())
    #     check_email = self.oi.check_email()
    #     check_sms = self.oi.check_sms()
    #     check_wapp = self.oi.check_whatsapp()
    #     check_phone = self.oi.check_phone()
    #     check_fax = self.oi.check_fax()
    #     check_postid = self.oi.check_postid()
    #     check_promtion = self.oi.check_promotions()
    #     check_privacy = self.oi.check_privacy_info()
    #     btn_next = self.oi.btn_next()
    #
    #     employers = ["Karunakar Tech", "Tech Innovators", "Future Solutions", "Digital Minds", "Code Masters"]
    #     employer_descriptions = ["Software Engineer", "QA Specialist", "Business Analyst", "Data Scientist",
    #                              "Product Manager"]
    #     annual_incomes = ["50000", "75000", "90000", "120000", "150000"]
    #     loyalty_card_numbers = ["1234567890", "2345678901", "3456789012", "4567890123", "5678901234"]
    #     pointss = ["100", "200", "300", "400", "500"]
    #     emails = ["karunakar1@example.com", "karunakar2@example.com", "karunakar3@example.com",
    #               "karunakar4@example.com", "karunakar5@example.com"]
    #     fax_numbers = ["123456", "234567", "345678", "456789", "567890"]
    #     additional_remarks = ["No remarks", "Client requested updates", "Pending approval", "Requires review",
    #                           "Final submission"]
    #     sp_needs_remarks = ["None", "Wheelchair accessible", "Hearing assistance needed", "Visual aid required",
    #                         "Special dietary requirements"]
    #     pep_remarkss = ["No PEP", "PEP relationship", "Family of PEP", "Former PEP", "Close associate of PEP"]
    #     search_customers = ["Customer One", "Customer Two", "Customer Three", "Customer Four", "Customer Five"]
    #     company_names = ["Company A", "Company B", "Company C", "Company D", "Company E"]
    #     locations = ["New York", "San Francisco", "Los Angeles", "Chicago", "Miami"]
    #     drp_annual_income_amounts = ["60000", "85000", "95000", "110000", "140000"]
    #     line_of_businesses = ["Technology", "Finance", "Healthcare", "Retail", "Manufacturing"]
    #     whatsapp_numbers = ["9876543210", "8765432109", "7654321098", "6543210987", "5432109876"]
    #     facebook_ids = ["fb_karunakar1", "fb_karunakar2", "fb_karunakar3", "fb_karunakar4", "fb_karunakar5"]
    #     twitter_ids = ["tw_karunakar1", "tw_karunakar2", "tw_karunakar3", "tw_karunakar4", "tw_karunakar5"]
    #     instagram_ids = ["ig_karunakar1", "ig_karunakar2", "ig_karunakar3", "ig_karunakar4", "ig_karunakar5"]
    #     linkedin_usernames = ["karunakar1", "karunakar2", "karunakar3", "karunakar4", "karunakar5"]
    #     websites = ["https://www.companyA.com", "https://www.companyB.com", "https://www.companyC.com",
    #                 "https://www.companyD.com", "https://www.companyE.com"]
    #     institution_names = ["Institute A", "Institute B", "Institute C", "Institute D", "Institute E"]
    #
    #     for i in range(len(employers)):
    #         if i == 0:
    #             toggle_other_source_of = self.oi.toggle_other_source_of_income()
    #             toggle_other_source_of.click()
    #         # Fill out the form fields
    #         drp_org_cate.select_by_index(2)
    #         drp_designation.select_by_index(2)
    #         employer.send_keys(employers[i])
    #         emploer_description.send_keys(employer_descriptions[i])
    #         drp_source_of_income.select_by_index(1)
    #         drp_slary_range.select_by_index(2)
    #         anaul_incom.send_keys(annual_incomes[i])
    #         drp_purpose.select_by_index(2)
    #         loyalty_card_no.send_keys(loyalty_card_numbers[i])
    #         drp_category.select_by_index(2)
    #         points.send_keys(pointss[i])
    #
    #         drp_second_income_source.select_by_index(1)
    #         drp_second_income_range.select_by_index(2)
    #         drp_demographics.select_by_index(1)
    #         drp_industry_type.select_by_index(2)
    #         drp_employemnt.select_by_index(1)
    #         drp_employee_type.select_by_index(2)
    #         email.send_keys(emails[i])
    #         drp_cb_purpose.select_by_index(2)
    #         drp_nearest_airport.select_by_index(1)
    #         fax.send_keys(fax_numbers[i])
    #         drp_customer_segment.select_by_index(2)
    #         drp_role.select_by_index(1)
    #         additional_remark.send_keys(additional_remarks[i])
    #         speci_need.click()
    #         drp_sp_needs.select_by_index(2)
    #         # sp_needs_remark.send_keys(sp_needs_remarks[i])
    #         toogle_is_pef.click()
    #         pep_remarks.send_keys(pep_remarkss[i])
    #         check_remit_product.click()
    #         time.sleep(1)
    #         check_forex.click()
    #         time.sleep(1)
    #         check_utility.click()
    #         time.sleep(1)
    #         drp_relation_type.select_by_index(2)
    #         search_customer.send_keys(search_customers[i])
    #         company_name.send_keys(company_names[i])
    #         location.send_keys(locations[i])
    #         drp_percent_holding.select_by_index(2)
    #         drp_annual_inc_curre.select_by_index(2)
    #         drp_annual_inc_freq.send_keys(drp_annual_income_amounts[i])
    #         line_of_bussiness.send_keys(line_of_businesses[i])
    #         btn_add.click()
    #         drp_applica_prority.select_by_index(2)
    #
    #         wsapp.send_keys(whatsapp_numbers[i])
    #         fb.send_keys(facebook_ids[i])
    #         x.send_keys(twitter_ids[i])
    #         insta.send_keys(instagram_ids[i])
    #         linked_in.send_keys(linkedin_usernames[i])
    #         website.send_keys(websites[i])
    #         insti_name.send_keys(institution_names[i])
    #         drp_insti_type.select_by_index(2)
    #         drp_membership.select_by_index(2)
    #         check_email.click()
    #         check_sms.click()
    #         check_wapp.click()
    #         check_phone.click()
    #         check_fax.click()
    #         check_postid.click()
    #         check_promtion.click()
    #         check_privacy.click()
    #
    #         self.error = self.cur.errorMessage()
    #         if self.error == "Required":
    #             assert False
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "OI_test_sending_bulk_data.png")
    #             assert True
    #         btn_next.click()
    #         self.ud.btn_back()
    #
    #         time.sleep(2)  # Optional: add sleep if needed to prevent race conditions
    #
    #     self.driver.quit()

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
        self.ud = Upload_documents(self.driver)
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

        toggle = self.id.toggle()
        toggle.click()

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

        self.id.btn_next()

        # Other information
        toggle_other_source_of = self.oi.toggle_other_source_of_income()
        toggle_other_source_of.click()

        drp_org_cate = Select(self.oi.req_drp_organzation_category())
        drp_designation = Select(self.oi.drp_designation())
        employer = self.oi.employer()
        emploer_description = self.oi.employer_description()
        drp_source_of_income = Select(self.oi.drp_source_of_income())
        drp_slary_range = Select(self.oi.drp_salary_range())
        anaul_incom = self.oi.annual_income()
        drp_purpose = Select(self.oi.drp_purpose())
        loyalty_card_no = self.oi.loyalty_card_no()
        drp_category = Select(self.oi.drp_categoty())
        points = self.oi.req_points()

        drp_second_income_source = Select(self.oi.drp_secondary_income_source())
        drp_second_income_range = Select(self.oi.drp_secondary_income_range())
        drp_demographics = Select(self.oi.drp_demographics())
        drp_industry_type = Select(self.oi.drp_industry_type())
        drp_employemnt = Select(self.oi.drp_employment())
        drp_employee_type = Select(self.oi.drp_employee_type())
        email = self.oi.professional_email()
        drp_cb_purpose = Select(self.oi.drp_cb_purpose())
        drp_nearest_airport = Select(self.oi.drp_customer_nearest_airport())
        fax = self.oi.fax()
        drp_customer_segment = Select(self.oi.drp_cusomer_segment())
        drp_role = Select(self.oi.drp_role())
        additional_remark = self.oi.additional_remarks()
        speci_need = self.oi.check_special_needs()
        drp_sp_needs = Select(self.oi.drp_details_of_spcial_needs())
        # sp_needs = self.oi.remarks_of_sp_needs()
        toogle_is_pef = self.oi.toggle_is_pef()
        pep_remarks = self.oi.pep_remarks()
        check_remit_product = self.oi.checkbox_remittance_products()
        check_forex = self.oi.checkbox_forex()
        check_utility = self.oi.checkbox_utility()
        drp_relation_type = Select(self.oi.drp_relationship_type())
        search_customer = self.oi.search_customer()
        company_name = self.oi.company_name()
        location = self.oi.location()
        drp_percent_holding = Select(self.oi.drp_percentage_holding())
        drp_annual_inc_curre = Select(self.oi.drp_annual_income_currency())
        drp_annual_inc_freq = self.oi.drp_annual_income_frequency()
        line_of_bussiness = self.oi.line_of_bussiness()
        # btn_clear = self.oi.btn_clear()
        btn_add = self.oi.btn_add()
        drp_applica_prority = Select(self.oi.drp_application_priority())
        wsapp = self.oi.whatsapp()
        fb = self.oi.facebook()
        x = self.oi.x()
        insta = self.oi.insta()
        linked_in = self.oi.linkedin()
        website = self.oi.website()
        insti_name = self.oi.institution_name()
        drp_insti_type = Select(self.oi.drp_institution_type())
        drp_membership = Select(self.oi.drp_mebmership())
        check_email = self.oi.check_email()
        check_sms = self.oi.check_sms()
        check_wapp = self.oi.check_whatsapp()
        check_phone = self.oi.check_phone()
        check_fax = self.oi.check_fax()
        check_postid = self.oi.check_postid()
        check_promtion = self.oi.check_promotions()
        check_privacy = self.oi.check_privacy_info()
        btn_next = self.oi.btn_next()

        drp_org_cate.select_by_index(2)
        drp_designation.select_by_index(2)
        employer.send_keys("Karunakar")
        emploer_description.send_keys("Tester")
        drp_source_of_income.select_by_index(1)
        drp_slary_range.select_by_index(2)
        anaul_incom.send_keys("100000")
        drp_purpose.select_by_index(2)
        loyalty_card_no.send_keys("1245789654")
        drp_category.select_by_index(2)
        points.send_keys("100")

        drp_second_income_source.select_by_index(1)
        drp_second_income_range.select_by_index(2)
        drp_demographics.select_by_index(1)
        drp_industry_type.select_by_index(2)
        drp_employemnt.select_by_index(1)
        drp_employee_type.select_by_index(2)
        email.send_keys("tester@gmail.com")
        drp_cb_purpose.select_by_index(2)
        drp_nearest_airport.select_by_index(1)
        fax.send_keys("212344")
        drp_customer_segment.select_by_index(2)
        drp_role.select_by_index(1)
        additional_remark.send_keys("No remarks for role")
        speci_need.click()
        drp_sp_needs.select_by_index(2)
        # sp_needs.send_keys("No remarks for special needs")
        toogle_is_pef.click()
        pep_remarks.send_keys("No remarks for PEP")
        check_remit_product.click()
        check_forex.click()
        check_utility.click()
        drp_relation_type.select_by_index(2)
        search_customer.send_keys("karunakar")
        time.sleep(2)
        # select_custom.click()
        company_name.send_keys("Finnest Tech")
        location.send_keys("Kerala")
        drp_percent_holding.select_by_index(12)
        drp_annual_inc_curre.select_by_index(7)
        drp_annual_inc_freq.send_keys("200000")
        line_of_bussiness.send_keys("Technology Business")

        # btn_clear.click()
        btn_add.click()
        self.oi.click_boc().click()
        time.sleep(2)
        drp_applica_prority.select_by_index(2)
        wsapp.send_keys("9854217")
        fb.send_keys("finnestfb")
        x.send_keys("finnestx")
        insta.send_keys("finnestx")
        linked_in.send_keys("finnestlinked")
        website.send_keys("https://chatgpt.com/")
        insti_name.send_keys("Institute Me")
        drp_insti_type.select_by_index(2)
        drp_membership.select_by_index(2)
        check_email.click()
        check_sms.click()
        check_wapp.click()
        check_phone.click()
        check_fax.click()
        check_postid.click()
        # check_promtion.click()
        check_privacy.click()
        select_custom = self.oi.select_customer()
        select_custom.click()

        drp_org_cate_val = drp_org_cate.first_selected_option.text
        drp_designation_val = drp_designation.first_selected_option.text
        employer_val = employer.get_attribute("value")
        emploer_description_val = emploer_description.get_attribute('value')
        drp_source_of_income_val = drp_source_of_income.first_selected_option.text
        drp_slary_range_val = drp_slary_range.first_selected_option.text
        anaul_incom_val = anaul_incom.get_attribute("value")
        drp_purpose_val = drp_purpose.first_selected_option.text
        loyalty_card_no_val = loyalty_card_no.get_attribute("value")
        drp_category_val = drp_category.first_selected_option.text
        points_val = points.get_attribute("value")
        drp_second_income_source_val = drp_second_income_source.first_selected_option.text
        drp_second_income_range_val = drp_second_income_range.first_selected_option.text
        drp_demographics_val = drp_demographics.first_selected_option.text
        drp_industry_type_val = drp_industry_type.first_selected_option.text
        drp_employemnt_val =  drp_employemnt.first_selected_option.text
        drp_employee_type_val = drp_employee_type.first_selected_option.text
        email_val = email.get_attribute("value")
        drp_cb_purpose_val = drp_cb_purpose.first_selected_option.text
        drp_nearest_airport_val = drp_nearest_airport.first_selected_option.text
        fax_val = fax.get_attribute("value")
        drp_customer_segment_val = drp_customer_segment.first_selected_option.text
        drp_role_val = drp_role.first_selected_option.text
        additional_remark_val = additional_remark.get_attribute("value")
        speci_need_val = speci_need.get_attribute("value")
        drp_sp_needs_val = drp_sp_needs.first_selected_option.text
        toogle_is_pef_val = toogle_is_pef.get_attribute("value")
        pep_remarks_val = pep_remarks.get_attribute("value")
        check_remit_product_val = check_remit_product.get_attribute("value")
        check_forex_val = check_forex.get_attribute("value")
        check_utility_val = check_utility.get_attribute("value")
        drp_relation_type_val = drp_relation_type.first_selected_option.text
        search_customer_val = search_customer.get_attribute("value")
        company_name_val = company_name.get_attribute("value")
        location_val = location.get_attribute("value")
        drp_percent_holding_val = drp_percent_holding.first_selected_option.text
        drp_annual_inc_curre_val = drp_annual_inc_curre.first_selected_option.text
        drp_annual_inc_freq_val = drp_annual_inc_freq.get_attribute("value")
        line_of_bussiness_val = line_of_bussiness.get_attribute("value")
        drp_applica_prority_val = drp_applica_prority.first_selected_option.text
        wsapp_val = wsapp.get_attribute("value")
        fb_val = fb.get_attribute("value")
        x_val = x.get_attribute("value")
        insta_val = insta.get_attribute("value")
        linked_in_val = linked_in.get_attribute("value")
        website_val = website.get_attribute("value")
        insti_name_val = insti_name.get_attribute("value")
        drp_insti_type_val = insti_name.get_attribute("value")
        drp_membership_val = drp_membership.first_selected_option.text
        check_email_val = check_email.get_attribute("value")
        check_sms_val = check_sms.get_attribute("value")
        check_wapp_val = check_wapp.get_attribute("value")
        check_phone_val = check_phone.get_attribute("value")
        check_fax_val = check_fax.get_attribute("value")
        check_postid_val = check_postid.get_attribute("value")
        check_privacy_val = check_privacy.get_attribute("value")

        print(
            "Actual value:",
            drp_org_cate_val,
            drp_designation_val,
            employer_val,
            emploer_description_val,
            drp_source_of_income_val,
            drp_slary_range_val,
            anaul_incom_val,
            drp_purpose_val,
            loyalty_card_no_val,
            drp_category_val,
            points_val,
            drp_second_income_source_val,
            drp_second_income_range_val,
            drp_demographics_val,
            drp_industry_type_val,
            drp_employemnt_val,
            drp_employee_type_val,
            email_val,
            drp_cb_purpose_val,
            drp_nearest_airport_val,
            fax_val,
            drp_customer_segment_val,
            drp_role_val,
            additional_remark_val,
            speci_need_val,
            drp_sp_needs_val,
            toogle_is_pef_val,
            pep_remarks_val,
            check_remit_product_val,
            check_forex_val,
            check_utility_val,
            drp_relation_type_val,
            search_customer_val,
            company_name_val,
            location_val,
            drp_percent_holding_val,
            drp_annual_inc_curre_val,
            drp_annual_inc_freq_val,
            line_of_bussiness_val,
            drp_applica_prority_val,
            wsapp_val,
            fb_val,
            x_val,
            insta_val,
            linked_in_val,
            website_val,
            insti_name_val,
            drp_insti_type_val,
            drp_membership_val,
            check_email_val,
            check_sms_val,
            check_wapp_val,
            check_phone_val,
            check_fax_val,
            check_postid_val,
            check_privacy_val,
            sep=' '
        )

        btn_next.click()
        time.sleep(2)
        self.ud.click_other_info_pre()
        time.sleep(2)
        print(
            "Data from preview:",
            self.ud.org_category_pre(),
            self.ud.designation_pre(),
            self.ud.employer_pre(),
            self.ud.employer_discri_pre(),
            self.ud.source_of_incom_pre(),
            self.ud.salary_range_pre(),
            self.ud.annual_income_pre(),
            self.ud.purpose_pre(),
            self.ud.loyalty_card_number_pre(),
            self.ud.category_pre(),
            self.ud.points_pre(),
            self.ud.second_income_source_pre(),
            self.ud.second_income_range_pre(),
            self.ud.demographic_pre(),
            self.ud.indu_type_pre(),
            self.ud.employement_pre(),
            self.ud.employement_type_pre(),

            self.ud.email_pre(),
            self.ud.cb_purpose_pre(),
            self.ud.cust_nearest_airport_pre(),
            self.ud.fax_pre(),
            self.ud.cust_segment_pre(),
            self.ud.role_pre(),
            self.ud.add_info_remarks_pre(),
            self.ud.sp_needs_pre(),
            self.ud.detail_sp_needs_pre(),
            self.ud.is_PEP_pre(),
            self.ud.PEP_remarks_pre(),
            self.ud.interested_product_remitance_pre(),
            self.ud.interested_product_forex_pre(),
            self.ud.interested_product_utility_pre(),

            #
            self.ud.company_name_pre(),
            self.ud.location_pre(),
            self.ud.percentage_holding_pre(),
            self.ud.annual_income_currency_pre(),
            self.ud.annual_income_amount_pre(),
            #

            self.ud.line_of_business_pre(),
            self.ud.application_priority_pre(),
            self.ud.whataapp_pre(),
            self.ud.fb_pre(),
            self.ud.x_pre(),
            self.ud.insta_pre(),
            self.ud.linked_in_pre(),
            self.ud.website_pre(),
            self.ud.institute_name_pre(),
            self.ud.institute_type_pre(),
            self.ud.mebership_type_pre(),
            self.ud.marketing_mail_pre(),
            self.ud.marketing_sms_pre(),
            self.ud.marketing_whatsaapp_pre(),
            self.ud.marketing_phone_pre(),
            self.ud.marketing_fax_pre(),
            self.ud.marketing_postal_id_pre(),
            self.ud.marketing_aggrement_pre(),
            self.ud.privacy_aggrement_pre(),
            sep = ' '
        )

        # self.error = self.cur.errorMessage()

        # if not self.error == "Required":
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "OI_test_sending_valid_data.png")
        #     assert False
        updated_values = {}

        assert drp_org_cate_val == self.ud.org_category_pre(), f"Mismatch in org_category_pre: {drp_org_cate_val} != {self.ud.org_category_pre()}"
        assert drp_designation_val == self.ud.designation_pre(), f"Mismatch in designation_pre: {drp_designation_val} != {self.ud.designation_pre()}"
        assert employer_val == self.ud.employer_pre(), f"Mismatch in employer_pre: {employer_val} != {self.ud.employer_pre()}"
        assert emploer_description_val == self.ud.employer_discri_pre(), f"Mismatch in employer_discri_pre: {emploer_description_val} != {self.ud.employer_discri_pre()}"
        assert drp_source_of_income_val == self.ud.source_of_incom_pre(), f"Mismatch in source_of_incom_pre: {drp_source_of_income_val} != {self.ud.source_of_incom_pre()}"
        assert drp_slary_range_val == self.ud.salary_range_pre(), f"Mismatch in salary_range_pre: {drp_slary_range_val} != {self.ud.salary_range_pre()}"
        assert anaul_incom_val == self.ud.annual_income_pre(), f"Mismatch in annual_income_pre: {anaul_incom_val} != {self.ud.annual_income_pre()}"
        assert drp_purpose_val == self.ud.purpose_pre(), f"Mismatch in purpose_pre: {drp_purpose_val} != {self.ud.purpose_pre()}"
        assert loyalty_card_no_val == self.ud.loyalty_card_number_pre(), f"Mismatch in loyalty_card_number_pre: {loyalty_card_no_val} != {self.ud.loyalty_card_number_pre()}"
        assert drp_category_val == self.ud.category_pre(), f"Mismatch in category_pre: {drp_category_val} != {self.ud.category_pre()}"
        assert points_val == self.ud.points_pre(), f"Mismatch in points_pre: {points_val} != {self.ud.points_pre()}"
        assert drp_second_income_source_val == self.ud.second_income_source_pre(), f"Mismatch in second_income_source_pre: {drp_second_income_source_val} != {self.ud.second_income_source_pre()}"
        assert drp_second_income_range_val == self.ud.second_income_range_pre(), f"Mismatch in second_income_range_pre: {drp_second_income_range_val} != {self.ud.second_income_range_pre()}"
        assert drp_demographics_val == self.ud.demographic_pre(), f"Mismatch in demographic_pre: {drp_demographics_val} != {self.ud.demographic_pre()}"
        assert drp_industry_type_val == self.ud.indu_type_pre(), f"Mismatch in indu_type_pre: {drp_industry_type_val} != {self.ud.indu_type_pre()}"
        assert drp_employemnt_val == self.ud.employement_pre(), f"Mismatch in employement_pre: {drp_employemnt_val} != {self.ud.employement_pre()}"
        assert drp_employee_type_val == self.ud.employement_type_pre(), f"Mismatch in employement_type_pre: {drp_employee_type_val} != {self.ud.employement_type_pre()}"
        assert email_val == self.ud.email_pre(), f"Mismatch in email_pre: {email_val} != {self.ud.email_pre()}"
        assert drp_cb_purpose_val == self.ud.cb_purpose_pre(), f"Mismatch in cb_purpose_pre: {drp_cb_purpose_val} != {self.ud.cb_purpose_pre()}"
        assert drp_nearest_airport_val == self.ud.cust_nearest_airport_pre(), f"Mismatch in cust_nearest_airport_pre: {drp_nearest_airport_val} != {self.ud.cust_nearest_airport_pre()}"
        assert fax_val == self.ud.fax_pre(), f"Mismatch in fax_pre: {fax_val} != {self.ud.fax_pre()}"
        assert drp_customer_segment_val == self.ud.cust_segment_pre(), f"Mismatch in cust_segment_pre: {drp_customer_segment_val} != {self.ud.cust_segment_pre()}"
        assert drp_role_val == self.ud.role_pre(), f"Mismatch in role_pre: {drp_role_val} != {self.ud.role_pre()}"
        assert additional_remark_val == self.ud.add_info_remarks_pre(), f"Mismatch in add_info_remarks_pre: {additional_remark_val} != {self.ud.add_info_remarks_pre()}"

        if speci_need_val == "on":
            updated_values['speci_need_val'] = "True"
        else:
            updated_values['speci_need_val'] = speci_need_val

        # assert speci_need_val == self.ud.sp_needs_pre(), f"Mismatch in sp_needs_pre: {speci_need_val} != {self.ud.sp_needs_pre()}"

        assert drp_sp_needs_val == self.ud.detail_sp_needs_pre(), f"Mismatch in detail_sp_needs_pre: {drp_sp_needs_val} != {self.ud.detail_sp_needs_pre()}"
        assert toogle_is_pef_val == self.ud.is_PEP_pre(), f"Mismatch in is_PEP_pre: {toogle_is_pef_val} != {self.ud.is_PEP_pre()}"
        assert pep_remarks_val == self.ud.PEP_remarks_pre(), f"Mismatch in PEP_remarks_pre: {pep_remarks_val} != {self.ud.PEP_remarks_pre()}"
        assert check_remit_product_val == self.ud.interested_product_remitance_pre(), f"Mismatch in interested_product_remitance_pre: {check_remit_product_val} != {self.ud.interested_product_remitance_pre()}"
        assert check_forex_val == self.ud.interested_product_forex_pre(), f"Mismatch in interested_product_forex_pre: {check_forex_val} != {self.ud.interested_product_forex_pre()}"
        assert check_utility_val == self.ud.interested_product_utility_pre(), f"Mismatch in interested_product_utility_pre: {check_utility_val} != {self.ud.interested_product_utility_pre()}"
        assert company_name_val == self.ud.company_name_pre(), f"Mismatch in company_name_pre: {company_name_val} != {self.ud.company_name_pre()}"
        assert location_val == self.ud.location_pre(), f"Mismatch in location_pre: {location_val} != {self.ud.location_pre()}"
        assert drp_percent_holding_val == self.ud.percentage_holding_pre(), f"Mismatch in percentage_holding_pre: {drp_percent_holding_val} != {self.ud.percentage_holding_pre()}"
        assert drp_annual_inc_curre_val == self.ud.annual_income_currency_pre(), f"Mismatch in annual_income_currency_pre: {drp_annual_inc_curre_val} != {self.ud.annual_income_currency_pre()}"
        assert drp_annual_inc_freq_val == self.ud.annual_income_amount_pre(), f"Mismatch in annual_income_amount_pre: {drp_annual_inc_freq_val} != {self.ud.annual_income_amount_pre()}"
        assert line_of_bussiness_val == self.ud.line_of_business_pre(), f"Mismatch in line_of_business_pre: {line_of_bussiness_val} != {self.ud.line_of_business_pre()}"
        assert drp_applica_prority_val == self.ud.application_priority_pre(), f"Mismatch in application_priority_pre: {drp_applica_prority_val} != {self.ud.application_priority_pre()}"
        assert wsapp_val == self.ud.whataapp_pre(), f"Mismatch in whataapp_pre: {wsapp_val} != {self.ud.whataapp_pre()}"
        assert fb_val == self.ud.fb_pre(), f"Mismatch in fb_pre: {fb_val} != {self.ud.fb_pre()}"
        assert x_val == self.ud.x_pre(), f"Mismatch in x_pre: {x_val} != {self.ud.x_pre()}"
        assert insta_val == self.ud.insta_pre(), f"Mismatch in insta_pre: {insta_val} != {self.ud.insta_pre()}"
        assert linked_in_val == self.ud.linked_in_pre(), f"Mismatch in linked_in_pre: {linked_in_val} != {self.ud.linked_in_pre()}"
        assert website_val == self.ud.website_pre(), f"Mismatch in website_pre: {website_val} != {self.ud.website_pre()}"
        assert insti_name_val == self.ud.institute_name_pre(), f"Mismatch in institute_name_pre: {insti_name_val} != {self.ud.institute_name_pre()}"
        assert drp_insti_type_val == self.ud.institute_type_pre(), f"Mismatch in institute_type_pre: {drp_insti_type_val} != {self.ud.institute_type_pre()}"
        assert drp_membership_val == self.ud.mebership_type_pre(), f"Mismatch in mebership_type_pre: {drp_membership_val} != {self.ud.mebership_type_pre()}"
        assert check_email_val == self.ud.marketing_mail_pre(), f"Mismatch in marketing_mail_pre: {check_email_val} != {self.ud.marketing_mail_pre()}"
        assert check_sms_val == self.ud.marketing_sms_pre(), f"Mismatch in marketing_sms_pre: {check_sms_val} != {self.ud.marketing_sms_pre()}"
        assert check_wapp_val == self.ud.marketing_whatsaapp_pre(), f"Mismatch in marketing_whatsaapp_pre: {check_wapp_val} != {self.ud.marketing_whatsaapp_pre()}"
        assert check_phone_val == self.ud.marketing_phone_pre(), f"Mismatch in marketing_phone_pre: {check_phone_val} != {self.ud.marketing_phone_pre()}"
        assert check_fax_val == self.ud.marketing_fax_pre(), f"Mismatch in marketing_fax_pre: {check_fax_val} != {self.ud.marketing_fax_pre()}"
        assert check_postid_val == self.ud.mark

        self.driver.quit()

