import time

from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Persomal_Information():
    # Verify Id
    drp_customer_status_notreq_id = "Customer Status"
    field_idno_notreq_id = "ID No."
    picker_doe_notreq_id = "//input[@name='Date of Expiry']"

    # Personal Information
    drp_title_req_id = "Title"
    field_first_name_req_id = "First Name"
    field_middle_name_notreq_id = "Middle Name"
    field_last_name_req_id = "Last Name"
    field_arabic_name_req_id = "Arabic Name"
    field_short_name_notreq_id = "Short Name"
    field_maiden_name_notreq_id = "Maiden Name"
    picker_dob_req_xpath = "//input[@name='Date of Birth']"
    drp_country_of_birth_req_id = "Country of Birth"
    drp_nationality_req_id = "Nationality"
    drp_citizenship_by_req_id = "Citizenship By"
    drp_country_of_residence_req_id = "Country of Residence"
    drp_residential_status_req_id = "Residential Status"
    drp_gender_req_id = "Gender"
    drp_marital_status_req_id = "Marital Status"
    drp_profession_req_id = "Profession"


    # buttons
    btn_verify_xpath = "(//button[@type='button'])[1]"
    btn_cancel_xpath = "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button"
    btn_cancel_confirm_xpath = "//button[normalize-space()='Yes']"
    btn_next_xpath = "(//button[normalize-space()='Next'])[1]"

    message = "//span[@class='error-message']"


    def __init__(self,driver):
        self.driver = driver

    # For Id Verifications
    def customerStatusDropdown_not_required(self):
        return self.driver.find_element(By.ID,self.drp_customer_status_notreq_id)

    def idNoField_not_required(self,id):
        self.driver.find_element(By.ID,self.field_idno_notreq_id).send_keys(id)

    def dateofexpiry_not_required(self,dobs):
        self.driver.find_element(By.XPATH,self.picker_doe_notreq_id).send_keys(dobs)

    def btnverify(self):
        self.driver.find_element(By.XPATH,self.btn_verify_xpath).click()

    # For Personal Information Validations

    def titleDropdown_required(self):
        return self.driver.find_element(By.ID,self.drp_title_req_id)

    def firstNameField_required(self, first_name):
        first = self.driver.find_element(By.ID,self.field_first_name_req_id)
        first.send_keys(first_name)

    def firstNameField_required_size(self):
        return self.driver.find_element(By.ID,self.field_first_name_req_id)

    def firstNameField_required_value(self):
        first = self.driver.find_element(By.ID,self.field_first_name_req_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def firstNameField_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_first_name_req_id)
        field_value = first.get_attribute('value')
        return field_value


    def first_clear(self):
        clear = self.driver.find_element(By.ID,self.field_first_name_req_id)
        clear.clear()

    def middleNameField_not_required(self,middlename):
        self.driver.find_element(By.ID,self.field_middle_name_notreq_id).send_keys(middlename)

    def middleNameField_not_required_size(self):
        return self.driver.find_element(By.ID,self.field_middle_name_notreq_id)

    def middle_clear(self):
        middle = self.driver.find_element(By.ID, self.field_middle_name_notreq_id)
        middle.clear()

    def middleNameField_not_required_value(self):
        first = self.driver.find_element(By.ID,self.field_middle_name_notreq_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def middleNameField_not_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_middle_name_notreq_id)
        field_value = first.get_attribute('value')
        return field_value

    def lastNameField_required(self,lastname):
        self.driver.find_element(By.ID,self.field_last_name_req_id).send_keys(lastname)

    def lastNameField_required_size(self):
        return self.driver.find_element(By.ID,self.field_last_name_req_id)

    def last_clear(self):
        last = self.driver.find_element(By.ID, self.field_last_name_req_id)
        last.clear()

    def lastNameField_required_value(self):
        first = self.driver.find_element(By.ID,self.field_last_name_req_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def lastNameField_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_last_name_req_id)
        field_value = first.get_attribute('value')
        return field_value

    def arabicNameFiels_required(self,arabic):
        self.driver.find_element(By.ID,self.field_arabic_name_req_id).send_keys(arabic)

    def arabicNameFiels_required_size(self,):
        return self.driver.find_element(By.ID,self.field_arabic_name_req_id)

    def arabic_clear(self):
        arabic = self.driver.find_element(By.ID, self.field_arabic_name_req_id)
        arabic.clear()

    def arabicNameFiels_required_value(self):
        first = self.driver.find_element(By.ID,self.field_arabic_name_req_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def arabicNameFiels_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_arabic_name_req_id)
        field_value = first.get_attribute('value')
        return field_value

    def shortNameField_not_required(self,shortname):
        self.driver.find_element(By.ID,self.field_short_name_notreq_id).send_keys(shortname)

    def shortNameField_not_required_size(self,):
        return self.driver.find_element(By.ID,self.field_short_name_notreq_id)

    def short_clear(self):
        short = self.driver.find_element(By.ID, self.field_short_name_notreq_id)
        short.clear()

    def shortNameField_not_required_value(self):
        first = self.driver.find_element(By.ID,self.field_short_name_notreq_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def shortNameField_not_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_short_name_notreq_id)
        field_value = first.get_attribute('value')
        return field_value

    def maidenNameFiels_not_required(self,maiden):
        self.driver.find_element(By.ID,self.field_maiden_name_notreq_id).send_keys(maiden)

    def maidenNameFiels_not_required_size(self):
        return self.driver.find_element(By.ID,self.field_maiden_name_notreq_id)

    def maiden_clear(self):
        maiden = self.driver.find_element(By.ID, self.field_maiden_name_notreq_id)
        maiden.clear()

    def maidenNameFiels_not_required_value(self):
        first = self.driver.find_element(By.ID,self.field_maiden_name_notreq_id)
        field_value = first.get_attribute('value')
        # Calculate and print the length of the value
        length_of_value = len(field_value)
        return length_of_value

    def maidenNameFiels_not_required_value_getting(self):
        first = self.driver.find_element(By.ID,self.field_maiden_name_notreq_id)
        field_value = first.get_attribute('value')
        return field_value

    def dobpicker_required(self,dob):
        self.driver.find_element(By.XPATH,self.picker_dob_req_xpath).send_keys(dob)

    def dobpicker_required_size(self):
        return self.driver.find_element(By.XPATH,self.picker_dob_req_xpath)
    def cobDropdown_required(self):
        return self.driver.find_element(By.ID,self.drp_country_of_birth_req_id)

    def nationality(self):
        return self.driver.find_element(By.ID,self.drp_nationality_req_id)

    def citizenship(self):
        return self.driver.find_element(By.ID,self.drp_citizenship_by_req_id)

    def countryofresidence(self):
        return self.driver.find_element(By.ID,self.drp_country_of_residence_req_id)

    def residentialstatus(self):
        return self.driver.find_element(By.ID,self.drp_residential_status_req_id)

    def gender(self):
        return self.driver.find_element(By.ID,self.drp_gender_req_id)

    def maritalstatus(self):
        return self.driver.find_element(By.ID,self.drp_marital_status_req_id)

    def profession(self):
        return self.driver.find_element(By.ID,self.drp_profession_req_id)

    def btncancel(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_xpath).click()

    def btn_canel_confirm(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_confirm_xpath).click()

    def btnnext(self):
        self.driver.find_element(By.XPATH,self.btn_next_xpath).click()

    def errorMessage(self):
        try:
            return self.driver.find_element(By.XPATH,self.message).text
        except:
            None


