from selenium.webdriver.common.by import By


class To_be_approved:

    def __init__(self, driver):
        self.driver = driver

    def to_be_approved(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]")

    def date_from_field(self):
        return self.driver.find_element(By.XPATH, "//input[@name='From Date']")

    def date_to_field(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]")

    def refresh_insd(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'d-flex align-items-center')]//img[contains(@alt,'delete icon')]").click()

    def click_new_deal(self):
        return self.driver.find_element(By.XPATH,
                                        "//button[normalize-space()='New Deal']")

    def drp_service_pro(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Service Provider']")

    def drp_country(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Country']")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Currency']")

    def refresh_out(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='d-flex flex-row justify-content-between align-items-end']//div//img[@alt='delete icon']").click()

    def select(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Select']")

    def drp_dealmode(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Deal Mode']")

    def deal_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Amount']")

    def deal_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Rate']")

    def deal_reverse_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Reverse Rate']")

    def fund_deduction(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Fund Deduction']")

    def deal_cost_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Cost Rate']")

    def cost_reverse_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Cost Reverse Rate']")

    def equilant_lc(self):
        return self.driver.find_element(By.XPATH, "//div[6]//div[3]//div[1]//div[1]//input[1]")

    def fund_rate(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

    def new_deal_position(self):
        return self.driver.find_element(By.XPATH, "//input[@id='New Deal Position']")

    def updated_cost_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Updated Cost Rate']")

    def equilant_lc2(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/input[1]")







    def request_for_approval(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']").click()


class Approved:

    def __init__(self, driver):
        self.driver = driver

    def to_be_approved(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/span").click()

    def date_from_field(self):
        return self.driver.find_element(By.XPATH, "//input[@name='From Date']")

    def date_to_field(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]")

    def refresh_insd(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'d-flex align-items-center')]//img[contains(@alt,'delete icon')]").click()

    def click_new_deal(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]")

    def drp_service_pro(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Service Provider']")

    def drp_country(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Country']")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Currency']")

    def refresh_out(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='d-flex flex-row justify-content-between align-items-end']//div//img[@alt='delete icon']").click()

    def select(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Select']")

    def drp_dealmode(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Deal Mode']")

    def deal_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Amount']")

    def deal_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='dealRate']")

    def deal_reverse_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='dealReverseRate']")

    def request_for_approval(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']").click()

    def select_first_Deal_phenom(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]").click()

    def select_second_deal_approval(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[2]/div[2]").click()

    def click_approve(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()

    def click_reject(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Reject']").click()

    def click_approved(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Approved']").click()

    def click_Reject(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Reject']").click()



