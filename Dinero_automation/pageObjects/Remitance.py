from selenium.webdriver.common.by import By


class Customer_Details:

    def __init__(self, driver):
        self.driver = driver

    def drp_transcation_type(self):
        return self.driver.find_element(By.ID, "Transaction Type")

    def customer_search_bar(self):
        return self.driver.find_element(By.ID, "floatingSearch")

    def search_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

    def customer_selector_karunakar(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='Karunakar middle last']").click()

    def custom_select1(self):
        return self.driver.find_element(By.XPATH, "//p[@class='dropdown-search-item-primary']").click()

    def cancel_btm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def cancel_confirm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

    def verify_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Verify']").click()

    def btn_next(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()


class Delegate_details:

    def __init__(self, driver):
        self.driver = driver

    def drp_transaction_mode(self):
        return self.driver.find_element(By.ID, "Transaction Mode")

    def delegate_searchbar(self):
        return self.driver.find_element(By.ID, "floatingSearch")

    def delegate_select_bar(self):
        return self.driver.find_element(By.XPATH, "//div[@class='dropdown-search-item']").click()

    def delegate_btn_search(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']")

    def btn_verify(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Verify']").click()

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_cancel_yes(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()

    def btn_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_nexte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def click_preview_customer_details(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'accordionHeader')]")

    def delegate_values_on_page_name(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='hilda dadad']")

    def delegate_values_on_page_arabic_name(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='asfasr']")

    def delegat_val_gender(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Female']")


class Beneficiary_details:

    def __init__(self, driver):
        self.driver = driver

    def beneficiary_search_bar(self):
        return self.driver.find_element(By.ID, "floatingSearch")

    def beneficiary_selectbar_ronaldo(self):
        return self.driver.find_element(By.XPATH, "//p[@class='dropdown-search-item-primary']").click()

    def beneficiary_select_bar_pisharadi(self):
        return self.driver.find_element(By.XPATH, "//p[@class='dropdown-search-item-primary']").click()

    def drp_location(self):
        return self.driver.find_element(By.ID, "Select Location")

    def location_select(self):
        return self.driver.find_element(By.XPATH,
                                        "//select[@id='Select Location']")

    def drp_bank(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Select Bank']")

    def btn_cancele(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def btn_backe(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_nexte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def click_delegtate_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div")


class Remittance_details:

    def __init__(self, driver):
        self.driver = driver

    def transaction_pin(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Transaction PIN']")

    def drp_remittance_purpose(self):
        return self.driver.find_element(By.ID, "Remittance Purpose")

    def drp_source_of_income(self):
        return self.driver.find_element(By.ID, "Source Of Income")

    def drp_currency(self):
        return self.driver.find_element(By.ID, "Currency")

    def drp_service_provider(self):
        return self.driver.find_element(By.ID, "Service Provider")

    def click_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Cash']").click()

    def click_pos(self):
        return self.driver.find_element(By.XPATH, "//input[@name='POS']").click()

    def click_cheque(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Cheque']").click()

    def click_online(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Online']").click()

    def click_digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Digital Pay']").click()

    def fc_type_area(self):
        return self.driver.find_element(By.XPATH, "//input[@id='remiFC']")

    def lc_type_area(self):
        return self.driver.find_element(By.XPATH, "//input[@id='remiLC']")

    def rate_type_area(self):
        return self.driver.find_element(By.XPATH, "//input[@id='remiRate']")

    def reverse_rate_type(self):
        return self.driver.find_element(By.XPATH, "//input[@id='remiRevRate']")

    def tax_typing(self):
        return self.driver.find_element(By.XPATH, "//input[@id='remiTax']")

    def btn_req_spl_rate(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request Special Rate']").click()

    def btn_cancl(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_bck(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_nxtee(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    def click_beneficiary_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id='root']/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div").click()

    def search_bene_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/span[2]").text

    def search_bank_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/span[2]").text

    def bank_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/span[2]").text

    def bank_code_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]/span[2]").text

    def bank_country_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[6]/span[2]").text

    def bank_branch_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[7]/span[2]").text

    def branch_address_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[8]/span[2]").text

    def branch_code_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[9]/span[2]").text

    def branch_country_preview(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[10]/span[2]").text


class Transaction_Review:

    def __init__(self, driver):
        self.driver = driver

    def cancele_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_backee(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']").click()

    def btn_confrm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']").click()

    def confirm_yes_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()


class Payment_details:

    def __init__(self, driver):
        self.driver = driver

    def cash_ampunt(self):
        return self.driver.find_element(By.ID, "Cash Input")

    def cash1000(self):
        return self.driver.find_element(By.ID, "Quantity 0")

    def cash100(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 1']")

    def cash10(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 2']")

    def cash1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Quantity 3']")

    def submit(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

    def pos_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='POS Amount']")

    def drp_pos_bank(self):
        return self.driver.find_element(By.XPATH, "//select[@id='POS Bank']")

    def pos_code(self):
        return self.driver.find_element(By.XPATH, "//input[@id='POS Code']")

    def cheque_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Cheque Amount']")

    def cheque_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Cheque Number']")

    def cheque_bank(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Cheque Bank']")

    def cheque_date(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floatingDate']")

    def online_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Online Amount']")

    def btn_share_url(self):
        return self.driver.find_element(By.XPATH, "//button[@title='Share']")

    def digital_pay(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Digital Pay']")

    def generate_qr_code(self):
        return self.driver.find_element(By.XPATH, "//button[@title='Generate QR']").click()

    def save_remittance(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save Remittance']").click()

    def btne_cancl(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btne_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def error_messge(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div")

    def error_messsge_notrecord(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[2]/div")