class Contact_Information():

    field_flat_housenumber_id = 'Flat/House Number'
    field_house_build_num_id = "House/Building Name"
    field_street_id = "Street"
    field_city_dist_id = "City/District"
    field_emirate_state_id = "Emirate/State"
    drp_country_id = "Country"
    drp_mobile_xpath = "//select[@class='countrySelector']"
    field_mobile_id = "Mobile Number"
    field_email = "Email"

    # Non-Resident

    non_field_flat_housenumber_id = 'Non Resident Flat'
    non_field_house_build_num_id = "Non Resident House"
    non_field_street_id = "Non Resident Street"
    non_field_city_dist_id = "Non Resident City"
    non_field_emirate_state_id = "Non Resident State"
    non_drp_country_id = "Non Resident Country"
    non_drp_visa_type_id = "Non Resident Visa Type"
    non_resi_visa_num_id = "Non Resident Visa Number"
    non_dat_pic_nonres_visa_issu_dat_name = "Non Resident Visa Issue Date"
    non_dat_pic_nonres_visa_expair_dat_name = "Non Resident Visa Expiry Date"
    remarks_id = "Remarks"



    # buttons
    btn_cancel_xpath = "//button[normalize-space()='Cancel']"
    btn_cancel_confirm_xpath = "//button[normalize-space()='Yes']"
    btn_cancel_no_xpath = "//button[normalize-space()='No']"
    btn_back_xpath = "//button[normalize-space()='Back']"
    btn_next_xpath = "//button[normalize-space()='Next']"

    # error mesaages


    # preview for personal information
    drp_preview_xpath = "//span[normalize-space()='Personal Information']"
    pre_title_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span[2]"
    pre_firstname_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/span[2]"
    pre_middlename_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/span[2]"
    pre_lastname_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/span[2]"
    pre_arabic_name_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[5]/span[2]"
    pre_short_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[6]/span[2]"
    pre_maiden_name_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[7]/span[2]"
    pre_dob_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[8]/span[2]"
    pre_cob_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[9]/span[2]"
    pre_nation_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[10]/span[2]"
    pre_citizen_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[11]/span[2]"
    pre_cor_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[12]/span[2]"
    pre_res_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[13]/span[2]"
    pre_gen_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[14]/span[2]"
    pre_marsta_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[15]/span[2]"
    pre_prof_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[16]/span[2]"

    def __init__(self,driver):
        self.driver = driver

    # 1
    def field_fh_num_required(self,flat):
        self.driver.find_element(By.ID, self.field_flat_housenumber_id).send_keys(flat)

    def field_fh_num_required_val(self):
        return self.driver.find_element(By.ID, self.field_flat_housenumber_id)

    def non_field_fh_num_required(self,flat):
        self.driver.find_element(By.ID, self.non_field_flat_housenumber_id).send_keys(flat)

    def non_field_fh_num_required_val(self):
        return self.driver.find_element(By.ID, self.non_field_flat_housenumber_id)

    def field_fh_num_required_clear(self):
        clr = self.driver.find_element(By.ID, self.field_flat_housenumber_id)
        clr.clear()

    # 2
    def field_hb_name_required(self,house):
        self.driver.find_element(By.ID, self.field_house_build_num_id).send_keys(house)

    def field_hb_name_required_val(self):
        return self.driver.find_element(By.ID, self.field_house_build_num_id)

    def non_field_hb_name_required(self,house):
        self.driver.find_element(By.ID, self.non_field_house_build_num_id).send_keys(house)

    def non_field_hb_name_required_val(self):
        return self.driver.find_element(By.ID, self.non_field_house_build_num_id)

    def field_hb_name_required_clear(self):
        clr = self.driver.find_element(By.ID, self.field_house_build_num_id)
        clr.clear()

    # 3

    def field_street_required(self,street):
        self.driver.find_element(By.ID, self.field_street_id).send_keys(street)

    def field_street_required_val(self):
        return self.driver.find_element(By.ID, self.field_street_id)

    def non_field_street_required(self,street):
        self.driver.find_element(By.ID, self.non_field_street_id).send_keys(street)

    def non_field_street_required_val(self):
        return self.driver.find_element(By.ID, self.non_field_street_id)

    def field_street_required_clear(self):
        clr = self.driver.find_element(By.ID, self.field_street_id)
        clr.clear()

    # 4

    def field_city_dist_required(self,city_dist):
        self.driver.find_element(By.ID, self.field_city_dist_id).send_keys(city_dist)

    def field_city_dist_required_val(self):
        return self.driver.find_element(By.ID, self.field_city_dist_id)

    def non_field_city_dist_required(self,city_dist):
        self.driver.find_element(By.ID, self.non_field_city_dist_id).send_keys(city_dist)

    def non_field_city_dist_required_value(self):
        return self.driver.find_element(By.ID, self.non_field_city_dist_id)

    def field_city_dist_required_clear(self):
        clr = self.driver.find_element(By.ID, self.field_city_dist_id)
        clr.clear()

    # 5

    def field_emin_dist(self,emin_dist):
        self.driver.find_element(By.ID, self.field_emirate_state_id).send_keys(emin_dist)

    def field_emin_dist_val(self):
        return self.driver.find_element(By.ID, self.field_emirate_state_id)

    def non_field_emin_dist(self,emin_dist):
        self.driver.find_element(By.ID, self.non_field_emirate_state_id).send_keys(emin_dist)

    def non_field_emin_dist_val(self):
        return self.driver.find_element(By.ID, self.non_field_emirate_state_id)

    def field_emin_state_clear(self):
        clr = self.driver.find_element(By.ID, self.field_emirate_state_id)
        clr.clear()

    # 6

    def drp_country_required(self):
        return self.driver.find_element(By.ID,self.drp_country_id)

    def non_drp_country_required(self):
        return self.driver.find_element(By.ID,self.non_drp_country_id)

    # 7

    def drp_mobile_required(self):
        return self.driver.find_element(By.XPATH, self.drp_mobile_xpath)

    def field_mobile_required(self,mobile):
        self.driver.find_element(By.NAME,self.field_mobile_id).send_keys(mobile)

    def field_mobile_required_val(self):
        return self.driver.find_element(By.NAME,self.field_mobile_id)

    def field_mobile_required_clear(self):
        clr = self.driver.find_element(By.ID,self.field_mobile_id)
        clr.clear()

    # 8

    def field_email_required(self,email):
        self.driver.find_element(By.ID, self.field_email).send_keys(email)

    def field_email_required_val(self):
        return self.driver.find_element(By.ID, self.field_email)

    def field_email_required_clear(self):
        clr = self.driver.find_element(By.ID, self.field_email)
        clr.clear()

    # Non
    def non_residen_visa_type_drp(self):
        return self.driver.find_element(By.ID, self.non_drp_visa_type_id)

    def non_residen_visa_number(self,vnum):
        self.driver.find_element(By.ID, self.non_resi_visa_num_id).send_keys(vnum)

    def non_residen_visa_number_val(self):
        return self.driver.find_element(By.ID, self.non_resi_visa_num_id)

    def non_residen_visa_issu_date(self,vidat):
        self.driver.find_element(By.NAME, self.non_dat_pic_nonres_visa_issu_dat_name).send_keys(vidat)

    def non_residen_visa_issu_date_val(self):
        return self.driver.find_element(By.NAME, self.non_dat_pic_nonres_visa_issu_dat_name)

    def non_residen_visa_expair_date(self,venum):
        self.driver.find_element(By.NAME, self.non_dat_pic_nonres_visa_expair_dat_name).send_keys(venum)

    def non_residen_visa_expair_date_val(self):
        return self.driver.find_element(By.NAME, self.non_dat_pic_nonres_visa_expair_dat_name)

    def remarks(self,remarks):
        self.driver.find_element(By.ID,self.remarks_id).send_keys(remarks)

    def remarks_val(self):
        return self.driver.find_element(By.ID,self.remarks_id)

    # buttons

    def btn_cancel(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_xpath).click()

    def btn_cancel_cfirm(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_confirm_xpath).click()

    def btn_cancel_no(self):
        self.driver.find_element(By.XPATH, self.btn_cancel_no_xpath).click()

    def btn_back(self):
        self.driver.find_element(By.XPATH,self.btn_back_xpath).click()

    def btn_next(self):
        self.driver.find_element(By.XPATH,self.btn_next_xpath).click()


   # preview
    def click_preview(self):
        self.driver.find_element(By.XPATH,self.drp_preview_xpath).click()

    def title(self):
        element = self.driver.find_element(By.XPATH, self.pre_title_xpath)
        return element.get_attribute('title')

    def firstname(self):
        element = self.driver.find_element(By.XPATH, self.pre_firstname_xpath)
        return element.get_attribute('title')
    def middlename(self):
        element = self.driver.find_element(By.XPATH, self.pre_middlename_xpath)
        return element.get_attribute('title')
    def lastname(self):
        element = self.driver.find_element(By.XPATH, self.pre_lastname_xpath)
        return element.get_attribute('title')

    def arabicname(self):
        element = self.driver.find_element(By.XPATH, self.pre_arabic_name_xpath)
        return element.get_attribute('title')

    def shortname(self):
        element = self.driver.find_element(By.XPATH, self.pre_short_xpath)
        return element.get_attribute('title')

    def maidenname(self):
        element = self.driver.find_element(By.XPATH, self.pre_maiden_name_xpath)
        return element.get_attribute('title')

    def dob(self):
        element = self.driver.find_element(By.XPATH, self.pre_dob_xpath)
        return element.get_attribute('title')

    def cob(self):
        element = self.driver.find_element(By.XPATH, self.pre_cob_xpath)
        return element.get_attribute('title')

    def natinality(self):
        element = self.driver.find_element(By.XPATH, self.pre_nation_xpath)
        return element.get_attribute('title')

    def citizen(self):
        element = self.driver.find_element(By.XPATH, self.pre_citizen_xpath)
        return element.get_attribute('title')

    def cor(self):
        element = self.driver.find_element(By.XPATH, self.pre_cor_xpath)
        return element.get_attribute('title')

    def res(self):
        element = self.driver.find_element(By.XPATH, self.pre_res_xpath)
        return element.get_attribute('title')

    def gender(self):
        element = self.driver.find_element(By.XPATH, self.pre_gen_xpath)
        return element.get_attribute('title')

    def marristatus(self):
        element = self.driver.find_element(By.XPATH, self.pre_marsta_xpath)
        return element.get_attribute('title')

    def profesion(self):
        element = self.driver.find_element(By.XPATH, self.pre_prof_xpath)
        return element.get_attribute('title')


