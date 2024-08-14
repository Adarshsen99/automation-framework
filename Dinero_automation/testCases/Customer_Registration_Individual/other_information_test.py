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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #     sp_needs.send_keys("No remarks for special needs")
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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #     sp_needs.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #     sp_needs.send_keys("123456789")
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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #     sp_needs.send_keys("qwertyuiop")
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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #     sp_needs.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
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
    #     # time.sleep(2)
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
    #     sp_needs = self.oi.remarks_of_sp_needs()
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
    #         try:
    #             # Fill out the form fields
    #             drp_org_cate.select_by_index(2)
    #             drp_designation.select_by_index(2)
    #             employer.send_keys(employers[i])
    #             emploer_description.send_keys(employer_descriptions[i])
    #             drp_source_of_income.select_by_index(1)
    #             drp_slary_range.select_by_index(2)
    #             anaul_incom.send_keys(annual_incomes[i])
    #             drp_purpose.select_by_index(2)
    #             loyalty_card_no.send_keys(loyalty_card_numbers[i])
    #             drp_category.select_by_index(2)
    #             points.send_keys(pointss[i])
    #
    #             drp_second_income_source.select_by_index(1)
    #             drp_second_income_range.select_by_index(2)
    #             drp_demographics.select_by_index(1)
    #             drp_industry_type.select_by_index(2)
    #             drp_employemnt.select_by_index(1)
    #             drp_employee_type.select_by_index(2)
    #             email.send_keys(emails[i])
    #             drp_cb_purpose.select_by_index(2)
    #             drp_nearest_airport.select_by_index(1)
    #             fax.send_keys(fax_numbers[i])
    #             drp_customer_segment.select_by_index(2)
    #             drp_role.select_by_index(1)
    #             additional_remark.send_keys(additional_remarks[i])
    #             speci_need.click()
    #             drp_sp_needs.select_by_index(2)
    #             sp_needs.send_keys(sp_needs_remarks[i])
    #             pep_status.click()
    #             drp_pep_relation.select_by_index(2)
    #             pep_remark.send_keys(pep_remarkss[i])
    #
    #             srch_customer.send_keys(search_customers[i])
    #             company_name.send_keys(company_names[i])
    #             drp_locate_company.select_by_index(2)
    #             company_location.send_keys(locations[i])
    #             drp_cb_annual_income.select_by_index(2)
    #             drp_cb_business.select_by_index(2)
    #             whats_number.send_keys(whatsapp_numbers[i])
    #             fb_id.send_keys(facebook_ids[i])
    #             twitt_id.send_keys(twitter_ids[i])
    #             insta_id.send_keys(instagram_ids[i])
    #             linkedin_username.send_keys(linkedin_usernames[i])
    #             website.send_keys(websites[i])
    #             insti_name.send_keys(institution_names[i])
    #
    #             # Click the "Add" button after filling in the fields
    #             add_button.click()
    #
    #             # Clear the fields for the next iteration
    #             drp_org_cate.deselect_all()
    #             drp_designation.deselect_all()
    #             employer.clear()
    #             emploer_description.clear()
    #             drp_source_of_income.deselect_all()
    #             drp_slary_range.deselect_all()
    #             anaul_incom.clear()
    #             drp_purpose.deselect_all()
    #             loyalty_card_no.clear()
    #             drp_category.deselect_all()
    #             points.clear()
    #
    #             drp_second_income_source.deselect_all()
    #             drp_second_income_range.deselect_all()
    #             drp_demographics.deselect_all()
    #             drp_industry_type.deselect_all()
    #             drp_employemnt.deselect_all()
    #             drp_employee_type.deselect_all()
    #             email.clear()
    #             drp_cb_purpose.deselect_all()
    #             drp_nearest_airport.deselect_all()
    #             fax.clear()
    #             drp_customer_segment.deselect_all()
    #             drp_role.deselect_all()
    #             additional_remark.clear()
    #             speci_need.click()
    #             drp_sp_needs.deselect_all()
    #             sp_needs.clear()
    #             pep_status.click()
    #             drp_pep_relation.deselect_all()
    #             pep_remark.clear()
    #
    #             srch_customer.clear()
    #             company_name.clear()
    #             drp_locate_company.deselect_all()
    #             company_location.clear()
    #             drp_cb_annual_income.deselect_all()
    #             drp_cb_business.deselect_all()
    #             whats_number.clear()
    #             fb_id.clear()
    #             twitt_id.clear()
    #             insta_id.clear()
    #             linkedin_username.clear()
    #             website.clear()
    #             insti_name.clear()
    #
    #         except Exception as e:
    #             print(f"An error occurred during iteration {i + 1}: {str(e)}")
    #             continue
    #
    #         time.sleep(2)  # Optional: add sleep if needed to prevent race conditions
    #
    #     self.driver.quit()