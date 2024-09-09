from selenium.webdriver.common.by import By

class Company_Information_Edit:
    company_name_id = "Company Name"
    arabic_name_id = "Arabic Name"
    building_number_id = "Building Number"
    building_name_id = "Building Name"
    street_id = "Street"
    postal_code_id = "Postal Code"
    city_district_id = "City/District"
    country_id = "Country"
    drp_mobile_xpath = "//select[@class='countrySelector']"
    mobile_num_name = "Mobile Number"
    email_id = "Email"

    next = "(//button[normalize-space()='Next'])[1]"
    cancel = "//button[normalize-space()='Cancel']"
    cancel_confirm = "//button[normalize-space()='Yes']"
    cancel_no = "//button[normalize-space()='No']"

    message = "//span[@class='error-message']"

    def __init__(self,driver):
        self.driver = driver

    def company_name(self):
        return self.driver.find_element(By.ID,self.company_name_id)

    def arabic_name(self):
        return self.driver.find_element(By.ID,self.arabic_name_id)

    def building_number(self):
        return self.driver.find_element(By.ID,self.building_number_id)

    def building_name(self):
        return self.driver.find_element(By.ID,self.building_name_id)

    def street(self):
        return self.driver.find_element(By.ID,self.street_id)

    def postal_code(self):
        return self.driver.find_element(By.ID,self.postal_code_id)

    def city_district(self):
        return self.driver.find_element(By.ID,self.city_district_id)

    def country(self):
        return self.driver.find_element(By.ID,self.country_id)

    def drp_mobile(self):
        return self.driver.find_element(By.XPATH,self.drp_mobile_xpath)

    def mobile_num(self):
        return self.driver.find_element(By.NAME,self.mobile_num_name)

    def email(self):
        return self.driver.find_element(By.ID,self.email_id)

    def btn_next(self):
        self.driver.find_element(By.XPATH,self.next).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, self.cancel).click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH,self.cancel_confirm).click()

    def btn_cancel_no(self):
        self.driver.find_element(By.XPATH,self.cancel_no).click()

    def errorMessage(self):
        try:
            self.driver.find_element(By.XPATH,self.message).text
        except:
            None

class Registration_Details_Edit:
    cancel = "//button[normalize-space()='Cancel']"
    cancel_confirm = "//*[@id='root']/div[1]/div/div/div/div/div/button[2]"
    back = "//button[normalize-space()='Back']"
    next = "//button[normalize-space()='Next']"

    comp_info_pre_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/span"

    # Preview for company registration

    company = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span[2]"
    arabic = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/span[2]"
    building_num = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/span[2]"
    building_name = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/span[2]"
    street = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[5]/span[2]"
    postal_code = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[6]/span[2]"
    city_district = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[7]/span[2]"
    country = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[8]/span[2]"
    email = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[10]/span[2]"

    drp_country_of_incorp_id = "Country of Incorporation"
    drp_licence_nature_id = "License Nature"
    drp_entity_type_id = "Entity Type"
    drp_operation_field = "Operation Field"
    drp_trade_service_sector_id = "Trade/Service Sector"
    capital_id = "Capital"
    regisration_purpose_id = "Registration Purpose"
    estimated_annaul_incode_id = "Estimated Annual Income"
    authorized_person_id = "Authorized Person"
    drp_designation_id = "Designation"
    drp_nationality_id = "Nationality"
    drp_id_type_id = "ID Type"
    id_no_id = "ID No."
    dpick_id_exp_name = "ID Expiry"
    cr_no_id = "CR No."
    comp_card_no_id = "Computer Card No"
    dpick_cr_issue_date_name = "CR Issue Date"
    dpick_cr_exp_date_name = "CR Expiry Date"
    dpick_cc_issue_date_name = "CC Issue Date"
    dpick_cc_expaire_date_name = "CC Expiry Date"

    def __init__(self,driver):
        self.driver = driver

    def drp_country_of_incorp(self):
        return self.driver.find_element(By.ID,self.drp_country_of_incorp_id)

    def drp_licence_nature(self):
        return self.driver.find_element(By.ID,self.drp_licence_nature_id)

    def drp_entity_type(self):
        return self.driver.find_element(By.ID,self.drp_entity_type_id)

    def drp_operation(self):
        return self.driver.find_element(By.ID,self.drp_operation_field)

    def drp_trade_service_sector(self):
        return self.driver.find_element(By.ID,self.drp_trade_service_sector_id)

    def capital(self):
        return self.driver.find_element(By.ID,self.capital_id)

    def regisration_purpose(self):
        return self.driver.find_element(By.ID,self.regisration_purpose_id)

    def estimated_annaul_incode(self):
        return self.driver.find_element(By.ID,self.estimated_annaul_incode_id)

    def authorized_person(self):
        return self.driver.find_element(By.ID,self.authorized_person_id)

    def drp_designation(self):
        return self.driver.find_element(By.ID,self.drp_designation_id)

    def drp_nationality(self):
        return self.driver.find_element(By.ID,self.drp_nationality_id)

    def drp_id_type(self):
        return self.driver.find_element(By.ID,self.drp_id_type_id)

    def id_no(self):
        return self.driver.find_element(By.ID,self.id_no_id)

    def dpick_id_exp(self):
        return self.driver.find_element(By.NAME,self.dpick_id_exp_name)

    def cr_no(self):
        return self.driver.find_element(By.ID, self.cr_no_id)

    def comp_card_no(self):
        return self.driver.find_element(By.ID,self.comp_card_no_id)

    def dpick_cr_issue_date(self):
        return self.driver.find_element(By.NAME,self.dpick_cr_issue_date_name)

    def dpick_cr_exp_date(self):
        return self.driver.find_element(By.NAME,self.dpick_cr_exp_date_name)

    def dpick_cc_issue_date(self):
        return self.driver.find_element(By.NAME,self.dpick_cc_issue_date_name)

    def dpick_cc_expaire_date(self):
        return self.driver.find_element(By.NAME, self.dpick_cc_expaire_date_name)

    def btn_back(self):
        self.driver.find_element(By.XPATH, self.back).click()

    def btn_next(self):
        self.driver.find_element(By.XPATH, self.next).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH,self.cancel).click()

    def btn_confirm(self):
        self.driver.find_element(By.XPATH,self.cancel_confirm).click()

