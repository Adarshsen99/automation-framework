
from selenium.webdriver.common.by import By

class Remittance_Details():

    remittance_xpath = "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div[1]"

    drp_currency_details_id = "Currency"
    rate_id = "remiRate"
    rev_rate_id = "remiRevRate"
    fc_amount_id = "remiFC"
    lc_amount_id = "remiLC"
    sc_id = "remiSC"
    tax_id = "remiTax"

    def __init__(self,driver):
        self.driver = driver

    def click_remitance(self):
        return self.driver.find_element(By.XPATH, self.remittance_xpath)

    def drp_currency_details(self):
        return self.driver.find_element(By.ID, self.drp_currency_details_id)

    def rate(self):
        return self.driver.find_element(By.ID, self.rate_id)

    def rev_rate(self):
        return self.driver.find_element(By.ID, self.rev_rate_id)

    def fc_amount(self):
        return self.driver.find_element(By.ID, self.fc_amount_id)

    def lc_amount(self):
        return self.driver.find_element(By.ID, self.lc_amount_id)

    def sc(self):
        return self.driver.find_element(By.ID, self.sc_id)

    def tax(self):
        return self.driver.find_element(By.ID, self.tax_id)
