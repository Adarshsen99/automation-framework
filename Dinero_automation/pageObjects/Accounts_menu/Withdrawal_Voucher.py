from selenium.webdriver.common.by import By


class withdrawalVoucher:
    def __init__(self, driver):
        self.driver = driver

    def create_new(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create']").click()

    def drp_bankaccount(self):
        return self.driver.find_element(By.XPATH, "//select[@name='bankAccount']")

    def click_cheque(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']")

    def cheque_number(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='d-flex flex-column justify-content-center m-4']//div[@class='form-floating m-1']//input[1]")

    def cheque_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Cheque Amount']")

    def cash1000(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 0']")

    def submit(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")

    def remarks(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='Remarks']")

    def drp_transitagent(self):
        return self.driver.find_element(By.XPATH, "//select[@name='transitAgent']")

    def click_card(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def drp_creditcard(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/select[1]")

    def card_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Card Amount']")

    def click_save(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
