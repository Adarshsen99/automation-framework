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
    btn_verify_xpath = "(//button[@type='button'])[1]"
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
        self.driver.find_element(By.ID,self.field_first_name_req_id).send_keys(first_name)

    def middleNameField_not_required(self,middlename):
        self.driver.find_element(By.ID,self.field_middle_name_notreq_id).send_keys(middlename)

    def lastNameField_required(self,lastname):
        self.driver.find_element(By.ID,self.field_last_name_req_id).send_keys(lastname)

    def arabicNameFiels_required(self,arabic):
        self.driver.find_element(By.ID,self.field_arabic_name_req_id).send_keys(arabic)

    def shortNameField_not_required(self,shortname):
        self.driver.find_element(By.ID,self.field_short_name_notreq_id).send_keys(shortname)

    def maidenNameFiels_not_required(self,maiden):
        self.driver.find_element(By.ID,self.field_maiden_name_notreq_id).send_keys(maiden)

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

    flat_housenumber_id = 'Flat/House Number'

    def __init__(self,driver):
        self.driver = driver

    def flat_house_required(self):
        return self.driver.find_element(By.ID,self.flat_housenumber_id)


class Id_details():
    pass



class Other_Information():
    pass

class Upload_documents():
    pass