from selenium.webdriver.common.by import By


class adding_account:

    def __init__(self, driver):
        self.driver = driver

    def account_name(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[1]/div[1]/div/input")

    def arabic_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Account Name Arabic']")

    def suffix(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")

    def is_gl_acc(self):
        return self.driver.find_element(By.XPATH, "//input[@id='GL Account']")

    def save_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def dlt_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")

    def new_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='New']")

    def account_num(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[2]/div[2]/div/div/input")

    def parent_account(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Parent Account']")

    def fc_account(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-FC Account Required']")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Currency']")

    def rate(self):
        return self.driver.find_element(By.XPATH, "//input[@type='number']")

    def journal_voucher(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Journal Voucher']")

    def deposit_voucher(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Deposit Voucher']")

    def withdrawal_voucher(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Withdrawal Voucher']")

    def receipt_voucher(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Receipt Voucher']")

    def payment_voucher(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Payment Voucher']")

    def recuring_pay_vou(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Recurring Payment Voucher']")

    def petty_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Petty Cash Voucher']")

    def save_messege(self):
        return self.driver.find_element(By.XPATH, "(//div[contains(@role,'status')])[1]").text

    def error_messege(self):
        return self.driver.find_element(By.XPATH, "//label[@for='checkbox-Account Name']//span[@class='error-message'][normalize-space()='Required']").text

    def delete_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")

    def updte_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']")

