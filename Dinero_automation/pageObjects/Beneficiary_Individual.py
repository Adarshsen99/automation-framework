from selenium.webdriver.common.by import By

class Personal_Details():
    drp_title_id = "Title"
    fname_id = "First Name"
    mname_id = "Middle Name"
    lname_id = "Last Name"
    short_id = "Short Name"
    cob_id = "Country of Birth"
    drp_national_id = "Nationality"
    drp_relation_id = "Relationship"
    drp_id_type_id = "ID Type"
    id_num_id = "ID Number"
    drp_trans_type_id = "Transaction Type"

    next_xpath = "//button[normalize-space()='Next']"
    cancel_xpath = "//button[normalize-space()='Cancel']"
    cancel_confirm_xpath = "//button[normalize-space()='Yes']"

    message = "//span[@class='error-message']"

    def __init__(self,driver):
        self.driver = driver

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.message).text
        except:
            None

    def drp_title(self):
        return self.driver.find_element(By.ID, self.drp_title_id)

    def fname(self):
        return self.driver.find_element(By.ID, self.fname_id)

    def mname(self):
        return self.driver.find_element(By.ID, self.mname_id)

    def lname(self):
        return self.driver.find_element(By.ID, self.lname_id)

    def short_name(self):
        return self.driver.find_element(By.ID, self.short_id)

    def drp_cob(self):
        return self.driver.find_element(By.ID, self.cob_id)

    def drp_nationality(self):
        return self.driver.find_element(By.ID, self.drp_national_id)

    def drp_relation(self):
        return self.driver.find_element(By.ID, self.drp_relation_id)

    def drp_id_type(self):
        return self.driver.find_element(By.ID, self.drp_id_type_id)

    def id_num(self):
        return self.driver.find_element(By.ID, self.id_num_id)

    def drp_trans_type(self):
        return self.driver.find_element(By.ID, self.drp_trans_type_id)

    def btn_next(self):
        return self.driver.find_element(By.XPATH, self.next_xpath)

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, self.cancel_xpath)

    def btn_cancel_confirm(self):
        return self.driver.find_element(By.XPATH, self.cancel_confirm_xpath)

class Contact_Information:
    next_xpath = "//button[normalize-space()='Next']"
    back_xpath = "//button[normalize-space()='Back']"
    cancel_xpath = "//button[normalize-space()='Cancel']"
    cancel_confirm_xpath = "//button[normalize-space()='Yes']"

    # Preview for personal information

    def __init__(self,driver):
        self.driver = driver

    def flat_house_number(self):
        return self.driver.find_element(By.ID, "Flat/House Number")

    def house_building_name(self):
        return self.driver.find_element(By.ID, "House/Building Name")

    def street(self):
        return self.driver.find_element(By.ID, "Street")

    def email(self):
        return self.driver.find_element(By.ID, "Email")

    def city(self):
        return self.driver.find_element(By.ID, "City")

    def drp_country(self):
        return self.driver.find_element(By.NAME, "Country")

    def drp_phone(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def phone(self):
        return self.driver.find_element(By.NAME, "Mobile Number")



    def btn_next(self):
        self.driver.find_element(By.XPATH, self.next_xpath).click()

    def btn_back(self):
        self.driver.find_element(By.XPATH,self.back_xpath).click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH,self.cancel_xpath).click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, self.cancel_confirm_xpath).click()

    # Preview for personal information

    def click_personal_info_preview(self):
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Personal Information']").click()

    def title_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span[2]").text

    def first_name_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/span[2]").text

    def middle_name_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/span[2]").text

    def last_name_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/span[2]").text

    def short_name_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[5]/span[2]").text

    def country_of_birth_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[6]/span[2]").text

    def nationality_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[7]/span[2]").text

    def relationship_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[8]/span[2]").text

    def id_type_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[9]/span[2]").text

    def id_number_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[10]/span[2]").text

    def transaction_type_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[11]/span[2]").text

class Bank_Information:

    def __init__(self,driver):
        self.driver = driver

    def send_bank_name(self):
        return self.driver.find_element(By.NAME,"Bank Name")

    def click_bank_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div/div[1]/div[2]/div/div/p")

    def send_branch_name(self):
        return self.driver.find_element(By.NAME,"Branch Name")

    def click_branch_name(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div/div[2]/div[2]/div/div/p")

    def account_number(self):
        return self.driver.find_element(By.ID,"Account Number")

    def confirm_account_numb(self):
        return self.driver.find_element(By.ID,"Confirm Account Number")

    def drp_account_type(self):
        return self.driver.find_element(By.ID, "Account Type")

    def drp_currency(self):
        return self.driver.find_element(By.ID, "Currency")

    def drp_purpose(self):
        return self.driver.find_element(By.ID, "Purpose Of Payment")

    def btn_add_bank(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Bank']").click()

    def btn_clear(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Clear']").click()

    # buttons

    def btn_back(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_next(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

    # Preview contact infirmation

    def click_contact_infirmation_pre(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Contact Information']").click()

    def fl_hn_num_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2]").text

    def ho_bu_name_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[2]").text

    def street_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/span[2]").text

    def cty_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/span[2]").text

    def country_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/span[2]").text

    def emai_pre(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[7]/span[2]").text


    def message(self):
        try:
            return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[2]").text
        except:
            None