#   Preview

    def comp_info_pre(self):
        self.driver.find_element(By.XPATH, self.comp_info_pre_xpath).click()

    def company_pre(self):
        return self.driver.find_element(By.XPATH, self.company).text

    def arabic_pre(self):
        return self.driver.find_element(By.XPATH, self.arabic).text

    def building_num_pre(self):
        return self.driver.find_element(By.XPATH, self.building_num).text

    def building_name_pre(self):
        return self.driver.find_element(By.XPATH, self.building_name).text

    def street_pre(self):
        return self.driver.find_element(By.XPATH, self.street).text

    def postal_code_pre(self):
        return self.driver.find_element(By.XPATH, self.postal_code).text

    def city_district_pre(self):
        return self.driver.find_element(By.XPATH, self.city_district).text

    def country_pre(self):
        return self.driver.find_element(By.XPATH, self.country).text

    def mobile_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[9]/span[2]").text

    def email_pre(self):
        return self.driver.find_element(By.XPATH, self.email).text

class Beneficial_Owners_Details_Edit:
    drp_registration_pre_xpath = "//span[normalize-space()='Registration Details']"
#     preview
    cont_of_incorp = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2]"
    license_nature = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[2]"
    entity_type = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/span[2]"
    operation_field = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/span[2]"
    trade_service_sector = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/span[2]"
    capital = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[6]/span[2]"
    regisration_purpose = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[7]/span[2]"
    estimated_annaul_incode = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[8]/span[2]"
    authorized_person = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[9]/span[2]"
    drp_designation_id = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[10]/span[2]"
    nationality = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[11]/span[2]"
    id_type = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[12]/span[2]"
    id_no = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[13]/span[2]"
    id_expiry = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[14]/span[2]"
    cr_no = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[15]/span[2]"
    comp_card_no = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[18]/span[2]"
    cr_iss_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[16]/span[2]"
    cr_exp_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[17]/span[2]"
    cc_iss_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[19]/span[2]"
    cc_exp_date = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[20]/span[2]"

    # button

    back = "//button[normalize-space()='Back']"
    next = "//button[normalize-space()='Next']"
    cancel = "//button[normalize-space()='Cancel']"
    cancel_confirm = "//button[normalize-space()='Yes']"

    # BOD
    title_id = "Title"
    f_name_id = "First Name"
    m_name_id = "Middle Name"
    l_name_id = "Last Name"
    dpick_dob_name = "Date of Birth"
    place_of_birth_id = "Place of Birth"
    gender_id = "Gender"
    fl_ho_name = "Flat/House Number"
    ho_bu_name = "House/Building Name"
    street_id = "Street"
    city_id = "City"
    country_id = "Country"
    natinality_id = "Nationality"
    id_type_id = "ID Type"
    id_no_id = "ID No"
    place_of_id_issu_id = "Place of ID Issue"
    dpick_id_expairy = "ID Expiry"

    # BOD Buttons
    add_details_btn = "//button[normalize-space()='Add Details']"
    clear_btn = "//button[normalize-space()='Clear']"
    update_btn = "//button[normalize-space()='Update']"

    update_bod = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/div[1]/div[1]"

    message = "//div[@role='status']"


    def __init__(self,driver):
        self.driver = driver

    def click_bod(self):
        self.driver.find_element(By.XPATH,"(//div[@class='added-list-items-wrapper'])[1]").click()

    def message_info(self):
        return self.driver.find_element(By.XPATH,self.message)

    def btn_update(self):
        self.driver.find_element(By.XPATH,self.update_btn).click()

    def click_update_bod(self):
        self.driver.find_element(By.XPATH, self.update_bod).click()

    def btn_add_details(self):
        self.driver.find_element(By.XPATH,self.add_details_btn).click()

    def btn_clear(self):
        self.driver.find_element(By.XPATH, self.clear_btn).click()

    # BOD Details
    def title(self):
        return self.driver.find_element(By.ID,self.title_id)

    def first_name(self):
        return self.driver.find_element(By.ID, self.f_name_id)

    def middle_name(self):
        return self.driver.find_element(By.ID, self.m_name_id)

    def last_name(self):
        return self.driver.find_element(By.ID, self.l_name_id)

    def dob(self):
        return self.driver.find_element(By.NAME, self.dpick_dob_name)

    def place_of_birth(self):
        return self.driver.find_element(By.ID, self.place_of_birth_id)

    def gender(self):
        return self.driver.find_element(By.ID, self.gender_id)

    def flat_house_number(self):
        return self.driver.find_element(By.NAME, self.fl_ho_name)

    def house_building_name(self):
        return self.driver.find_element(By.NAME, self.ho_bu_name)

    def street(self):
        return self.driver.find_element(By.ID, self.street_id)

    def city(self):
        return self.driver.find_element(By.ID, self.city_id)

    def country(self):
        return self.driver.find_element(By.ID, self.country_id)

    def nationality(self):
        return self.driver.find_element(By.ID, self.natinality_id)

    def id_type(self):
        return self.driver.find_element(By.ID, self.id_type_id)

    def id_no(self):
        return self.driver.find_element(By.ID, self.id_no_id)

    def place_of_id_issu(self):
        return self.driver.find_element(By.ID, self.place_of_id_issu_id)

    def id_expiry(self):
        return self.driver.find_element(By.NAME, self.dpick_id_expairy)

    # buttons
    def btn_back(self):
        self.driver.find_element(By.XPATH, self.back).click()

    def btn_next(self):
        self.driver.find_element(By.XPATH, self.next).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, self.cancel).click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, self.cancel_confirm).click()

    # Preview

    def registration_preview(self):
        self.driver.find_element(By.XPATH,self.drp_registration_pre_xpath).click()

    def cont_of_incorp_pre(self):
        element = self.driver.find_element(By.XPATH,self.cont_of_incorp)
        return element.get_attribute('title')
    def license_nature_pre(self):
        element = self.driver.find_element(By.XPATH, self.license_nature)
        return element.get_attribute('title')
    def entity_type_pre(self):
        element = self.driver.find_element(By.XPATH, self.entity_type)
        return element.get_attribute('title')
    def operation_field_pre(self):
        element = self.driver.find_element(By.XPATH, self.operation_field)
        return element.get_attribute('title')
    def trade_service_sector_pre(self):
        element = self.driver.find_element(By.XPATH, self.trade_service_sector)
        return element.get_attribute('title')
    def capital_pre(self):
        element = self.driver.find_element(By.XPATH, self.capital)
        return element.get_attribute('title')
    def regisration_purpose_pre(self):
        element = self.driver.find_element(By.XPATH, self.regisration_purpose)
        return element.get_attribute('title')
    def estimated_annaul_incode_pre(self):
        element = self.driver.find_element(By.XPATH, self.estimated_annaul_incode)
        return element.get_attribute('title')
    def authorized_person_pre(self):
        element = self.driver.find_element(By.XPATH, self.authorized_person)
        return element.get_attribute('title')
    def drp_designation_id_pre(self):
        element = self.driver.find_element(By.XPATH, self.drp_designation_id)
        return element.get_attribute('title')
    def nationality_pre(self):
        element = self.driver.find_element(By.XPATH, self.nationality)
        return element.get_attribute('title')
    def id_type_pre(self):
        element = self.driver.find_element(By.XPATH, self.id_type)
        return element.get_attribute('title')
    def id_no_pre(self):
        element = self.driver.find_element(By.XPATH, self.id_no)
        return element.get_attribute('title')
    def id_expiry_pre(self):
        element = self.driver.find_element(By.XPATH, self.id_expiry)
        return element.get_attribute('title')
    def comp_card_no_pre(self):
        element = self.driver.find_element(By.XPATH, self.comp_card_no)
        return element.get_attribute('title')
    def cr_no_pre(self):
        element = self.driver.find_element(By.XPATH, self.cr_no)
        return element.get_attribute('title')
    def cr_iss_date_pre(self):
        element = self.driver.find_element(By.XPATH, self.cr_iss_date)
        return element.get_attribute('title')
    def cr_exp_date_pre(self):
        element = self.driver.find_element(By.XPATH, self.cr_exp_date)
        return element.get_attribute('title')
    def cc_iss_date_pre(self):
        element = self.driver.find_element(By.XPATH, self.cc_iss_date)
        return element.get_attribute('title')
    def cc_exp_date_pre(self):
        element = self.driver.find_element(By.XPATH, self.cc_exp_date)
        return element.get_attribute('title')


