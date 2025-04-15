from selenium.webdriver.common.by import By


class Add_banks:
    def __init__(self, driver):
        self.driver = driver

    def add_bank_click(self):
        return self.driver.find_element(By.XPATH, "//div[@class='addLclBnkContainer']")

    def bank_name(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='bsc_nm_bank_name'])[1]")

    def Bank_short_name(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='bsc_nm_short_name'])[1]")

    def arabic_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_nm_arabic_name']")

    def branch_code(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cd_branch_code']")

    def branch_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cd_branch_name']")

    def branch_short_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cd_short_name']")

    def contact_person(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cntct_contact_person']")

    def designation(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cntct_designation']")

    def telephone_no(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cntct_telephone_no']")

    def mob_no(self):
        return self.driver.find_element(By.XPATH, "//input[@id='bsc_cntct_mobile_no']")


class Account_profile:

    def __init__(self, driver):
        self.driver = driver

    def click_account_profile(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Account Profile']")

    def drp_account_type(self):
        return self.driver.find_element(By.XPATH, "(//select[@name='lcl_bnk_modal_ac_type'])[1]")

    def drp_currency(self):
        return self.driver.find_element(By.XPATH, "(//select[@name='lcl_bnk_modal_ac_currency'])[1]")

    def account_num(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_modal_ac_number']")

    def IBAN_num(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_modal_iban']")

    def over_draft_click(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-lcl_bnk_modal_od_allowed']")

    def overdraft_limit(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_modal_od_limit']")

    def cardType_1(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span[1]/select[1]")

    def card_number_1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_crd_no_0']")

    def card_expiry_1(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id='root']/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/span[3]/div/div/div[1]/input")

    def card_limit_1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_crd_lmt_0']")

    def click_new_card_row(self):
        return self.driver.find_element(By.XPATH, "//button[@type='button'][normalize-space()='New Row']")

    def cardType_2(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'lclBnkCardTblRws')]//div[2]//span[1]//select[1]")

    def card_number_2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_crd_no_1']")

    def card_expiry_2(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/span[3]/div/div/div[1]/input")

    def card_limit_2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lcl_bnk_crd_lmt_1']")

    def pos_enabled(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-lcl_bnk_fnd_tbl_pos_enabled']")

    def cover_up_fund(self):
        return self.driver.find_element(By.XPATH, "//input[@id='checkbox-lcl_bnk_fnd_tbl_cover_up']")

    def drp_fund_curr_1(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[1]/span[1]/select[1]")

    def daily_fund_lim_1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lc_bnk_fnd_tbl_daily_funding_limit_0']")

    def fund_rate_1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lc_bnk_fnd_tbl_fund_currency_rate_0']")

    def new_fund_row(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='LclBankFundsDetailsTableContainer']//div//button[@title='New Row'][normalize-space()='New Row']")

    def drp_fund_curr_2(self):
        return self.driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/span[1]/select[1]")

    def daily_fund_lim_2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lc_bnk_fnd_tbl_daily_funding_limit_1']")

    def fund_rate_2(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lc_bnk_fnd_tbl_fund_currency_rate_1']")

    def Add_click(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")

    def click_update(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']")

    def click_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
