from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CustPulldownmenu():
    cust_pull_xpath = "(//div[@class='pullDwnMenu_Head pullDwnMenu_Dropdown'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_pull(self, ):
        return self.driver.find_element(By.XPATH, self.cust_pull_xpath)
        # Hover over the pull-down menu

    def click_corp_customer(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Corporate Customers']").click()

    def click_ind_customer(self):
        self.driver.find_element(By.XPATH,
                                 "//span[@class='pullDwn_custPage'][normalize-space()='Individual Customers']")

    def click_manage_customer(self):
        self.driver.find_element(By.XPATH,
                                 "//span[@class='pullDwn_custPage'][normalize-space()='Individual Customers']").click()

    def click_ind_beneficiaries(self):
        self.driver.find_element(By.XPATH,
                                 "//span[@class='pullDwn_custPage'][normalize-space()='Individual Beneficiaries']").click()

    def click_corp_beneficiaries(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Corporate Beneficiaries']").click()


class Account_pulldownmenu():
    def __init__(self, driver):
        self.driver = driver

    def click_account_menu(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[5]")

    def click_transit_agent(self):
        return self.driver.find_element(By.XPATH,
                                        "//span[@class='pullDwn_custPage'][normalize-space()='Transit Agent']")

    def click_withdrawal_voucher(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Withdrawal']")

    def click_vendor(self):
        return self.driver.find_element(By.XPATH, "//div[5]//div[1]//div[2]//span[1]")

    def click_self_cash(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Deposits Self']")

    def click_local_bank(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'Local Banks')]")

    def click_journel_entries(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Journal Entries']")


class AML_MENU():
    def __init__(self, driver):
        self.driver = driver

    def click_aml_menu(self):
        return self.driver.find_element(By.XPATH, "//div[normalize-space()='AML'][1]")

    def click_aml_auth(self):
        return self.driver.find_element(By.XPATH, "//div[normalize-space()='Authorization'][1]")
