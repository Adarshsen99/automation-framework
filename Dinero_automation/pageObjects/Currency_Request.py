from selenium.webdriver.common.by import By


class Create_Request:
    def __init__(self, driver):
        self.driver = driver

    def click_request(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create Request']")

    def drp_FC_name(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/span[2]/select")

    def FC_amount(self):
        return self.driver.find_element(By.XPATH, "//input[@id='cr-req-table-fc-amt-no-1']")

    def click_ins_new(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='New']")

    def drp_second_Fc(self):
        return self.driver.find_element(By.XPATH, "(//select[contains(@class,'false')])[2]")

    def second_FC_amount(self):
        return self.driver.find_elemen(By.XPATH, "//input[@id='cr-req-table-fc-amt-no-2']")

    def to_be_approved(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Request for Approval']")


class Tobe_approved:
    def __init__(self, driver):
        self.driver = driver

    def click_to_be_approved(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[18]")

    def click_reject(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']")

    def click_approve(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def click_purchase_order(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-8']//input[@id='1']")

    def click_internal_transfer(self):
        return self.driver.find_element(By.XPATH, "//div[@class='col-8']//input[@id='2']")

    def drp_branch(self):
        return self.driver.find_element(By.XPATH, "(//select[contains(@class,'false')])[1]")

    def click_process(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Process']")


class Tobe_Processed:
    def __init__(self, driver):
        self.driver = driver

    def select_row(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[50]/span[1]/div/input")

    def click_intiate_po(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/button")


class Purchase_orders:
    def __init__(self, driver):
        self.driver = driver

    def click_row(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='InitPOTableRow'])[9]")

    def drp_vendor(self):
        return self.driver.find_element(By.XPATH, "//select[contains(@name,'po_modal_vendor')]")

    def drp_bill_to(self):
        return self.driver.find_element(By.XPATH, "//select[@name='po_modal_bill_to']")

    def drp_deliver_to(self):
        return self.driver.find_element(By.XPATH, "//select[@name='po_modal_deliver_to']")

    def drp_shipping_mode(self):
        return self.driver.find_element(By.XPATH, "//div[@class='POsModInitiateContainer .POsShipping']//select[@name='po_modal_shipping_mode']")

    def transit_agent(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'POsModInitiateContainer .POsTransit')]//select[contains(@name,'po_modal_shipping_mode')]")

    def delivery_date(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@name,'Delivery Date')]")

    def drp_settlement_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@name='Settlement Currency']")

    def rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='pos_mod_init_rate']")

    def click_fix_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']")

    def unfix_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def fc_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='fc_rate_94']")

    def Fc_rate(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lc_rate_94']")

    def process_po(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Process PO']")

    def click_receive_shipment(self):
        return self.driver.find_element(By.XPATH, "//span[@class='CRPOBodyTab selectedCRPOBodyTab']")

    def click_row_po(self):
        return self.driver.find_element(By.XPATH, "//div[33]")

    def click_verify(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Verify']")

    def cash500(self):
        return self.driver.find_element(By.XPATH, "//input[@id='po_mod_denom_input_0']")

    def cash20(self):
        return self.driver.find_element(By.XPATH, "//input[@id='po_mod_denom_input_1']")

    def cash10(self):
        return self.driver.find_element(By.XPATH, "//input[@id='po_mod_denom_input_2']")

    def cash2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='po_mod_denom_input_3']")

    def cash1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='po_mod_denom_input_4']")

    def btn_verify(self):
        return self.driver.find_element(By.XPATH, "//div[@class='POModDenomActions']//button[@title='Verify'][normalize-space()='Verify']")

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def click_completed_pos(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Completed POs']")

    def click_intiated_int_trasn(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'CurrencyRequestModuleContainer')]//div[3]")

    def click_intiate_row(self):
        return self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[11]")

    def interwallet(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']")

    def interbranch(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def rate_row(self):
        return self.driver.find_element(By.XPATH, "//input[@id='rate_45']")

    def rev_rate_raw(self):
        return self.driver.find_element(By.XPATH, "//input[@id='rev_rate_45']")

    def process_shipment(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Process Shipment']")

    def click_receive_shipment(self):