class Beneficiaries:
    def __init__(self, driver):
        self.driver = driver

    def search_bene(self):
        return self.driver.find_element(By.NAME, "Search")

    def select_beneficiary(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='dropdown-search-item'])[1]")

    def btn_next(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")

    def click_beneficiaries(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='tableBody bordered pointer-cursor'])[1]")

    def get_fastcash_locations(self):
        elements = self.driver.find_elements(By.XPATH, "(//div[@class='reviewContainer m-2'])")
        return [element.text for element in elements]  # Get the text from each element

    def remove_beneficiaries(self):
        self.driver.find_element(By.XPATH,"(//img[@alt='delete'])[1]").click()

    def bene_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/span[1]").text

class Delegate:
    def __init__(self, driver):
        self.driver = driver

    def btn_next(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")


class Upload_Documents_Edit:
    passport_xpath = "//li[normalize-space()='Passport']"
    id_xpath = "//li[normalize-space()='ID']"
    visa_xpath = "//li[normalize-space()='Visa']"

    front_xpath = "//li[normalize-space()='Front']"
    rear_xpath = "//li[normalize-space()='Rear']"
    full_xpath = "//li[normalize-space()='Full']"

    cancel_btn = "//button[normalize-space()='Cancel']"
    cancel_confirm = "//button[normalize-space()='Yes']"
    back_btn = "//button[normalize-space()='Back']"
    next_btn = "//button[normalize-space()='Next']"

    save_btn = "//button[normalize-space()='Save']"


    def __init__(self,driver):
        self.driver = driver

    def click_passport(self):
        self.driver.find_element(By.XPATH, self.passport_xpath).click()

    def click_ID(self):
        self.driver.find_element(By.XPATH, self.id_xpath).click()

    def click_visa(self):
        self.driver.find_element(By.XPATH, self.visa_xpath).click()

    # Send files
    def send_front(self):
        return self.driver.find_element(By.XPATH, self.front_xpath)

    def send_rear(self):
        return self.driver.find_element(By.XPATH, self.rear_xpath)

    def send_full(self):
        return self.driver.find_element(By.XPATH, self.full_xpath)

    # buttons

    def btn_back(self):
        self.driver.find_element(By.XPATH, self.back_btn).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, self.cancel_confirm).click()

    def btn_next(self):
        self.driver.find_element(By.XPATH, self.next_btn).click()

    def btn_save(self):
        return self.driver.find_element(By.XPATH, self.save_btn)
