class Id_details():
    click = "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/div[1]"

    drp_id_type_id = "ID Type"
    field_place_of_id_issue_id = "Place of ID Issue"
    field_id_nmuber_id = "ID Number"
    da_pick_id_issue_date_name = "ID Issue Date"
    da_pick_id_expaire_date_name = "ID Expiry Date"
    drp_place_of_passport_issue_id = "Place of Passport Issue"
    field_passport_number_id = "Passport Number"
    da_pick_pass_issue_date_name = "Passport Issue Date"
    da_pick_pass_exp_date_xpath = "//input[@name='Passport Expiry Date']"

#   Dual natinality
    toggle_btn_dual_nation_id = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div/input"

    drp_nation_id = "Nationality 2"
    drp_pla_of_passport_iss_id = "Place of Passport 2 Issue"
    field_pass_num = "Passport 2 Number"
    da_pick_pass_iss_date_name = "Passport 2 Issue Date"
    da_pick_pass_exp_date_name = "Passport 2 Expiry Date"

#     Preview
    pre_ci_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/span"

    pre_fh_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2]"
    pre_hb_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[2]"
    pre_stre_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/span[2]"
    pre_cidi_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/span[2]"
    pre_emist_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/span[2]"
    pre_con_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[6]/span[2]"
    pre_mob_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[7]/span[2]"
    pre_email_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[8]/span[2]"

    # Non-Residental
    pre_fh_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[11]/span[2]"
    pre_hb_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[12]/span[2]"
    pre_stre_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[13]/span[2]"
    pre_cidi_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[14]/span[2]"
    pre_emist_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[15]/span[2]"
    pre_con_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[16]/span[2]"
    pre_vtype_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[17]/span[2]"
    pre_vnum_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[18]/span[2]"
    pre_v_isdat_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[19]/span[2]"
    pre_v_exdat_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[20]/span[2]"
    pre_remar_non_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[21]/span[2]"

