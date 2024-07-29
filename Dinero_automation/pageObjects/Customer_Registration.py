from selenium.webdriver.common.by import By

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
    # btn_verify_xpath = "(//button[@type='button'])[1]"
    btn_cancel_xpath = "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button"
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

    def first_clear(self):
        clear = self.driver.find_element(By.ID,self.field_first_name_req_id)
        clear.clear()

    def middleNameField_not_required(self,middlename):
        self.driver.find_element(By.ID,self.field_middle_name_notreq_id).send_keys(middlename)

    def middle_clear(self):
        middle = self.driver.find_element(By.ID, self.field_middle_name_notreq_id)
        middle.clear()

    def lastNameField_required(self,lastname):
        self.driver.find_element(By.ID,self.field_last_name_req_id).send_keys(lastname)

    def last_clear(self):
        last = self.driver.find_element(By.ID, self.field_last_name_req_id)
        last.clear()

    def arabicNameFiels_required(self,arabic):
        self.driver.find_element(By.ID,self.field_arabic_name_req_id).send_keys(arabic)

    def arabic_clear(self):
        arabic = self.driver.find_element(By.ID, self.field_arabic_name_req_id)
        arabic.clear()

    def shortNameField_not_required(self,shortname):
        self.driver.find_element(By.ID,self.field_short_name_notreq_id).send_keys(shortname)

    def short_clear(self):
        short = self.driver.find_element(By.ID, self.field_short_name_notreq_id)
        short.clear()

    def maidenNameFiels_not_required(self,maiden):
        self.driver.find_element(By.ID,self.field_maiden_name_notreq_id).send_keys(maiden)

    def maiden_clear(self):
        maiden = self.driver.find_element(By.ID, self.field_maiden_name_notreq_id)
        maiden.clear()

    def dobpicker_required(self,dob):
        self.driver.find_element(By.XPATH,self.picker_dob_req_xpath).send_keys(dob)

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

    def btnnext(self):
        self.driver.find_element(By.XPATH,self.btn_next_xpath).click()

    def errorMessage(self):
        try:
            self.driver.find_element(By.XPATH,self.message).text
        except:
            None


class Contact_Information():

    field_flat_housenumber_id = 'Flat/House Number'
    field_house_build_num_id = "House/Building Name"
    field_street_id = "Street"
    field_city_dist_id = "City/District"
    field_emirate_state_id = "Emirate/State"
    drp_country_id = "Country"
    drp_phone_id = "phoneInputField"
    field_email = "Email"

    # buttons
    btn_cancel_xpath = "//button[normalize-space()='Cancel']"
    btn_back_xpath = "//button[normalize-space()='Back']"
    btn_next_xpath = "//button[normalize-space()='Next']"

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

    def field_flat_house_required(self,flat):
        self.driver.find_element(By.ID, self.field_flat_housenumber_id).send_keys(flat)

    def field_house_build_num_required(self,house):
        self.driver.find_element(By.ID, self.field_house_build_num_id).send_keys(house)

    def field_street_required(self,street):
        self.driver.find_element(By.ID, self.field_street_id).send_keys(street)

    def field_city_dist_required(self,city_dist):
        self.driver.find_element(By.ID, self.field_city_dist_id).send_keys(city_dist)

    def field_emin_dist(self,emin_dist):
        self.driver.find_element(By.ID, self.field_emirate_state_id).send_keys(emin_dist)

    def drp_country_required(self):
        return self.driver.find_element(By.ID,self.drp_country_id)

    def drp_mobile_required(self):
        return self.driver.find_element(By.ID,self.drp_phone_id)

    def field_email_required(self,email):
        self.driver.find_element(By.ID, self.field_email).send_keys(email)

    # buttons

    def btn_cancel(self):
        self.driver.find_element(By.XPATH,self.btn_cancel_xpath).click()

    def btn_back(self):
        self.driver.find_element(By.XPATH,self.btn_back_xpath).click()

    # def btn_next(self):
    #     self.driver.find_element(By.XPATH,self.btn_next_xpath).click()


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
    pass



class Other_Information():
    pass

class Upload_documents():
    pass