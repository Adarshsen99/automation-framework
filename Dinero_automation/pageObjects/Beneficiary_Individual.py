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
        return self.driver.find_element(By.XPATH, "//select[@id='Country of Birth']")

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
        return self.driver.find_element(By.XPATH, "//select[@id='Country']")

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
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")

    def click_bank_name(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")

    def send_branch_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div/div/input")

    def click_branch_name(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]")

    def click_second_bank(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")

    def click_second_branch(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]")
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

    def btn_update(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']").click()

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

    def meassage_text(self):
        try:
            return self.driver.find_element(By.XPATH,"//div[contains(text(),'Bank already exists in the list.')]").text
        except:
            None

    def message_2(self):
        try:
            return self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div").text
        except:
            None

    def banks_data_1(self):
        return self.driver.find_element(By.XPATH,"(//div[@class='selected-container'])[1]")

    def banks_data_2(self):
        return self.driver.find_element(By.XPATH,"(//div[@class='selected-container'])[2]")

    # Bank preview

    def click_bank_info_preview(self):
        self.driver.find_element(By.XPATH,"//div[@class='accordionHeader']//span[contains(text(),'Bank Information')]").click()

    def bank_name_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/span[2]").text

    def branch_name_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[3]/span[2]").text

    def branch_address_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[4]/span[2]").text

    def branch_code_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[5]/span[2]").text

    def account_num_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[9]/span[2]").text

    def confirm_account_num_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[10]/span[2]").text

    def account_type_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[11]/span[2]").text

    def currency_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[12]/span[2]").text

    def purpose_of_payment_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[13]/span[2]").text

    def branch_address(self):
        return self.driver.find_element(By.ID,"Branch Address")

    def branch_code(self):
        return self.driver.find_element(By.ID,"Branch Code")

class Fastcash_Location:
    def __init__(self, driver):
        self.driver = driver

    def fastcash_1(self):
        return self.driver.find_element(By.XPATH,"(//div[@class='added-list-items-wrapper'])[1]")

    def fastcash_2(self):
        self.driver.find_element(By.XPATH,"(//div[@class='added-list-items-wrapper'])[2]").click()

    def fastcash_3(self):
        self.driver.find_element(By.XPATH,"(//div[@class='added-list-items-wrapper'])[3]").click()

    # Payout anywhare

    def click_payout_anywhere(self):
        return self.driver.find_element(By.XPATH, "//input[@value='1']")

    def drp_country(self):
        return self.driver.find_element(By.ID,"Country")

    def drp_num_country(self):
        return self.driver.find_element(By.XPATH,"//select[@class='countrySelector']")

    def mobile_number(self):
        return self.driver.find_element(By.NAME, "Mobile Number")

    def btn_add_location(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Location']").click()

    def btn_clear(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Clear']").click()

    # Specific location
    def click_specific_location(self):
        self.driver.find_element(By.XPATH, "//input[@value='2']").click()

    def drp_country_splocation(self):
        return self.driver.find_element(By.ID, "Country")

    def drp_num_country_splocation(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def mobile_number_splocation(self):
        return self.driver.find_element(By.NAME, "Mobile Number")

    def address_1_splocation(self):
        return self.driver.find_element(By.ID, "Address Line 1")

    def address_2_splocation(self):
        return self.driver.find_element(By.ID, "Address Line 2")

    def address_3_splocation(self):
        return self.driver.find_element(By.ID, "Address Line 3")

    def city_splocation(self):
        return self.driver.find_element(By.ID, "City")

    def btn_add_location_splocation(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Location']").click()

    def btn_clear_splocation(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Clear']").click()

#     Button

    def btn_next(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def btn_back(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

#   Preview for payout anywhere

    def click_fastcash_location(self):
        self.driver.find_element(By.XPATH,"(//span[contains(text(),'Fast Cash Location')])[2]").click()

    def country_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/span[2]").text

    def mobile_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[3]/span[2]").text

    def payout_anywhere_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[4]/span[2]").text

#  Preview for specific location

    def address_1_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/span[2]").text

    def address_2_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[3]/span[2]").text

    def address_3_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[4]/span[2]").text

    def city_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[5]/span[2]").text

    def country_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[6]/span[2]").text

    def mobile_sp_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[7]/span[2]").text

    def payout_specific_location_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div[8]/span[2]").text

class Final_Preview:

    def __init__(self, driver):
        self.driver = driver

    def btn_save(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def btn_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def meassge_final(self):
        try:
            return self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div[2]").text
        except:
            None

    def editmode_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div/div").text
        except:
            None