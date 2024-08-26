from selenium.webdriver.common.by import By

class Company_Information:

    def __init__(self,driver):
        self.driver = driver

    def company_name(self):
        return self.driver.find_element(By.ID, "Company Name")

    def short_name(self):
        return self.driver.find_element(By.ID, "Short Name")

    def drp_country_of_incorporation(self):
        return self.driver.find_element(By.ID, "Country of Incorporation")

    def drp_relation(self):
        return self.driver.find_element(By.ID, "Relationship")

    def btn_next(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None

class Contact_Information:

    def __init__(self,driver):
        self.driver = driver

    def building_number(self):
        return self.driver.find_element(By.ID, "Building Number")

    def building_name(self):
        return self.driver.find_element(By.ID, "Building Name")

    def street(self):
        return self.driver.find_element(By.ID, "Street")

    def city_district(self):
        return self.driver.find_element(By.ID, "City/District")

    def drp_country(self):
        return self.driver.find_element(By.ID, "Country")

    def drp_country_code(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def mobile_number(self):
        return self.driver.find_element(By.NAME, "Mobile Number")

    def email(self):
        return self.driver.find_element(By.ID, "Email")

    def btn_next(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def btn_back(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

#   company_preview
    def click_company_info_pre(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Company Information']").click()

    def company_name_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span[2]").text

    def short_name_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/span[2]").text

    def country_of_incorporation_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[3]/span[2]").text

    def relation_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/span[2]").text


class Bank_Information:
    def __init__(self, driver):
        self.driver = driver

    def send_bank_name(self):
        return self.driver.find_element(By.NAME,"Bank Name")

    def click_bank_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/div[1]/div[1]/div[2]/div/div/p")

    def send_branch_name(self):
        return self.driver.find_element(By.NAME,"Branch Name")

    def click_branch_name(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/div[1]/div[2]/div[2]/div/div/p")

    def account_number(self):
        return self.driver.find_element(By.ID,"Account Number")

    def confirm_account_numb(self):
        return self.driver.find_element(By.ID,"Confirm Account Number")

    def drp_account_type(self):
        return self.driver.find_element(By.ID, "Account Type")

    def drp_currency(self):
        return self.driver.find_element(By.ID, "Currency")

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

    def banks_data_1(self):
        return self.driver.find_element(By.XPATH,"(//div[@class='selected-container'])[1]")

    def banks_data_2(self):
        return self.driver.find_element(By.XPATH,"(//div[@class='selected-container'])[2]")

    # Preview contact infirmation

    def click_contact_info_pre(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Contact Information']").click()

    def building_numb_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2]").text

    def building_name_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/span[2]").text

    def street_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/span[2]").text

    def city_district_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/span[2]").text

    def country_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[5]/span[2]").text

    def mobile_num_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[6]/span[2]").text

    def email_pre(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[7]/span[2]").text

class Final_Preview:
    def __init__(self, driver):
        self.driver = driver

    def btn_save(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    def btn_back(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_cancel(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_cancel_confirm(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
