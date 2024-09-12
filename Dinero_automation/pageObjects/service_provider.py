
from selenium.webdriver.common.by import By

class General_Information():
    def __init__(self, driver):
        self.driver = driver

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None

    def drp_category(self):
        return self.driver.find_element(By.ID,"Category")

    def catego_other_field(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Other Category']")

    def name(self):
        return self.driver.find_element(By.ID, "Name")

    def arabic_name(self):
        return  self.driver.find_element(By.ID, "Arabic Name")

    def adress_1(self):
        return self.driver.find_element(By.ID, "Address 1")

    def adress_2(self):
        return self.driver.find_element(By.ID, "Address 2")

    def adress_3(self):
        return self.driver.find_element(By.ID, "Address 3")

    def postal_code(self):
        return self.driver.find_element(By.ID, "Postal Code")

    def city(self):
        return self.driver.find_element(By.ID, "City")

    def drp_country(self):
        return self.driver.find_element(By.ID, "Country")

    def drp_country_of_incorporation(self):
        return self.driver.find_element(By.ID, "Country of Incorporation")

    def drp_country_code(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def mobile_number(self):
        return  self.driver.find_element(By.NAME, "Mobile Number")
    def email(self):
        return  self.driver.find_element(By.ID, "Email")

    def btn_nxt(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]")

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_cancelconfirm(self):
        return  self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")



class Agreement_Details():
    def __init__(self, driver):
        self.driver = driver

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None
    def dpick_agreement_start_details(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Agreement Start Date']")

    def dpick_agreement_end_details(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Agreement End Date']")
    def registration_number(self):
        return self.driver.find_element(By.ID, "Registration Number")
    def dpick_registration_exp_date(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@name,'Registration Expiry Date')]")

    def trade_license_number(self):
        return self.driver.find_element(By.ID, "Trade License Number")
    def dpick_trade_exp_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Trade License Expiry Date']")
    def license_number(self):
        return self.driver.find_element(By.ID, "License Number")
    def licensing_authority(self):
        return self.driver.find_element(By.ID, "Licensing Authority")
    def authoritzed_person_name(self):
        return self.driver.find_element(By.ID, "Authorized Person Name")
    def drp_gender(self):
        return self.driver.find_element(By.ID, "Gender")
    def dpick_date_of_birth(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[6]/div[2]/div/div[2]/input")
    def drp_country_of_birh(self):
        return self.driver.find_element(By.ID, "Country of Birth")
    def drp_nationality(self):
        return self.driver.find_element(By.ID, "Nationality")
    def fund_btn_new(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/button")
    def drp_fund_curency(self):
        return self.driver.find_element(By.ID, "Fund Currency")
    def rate(self):
        return self.driver.find_element(By.ID, "Rate")
    def settlement_rate(self):
        return self.driver.find_element(By.ID, "Settlement Rate")
    def pay_settelement_rate(self):
        return self.driver.find_element(By.ID, "Pay-in Settlement Rate")
    def balance_trigger(self):
        return self.driver.find_element(By.ID, "Balance Alert Trigger")
    def btn_add(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/div[2]/div/div/div[2]/div/button[2]")
    def btn_cancel_fund(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/div[2]/div/div/div[2]/div/button[1]")
    def fundcurr_table(self):
        self.driver.find_element(By.XPATH, "//div[contains(@class,'pointer-cursor')]").click()
    def delete(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")
    def btn_nxt(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/button")
    def btn_cancl_confm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")

    def btn_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")
    def btn_updte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']")

class Upload_document():
    def __init__(self, driver):
        self.driver = driver

    def doc_selector(self):
        return self.driver.find_element(By.XPATH, "//div[@class='uploadActionsContainer p-5']")
    def btn_cancle(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
    def btn_nexte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
    def btn_backe(self):
         return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")
    def doc_delte(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'page-layout')]//div[4]//img[1]")
    def doc_preview(self):
        return self.driver.find_element(By.XPATH, "(//img[contains(@class,'icon-styles cursor-pointer')])[1]")

    def doc_container(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'uploadedTable card pt-2 pb-2 mt-4')]")

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None






