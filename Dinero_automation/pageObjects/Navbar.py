from selenium.webdriver.common.by import By

class Navigation_Page():
    btn_nav_open_xpath = "//img[@class='icon-styles arrow-closed']"
    btn_nav_close_xpath = "//img[@class='icon-styles arrow-open']"
    dashboard_xpath = "//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[1]/span"
    customer_Registration_xpath ="//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[2]/span"
    corporate_customer_link_text ="//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[3]/span"
    benificiary_link_text = "//span[normalize-space()='Beneficiary']"
    corporate_beneficiary_link_text = "//span[normalize-space()='Corporate Beneficiary']"
    remittance_link_text = "//span[normalize-space()='Remittance']"
    # currency_trade_link_text = ""
    # bank_link_text = ""
    # service_provider_link_text = ""

    def __init__(self,driver):
        self.driver = driver

    def click_navbar(self):
        self.driver.find_element(By.XPATH, self.btn_nav_open_xpath).click()

    def close_navbar(self):
        self.driver.find_element(By.XPATH, self.btn_nav_close_xpath).click()

    def click_dashboard(self):
        self.driver.find_element(By.LINK_TEXT,self.dashboard_xpath)

    def click_customer_registration(self):
        self.driver.find_element(By.XPATH,self.customer_Registration_xpath).click()

    def click_customer_registration_corporate(self):
        self.driver.find_element(By.XPATH,self.corporate_customer_link_text).click()

    def click_benificiary_individual(self):
        self.driver.find_element(By.XPATH,self.benificiary_link_text).click()

    def click_benificiary_corporate(self):
        self.driver.find_element(By.XPATH,self.corporate_beneficiary_link_text).click()

    def click_remitance(self):
        self.driver.find_element(By.XPATH,self.remittance_link_text).click()

