import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Accounts_menu.Payment_voucher import Add_new
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_add_new:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_name_self(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_debitcard().click()
        self.an.digital_pay().click()
        self.an.invoice_refrence().send_keys("654548")

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("1000")

        self.an.enter_cash().send_keys("250")

        self.an.enter_cheque().send_keys("250")
        self.an.enter_debitcard().send_keys("250")
        self.an.enter_digital_pay().send_keys("250")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_valid_data_delegate(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        self.an.delegate_search().send_keys("Abooba")

        deleg_click = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_debitcard().click()
        self.an.digital_pay().click()
        self.an.invoice_refrence().send_keys("654548")

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("1000")

        self.an.enter_cash().send_keys("250")

        self.an.enter_cheque().send_keys("250")
        self.an.enter_debitcard().send_keys("250")
        self.an.enter_digital_pay().send_keys("250")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_without_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        # customer_typ = Select(self.an.drp_customer_typ())
        # customer_typ.select_by_index(1)
        # time.sleep(2)
        #
        # self.an.customer_search().send_keys("Badasaab")
        # cust_click = self.driver.find_element(By.XPATH,
        #                                       "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # cust_click.click()
        # time.sleep(2)
        #
        # transc_mode = Select(self.an.drp_transcation_mode())
        # transc_mode.select_by_index(1)
        # time.sleep(2)
        # self.an.delegate_search().send_keys("Abooba")
        #
        # deleg_click = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # deleg_click.click()
        # time.sleep(2)
        #
        # branch = Select(self.an.branch())
        # branch.select_by_index(2)
        #
        # user = Select(self.an.user())
        # user.select_by_index(1)
        #
        # wallet = Select(self.an.wallet())
        # wallet.select_by_index(2)
        #
        # self.an.click_antedate().click()
        # time.sleep(2)
        # self.an.effective_date().send_keys("26082024")
        #
        # effct_gene = Select(self.an.drp_effect_general())
        # effct_gene.select_by_index(1)
        #
        # time.sleep(2)
        #
        # self.an.click_cash().click()
        # self.an.click_cheque().click()
        # self.an.click_pos().click()
        # self.an.click_online().click()
        # self.an.digital_pay().click()
        #
        # genral_led = Select(self.an.drp_gender_led_acc())
        # genral_led.select_by_index(2)
        # time.sleep(2)
        #
        # self.an.transaction_remark().send_keys("cash")
        # self.an.lc_amount1().send_keys("1500")
        #
        # self.an.enter_cash().send_keys("300")
        # self.an.enter_pos().send_keys("300")
        # self.an.enter_cheque().send_keys("300")
        # self.an.enter_online().send_keys("300")
        # self.an.enter_digital_pay().send_keys("300")
        #
        # time.sleep(2)

        self.an.req_for_approval().click()

    def test_adding_without_delegate(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        # self.an.delegate_search().send_keys("Abooba")
        #
        # deleg_click = self.driver.find_element(By.XPATH,
        #                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_debitcard().click()
        self.an.digital_pay().click()
        self.an.invoice_refrence().send_keys("654548")

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("1000")

        self.an.enter_cash().send_keys("250")

        self.an.enter_cheque().send_keys("250")
        self.an.enter_debitcard().send_keys("250")
        self.an.enter_digital_pay().send_keys("250")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_sending_spl_char_num(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        # cust_click = self.driver.find_element(By.XPATH,
        #                                       "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        self.an.delegate_search().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        # deleg_click = self.driver.find_element(By.XPATH,
        #                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_debitcard().click()
        self.an.digital_pay().click()
        self.an.invoice_refrence().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.lc_amount1().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        self.an.enter_cash().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        self.an.enter_cheque().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_debitcard().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_digital_pay().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_clear_post_date(self, setup):
        ###########test checking after clearing post date values are not going################

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        self.an.delegate_search().send_keys("Abooba")

        deleg_click = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        date_val = self.an.effective_date().get_attribute("value")
        print("date_val:", date_val)

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        effct_gene_val = effct_gene.first_selected_option.text
        print("effct_gene_val:", effct_gene_val)

        time.sleep(2)
        self.an.click_postdate().click()

        print("values after deselecting ")

        date_val_aft = self.an.effective_date().get_attribute("value")
        print("date_val_aft:", date_val_aft)

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        effct_gene_val_aft = effct_gene.first_selected_option.text
        print("effct_gene_val_aft:", effct_gene_val_aft)

        if date_val != date_val_aft:
            assert True
        else:
            assert False

        if effct_gene_val != effct_gene_val_aft:
            assert True
        else:
            assert False

    def test_selecting_and_deselecting_receipt_mode(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        pay_voucher = self.driver.find_element(By.XPATH,
                                               "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
        pay_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_vendor_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.vendor_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        self.an.delegate_search().send_keys("Abooba")

        deleg_click = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_postdate().click()
        time.sleep(3)
        self.an.effective_date().send_keys("01112024")
        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("600")

        self.an.enter_cash().send_keys("300")

        cash_val = self.an.enter_cash().get_attribute("value")

        print("cash_val:", cash_val,
              )

        time.sleep(2)

        self.an.click_cash().click()

        time.sleep(2)

        self.an.click_cash().click()

        print("values after deselecting")

        cash_val_aft = self.an.enter_cash().get_attribute("value")

        print("cash_val_aft:", cash_val_aft,
              )

        if cash_val != cash_val_aft:
            assert True
        else:
            assert False

    # def test_add_2_gl_account_and_save(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #
    #     self.lp.clickLogin()
    #     time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
#     vouchers.click()
#     time.sleep(1)
# #
#     receipt_voucher = self.driver.find_element(By.XPATH,
#                                                "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
#     receipt_voucher.click()
#     time.sleep(2)
#     self.an = Add_new(self.driver)
#
#     self.an.click_new_btn().click()
#     time.sleep(1)
#
#     customer_typ = Select(self.an.drp_customer_typ())
#     customer_typ.select_by_index(1)
#     time.sleep(2)
#
#     self.an.customer_search().send_keys("Badasaab")
#     cust_click = self.driver.find_element(By.XPATH,
#                                           "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
#     cust_click.click()
#     time.sleep(2)
#
#     transc_mode = Select(self.an.drp_transcation_mode())
#     transc_mode.select_by_index(2)
#     time.sleep(2)
#
#     branch = Select(self.an.branch())
#     branch.select_by_index(2)
#
#     user = Select(self.an.user())
#     user.select_by_index(1)
#
#     wallet = Select(self.an.wallet())
#     wallet.select_by_index(2)
#
#     self.an.click_antedate().click()
#     time.sleep(2)
#     self.an.effective_date().send_keys("26082024")
#
#     effct_gene = Select(self.an.drp_effect_general())
#     effct_gene.select_by_index(1)
#
#     time.sleep(2)
#
#     self.an.click_cash().click()
#     self.an.click_cheque().click()
#     self.an.click_pos().click()
#     self.an.click_online().click()
#     self.an.digital_pay().click()
#
#     genral_led = Select(self.an.drp_gender_led_acc())
#     genral_led.select_by_index(2)
#     time.sleep(2)
#
#     self.an.transaction_remark().send_keys("cash")
#     self.an.lc_amount1().send_keys("750")
#     time.sleep(3)
#     self.an.click_new_row().click()
#     time.sleep(1)
#
#     second_gl = Select(self.an.click_2nd_gl())
#     second_gl.select_by_index(1)
#
#     self.an.click_2nd_transaction_remark().send_keys("3265")
#
#     self.an.lc_2nd_amount().send_keys("750")
#     time.sleep(2)
#     self.an.enter_cash().send_keys("300")
#     self.an.enter_pos().send_keys("300")
#     self.an.enter_cheque().send_keys("300")
#     self.an.enter_online().send_keys("300")
#     self.an.enter_digital_pay().send_keys("300")
#
#     time.sleep(2)
#
#     self.an.req_for_approval().click()
#
# def test_approve_click(self, setup):
#
#     self.driver = setup
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#     self.driver.implicitly_wait(30)
#     self.lp = LoginPage(self.driver)
#     self.lp.setUsername(self.uname)
#     self.lp.setPassword(self.upass)
#
#     self.lp.clickLogin()
#     time.sleep(2)
#
#     # click action for nav bar arrow
#     vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
#     vouchers.click()
#     time.sleep(1)
#
#     receipt_voucher = self.driver.find_element(By.XPATH,
#                                                "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
#     receipt_voucher.click()
#     time.sleep(2)
#
#     approval_row = self.driver.find_element(By.XPATH,
#                                             "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
#     approval_row.click()
#     time.sleep(2)
#
#     Approve_click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']")
#     Approve_click.click()
#
# def test_reject_click(self, setup):
#     self.driver = setup
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#     self.driver.implicitly_wait(30)
#     self.lp = LoginPage(self.driver)
#     self.lp.setUsername(self.uname)
#     self.lp.setPassword(self.upass)
#
#     self.lp.clickLogin()
#     time.sleep(2)
#
#     # click action for nav bar arrow
#     vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
#     vouchers.click()
#     time.sleep(1)
#
#     receipt_voucher = self.driver.find_element(By.XPATH,
#                                                "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
#     receipt_voucher.click()
#     time.sleep(2)
#
#     reject_row = self.driver.find_element(By.XPATH,
#                                           "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
#     reject_row.click()
#     time.sleep(2)
#
#     reject_click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Reject']")
#     reject_click.click()
#
# def test_testing(self, setup):
#     self.driver = setup
#     self.driver.get(self.url)
#     self.driver.maximize_window()
#     self.driver.implicitly_wait(30)
#     self.lp = LoginPage(self.driver)
#     self.lp.setUsername(self.uname)
#     self.lp.setPassword(self.upass)
#
#     self.lp.clickLogin()
#     time.sleep(2)
#
#     # click action for nav bar arrow
#     vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
#     vouchers.click()
#     time.sleep(1)
#
#     pay_voucher = self.driver.find_element(By.XPATH,
#                                            "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Payment Voucher']")
#     pay_voucher.click()
#     time.sleep(2)
#     self.an = Add_new(self.driver)
#
#     self.an.click_new_btn().click()
#     time.sleep(1)
#
#     # customer_typ = Select(self.an.drp_customer_typ())
#     # customer_typ.select_by_index(1)
#     # time.sleep(2)
#     #
#     # self.an.customer_search().send_keys("Badasaab")
#     # cust_click = self.driver.find_element(By.XPATH,
#     #                                       "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
#     # cust_click.click()
#     # time.sleep(2)
#
#     transc_mode = Select(self.an.drp_transcation_mode())
#     transc_mode.select_by_index(2)
#     time.sleep(2)
#
#     branch = Select(self.an.branch())
#     branch.select_by_index(2)
#
#     user = Select(self.an.user())
#     user.select_by_index(1)
#
#     wallet = Select(self.an.wallet())
#     wallet.select_by_index(2)
#
#     # self.an.click_antedate().click()
#     # time.sleep(2)
#     # self.an.effective_date().send_keys("26082024")
#
#     # effct_gene = Select(self.an.drp_effect_general())
#     # effct_gene.select_by_index(1)
#     #
#     # time.sleep(2)
#
#     self.an.click_cash().click()
#     self.an.click_cheque().click()
#     # self.an.click_pos().click()
#     # self.an.click_online().click()
#     self.an.digital_pay().click()
#
#     genral_led = Select(self.an.drp_gender_led_acc())
#     genral_led.select_by_index(2)
#     time.sleep(2)
#
#     self.an.transaction_remark().send_keys("cash")
#     self.an.lc_amount1().send_keys("1500")
#
#     self.an.enter_cash().send_keys("300")
#     # self.an.enter_pos().send_keys("300")
#     self.an.enter_cheque().send_keys("300")
#     # self.an.enter_online().send_keys("300")
#     self.an.enter_digital_pay().send_keys("300")
#
#     time.sleep(2)
#
#     self.an.req_for_approval().click()
