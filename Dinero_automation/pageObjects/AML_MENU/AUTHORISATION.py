from selenium.webdriver.common.by import By


class Add_new:

    def __init__(self, driver):
        self.driver = driver

    def create_new(self):
        return self.driver.find_element(By.XPATH, "//div[@class='aml-rule-category-create-new'][1]")

    def name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='categoryName'][1]")

    def descriptiopn(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='categoryDes']")

    def user_search(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floatingSearch']")

    def user_select(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'searchItem mb-1')][1]")

    def save_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save'][1]")

    def cancel_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")