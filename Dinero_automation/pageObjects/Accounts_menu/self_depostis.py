from selenium.webdriver.common.by import By


class Self_cash:
    def __init__(self, driver):
        self.driver = driver

    def click_new(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='New']")

    def bank_account(self):
        return self.driver.find_element(By.XPATH, "//select[@name='BankAccount']")

    def transit_agent(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Transit Agent']")

    def cash1000(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 0']")

    def cash500(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 1']")

    def cash100(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 2']")

    def cash10(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 3']")

    def cash5(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 4']")

    def cash1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 5']")

    #card

    def click_chque(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def click_new_cheque(self):
        return self.driver.find_element(By.XPATH, "//div[@class='sd-grid-cell d-flex align-items-center justify-content-center gap-2']")

    def chequeno(self):
        return self.driver.find_element(By.XPATH, "//input[@id='selfdata.0.chequeNo']")

    def drp_bank_isnd(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@fdprocessedid,'hwjpe')]")

    def amount_enter(self):
        return self.driver.find_element(By.XPATH, "//input[@id='selfdata.0.amount']")

    def remarks(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='Remarks']")


    def click_save(self):
       return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def click_intiater(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]")

    def click_intrasnit(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='In-Transit']")

    def click_og_in_transit(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='In-Transit']")

    def click_intransiter(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div")

    def click_completed(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Completed']")

    def click_og_completed(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Completed']")

    def click_complterer(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/span[1]")