#   Buttons

    btn_cancel_xpath = "(//button[normalize-space()='Cancel'])[1]"
    btn_cancel_no = "//button[normalize-space()='No']"
    btn_cancel_yes = "/html/body/div[1]/div[1]/div/div/div/div/div/button[2]"

    btn_back_xpath = "//button[@class='m-2 button-custom variant-outline size-undefined']"
    btn_next_xpath = "//button[normalize-space()='Next']"

    def __init__(self, driver):
        self.driver = driver

    def visible_id(self):
        element = self.driver.find_element(By.XPATH,self.btn_next_xpath)
        dis = element.is_displayed()
        return dis

    # ID Details
    def id_type_field_req(self):
        return self.driver.find_element(By.ID,self.drp_id_type_id)

    def place_of_id_issue_field_req(self):
        return self.driver.find_element(By.ID,self.field_place_of_id_issue_id)

    def id_number_field_req(self):
        return self.driver.find_element(By.ID,self.field_id_nmuber_id)

    def id_issue_date_dpick_req(self):
        return self.driver.find_element(By.NAME,self.da_pick_id_issue_date_name)

    def id_expaire_date_dpick_req(self):
        return self.driver.find_element(By.NAME,self.da_pick_id_expaire_date_name)

    def place_of_passport_isse_drp_req(self):
        return self.driver.find_element(By.ID,self.drp_place_of_passport_issue_id)

    def passport_numb_field_req(self):
        return self.driver.find_element(By.ID, self.field_passport_number_id)

    def passport_issue_date_dpick_req(self):
        return self.driver.find_element(By.NAME,self.da_pick_pass_issue_date_name)

    def passport_expi_date_dpick_req(self):
        return self.driver.find_element(By.XPATH,self.da_pick_pass_exp_date_xpath)

    # Dual nationality toggle

    def toggle(self):
        return self.driver.find_element(By.XPATH, self.toggle_btn_dual_nation_id)

    def nationality_drp_req_dual(self):
        return self.driver.find_element(By.ID, self.drp_nation_id)

    def place_of_pass_issue_drp_req_dual(self):
        return self.driver.find_element(By.ID,self.drp_pla_of_passport_iss_id)

    def passport_num_req_dual(self):
        return self.driver.find_element(By.ID, self.field_pass_num)

    def passport_issue_date_dpick_req_dual(self):
        return self.driver.find_element(By.NAME,self.da_pick_pass_iss_date_name)

    def passport_expai_date_dpick_req_dual(self):
        return self.driver.find_element(By.NAME,self.da_pick_pass_exp_date_name)

    # Buttons

    def btn_next(self):
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()


    def btn_back_id(self):
        attempts = 0
        while attempts < 3:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.btn_back_xpath))
                )
                element.click()
                return
            except StaleElementReferenceException:
                attempts += 1
        # If all attempts fail, find and click the element directly
        self.driver.find_element(By.XPATH, self.btn_back_xpath).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, self.btn_cancel_xpath).click()

    def btn_cancel_conf(self):
        self.driver.find_element(By.XPATH, self.btn_cancel_yes).click()


