from selenium.webdriver.common.by import By

class Dashboard():

    def __init__(self,driver):
        self.driver = driver

    def customer_type(self):
        return self.driver.find_element(By.ID, "Customer Type")

    def sending_customers(self):
        return self.driver.find_element(By.NAME, "Customers")

    def click_customers(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/p")

    def click_edit_mode(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Edit Customer']").click()
