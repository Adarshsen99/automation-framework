from selenium.webdriver.common.by import By


class Add_Bank:

    def __init__(self, driver):
        self.driver = driver

    def btn_add_bank(self):
        return self.driver.find_element(By.XPATH, "//div[@class='addBank']").click()

    def bank_name(self):
        return self.driver.find_element(By.ID, "Bank Name")

    def bank_name_local_language(self):
        return self.driver.find_element(By.ID, "Bank Name in Local Language")

    def bank_code(self):
        return self.driver.find_element(By.ID, "Bank Code")

    def drp_country(self):
        return self.driver.find_element(By.ID, "Country")

    def btn_delete_bank(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete Bank']").click()

    def btn_cancel_bank(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_save_bank(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    def get_banknames(self):
        return self.driver.find_elements(By.XPATH,"//div[@class='bankListName']")

class Add_branch:

    def __init__(self, driver):
        self.driver = driver


    def btn_add_branch(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Branch']").click()

    def branch_name(self):
        return self.driver.find_element(By.ID, "Branch Name")

    def branch_local_nme(self):
        return self.driver.find_element(By.ID, "Branch Name in Local Language")

    def branch_address(self):
        return self.driver.find_element(By.ID, "Branch Address")

    def branch_code(self):
        return self.driver.find_element(By.ID, "Branch Code")

    def drp_country(self):
        return self.driver.find_element(By.ID, "Country")

    def btn_branch_save(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    def first_banK_select(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]")

    def second_selected_bank(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]")

    def third_selected_bank(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]")

    def fourth_selected_bank(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]")

    def fifth_selected_bank(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[5]")





