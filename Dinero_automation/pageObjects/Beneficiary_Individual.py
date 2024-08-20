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

    def __init__(self,driver):
        self.driver = driver

    def btn_back(self):
        self.driver.find_element(By.XPATH,self.back_xpath).click()



