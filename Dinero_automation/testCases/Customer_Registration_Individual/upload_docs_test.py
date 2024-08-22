from pynput.keyboard import Controller, Key
from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details, Other_Information,Upload_documents,Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Other_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    def test_sending_docs(self ,setup):
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
        self.fp = Final_Preview(self.driver)

        # self.cu_status = Select(self.cur.customerStatusDropdown_not_required())
        # self.cu_status.select_by_index(1)
        # self.cur.idNoField_not_required("7")
        # self.cur.dateofexpiry_not_required(12102024)
        # self.cur.btnverify()
        # time.sleep(2)

        # assign data in to the fields
        fname = "Karunakar"
        mname = "middle"
        lname = "last"
        arbname = "Khan"
        shname = "QA Automation"
        mainame = "Nayana"
        dob = 30032000

        # perform personal information
        self.drp = Select(self.cur.titleDropdown_required())
        time.sleep(2)
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
        hb_name = "Monlas"
        stre = "Main roa"
        cit_dis = "Kochii"
        emi_sta = "Keralaa"
        mob = "95051237"
        email = "finnesttechn@zooker.com"

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
        # send data
        place_of_id_send = "Kochii"
        id_num_send = "56789999"
        date_of_id_issue_send = "30042004"
        date_of_id_expaire_send = "30042025"
        passport_numb_send = "KTYUOA97761"
        passport_issue_date_send = "30042010"
        passport_expi_date_send = "30052025"

        # Dual nation
        passport_num_req_send = "MYNATAXQT"
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
        time.sleep(2)
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
        loyalty_card_no.send_keys("124578988654")
        drp_category.select_by_index(2)
        points.send_keys("100")

        drp_second_income_source.select_by_index(1)
        drp_second_income_range.select_by_index(2)
        drp_demographics.select_by_index(1)
        drp_industry_type.select_by_index(2)
        drp_employemnt.select_by_index(1)
        drp_employee_type.select_by_index(2)
        email.send_keys("testers@gmail.com")
        drp_cb_purpose.select_by_index(2)
        drp_nearest_airport.select_by_index(1)
        fax.send_keys("2123744")
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
        time.sleep(2)
        # select_custom = self.oi.select_customer()
        # select_custom.click()
        btn_next.click()

        self.ud.passport()
        self.ud.front()
        time.sleep(5)
        keyword = Controller()
        keyword.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-08-19 18-18-16.png")
        keyword.press(Key.enter)
        keyword.release(Key.enter)
        time.sleep(3)
        self.ud.btn_next()
        time.sleep(3)

        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Locate the element before using it in WebDriverWait
        element = self.fp.btn_save()
        try:
            WebDriverWait(self.driver, 10).until(lambda d: element.is_displayed() and element.is_enabled())
            element.click()
        except ElementClickInterceptedException:
            # If another element is blocking the button, scroll it into view and retry
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            try:
                element.click()
            except ElementClickInterceptedException:
                # As a last resort, use JavaScript to force the click
                self.driver.execute_script("arguments[0].click();", element)

        time.sleep(6)

        # Close the browser
        self.driver.quit()