# Preview

    def drp_ci_pre(self):
        self.driver.find_element(By.XPATH,self.pre_ci_xpath).click()

    def fh_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_fh_xpath)
        return element.get_attribute('title')

    def hb_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_hb_xpath)
        return element.get_attribute('title')
    def stre_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_stre_xpath)
        return element.get_attribute('title')
    def cidi_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_cidi_xpath)
        return element.get_attribute('title')
    def emist_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_emist_xpath)
        return element.get_attribute('title')
    def con_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_con_xpath)
        return element.get_attribute('title')
    def mob_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_mob_xpath)
        return element.get_attribute('title')
    def email_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_email_xpath)
        return element.get_attribute('title')

    #Non-Residental

    def fh_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_fh_non_xpath)
        return element.get_attribute('title')

    def hb_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_hb_non_xpath)
        return element.get_attribute('title')

    def stre_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_stre_non_xpath)
        return element.get_attribute('title')

    def cidi_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_cidi_non_xpath)
        return element.get_attribute('title')

    def emist_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_emist_non_xpath)
        return element.get_attribute('title')

    def con_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_con_non_xpath)
        return element.get_attribute('title')

    def vtype_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_vtype_non_xpath)
        return element.get_attribute('title')

    def vnum_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_vnum_non_xpath)
        return element.get_attribute('title')

    def v_isdat_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_v_isdat_non_xpath)
        return element.get_attribute('title')

    def v_exdat_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_v_exdat_non_xpath)
        return element.get_attribute('title')

    def remar_isdat_non_pre(self):
        element = self.driver.find_element(By.XPATH, self.pre_remar_non_xpath)
        return element.get_attribute('title')


