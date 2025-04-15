from selenium.webdriver.common.by import By


class Add_new:

    def __init__(self, driver):
        self.driver = driver

    def click_new_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create New']")

    def drp_customer_typ(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Customer Type']")

    def client_search(self):
        return self.driver.find_element(By.XPATH,
                                        "(//input[@id='floatingSearch'])[1]")

    def drp_transcation_mode(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@name,'Transaction Mode')]")

    def delegate_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]")

    def branch(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@name,'branch')]")

    def user(self):
        return self.driver.find_element(By.XPATH, "//select[@name='user']")

    def wallet(self):
        return self.driver.find_element(By.XPATH, "//select[@name='wallet']")

    def client_rep_name(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='name'])[1]")

    def id_num(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='idNumber'])[1]")

    def id_exp_date(self):
        return self.driver.find_element(By.XPATH, "(//input[@name='idExpiryDate'])[1]")

    def click_post_date(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='checkbox-postDated'])[1]")

    def effective_date(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@name='effectiveDate']")

    def effect_general(self):
        return self.driver.find_element(By.XPATH, "(//input[@placeholder='Effective General Ledger A/C'])[1]")

    def gl_account(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[4]/div[3]/div/div/div[2]/div/div[1]")

    def click_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-cashCheckBox']")

    def click_cheque(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-chequeCheckBox']")

    def click_digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-digitalPayCheckBox']")

    def click_online(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='checkbox-onlineCheckBox'])[1]")

    def credit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-creditOrDebitCheckbox']")

    def pos(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='checkbox-posCheckBox'])[1]")

    def drp_gender_led_acc(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/select[1]")

    def transaction_remark(self):
        return self.driver.find_element(By.XPATH, "//textarea[@name='remarks']")

    def lc_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcAmount']")

    def enter_cash(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]").click()

    def denom1(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='Quantity 6'])[1]")

    def cashsubmitt(self):
        return self.driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]")


    def enter_pos(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@fdprocessedid,'brcfs')])[1]").click()

    def pos_amount(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='POSAmount'])[1]")

    def drp_pos_bank(self):
        return self.driver.find_element(By.XPATH, "(//select[@name='POS-bankAccProfile'])[1]")

    def pos_reference(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='POSRef'])[1]")

    def pos_submitt(self):
        return self.driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]")

    def enter_cheque(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@class,'form-control')])[11]")

    def enter_online(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@class,'form-control')])[12]")

    def enter_digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@fdprocessedid,'batcgm')])[1]").click()

    def digital_amunt(self):
        return self.driver.find_element(By.XPATH, "")



    def req_for_approval(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']")

    def click_new_row(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div[1]")

    def click_2nd_gl(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div[1]/select")

    def click_2nd_transaction_remark(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/input[1]")

    def lc_2nd_amount(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]/input[1]")

    def delete_1st_gl(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[7]")

    def delete_2nd_gl(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[7]/img[1]")
