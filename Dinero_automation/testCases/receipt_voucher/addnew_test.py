import time


import self
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Pulldownmenu import Account_pulldownmenu
from Dinero_automation.pageObjects.Receipt_vouchers import Add_new
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
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

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)

        # click action for nav bar arrow
        self.acc = Account_pulldownmenu(self.driver)

        # Locate the customer pull-down element
        Acc_pull_element = self.driver.find_element(By.XPATH,
                                                    "//div[normalize-space()='Accounts']")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Acc_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        receipt_element = self.driver.find_element(By.XPATH,
                                                   "//div[normalize-space()='Receipts']")
        receipt_element.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(3)
        client = self.an.client_search()

        client.send_keys("MRF TYRES")
        cust_click = self.driver.find_element(By.XPATH,
                                              "//div[@class='searchItem mb-1']")
        cust_click.click()
        time.sleep(2)

        client_rep = self.an.client_rep_name()
        client_rep.send_keys("Subash")

        id_num = self.an.id_num()
        id_num.send_keys("567867867")

        id_exp = self.an.id_exp_date()
        id_exp.send_keys("22101999")

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_post_date().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

        effct_gene = self.an.effect_general()
        effct_gene.send_keys("client MRF")

        time.sleep(2)
        glaccount_sel = self.an.gl_account()
        glaccount_sel.click()

        time.sleep(2)

        self.an.click_cash().click()
        #self.an.click_cheque().click()
        self.an.click_digital_pay().click()
        self.an.click_online().click()
        
        self.an.pos().click()


        self.an.lc_amount().send_keys("1500")
        self.an.transaction_remark().send_keys("cash")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.an.enter_cash()
        denom1 = self.an.denom1()
        denom1.send_keys("300")
        self.an.cashsubmitt().click()
        time.sleep(2)

        self.an.enter_pos()
        pos_amount = self.an.pos_amount()
        pos_amount.send_keys("300")
        bankpos = Select(self.an.drp_pos_bank())
        bankpos.select_by_index(2)
        self.an.pos_submitt.click()
        time.sleep(2)

        # self.an.enter_cheque().send_keys("300")
        # self.an.enter_online()
        #
        # time.sleep(2)

        self.an.enter_digital_pay()
        dig_amount = self.an.digital_amunt()
        dig_amount.send_keys("300")
        bankpos = Select(self.an.drp_pos_bank())
        bankpos.select_by_index(2)
        self.an.pos_submitt.click()

        time.sleep(2)

        # self.an.req_for_approval().click()

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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("Badasaab")
        cust_click = self.driver.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(1)
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

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_pos().click()
        self.an.click_online().click()
        self.an.digital_pay().click()

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("1500")

        self.an.enter_cash().send_keys("300")
        self.an.enter_pos().send_keys("300")
        self.an.enter_cheque().send_keys("300")
        self.an.enter_online().send_keys("300")
        self.an.enter_digital_pay().send_keys("300")

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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("Badasaab")
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

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_pos().click()
        self.an.click_online().click()
        self.an.digital_pay().click()

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("1500")

        self.an.enter_cash().send_keys("300")
        self.an.enter_pos().send_keys("300")
        self.an.enter_cheque().send_keys("300")
        self.an.enter_online().send_keys("300")
        self.an.enter_digital_pay().send_keys("300")

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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        # cust_click = self.driver.find_element(By.XPATH,
        #                                       "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # cust_click.click()
        time.sleep(2)

        transc_mode = Select(self.an.drp_transcation_mode())
        transc_mode.select_by_index(2)
        time.sleep(2)
        self.an.delegate_search().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        # deleg_click = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        # deleg_click.click()
        time.sleep(2)

        branch = Select(self.an.branch())
        branch.select_by_index(2)

        user = Select(self.an.user())
        user.select_by_index(1)

        wallet = Select(self.an.wallet())
        wallet.select_by_index(2)

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_pos().click()
        self.an.click_online().click()
        self.an.digital_pay().click()

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        self.an.enter_cash().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_pos().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_cheque().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_online().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        self.an.enter_digital_pay().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_clear_ante_date(self, setup):
        ###########test checking after clearing ante date values are not going################

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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("Badasaab")
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

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")
        time.sleep(2)
        date_val = self.an.effective_date().get_attribute("value")
        print("date_val:", date_val)

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        effct_gene_val = effct_gene.first_selected_option.text
        print("effct_gene_val:", effct_gene_val)

        time.sleep(2)
        self.an.click_antedate().click()

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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("Badasaab")
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

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

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

    def test_add_2_gl_account_and_save(self, setup):
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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)
        self.an = Add_new(self.driver)

        self.an.click_new_btn().click()
        time.sleep(1)

        customer_typ = Select(self.an.drp_customer_typ())
        customer_typ.select_by_index(1)
        time.sleep(2)

        self.an.customer_search().send_keys("Badasaab")
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

        self.an.click_antedate().click()
        time.sleep(2)
        self.an.effective_date().send_keys("26082024")

        effct_gene = Select(self.an.drp_effect_general())
        effct_gene.select_by_index(1)

        time.sleep(2)

        self.an.click_cash().click()
        self.an.click_cheque().click()
        self.an.click_pos().click()
        self.an.click_online().click()
        self.an.digital_pay().click()

        genral_led = Select(self.an.drp_gender_led_acc())
        genral_led.select_by_index(2)
        time.sleep(2)

        self.an.transaction_remark().send_keys("cash")
        self.an.lc_amount1().send_keys("750")
        time.sleep(3)
        self.an.click_new_row().click()
        time.sleep(1)

        second_gl = Select(self.an.click_2nd_gl())
        second_gl.select_by_index(1)

        self.an.click_2nd_transaction_remark().send_keys("3265")

        self.an.lc_2nd_amount().send_keys("750")
        time.sleep(2)
        self.an.enter_cash().send_keys("300")
        self.an.enter_pos().send_keys("300")
        self.an.enter_cheque().send_keys("300")
        self.an.enter_online().send_keys("300")
        self.an.enter_digital_pay().send_keys("300")

        time.sleep(2)

        self.an.req_for_approval().click()

    def test_approve_click(self, setup):
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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)

        approval_row = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
        approval_row.click()
        time.sleep(2)

        Approve_click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']")
        Approve_click.click()

    def test_reject_click(self, setup):
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

        receipt_voucher = self.driver.find_element(By.XPATH,
                                                   "//span[contains(@class,'pullDwn_benePage')][normalize-space()='Receipt Voucher']")
        receipt_voucher.click()
        time.sleep(2)

        reject_row = self.driver.find_element(By.XPATH,
                                              "/html/body/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]")
        reject_row.click()
        time.sleep(2)

        reject_click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Reject']")
        reject_click.click()