class Other_Information():
    btn_next_xpath = "//button[normalize-space()='Next']"

    btn_back_xpath = "//button[normalize-space()='Back']"

    id_details_drp = "//span[normalize-space()='ID Details']"

    # preview
    passport_num = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[1]/span[2]"
    place_of_passport_issue = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/span[2]"
    passport_issue_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/span[2]"
    passport_expaire_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[4]/span[2]"
    id_type = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[5]/span[2]"
    id_num = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[6]/span[2]"
    place_of_id_issue = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[7]/span[2]"
    id_issue_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[8]/span[2]"
    id_expaire_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[9]/span[2]"

    nationality = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[12]/span[2]"
    place_of_passport_issue_dual = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[13]/span[2]"
    passport_num_dual = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[14]/span[2]"
    passport_issue_date_dual = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[15]/span[2]"
    passport_expaire_date_dual = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[16]/span[2]"

    #
    drp_org_category_id = "Organization Category"
    designation_id = "Designation"
    employer_id = "Employer"
    employer_description_id = "Employer Description"
    source_of_income_id = "Source Of Income"
    salary_range_id = "Salary Range"
    annual_income_id = "Annual Income"
    drp_purpose_id = "Purpose"
    loyalty_card_no_id = "Loyalty Card Number"
    drp_categoty_id = "Category"
    points_id = "Points"
    toggle_other_source_of_income_id = "Other Sources of Income?"
    drp_secondary_income_source_id = "Secondary Income Source"
    drp_secondary_income_range_id = "Secondary Income Range"
    drp_demographics_id = "Demographics"
    drp_industry_type_id = "Industry Type"
    drp_employment_id = "Employment"
    drp_employee_type_id = "Employee Type"
    professional_email_id = "Professional Email ID"
    drp_cb_purpose_id = "CB Purpose"
    drp_customer_nearest_airport_id = "Customer Nearest Airport"
    fax_id = "Fax"
    drp_customer_segment = "Customer Segment"
    drp_role_id = "Role"
    additional_remarks_id = "Add Info Remarks"
    checkbox_specialneeds_name = "Special Needs"
    drp_details_of_spcial_needs_id = "Details of Special Needs"
    remarks_of_sp_needs_name = "Details Remarks"
    is_pef_toggle_id = "Is PEP ?"
    pep_remarks_id = "PEP Remarks"
    checkbox_remittance_name = "Interested remittance Products"
    checkbox_forex_name = "Interested forex Products"
    checkbox_utility_name = "Interested utility Products"
    checkbox_equity_name = "Interested Equity Products"

    drp_relation_type = "Relationship Type"
    search_customer_id = "floatingSearch"
    select_customer_xpath = "//img[@alt='PlusIcon']"

    company_name_id = "Company Name"
    location_id = "Location"
    drp_percentage_holding_id = "Percentage Holding"
    drp_annal_income_currency_id = "Annual Income Currency"
    annal_incom_ammount_id = "Annual Income Amount"
    line_of_bussiness_id = "Line of Business"

    # btns

    clear_btn_xpath = "//button[normalize-space()='Clear']"
    add_btn_xpath = "//button[normalize-space()='Add']"

    drp_application_priority_id = "Application Priority"

    whatsapp_number_id = "Whatsapp Number"
    facebook_user_id = "Facebook Username"
    x_user_id = "X Username"
    insta_user_id = "Instagram Username"
    linked_user_id = "Linkedin Username"
    website_id = "Website"

    institution_name_id = "Institution Name"
    drp_institution_type_id = "Institution Type"
    drp_membership_id = "Membership Type"

    check_email_name = "Marketing Email"
    check_sms_name = "Marketing SMS"
    check_whatsapp_name = "Marketing Whatsapp"
    check_phone_name = "Marketing Phone"
    check_fax_name = "Marketing Fax"
    check_postal_name = "Marketing Postal ID"
    check_promotions_name = "I agree to recieve marketing messages Including offers and promotions."

    check_privacy_policy_name = "I hereby agree to the terms and conditions of this exchange"

    boc_click = "//div[@class='added-list-items-wrapper']"

    # btns
    cancel_btn_xpath = "//button[normalize-space()='Cancel']"
    cancel_confirm_btn_xpath = "//button[normalize-space()='Yes']"


    def __init__(self, driver):
        self.driver = driver

    def req_drp_organzation_category(self):
        return self.driver.find_element(By.ID, self.drp_org_category_id)

    def drp_designation(self):
        return self.driver.find_element(By.ID, self.designation_id)

    def employer(self):
        return self.driver.find_element(By.ID, self.employer_id)

    def employer_description(self):
        return self.driver.find_element(By.ID, self.employer_description_id)

    def drp_source_of_income(self):
        return self.driver.find_element(By.ID, self.source_of_income_id)

    def drp_salary_range(self):
        return self.driver.find_element(By.ID, self.salary_range_id)

    def annual_income(self):
        return self.driver.find_element(By.ID, self.annual_income_id)

    def drp_purpose(self):
        return self.driver.find_element(By.ID, self.drp_purpose_id)

    def loyalty_card_no(self):
        return self.driver.find_element(By.ID, self.loyalty_card_no_id)

    def drp_categoty(self):
        return self.driver.find_element(By.ID, self.drp_categoty_id)

    def req_points(self):
        return self.driver.find_element(By.ID, self.points_id)

    def toggle_other_source_of_income(self):
        return self.driver.find_element(By.ID, self.toggle_other_source_of_income_id)

    def drp_secondary_income_source(self):
        return self.driver.find_element(By.ID, self.drp_secondary_income_source_id)

    def drp_secondary_income_range(self):
        return self.driver.find_element(By.ID, self.drp_secondary_income_range_id)

    def drp_demographics(self):
        return self.driver.find_element(By.ID, self.drp_demographics_id)

    def drp_industry_type(self):
        return self.driver.find_element(By.ID, self.drp_industry_type_id)

    def drp_employment(self):
        return self.driver.find_element(By.ID, self.drp_employment_id)

    def drp_employee_type(self):
        return self.driver.find_element(By.ID, self.drp_employee_type_id)

    def professional_email(self):
        return self.driver.find_element(By.ID, self.professional_email_id)

    def drp_cb_purpose(self):
        return self.driver.find_element(By.ID, self.drp_cb_purpose_id)

    def drp_customer_nearest_airport(self):
        return self.driver.find_element(By.ID, self.drp_customer_nearest_airport_id)

    def fax(self):
        return self.driver.find_element(By.ID, self.fax_id)

    def drp_cusomer_segment(self):
        return self.driver.find_element(By.ID, self.drp_customer_segment)

    def drp_role(self):
        return self.driver.find_element(By.ID, self.drp_role_id)

    def additional_remarks(self):
        return self.driver.find_element(By.ID, self.additional_remarks_id)

    def check_special_needs(self):
        return self.driver.find_element(By.NAME, self.checkbox_specialneeds_name)

    def drp_details_of_spcial_needs(self):
        return self.driver.find_element(By.ID, self.drp_details_of_spcial_needs_id)

    def remarks_of_sp_needs(self):
        return self.driver.find_element(By.NAME, self.remarks_of_sp_needs_name)

    def toggle_is_pef(self):
        return self.driver.find_element(By.ID, self.is_pef_toggle_id)

    def pep_remarks(self):
        return self.driver.find_element(By.ID, self.pep_remarks_id)

    def checkbox_remittance_products(self):
        return self.driver.find_element(By.NAME, self.checkbox_remittance_name)

    def checkbox_forex(self):
        return self.driver.find_element(By.NAME, self.checkbox_forex_name)

    def checkbox_utility(self):
        return self.driver.find_element(By.NAME, self.checkbox_utility_name)

    def checkbox_equity(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, self.checkbox_equity_name))
        )

        # Locate and return the checkbox element
        return self.driver.find_element(By.NAME, self.checkbox_equity_name)

    def drp_relationship_type(self):
        return self.driver.find_element(By.ID,self.drp_relation_type)

    def search_customer(self):
        return self.driver.find_element(By.ID, self.search_customer_id)

    def select_customer(self):
        return self.driver.find_element(By.XPATH, self.select_customer_xpath)

    def company_name(self):
        return self.driver.find_element(By.ID, self.company_name_id)

    def location(self):
        return self.driver.find_element(By.ID, self.location_id)

    def drp_percentage_holding(self):
        return self.driver.find_element(By.ID, self.drp_percentage_holding_id)

    def drp_annual_income_currency(self):
        return self.driver.find_element(By.ID, self.drp_annal_income_currency_id)

    def drp_annual_income_frequency(self):
        return self.driver.find_element(By.ID, self.annal_incom_ammount_id)

    def line_of_bussiness(self):
        return self.driver.find_element(By.ID, self.line_of_bussiness_id)

    def click_boc(self):
        return self.driver.find_element(By.XPATH,self.boc_click)

    def btn_clear(self):
        return self.driver.find_element(By.XPATH, self.clear_btn_xpath)

    def btn_add(self):
        return self.driver.find_element(By.XPATH, self.add_btn_xpath)

    def drp_application_priority(self):
        return self.driver.find_element(By.ID, self.drp_application_priority_id)

    def whatsapp(self):
        return self.driver.find_element(By.ID, self.whatsapp_number_id)

    def facebook(self):
        return self.driver.find_element(By.ID, self.facebook_user_id)

    def x(self):
        return self.driver.find_element(By.ID, self.x_user_id)

    def insta(self):
        return self.driver.find_element(By.ID,self.insta_user_id)

    def linkedin(self):
        return self.driver.find_element(By.ID, self.linked_user_id)

    def website(self):
        return self.driver.find_element(By.ID, self.website_id)

    def btn_next(self):
        return self.driver.find_element(By.XPATH, self.btn_next_xpath)

    def institution_name(self):
        return self.driver.find_element(By.ID, self.institution_name_id)

    def drp_institution_type(self):
        return self.driver.find_element(By.ID, self.drp_institution_type_id)

    def drp_mebmership(self):
        return self.driver.find_element(By.ID, self.drp_membership_id)

    def check_email(self):
        return self.driver.find_element(By.NAME, self.check_email_name)

    def check_sms(self):
        return self.driver.find_element(By.NAME, self.check_sms_name)

    def check_whatsapp(self):
        return self.driver.find_element(By.NAME, self.check_whatsapp_name)

    def check_phone(self):
        return self.driver.find_element(By.NAME, self.check_phone_name)

    def check_fax(self):
        return self.driver.find_element(By.NAME, self.check_fax_name)

    def check_postid(self):
        return self.driver.find_element(By.NAME, self.check_postal_name)

    def check_promotions(self):
        return self.driver.find_element(By.NAME, self.check_promotions_name)

    def check_privacy_info(self):
        return self.driver.find_element(By.NAME, self.check_privacy_policy_name)

    def click_id_details_drp(self):
        self.driver.find_element(By.XPATH, self.id_details_drp).click()

    def passport_num_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_num).text

    def place_of_passport_issue_pre(self):
        return self.driver.find_element(By.XPATH, self.place_of_passport_issue).text

    def passport_issue_date_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_issue_date).text

    def passport_expaire_date_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_expaire_date).text

    def id_type_pre(self):
        return self.driver.find_element(By.XPATH, self.id_type).text

    def id_num_pre(self):
        return self.driver.find_element(By.XPATH, self.id_num).text

    def place_of_id_issue_pre(self):
        return self.driver.find_element(By.XPATH, self.place_of_id_issue).text

    def id_issue_date_pre(self):
        return self.driver.find_element(By.XPATH, self.id_issue_date).text

    def id_expaire_date_pre(self):
        return self.driver.find_element(By.XPATH, self.id_expaire_date).text

    def nationality_pre(self):
        return self.driver.find_element(By.XPATH, self.nationality).text

    def place_of_passport_issue_dual_pre(self):
        return self.driver.find_element(By.XPATH, self.place_of_passport_issue_dual).text

    def passport_num_dual_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_num_dual).text

    def passport_issue_date_dual_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_issue_date_dual).text

    def passport_expaire_date_dual_pre(self):
        return self.driver.find_element(By.XPATH, self.passport_expaire_date_dual).text

    def btn_back(self):
        attempts = 0
        while attempts < 3:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.btn_back_xpath))
                )
                element.click()
                return
            except StaleElementReferenceException:
                attempts += 1
        # If all attempts fail, find and click the element directly
        self.driver.find_element(By.XPATH, self.btn_back_xpath).click()

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH,self.cancel_btn_xpath)

    def btn_cancel_confirm(self):
        return self.driver.find_element(By.XPATH, self.cancel_confirm_btn_xpath)


