from selenium.webdriver.common.by import By


class Vendor_reg:
    def __init__(self, driver):
        self.driver = driver

    def click_new(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Create New']")

    def click_both(self):
        return self.driver.find_element(By.XPATH, "(//input[@id='3'])[1]")

    def click_client(self):
        return self.driver.find_element(By.XPATH, "//input[@id='2']")

    def click_vendor(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']")

    def company_name(self):
        return self.driver.find_element(By.ID, "vndr_comp_info_cmp_nm")

    def arabic_name(self):
        return  self.driver.find_element(By.XPATH,"//input[@id='vndr_comp_info_arb_nm']")

    def building_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_bld_num']")

    def building_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_bld_nm']")

    def street(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_strt']")

    def postal_code(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_pst_cd']")

    def city(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_cty']")

    def country(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_comp_info_cntry']")

    def country_code(self):
        return self.driver.find_element(By.XPATH, "//select[@class='countrySelector']")

    def mob_number(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Vendor Number']")

    def email(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_comp_info_email']")

    def click_next(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")

    def search_parentgl(self):
        return self.driver.find_element(By.XPATH, "//input[@id='floatingSearch']")

    def click_cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    # Registration Info
    def country_of_incorp(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_cnt_inc']")

    def license_nature(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_lic_ntr']")

    def entity_type(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_ent_tp']")

    def operation_field(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_oprn_fld']")

    def trade(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_trd_srv_prdr']")

    def capital(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_info_cptl']")

    def Auth_person(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_info_auth_prsn']")

    def designation(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_dsgn']")

    def nationality(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_ntnlty']")

    def IdType(self):
        return self.driver.find_element(By.XPATH, "//select[@name='vndr_info_id_tp']")

    def Id_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_info_id_nm']")

    def id_expiry(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[6]/div[2]/div/div[2]/input")

    def cr_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_info_cr_nm']")

    def cc_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='vndr_info_cc_nm']")

    def cr_issue_date(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]/div[1]/div[2]/div[2]/input")

    def cc_issue_date(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]/div[2]/div[2]/div[2]/input")

    def cr_expiry_dt(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]/div[1]/div[3]/div[2]/input")

    def cc_exp_date(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]/div[2]/div[3]/div[2]/input")

    def cancel(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def btn_back(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Back']")

    def brn_save(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")