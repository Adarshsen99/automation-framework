from selenium.webdriver.common.by import By


class Request_rate:
    def __init__(self, driver):
        self.driver = driver

    def click_request_rate(self):
        return self.driver.find_element(By.XPATH, "//span[@class='RCAccessItems selectedRCAccess']")

    def drp_service_provider(self):
        return self.driver.find_element(By.NAME, "filter_sp")

    def drp_country(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/select[1]")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@name='filter_crncy']")

    def drp_branch(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/select[1]")

    def click_filter(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']")

    def click_reset(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Reset']")

    def drp_margin_control(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/span[9]/div/select")

    def issue_rate_input(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/span[10]/input")

    def slab_wise(self):
        return self.driver.find_element(By.XPATH, "//input[@id='slabwise-1-req']")

    def slab_selector(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/span[13]/span[1]/img[1]")

    def best_rate_perc(self):
        return self.driver.find_element(By.XPATH, "//input[@id='best_rate_percentage']")

    def best_rate(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")

    def from_amount(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")

    def slab_iss_perc(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")

    def slab_issue_rate(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]")

    def slab_best_rate_perc(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/input[1]")

    def slab_best_rate(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/input[1]" )

    def slab_delete(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[6]/span[1]")

    def click_req_for_apprvl(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']")