class Upload_documents():
    btn_back_xpath = "//button[normalize-space()='Back']"

    # Preview for Other Information
    org_category = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[1]/span[2]"
    designation = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[2]/span[2]"
    employer = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[3]/span[2]"
    employer_discri = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[4]/span[2]"
    source_of_incom = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[5]/span[2]"
    salary_range = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[6]/span[2]"
    annual_income = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[7]/span[2]"
    purpose = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[8]/span[2]"
    loyalty_card_number = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[9]/span[2]"
    category = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[10]/span[2]"
    points = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[11]/span[2]"
    second_income_source = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[12]/span[2]"
    second_income_range = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[13]/span[2]"
    demographic = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[14]/span[2]"
    indu_type = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[15]/span[2]"
    employement = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[16]/span[2]"
    employement_type = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[17]/span[2]"
    email = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[18]/span[2]"
    # remittance_vol = ""
    # remittance_freq = ""
    # fc_volume = ""
    # fc_frequency = ""
    cb_purpose = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[23]/span[2]"
    cust_nearest_airport = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[24]/span[2]"
    fax = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[25]/span[2]"
    cust_segment = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[26]/span[2]"
    role = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[27]/span[2]"
    add_info_remarks = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[28]/span[2]"
    sp_needs = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[29]/span[2]"
    detail_sp_needs = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[30]/span[2]"
    is_PEP = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[32]/span[2]"
    PEP_remarks = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[33]/span[2]"
    interested_product_remitance = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[53]/span[2]"
    interested_product_forex = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[54]/span[2]"
    interested_product_utility = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[55]/span[2]"

    company_name = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[2]/span[2]"
    location = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[3]/span[2]"
    percentage_holding = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[4]/span[2]"
    annual_income_currency = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[6]/span[2]"
    annual_income_amount = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[6]/span[2]"
    line_of_business = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[57]/div[7]/span[2]"
    application_priority = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[34]/span[2]"

    whataapp = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[35]/span[2]"
    fb = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[36]/span[2]"
    x = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[37]/span[2]"
    insta = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[38]/span[2]"
    linked_in = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[39]/span[2]"
    website = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[40]/span[2]"

    institute_name = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[48]/span[2]"
    institute_type = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[49]/span[2]"
    mebership_type = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[50]/span[2]"

    marketing_mail = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[41]/span[2]"
    marketing_sms = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[42]/span[2]"
    marketing_whatsaapp = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[43]/span[2]"
    marketing_phone = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[44]/span[2]"
    marketing_fax = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[45]/span[2]"
    marketing_postal_id = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[46]/span[2]"

    marketing_aggrement = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[58]/span[2]"
    privacy_aggrement = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]/div[2]/div[59]/span[2]"

    other_info = "//span[normalize-space()='Other Information']"

    def __init__(self, driver):
        self.driver = driver

    def btn_back(self):
        self.driver.find_element(By.XPATH,self.btn_back_xpath).click()

    def click_other_info_pre(self):
        self.driver.find_element(By.XPATH, self.other_info).click()

    # Preview
    def org_category_pre(self):
        return self.driver.find_element(By.XPATH, self.org_category).text

    def designation_pre(self):
        return self.driver.find_element(By.XPATH, self.designation).text

    def employer_pre(self):
        return self.driver.find_element(By.XPATH, self.employer).text

    def employer_discri_pre(self):
        return self.driver.find_element(By.XPATH, self.employer_discri).text

    def source_of_incom_pre(self):
        return self.driver.find_element(By.XPATH, self.source_of_incom).text

    def salary_range_pre(self):
        return self.driver.find_element(By.XPATH, self.salary_range).text

    def annual_income_pre(self):
        return self.driver.find_element(By.XPATH, self.annual_income).text

    def purpose_pre(self):
        return self.driver.find_element(By.XPATH, self.purpose).text

    def loyalty_card_number_pre(self):
        return self.driver.find_element(By.XPATH, self.loyalty_card_number).text

    def category_pre(self):
        return self.driver.find_element(By.XPATH, self.category).text

    def points_pre(self):
        return self.driver.find_element(By.XPATH, self.points).text

    def second_income_source_pre(self):
        return self.driver.find_element(By.XPATH, self.second_income_source).text

    def second_income_range_pre(self):
        return self.driver.find_element(By.XPATH, self.second_income_range).text

    def demographic_pre(self):
        return self.driver.find_element(By.XPATH, self.demographic).text

    def indu_type_pre(self):
        return self.driver.find_element(By.XPATH, self.indu_type).text

    def employement_pre(self):
        return self.driver.find_element(By.XPATH, self.employement).text

    def employement_type_pre(self):
        return self.driver.find_element(By.XPATH, self.employement_type).text

    # TODO:
    def email_pre(self):
        return self.driver.find_element(By.XPATH, self.email).text

    def cb_purpose_pre(self):
        return self.driver.find_element(By.XPATH, self.cb_purpose).text

    def cust_nearest_airport_pre(self):
        return self.driver.find_element(By.XPATH, self.cust_nearest_airport).text

    def fax_pre(self):
        return self.driver.find_element(By.XPATH, self.fax).text

    def cust_segment_pre(self):
        return self.driver.find_element(By.XPATH, self.cust_segment).text

    def role_pre(self):
        return self.driver.find_element(By.XPATH, self.role).text

    def add_info_remarks_pre(self):
        return self.driver.find_element(By.XPATH, self.add_info_remarks).text

    def sp_needs_pre(self):
        return self.driver.find_element(By.XPATH, self.sp_needs).text

    def detail_sp_needs_pre(self):
        return self.driver.find_element(By.XPATH, self.detail_sp_needs).text

    def is_PEP_pre(self):
        return self.driver.find_element(By.XPATH, self.is_PEP).text

    def PEP_remarks_pre(self):
        return self.driver.find_element(By.XPATH, self.PEP_remarks).text

    def interested_product_remitance_pre(self):
        return self.driver.find_element(By.XPATH, self.interested_product_remitance).text

    def interested_product_forex_pre(self):
        return self.driver.find_element(By.XPATH, self.interested_product_forex).text

    def interested_product_utility_pre(self):
        return self.driver.find_element(By.XPATH, self.interested_product_utility).text

    def company_name_pre(self):
        return self.driver.find_element(By.XPATH, self.company_name).text

    def location_pre(self):
        return self.driver.find_element(By.XPATH, self.location).text

    def percentage_holding_pre(self):
        return self.driver.find_element(By.XPATH, self.percentage_holding).text

    def annual_income_currency_pre(self):
        return self.driver.find_element(By.XPATH, self.annual_income_currency).text

    def annual_income_amount_pre(self):
        return self.driver.find_element(By.XPATH, self.annual_income_amount).text

    def line_of_business_pre(self):
        return self.driver.find_element(By.XPATH, self.line_of_business).text

    def application_priority_pre(self):
        return self.driver.find_element(By.XPATH, self.application_priority).text

    def whataapp_pre(self):
        return self.driver.find_element(By.XPATH, self.whataapp).text

    def fb_pre(self):
        return self.driver.find_element(By.XPATH, self.fb).text

    def x_pre(self):
        return self.driver.find_element(By.XPATH, self.x).text

    # Todo:

    def insta_pre(self):
        return self.driver.find_element(By.XPATH, self.insta).text

    def linked_in_pre(self):
        return self.driver.find_element(By.XPATH, self.linked_in).text

    def website_pre(self):
        return self.driver.find_element(By.XPATH, self.website).text

    def institute_name_pre(self):
        return self.driver.find_element(By.XPATH, self.institute_name).text

    def institute_type_pre(self):
        return self.driver.find_element(By.XPATH, self.institute_type).text

    def mebership_type_pre(self):
        return self.driver.find_element(By.XPATH, self.mebership_type).text

    def marketing_mail_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_mail).text

    def marketing_sms_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_sms).text

    def marketing_whatsaapp_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_whatsaapp).text

    def marketing_phone_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_phone).text

    def marketing_fax_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_fax).text

    def marketing_fax_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_fax).text

    def marketing_postal_id_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_postal_id).text

    def marketing_aggrement_pre(self):
        return self.driver.find_element(By.XPATH, self.marketing_aggrement).text

    def privacy_aggrement_pre(self):
        return self.driver.find_element(By.XPATH, self.privacy_aggrement).text
