import random
import string
from Dinero_automation.utilities import screenShort
from selenium.webdriver.support.ui import WebDriverWait, Select
from Dinero_automation.pageObjects.Customer_Registration_Individual_edit import Personal_Information_Edit,Contact_Information_Edit,Id_details_Edit,Add_Beneficiaries_Edit,Add_Delegates_Edit,Other_Information_Edit,Upload_documents_Edit,Final_Preview_Edit
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details, Other_Information,Upload_documents,Final_Preview
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException

class Test_Personal_Info_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def generate_random_email(self):
        return self.generate_random_string(5) + "@example.com"

    def test_goingto_editmode(self,setup):

        responce = []
        # Setup the driver for each iteration
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)
        self.cur = Persomal_Information(self.driver)
        self.ci = Contact_Information(self.driver)
        self.id = Id_details(self.driver)
        self.oi = Other_Information(self.driver)
        self.ud = Upload_documents(self.driver)
        self.fp = Final_Preview(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to customer registration
        self.nav.click_navbar()
        self.nav.click_customer_registration()

        # Personal Information
        fname = self.generate_random_string()
        mname = self.generate_random_string(6)
        lname = self.generate_random_string(8)
        arbname = self.generate_random_string(6)
        shname = self.generate_random_string(6)
        mainame = self.generate_random_string(6)
        dob = 31032000

        self.drp = Select(self.cur.titleDropdown_required())
        time.sleep(2)
        self.drp.select_by_index(1)
        self.cur.firstNameField_required(fname)
        self.cur.middleNameField_not_required(mname)
        self.cur.lastNameField_required(lname)
        self.cur.arabicNameFiels_required(arbname)
        self.cur.shortNameField_not_required(shname)
        self.cur.maidenNameFiels_not_required(mainame)
        self.cur.dobpicker_required(dob)

        # Dropdown selections
        cob_drp = Select(self.cur.cobDropdown_required())
        cob_drp.select_by_index(2)
        nation_drp = Select(self.cur.nationality())
        nation_drp.select_by_index(2)
        citizen_drp = Select(self.cur.citizenship())
        citizen_drp.select_by_index(2)
        count_of_res_drp = Select(self.cur.countryofresidence())
        count_of_res_drp.select_by_index(2)
        residen_ststus_res = Select(self.cur.residentialstatus())
        residen_ststus_res.select_by_index(1)
        gender_drp = Select(self.cur.gender())
        gender_drp.select_by_index(2)
        marrage_drp = Select(self.cur.maritalstatus())
        marrage_drp.select_by_index(2)
        profession_drp = Select(self.cur.profession())
        profession_drp.select_by_index(2)
        #
        # # Gather values to return
        # result = {
        #     "drp_val": self.drp.first_selected_option.text,
        #     "fname_val": self.cur.firstNameField_required_value_getting(),
        #     "mname_val": self.cur.middleNameField_not_required_value_getting(),
        #     "lname_val": self.cur.lastNameField_required_value_getting(),
        #     "arbname_val": self.cur.arabicNameFiels_required_value_getting(),
        #     "shname_val": self.cur.shortNameField_not_required_value_getting(),
        #     "mainame_val": self.cur.maidenNameFiels_not_required_value_getting(),
        #     "cob_drp_val": cob_drp.first_selected_option.text,
        #     "nation_drp_val": nation_drp.first_selected_option.text,
        #     "citizen_drp_val": citizen_drp.first_selected_option.text,
        #     "count_of_res_drp_val": count_of_res_drp.first_selected_option.text,
        #     "residen_ststus_res_val": residen_ststus_res.first_selected_option.text,
        #     "gender_drp_val": gender_drp.first_selected_option.text,
        #     "marrage_drp_val": marrage_drp.first_selected_option.text,
        #     "profession_drp_val": profession_drp.first_selected_option.text
        # }

        self.cur.btnnext()

        # Contact Information
        fh_number = self.generate_random_string(4)
        hb_name = self.generate_random_string(6)
        stre = self.generate_random_string(10)
        cit_dis = self.generate_random_string(6)
        emi_sta = self.generate_random_string(6)
        mob = self.generate_random_digits(8)
        email = self.generate_random_email()

        self.ci.field_fh_num_required(fh_number)
        self.ci.field_hb_name_required(hb_name)
        self.ci.field_street_required(stre)
        self.ci.field_city_dist_required(cit_dis)
        self.ci.field_emin_dist(emi_sta)
        Select(self.ci.drp_country_required()).select_by_visible_text("India")
        Select(self.ci.drp_mobile_required()).select_by_index(69)
        self.ci.field_mobile_required(mob)
        self.ci.field_email_required(email)
        self.ci.btn_next()

        # ID Details
        Select(self.id.id_type_field_req()).select_by_index(1)
        self.id.place_of_id_issue_field_req().send_keys(self.generate_random_string(6))
        self.id.id_number_field_req().send_keys(self.generate_random_digits(8))
        self.id.id_issue_date_dpick_req().send_keys("30042004")
        self.id.id_expaire_date_dpick_req().send_keys("30042025")
        Select(self.id.place_of_passport_isse_drp_req()).select_by_index(1)
        self.id.passport_numb_field_req().send_keys(self.generate_random_string(10))
        self.id.passport_issue_date_dpick_req().send_keys("30042010")
        self.id.passport_expi_date_dpick_req().send_keys("30052025")

        # Dual Nation
        self.id.toggle().click()
        Select(self.id.nationality_drp_req_dual()).select_by_index(3)
        Select(self.id.place_of_pass_issue_drp_req_dual()).select_by_index(2)
        self.id.passport_num_req_dual().send_keys(self.generate_random_string(10))
        self.id.passport_issue_date_dpick_req_dual().send_keys("30042011")
        self.id.passport_expai_date_dpick_req_dual().send_keys("30052025")
        self.id.btn_next()

        # Other Information
        self.oi.toggle_other_source_of_income().click()
        Select(self.oi.req_drp_organzation_category()).select_by_index(2)
        Select(self.oi.drp_designation()).select_by_index(2)
        self.oi.employer().send_keys(self.generate_random_string(10))
        self.oi.employer_description().send_keys("Description")
        Select(self.oi.drp_source_of_income()).select_by_index(1)
        Select(self.oi.drp_salary_range()).select_by_index(2)
        self.oi.annual_income().send_keys("100000")
        Select(self.oi.drp_purpose()).select_by_index(2)
        self.oi.loyalty_card_no().send_keys(self.generate_random_digits(12))
        Select(self.oi.drp_categoty()).select_by_index(2)
        self.oi.req_points().send_keys("100")

        # Additional details
        Select(self.oi.drp_secondary_income_source()).select_by_index(1)
        Select(self.oi.drp_secondary_income_range()).select_by_index(2)
        Select(self.oi.drp_demographics()).select_by_index(1)
        Select(self.oi.drp_industry_type()).select_by_index(2)
        Select(self.oi.drp_employment()).select_by_index(1)
        Select(self.oi.drp_employee_type()).select_by_index(2)
        self.oi.professional_email().send_keys(self.generate_random_email())
        Select(self.oi.drp_cb_purpose()).select_by_index(2)
        Select(self.oi.drp_customer_nearest_airport()).select_by_index(1)
        self.oi.fax().send_keys(self.generate_random_digits(7))
        Select(self.oi.drp_cusomer_segment()).select_by_index(2)
        Select(self.oi.drp_role()).select_by_index(1)
        self.oi.additional_remarks().send_keys("No remarks")
        self.oi.check_special_needs().click()
        Select(self.oi.drp_details_of_spcial_needs()).select_by_index(2)
        self.oi.toggle_is_pef().click()
        self.oi.pep_remarks().send_keys("No remarks for PEP")
        self.oi.checkbox_remittance_products().click()
        self.oi.checkbox_forex().click()
        self.oi.checkbox_utility().click()
        Select(self.oi.drp_relationship_type()).select_by_index(2)
        self.oi.search_customer().send_keys(self.generate_random_string(8))
        self.oi.company_name().send_keys(self.generate_random_string(10))
        self.oi.location().send_keys(self.generate_random_string(6))
        Select(self.oi.drp_percentage_holding()).select_by_index(12)
        Select(self.oi.drp_annual_income_currency()).select_by_index(7)
        self.oi.drp_annual_income_frequency().send_keys("200000")
        self.oi.line_of_bussiness().send_keys("Technology Business")
        self.oi.btn_add().click()
        Select(self.oi.drp_application_priority()).select_by_index(2)
        self.oi.whatsapp().send_keys(self.generate_random_digits(7))
        self.oi.facebook().send_keys(self.generate_random_string(8))
        self.oi.x().send_keys(self.generate_random_string(8))
        self.oi.insta().send_keys(self.generate_random_string(8))
        self.oi.linkedin().send_keys(self.generate_random_string(10))
        self.oi.website().send_keys("https://example.com/")
        self.oi.institution_name().send_keys(self.generate_random_string(10))
        Select(self.oi.drp_institution_type()).select_by_index(2)
        Select(self.oi.drp_mebmership()).select_by_index(2)
        self.oi.check_email().click()
        self.oi.check_sms().click()
        self.oi.check_whatsapp().click()
        self.oi.check_phone().click()
        self.oi.check_fax().click()
        self.oi.check_postid().click()
        self.oi.check_privacy_info().click()
        time.sleep(2)
        self.oi.btn_next().click()

        # Document Upload
        self.ud.passport()
        self.ud.front()
        time.sleep(5)
        keyboard = Controller()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-08-19 11-43-05.png")
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)
        self.ud.btn_next()
        time.sleep(2)

        # Final Preview
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

        time.sleep(2)

        document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

        if self.fp.editmode_message() == "You're in edit mode":
            responce.append(document)
            for res in responce:
                url = res['root']['baseURL']
                return url
            assert True
        else:
            None

        self.driver.quit()

    def test_edit_personal_info_clear_non_req_field_and_save(self,setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to customer registration
        self.nav.click_navbar()
        self.nav.click_customer_registration()
        #
        url = self.test_goingto_editmode(setup)  # Call the method and capture the URL
        print("Returned URL:", url)

        self.driver.get(url)
        time.sleep(2)

        self.pi = Personal_Information_Edit(self.driver)
        self.ci = Contact_Information_Edit(self.driver)
        self.id = Id_details_Edit(self.driver)
        self.be = Add_Beneficiaries_Edit(self.driver)
        self.de = Add_Delegates_Edit(self.driver)
        self.oi = Other_Information_Edit(self.driver)
        self.ud = Upload_documents_Edit(self.driver)
        self.fp = Final_Preview_Edit(self.driver)



        title_drp = Select(self.pi.titleDropdown_required())
        f_name = self.pi.firstNameField_required()
        m_name = self.pi.middleNameField_not_required()
        l_name = self.pi.lastNameField_required()
        arb_name = self.pi.arabicNameFiels_required()
        short_name = self.pi.shortNameField_not_required()
        maid_name = self.pi.maidenNameFiels_not_required()
        dob = self.pi.dobpicker_required()
        cob_drp = Select(self.pi.cobDropdown_required())
        nation_drp = Select(self.pi.nationality())
        citizen_drp = Select(self.pi.citizenship())
        cor_drp = Select(self.pi.countryofresidence())
        resi_status_drp = Select(self.pi.residentialstatus())
        gen_drp = Select(self.pi.gender())
        marr_stsus_drp = Select(self.pi.maritalstatus())
        pro_sts_drp = Select(self.pi.profession())

        title_drp_val = title_drp.first_selected_option.text
        f_name_val = f_name.get_attribute("value")
        m_name_val = m_name.get_attribute("value")
        l_name_val = l_name.get_attribute("value")
        arb_name_val = arb_name.get_attribute("value")
        short_name_val = short_name.get_attribute("value")
        maid_name_val = maid_name.get_attribute("value")
        dob_val = dob.get_attribute("value")
        cob_drp_val = cob_drp.first_selected_option.text
        nation_drp_val = nation_drp.first_selected_option.text
        citizen_drp_val = citizen_drp.first_selected_option.text
        cor_drp_val = cor_drp.first_selected_option.text
        resi_status_drp_val = resi_status_drp.first_selected_option.text
        gen_drp_val = gen_drp.first_selected_option.text
        marr_stsus_drp_val = marr_stsus_drp.first_selected_option.text
        pro_sts_drp_val = pro_sts_drp.first_selected_option.text

        print(title_drp_val,f_name_val,m_name_val,l_name_val,arb_name_val,short_name_val,maid_name_val,dob_val,cob_drp_val,nation_drp_val,citizen_drp_val,cor_drp_val,resi_status_drp_val,gen_drp_val,marr_stsus_drp_val,pro_sts_drp_val)
        time.sleep(2)
        m_name.clear()
        time.sleep(2)
        short_name.clear()
        time.sleep(2)
        maid_name.clear()

        time.sleep(2)
        self.pi.btnnext()
        time.sleep(2)
        self.ci.btn_next()
        time.sleep(2)
        self.id.btn_next()
        time.sleep(2)
        self.be.btn_next().click()
        time.sleep(2)
        self.de.btn_next().click()
        time.sleep(2)
        self.oi.check_privacy_info().click()
        self.oi.btn_next().click()
        time.sleep(2)
        self.ud.btn_next()
        time.sleep(2)

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

        time.sleep(3)

        m_name = self.pi.middleNameField_not_required()
        short_name = self.pi.shortNameField_not_required()
        maid_name = self.pi.maidenNameFiels_not_required()

        m_name_val_af = m_name.get_attribute("value")
        short_name_val_af = short_name.get_attribute("value")
        maid_name_val_af = maid_name.get_attribute("value")

        print(m_name_val_af,short_name_val_af,maid_name_val_af)

        if m_name_val != m_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "Edit_CI_test_edit_personal_info_middlename.png")
            assert False

        if short_name_val != short_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "Edit_CI_test_edit_personal_info_shortname.png")
            assert False

        if maid_name_val != maid_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "Edit_CI_test_edit_personal_info_maidname.png")
            assert False

        self.driver.quit()

    def test_edit_personal_validating_preview(self,setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to customer registration
        self.nav.click_navbar()
        self.nav.click_customer_registration()
        #
        url = self.test_goingto_editmode(setup)  # Call the method and capture the URL
        print("Returned URL:", url)

        self.driver.get(url)
        time.sleep(2)

        self.pi = Personal_Information_Edit(self.driver)
        self.ci = Contact_Information_Edit(self.driver)
        self.id = Id_details_Edit(self.driver)
        self.be = Add_Beneficiaries_Edit(self.driver)
        self.de = Add_Delegates_Edit(self.driver)
        self.oi = Other_Information_Edit(self.driver)
        self.ud = Upload_documents_Edit(self.driver)
        self.fp = Final_Preview_Edit(self.driver)

        title_drp = Select(self.pi.titleDropdown_required())
        f_name = self.pi.firstNameField_required()
        m_name = self.pi.middleNameField_not_required()
        l_name = self.pi.lastNameField_required()
        arb_name = self.pi.arabicNameFiels_required()
        short_name = self.pi.shortNameField_not_required()
        maid_name = self.pi.maidenNameFiels_not_required()
        dob = self.pi.dobpicker_required()
        cob_drp = Select(self.pi.cobDropdown_required())
        nation_drp = Select(self.pi.nationality())
        citizen_drp = Select(self.pi.citizenship())
        cor_drp = Select(self.pi.countryofresidence())
        resi_status_drp = Select(self.pi.residentialstatus())
        gen_drp = Select(self.pi.gender())
        marr_stsus_drp = Select(self.pi.maritalstatus())
        pro_sts_drp = Select(self.pi.profession())

        self.pi.btnnext()

        self.ci.click_preview()

        if title_drp == self.ci.title():
            assert True
        else:
            assert False
        if f_name == self.ci.firstname():
            assert True
        else:
            assert False

        if m_name == self.ci.middlename():
            assert True
        else:
            assert False
        if l_name == self.ci.lastname():
            assert True
        else:
            assert False
        if arb_name == self.ci.arabicname():
            assert True
        else:
            assert False
        if short_name == self.ci.shortname():
            assert True
        else:
            assert False
        if maid_name == self.ci.maidenname():
            assert True
        else:
            assert False
        if dob == self.ci.dob():
            assert True
        else:
            assert False
        if cob_drp == self.ci.cob():
            assert True
        else:
            assert False
        if nation_drp == self.ci.natinality():
            assert True
        else:
            assert False
        if citizen_drp == self.ci.citizen():
            assert True
        else:
            assert False
        if cor_drp == self.ci.cor():
            assert True
        else:
            assert False
        if resi_status_drp == self.ci.res():
            assert True
        else:
            assert False
        if gen_drp == self.ci.gender():
            assert True
        else:
            assert False
        if marr_stsus_drp == self.ci.marristatus():
            assert True
        else:
            assert False
        if pro_sts_drp == self.ci.profesion():
            assert True
        else:
            assert False

        self.driver.quit()
















