from selenium.webdriver.common.by import By


class General_Information():
    def __init__(self, driver):
        self.driver = driver

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None

    def drp_category(self):
        return self.driver.find_element(By.ID, "Category")

    def catego_other_field(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Other Category']")

    def name(self):
        return self.driver.find_element(By.ID, "Name")

    def arabic_name(self):
        return self.driver.find_element(By.ID, "Arabic Name")

    def adress_1(self):
        return self.driver.find_element(By.ID, "Address 1")

    def adress_2(self):
        return self.driver.find_element(By.ID, "Address 2")

    def adress_3(self):
        return self.driver.find_element(By.ID, "Address 3")

    def postal_code(self):
        return self.driver.find_element(By.ID, "Postal Code")

    def city(self):
        return self.driver.find_element(By.ID, "City")

    def drp_country(self):
        return self.driver.find_element(By.ID, "Country")

    def drp_country_of_incorporation(self):
        return self.driver.find_element(By.ID, "Country of Incorporation")

    def drp_country_code(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def mobile_number(self):
        return self.driver.find_element(By.NAME, "Mobile Number")

    def email(self):
        return self.driver.find_element(By.ID, "Email")

    def btn_nxt(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]")

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_cancelconfirm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")


class Agreement_Details():
    def __init__(self, driver):
        self.driver = driver

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None

    def dpick_agreement_start_details(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Agreement Start Date']")

    def dpick_agreement_end_details(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Agreement End Date']")

    def registration_number(self):
        return self.driver.find_element(By.ID, "Registration Number")

    def dpick_registration_exp_date(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@name,'Registration Expiry Date')]")

    def trade_license_number(self):
        return self.driver.find_element(By.ID, "Trade License Number")

    def dpick_trade_exp_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Trade License Expiry Date']")

    def license_number(self):
        return self.driver.find_element(By.ID, "License Number")

    def licensing_authority(self):
        return self.driver.find_element(By.ID, "Licensing Authority")

    def authoritzed_person_name(self):
        return self.driver.find_element(By.ID, "Authorized Person Name")

    def drp_gender(self):
        return self.driver.find_element(By.ID, "Gender")

    def dpick_date_of_birth(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[6]/div[2]/div/div[2]/input")

    def drp_country_of_birh(self):
        return self.driver.find_element(By.ID, "Country of Birth")

    def drp_nationality(self):
        return self.driver.find_element(By.ID, "Nationality")

    def fund_btn_new(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/button")

    def drp_fund_curency(self):
        return self.driver.find_element(By.ID, "Fund Currency")

    def rate(self):
        return self.driver.find_element(By.ID, "Rate")

    def settlement_rate(self):
        return self.driver.find_element(By.ID, "Settlement Rate")

    def pay_settelement_rate(self):
        return self.driver.find_element(By.ID, "Pay-in Settlement Rate")

    def balance_trigger(self):
        return self.driver.find_element(By.ID, "Balance Alert Trigger")

    def btn_add(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/div[2]/div/div/div[2]/div/button[2]")

    def btn_cancel_fund(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[1]/div[8]/div[2]/div/div/div[2]/div/button[1]")

    def fundcurr_table(self):
        self.driver.find_element(By.XPATH, "//div[contains(@class,'pointer-cursor')]").click()

    def delete(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")

    def btn_nxt(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/button")

    def btn_cancl_confm(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']")

    def btn_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def btn_updte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']")


class Upload_document:
    def __init__(self, driver):
        self.driver = driver

    def doc_selector(self):
        return self.driver.find_element(By.XPATH, "//div[@class='uploadActionsContainer p-5']")

    def btn_cancle(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_nexte(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")

    def btn_backe(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def doc_delte(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'page-layout')]//div[4]//img[1]")

    def doc_preview(self):
        return self.driver.find_element(By.XPATH, "(//img[contains(@class,'icon-styles cursor-pointer')])[1]")

    def doc_container(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'uploadedTable card pt-2 pb-2 mt-4')]")

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None


class PayoutProfile:

    def __init__(self, driver):
        self.driver = driver

    def click_payout_profile(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Payout Profile']")

    def click_final_save_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def click_button_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def btn_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def drp_country(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Country']")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Currency']")

    def drp_date_formatt(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Date Format']")

    def drp_cost_rate_source(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[2]/div[1]/select[1]")

    def drp_fund_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Fund Currency']")

    def click_bank_transfer(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Status_0']")

    def click_fast_cash(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Status_1']")

    def click_api_available(self):
        return self.driver.find_element(By.XPATH, "//input[@name='API Available']")

    def deal_balance_alert(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Deal Balance Alert']")

    def transcation_appr_req(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Transaction Approval Required']")

    def batch_processing_req(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Batch Processing Required']")

    def customer_req_sms(self):
        return self.driver.find_element(By.XPATH, "//input[@name='Customer SMS Required']")

    def click_none(self):
        return self.driver.find_element(By.XPATH, "//label[normalize-space()='None']")

    def click_overdraft_allowed(self):
        return self.driver.find_element(By.XPATH, "//input[@value='2']")

    def overdraft_limit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Overdraft Limit']")

    def over_draft_limitalert(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Overdraft Limit Alert']")

    def overide_insuf_balance(self):
        return self.driver.find_element(By.XPATH, "//input[@value='3']")

    def click_ind_to_ind(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Individual to Individual']")

    def ind_to_indtrancs_limit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='ITI Transaction Limit']")

    def ind_to_inddrptransc_lim_currenc(self):
        return self.driver.find_element(By.XPATH, "//select[@id='ITI Transaction Limit Currency']")

    def click_ind_to_corp(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Individual to Corporate']")

    def indcop_trans_limit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='ITC Transaction Limit']")

    def indcorp_drp_trans_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='ITC Transaction Limit Currency']")

    def click_corp_to_ind(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Corporate to Individual']")

    def corp_ind_transc_limit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='CTI Transaction Limit']")

    def corp_ind_drp_trasc_curr_limlt(self):
        return self.driver.find_element(By.XPATH, "//select[@id='CTI Transaction Limit Currency']")

    def click_corp_to_corp(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Corporate to Corporate']")

    def corp_corp_transc_limi(self):
        return self.driver.find_element(By.XPATH, "//input[@id='CTC Transaction Limit']")

    def corp_to_corp_drp_trans_curre_lim(self):
        return self.driver.find_element(By.XPATH, "//select[@id='CTC Transaction Limit Currency']")

    def ban_transfer_down_select(self):
        return self.driver.find_element(By.XPATH, "//div[@class='menu-item active ']")

    def fast_cash_down_select(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'menu-item active')]")

    def click_service_charges(self):
        return self.driver.find_element(By.XPATH,
                                        "//body/div[@id='root']/div/div/div[contains(@class,'d-flex')]/div[contains(@class,'d-flex flex-column w-100 dir-ltr')]/div[contains(@class,'page-layout')]/div[contains(@class,'d-flex')]/div[contains(@class,'')]/div[contains(@class,'d-flex flex-column justify-content-center')]/div/div[contains(@class,'modal')]/div[contains(@class,'modalContent size-large')]/form/div[contains(@class,'payoutprofilesettings')]/div[contains(@class,'profileScrollable')]/div[contains(@class,'wideboxPanel')]/div[contains(@class,'d-flex flex-column')]/div[1]")

    def click_sc_from_api(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-SC from API_1']")

    def drp_sc_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='SC Currency_1']")

    def drp_sc_share_mode(self):
        return self.driver.find_element(By.XPATH, "//select[@id='SC Share Mode_1']")

    def share_factor(self):
        return self.driver.find_element(By.XPATH, "//input[@id='Share Factor_1']")

    def click_new_branch(self):
        return self.driver.find_element(By.XPATH, "//button[@title='New']")

    def click_drp_branch_id(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Branch ID']")

    def click_new_branch_id2nd(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/form/div/div[2]/div[9]/div[2]/div[1]/div[2]/div/div[6]/div[1]/div/div/select")

    def sc_data(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[2]/div[1]/div[6]/div[2]/div[2]/div[2]/input[1]")

    def click_sc_branch_new(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/form/div/div[2]/div[9]/div[2]/div[1]/div[2]/div/button")

    def sc_add_and_close(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add & Close']")

    def sc_cancel_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='newDiv']//button[@title='Cancel'][normalize-space()='Cancel']")

    def sc_new2nd_click(self):
        return self.driver.find_element(By.XPATH, "//button[@title='New']")

    def click_incentive(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[9]/div[2]/div[2]")

    def click_incentive_slecter(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Incentive_1']")

    def drp_incentive_mode(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Incentive Mode_1']")

    def drp_settlement_cycle(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Settlement Cycle_1']")

    def incentive_curency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Incentive Currency_1']")

    def incentive_data_typing(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[9]/div[2]/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/input[1]")

    def incentive_click_new(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'d-flex m-2')]//div[contains(@class,'tableCell addNewRow')]")

    def click_other_bank_depos(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[9]/div[2]/div[3]")

    def click_third_party(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-Third-Party Bank Deposit Charges_1']")

    def drp_other_bank_currency(self):
        return self.driver.find_element(By.XPATH, "//select[@id='Other Bank Deposit Charge Currency_1']")

    def other_bank_data_typin(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[1]//div[3]//div[1]//form[1]//div[1]//div[2]//div[9]//div[2]//div[3]//div[2]//div[1]//div[3]//div[2]//div[2]//input[1]")

    def other_bank_new_click(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[2]/div[9]/div[2]/div[3]/div[2]/div[1]/div[3]/div[3]/div[1]/button[1]")

    def payout_save_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'d-flex justify-content-between')]//button[contains(@title,'Save')][normalize-space()='Save']")

    def click_cancel_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/div[1]/div[3]/button[1]")

    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//span[@class='error-message']").text
        except:
            None

    def transfer_type_error(self):
        try:
            return self.driver.find_element(By.XPATH, "//div[@class='errorMsgContainer']").text
        except:
            None

    def editmode_message(self):
        try:
            return self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div/div").text
        except:
            None