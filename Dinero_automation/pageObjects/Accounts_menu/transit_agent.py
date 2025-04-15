from selenium.webdriver.common.by import By


class Transit_agent:
    def __init__(self, driver):
        self.driver = driver

    def click_create_new(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create New']")

    def transit_agent_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_name']")

    def short_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_short_name']")
    def address(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_addr']")

    def email(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_mail']")

    def telephone_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_tlphn_no']")

    def contact_person(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_cntct_prsn']")

    def contact_person_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_cntct_prsn_no']")

    def transit_agent_city(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_cty']")

    def region(self):
        return self.driver.find_element(By.XPATH, "//input[@id='trn_agnt_rgn']")

    def button_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def buttton_save(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")



