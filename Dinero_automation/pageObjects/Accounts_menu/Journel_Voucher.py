from selenium.webdriver.common.by import By


class Add_new:

    def __init__(self, driver):
        self.driver = driver

    def new_btn(self):
        return  self.driver.find_element(By.XPATH, "//button[normalize-space()='New']")

    def date(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")



    def click_ante_date(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Ante dated']")

    def effective_date(self):
        return self.driver.find_element(By.NAME, "Effective Date")


    def new_typ(self):
        return self.driver.find_element(By.XPATH, "//div[@class='jv-grid-cell d-flex align-items-center justify-content-center gap-2']")

    def type1(self):
        return self.driver.find_element(By.XPATH, "//select[@fdprocessedid='topin']")

    def branch1(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/select[1]")

    def Gl_account(self):
        return self.driver.find_element(By.XPATH, "//input[@id='jv_details.0.generalledgeraccount']")

    def transaction_remark(self):
        return self.driver.find_element(By.ID, "transactionRemark-0")

    def lc_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcAmount-0']")

    def delete_first_row(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'modal')]//div[2]//div[9]")

    def click_new(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]")

    def type2(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/select[1]")

    def branch_scond(self):
        return self.driver.find_element(By.XPATH, "(//select)[9]")

    def gl_second(self):
        return self.driver.find_element(By.XPATH, "(//select)[10]")

    def transaction_remark_second(self):
        return self.driver.find_element(By.ID, "transactionRemark-1")

    def lc_amount_second(self):
        return self.driver.find_element(By.ID, "lcAmount-1")

    def drp_description(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='Description']")

    def debit_total(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div[1]/div[2]").text

    def credit_total(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div[2]/div[2]").text

    def req_for_approval(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']")

    def search_transaction_reference(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Transaction Reference']")

    def search_branch(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Branch']")

    def search_Gl_account(self):
        return self.driver.find_element(By.XPATH, "//select[@name='GL Account']")

    def from_date(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[4]/div/div[2]/input")

    def to_date(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[5]/div/div[2]/input")

    def refresh_btn(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='delete icon']")

    def filter_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']")

    def outside_approve_click(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Approved']")

    def outside_reject_click(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Reject']")

    def click_approve(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']")

    def click_reject(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Reject']")


