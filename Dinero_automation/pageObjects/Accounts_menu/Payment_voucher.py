from selenium.webdriver.common.by import By


class Add_new:

    def __init__(self, driver):
        self.driver = driver

    def click_new_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create New']")

    def vendor_name(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div/div[@class='d-flex']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")



    def drp_transcation_mode(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@name,'Transaction Mode')]")

    def client_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='name']")

    def id_number(self):
        return self.driver.find_element(By.XPATH, "")

    def id_expiry(self):
        return self.driver.find_element(By.XPATH, "")


    def wallet(self):
        return self.driver.find_element(By.XPATH, "//select[@name='wallet']")

    def click_postdate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-postDated']")

    def effective_date(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]/input[1]")

    def drp_effect_general(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-cashCheckBox']")

    def click_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-cashCheckBox']")

    def click_cheque(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-chequeCheckBox']")

    def click_debitcard(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-creditOrDebitCheckbox']")

    def invoice_refrence(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Invoice Reference']")

    def digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-digitalPayCheckBox']")


    def lc_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcAmount']")

    def FC_name(self):
        return self.driver.find_element(By.XPATH, "")

    def fc_rate(self):
        return self.driver.find_element(By.XPATH, "")


    def Fc_amount(self):
        return self.driver.find_element(By.XPATH, "")



    def enter_cash(self):
        return self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/div/div[1]/div/div/input")

    def cash_50(self):
        return self.driver.find_element(By.XPATH," ")

    def cash_20(self):
        return self.driver.find_element(By.XPATH, "")

    def cash_10(self):
        return self.driver.find_element(By.XPATH, "")

    def cash_5(self):
        return self.driver.find_element(By.XPATH, "")

    def cash_1(self):
        return self.driver.find_element(By.XPATH, "")

    def submit_csh(self):
        return self.driver.find_element(By.XPATH, "")

    def click_clear(self):
        return self.driver.find_element(By.XPATH, "")

    def enter_cheque(self):
        return self.driver.find_element(By.XPATH, "")

    def cheque_amount(self):
        return self.driver.find_element(By.XPATH, "")

    def drp_bank_account_prof(self):
        return self.driver.find_element(By.XPATH, "")

    def cheque_number(self):
        return self.driver.find_element(By.XPATH, "")

    def cheque_date(self):
        return self.driver.find_element(By.XPATH, "")

    def submit_chq(self):
        return self.driver.find_element(By.XPATH, "")

    def enter_dig_pay(self):
        return self.driver.find_element(By.XPATH, "")

    def dig_pay_amount(self):
        return self.driver.find_element(By.XPATH, "")

    def drp_bank_acc_prof_dig(self):
        return self.driver.find_element(By.XPATH, "")

    def reference_dig(self):
        return self.driver.find_element(By.XPATH, "")

    def submit_dig(self):
        return self.driver.find_element(By.XPATH, "")

    def enter_debit_card(self):
        return self.driver.find_element(By.XPATH, "")

    def credit_amount(self):
        return self.driver.find_element(By.XPATH, "")

    def drp_deb(self):
        return self.driver.find_element(By.XPATH, "")

    def reference_deb(self):
        return self.driver.find_element(By.XPATH, "")

    def submit_deb(self):
        return self.driver.find_element(By.XPATH, "")

    def req_for_approval(self):
        return self.driver.find_element(By.XPATH, "")

    def back_to_list(self):
        return self.driver.find_element(By.XPATH, "")






