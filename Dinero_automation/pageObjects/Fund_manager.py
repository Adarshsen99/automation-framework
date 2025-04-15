from selenium.webdriver.common.by import By


class Requests:

    def __init__(self, driver):
        self.driver = driver

    def click_request(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[1]/span").click()

    def drp_serv_pro(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div/div/span").click()

    def ser_pro_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/input")

    def search_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[3]/button").click()

    def clear_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[4]/button").click()

    def select_phenom_money(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/label/div/span").click()

    def click_phenom(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[1]/div[3]/div/div[1]/input").click()

    def fund_request(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[1]/div[3]/div/div[2]/div/input")

    def req_for_apprval(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/button").click()


class Tobeapproved:

    def __init__(self, driver):
        self.driver = driver

    def approveclick(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='To Be Approved']").click()

    def drp_serv_pro(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div/div/span").click()

    def ser_pro_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/input")

    def search_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//button[normalize-space()='Search']").click()

    def clear_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[4]/button").click()

    def select_phenom_money(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/label/div/span").click()

    def click_phenom(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@id='checkbox-Fund Row 0-To Be Approved']").click()

    def fund_approved(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div/div[1]/div/input")

    def Add_bank(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div/div[3]/button").click()

    def click_new(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]").click()

    def drp_bank(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/select")

    def Fc_amount(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/input")

    def click_confirm(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div[2]/div/div/div[3]/button[2]").click()

    def click_approve(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/button[2]").click()

    def click_rejected(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Reject']").click()


class Tobeprocessed:

    def __init__(self, driver):
        self.driver = driver

    def click_tbproce(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[4]/span").click()

    def drp_serv_pro(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div/div/span").click()

    def ser_pro_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/input")

    def search_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//button[normalize-space()='Search']").click()

    def clear_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[4]/button").click()

    def select_phenom_money(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/label/div/span").click()

    def click_phenom(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@id='checkbox-Fund Row 0-To Be Processed']").click()

    def fund_procesed(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@id='Fund Processed 0-To Be Processed']")

    def rate(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@id='Rate Field 0-To Be Processed']")

    def processed(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/button").click()


class Rejected:

    def __init__(self, driver):
        self.driver = driver

    def click_rejected(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[3]/span").click()

    def drp_serv_pro(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div/div/span").click()

    def ser_pro_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/input")

    def search_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//button[normalize-space()='Search']").click()

    def clear_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[4]/button").click()

    def select_phenom_money(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/label/div/span").click()

    def click_phenom(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div[1]/div[3]/div/div[1]/input").click()


class Processed:

    def __init__(self, driver):
        self.driver = driver

    def click_processed(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/div/div[5]/span").click()

    def drp_serv_pro(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div/div/span").click()

    def ser_pro_search(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/input")

    def search_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//button[normalize-space()='Search']").click()

    def clear_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[4]/button").click()

    def select_phenom_money(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div[1]/div/div/div[2]/div/div/ul/li[9]/label/div/span").click()


