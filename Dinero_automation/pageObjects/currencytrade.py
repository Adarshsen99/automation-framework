from selenium.webdriver.common.by import By


class SelectCustomer:

    def __init__(self, driver):
        self.driver = driver

    def customersearching(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floatingSearch']")

    def customerselect(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()

    def customer_name(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[1]/div[1]/span[2]").text

    def status(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[2]").text

    def idtype(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[2]").text

    def idnumber(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]").text

    def idexpiry(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[3]/span[2]").text

    def dob(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[2]").text

    def cob(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/span[2]").text

    def nationality(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[3]/span[2]").text

    def address1(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[1]/span[2]").text

    def address2(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[2]/span[2]").text

    def address3(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[3]/span[2]").text

    def city(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/span[2]").text

    def country(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[2]/span[2]").text

    def phonenum(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[3]/span[2]").text

    def profession(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[1]/span[2]").text

    def employed(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[2]/span[2]").text

    def empcategory(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[2]/span[2]").text

    def salaryrange(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[7]/div[2]/span[2]").text

    def cancelbtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def cancelyes(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

    def verifybtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Verify']").click()

    def nextbtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()


class Selectdelegate:

    def __init__(self, driver):
        self.driver = driver

    def Drptransction(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]")

    def delegate_search(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@id='floatingSearch']")

    def delegate_selecer(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div")

    def delegate_name(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]")

    def status(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[2]")

    def idtype(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[2]").text

    def idnumber(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[2]").text

    def idexpiry(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[2]/div[3]/span[2]").text

    def dob(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[2]").text

    def cob(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/span[2]").text

    def nationality(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[3]/div[3]/span[2]").text

    def address1(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[1]/span[2]").text

    def address2(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[2]/span[2]").text

    def address3(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[4]/div[3]/span[2]").text

    def city(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[1]/span[2]").text

    def country(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[2]/span[2]").text

    def phonenum(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[5]/div[3]/span[2]").text

    def profession(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[1]/span[2]").text

    def employed(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[2]/span[2]").text

    def empcategory(self):
        return self.driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[6]/div[2]/span[2]").text

    def salaryrange(self):
        return self.driver.find_element(By.XPATH,

                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[7]/div[2]/span[2]").text

    def cancelbtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def cancelyes(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

    def backbtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def nextbtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()


class Transaction_details:

    def __init__(self, driver):
        self.driver = driver

    def transaction_purpose(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Transaction Purpose']")

    def source_of_income(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@name,'Source of Income')]")

    def click_to_add(self):
        return self.driver.find_element(By.XPATH, "//div[@class='CTTableHeader']")

    def transc_type1(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]")

    def drp_currency1(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/select[1]")

    def fc_amount1(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[3]/input[1]")

    def rate1(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[4]/input[1]")

    def service_charge1(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[7]/input[1]")

    def add_row_click(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div[1]/div[2]/div/span")

    def transc_type2(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/span[1]/select[1]")

    def drp_currency2(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/span[2]/select[1]")

    def fc_amount2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floating_ct_table_fc_amount_1738650835533']")

    def rate2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floating_ct_table_rate_1738650835533']")

    def service_charge2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floating_ct_table_sc_1738650835533']")

    def close_button_click(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div[2]/div/span/img[2]")

    def pos_click(self):
        return self.driver.find_element(By.XPATH, "//input[@name='POS']")

    def cash_click(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Cash']")

    def online_click(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Online']")

    def cheque_click(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Cheque']")

    def digital_click(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Digital Pay']")

    def pos_type(self):
        return self.driver.find_element(By.XPATH, "//select[@name='pymnt_chcs_pos_tp']")

    def click_next(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")

    def click_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def click_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")


class Transaction_review:

    def __init__(self, driver):
        self.driver = driver

    def click_confirm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']")

    def click_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def click_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")


class Payment_details:

    def __init__(self, driver):
        self.driver = driver

    def enter_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@id='cash_input']")

    def enter_pos_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='pos_amount']")

    def drp_pos_bank(self):
        return self.driver.find_element(By.XPATH, "//select[@name='pos_bank']")

    def pos_code(self):
        return self.driver.find_element(By.XPATH, "//input[@id='pos_code']")

    def cheque_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='cheque_amount']")

    def cheque_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='cheque_number']")

    def cheque_bank(self):
        return self.driver.find_element(By.XPATH, "//input[@id='cheque_bank']")

    def cheque_date(self):
        return self.driver.find_element(By.XPATH,
                                        "//body//div//form//div//div//div//div[2]")

    def online_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='online_amount']")

    def digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[@id='digital_pay']")

    def cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def savebtn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save Currency Trade']")
    
