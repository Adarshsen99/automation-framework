import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Accounts_menu.Journel_Voucher import Add_new
from Dinero_automation.pageObjects.Pulldownmenu import Account_pulldownmenu
from Dinero_automation.utilities.readProperties import ReadConfig
from datetime import datetime


class Test_add_new:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data_(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        # time.sleep(2)
        self.lp.clickLogin()
        time.sleep(3)
        self.acc = Account_pulldownmenu(self.driver)
        account_menu = self.acc.click_account_menu()

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(account_menu).perform()
        time.sleep(1)
        self.acc.click_journel_entries().click()
        time.sleep(2)

        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()



        self.an.click_ante_date().click()
        time.sleep(2)

        self.an.effective_date().send_keys("10032022")
        time.sleep(2)

        self.an.new_typ().click()
        time.sleep(1)

        branch = Select(self.an.branch1())
        branch.select_by_index(1)

        gl_account = Select(self.an.Gl_account())
        gl_account.select_by_index(3)
        time.sleep(2)

        self.an.transaction_remark().send_keys("Cash")
        LC_amount = self.an.lc_amount()
        LC_amount.send_keys("50000")
        time.sleep(2)

        self.an.click_new().click()
        time.sleep(1)

        typ = Select(self.an.type2())
        typ.select_by_index(2)

        branch2 = Select(self.an.branch_scond())
        branch2.select_by_index(2)

        gl2 = Select(self.an.gl_second())
        gl2.select_by_index(2)

        self.an.transaction_remark_second().send_keys("only cash")
        LC_2nd = self.an.lc_amount_second()
        LC_2nd.send_keys("50000")

        debit_amount = self.an.debit_total()
        print("debit_amount:", debit_amount)

        credit_total = self.an.credit_total()
        print("credit_total:", credit_total)
        time.sleep(2)

        self.an.req_for_approval().click()

    def test_send_without_data(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()
        #
        # date = self.an.date().get_attribute("value")
        # print(date)
        #
        # journel_vou_num = self.an.Journel_vouche_numb()
        # journel_vou_num.send_keys("1555")
        #
        # self.an.click_ante_date().click()
        # time.sleep(2)
        #
        # self.an.effective_date().send_keys("10032022")
        # time.sleep(2)
        #
        # type = Select(self.an.type())
        # type.select_by_index(1)
        #
        # branch = Select(self.an.branch())
        # branch.select_by_index(1)
        #
        # gl_account = Select(self.an.Gl_account())
        # gl_account.select_by_index(3)
        # time.sleep(2)
        #
        # self.an.transaction_remark().send_keys("Cash")
        # LC_amount = self.an.lc_amount()
        # LC_amount.send_keys("50000")
        # time.sleep(2)
        #
        # self.an.click_new().click()
        # time.sleep(1)
        #
        # typ = Select(self.an.type2())
        # typ.select_by_index(2)
        #
        # branch2 = Select(self.an.branch_scond())
        # branch2.select_by_index(2)
        #
        # gl2 = Select(self.an.gl_second())
        # gl2.select_by_index(2)
        #
        # # self.an.transaction_remark_second().send_keys("only cash")
        # LC_2nd = self.an.lc_amount_second()
        # LC_2nd.send_keys("50000")
        #
        # debit_amount = self.an.debit_total()
        # print("debit_amount:", debit_amount)
        #
        # credit_total = self.an.credit_total()
        # print("credit_total:", credit_total)
        # time.sleep(2)

        self.an.req_for_approval().click()

    def test_sendingspl_char(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()

        date = self.an.date().get_attribute("value")
        print(date)

        journel_vou_num = self.an.Journel_vouche_numb()
        journel_vou_num.send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        self.an.click_ante_date().click()
        time.sleep(2)

        self.an.effective_date().send_keys("10032022")
        time.sleep(2)

        type = Select(self.an.type())
        type.select_by_index(1)

        branch = Select(self.an.branch())
        branch.select_by_index(1)

        gl_account = Select(self.an.Gl_account())
        gl_account.select_by_index(3)
        time.sleep(2)

        self.an.transaction_remark().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        LC_amount = self.an.lc_amount()
        LC_amount.send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        time.sleep(2)

        self.an.click_new().click()
        time.sleep(1)

        typ = Select(self.an.type2())
        typ.select_by_index(2)

        branch2 = Select(self.an.branch_scond())
        branch2.select_by_index(2)

        gl2 = Select(self.an.gl_second())
        gl2.select_by_index(2)

        self.an.transaction_remark_second().send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")
        LC_2nd = self.an.lc_amount_second()
        LC_2nd.send_keys("ave091847!@#$%^&*()_+{}|""?>,.-+*/")

        debit_amount = self.an.debit_total()
        print("debit_amount:", debit_amount)

        credit_total = self.an.credit_total()
        print("credit_total:", credit_total)
        time.sleep(2)

        self.an.req_for_approval().click()

    def test_ante_date_uncheck(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()

        date = self.an.date().text

        print(date)

        journel_vou_num = self.an.Journel_vouche_numb()
        journel_vou_num.send_keys("1555")

        self.an.click_ante_date().click()
        time.sleep(2)

        effec_date = self.an.effective_date()
        effec_date.send_keys("10032022")
        data = effec_date.get_attribute("value")
        time.sleep(2)

        print("effective", data)

        self.an.click_ante_date().click()
        time.sleep(2)

        effec_date_aft = self.an.effective_date().get_attribute("value")
        time.sleep(2)

        print("after deselecting")

        print(effec_date_aft)

        if effec_date != effec_date_aft:
            assert True
        else:
            assert False

    def test_ante_accept_future_date(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # Click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()

        date = self.an.date().text
        print(date)

        journel_vou_num = self.an.Journel_vouche_numb()
        journel_vou_num.send_keys("1555")

        self.an.click_ante_date().click()
        time.sleep(2)

        effec_date = self.an.effective_date()
        effec_date.send_keys("25112026")
        data = effec_date.get_attribute("value")
        time.sleep(2)

        print("effective", data)

        # Target date to compare
        target_date = datetime.strptime("31-10-2024", "%d-%m-%Y")

        # Convert the date from the effective date field with format "YYYY-MM-DD"
        test_date = datetime.strptime(data, "%Y-%m-%d")

        # Assert if the test date is less than the target date
        assert test_date < target_date, f"Test failed: {data} is not earlier than 31-10-2024."

    def test_ante_date_accepts_correct_value(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)

        self.lp.clickLogin()
        time.sleep(2)

        # Click action for nav bar arrow
        vouchers = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]")
        vouchers.click()
        time.sleep(1)

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()

        date = self.an.date().text
        print(date)

        journel_vou_num = self.an.Journel_vouche_numb()
        journel_vou_num.send_keys("1555")

        self.an.click_ante_date().click()
        time.sleep(2)

        effec_date = self.an.effective_date()
        effec_date.send_keys("31-10-2024")
        data = effec_date.get_attribute("value")
        time.sleep(2)

        print("effective", data)

        # Target date to compare
        target_date = datetime.strptime("31-10-2024", "%d-%m-%Y")

        # Convert the date from the effective date field with format "YYYY-MM-DD"
        test_date = datetime.strptime(data, "%Y-%m-%d")

        # Assert if the test date is less than the target date
        assert test_date < target_date, f"Test failed: {data} is not earlier than 31-10-2024."

    def test_deleting_first_row_and_check_bottom_remains(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.new_btn().click()

        date = self.an.date().get_attribute("value")
        print(date)

        journel_vou_num = self.an.Journel_vouche_numb()
        journel_vou_num.send_keys("1555")

        self.an.click_ante_date().click()
        time.sleep(2)

        self.an.effective_date().send_keys("10032022")
        time.sleep(2)

        type = Select(self.an.type())
        type.select_by_index(1)

        branch = Select(self.an.branch())
        branch.select_by_index(1)

        gl_account = Select(self.an.Gl_account())
        gl_account.select_by_index(3)
        time.sleep(2)

        self.an.transaction_remark().send_keys("Cash")
        LC_amount = self.an.lc_amount()
        LC_amount.send_keys("50000")
        time.sleep(2)

        self.an.click_new().click()
        time.sleep(1)

        typ = Select(self.an.type2())
        typ.select_by_index(2)

        branch2 = Select(self.an.branch_scond())
        branch2.select_by_index(2)

        gl2 = Select(self.an.gl_second())
        gl2.select_by_index(2)

        self.an.transaction_remark_second().send_keys("only cash")
        LC_2nd = self.an.lc_amount_second()
        LC_2nd.send_keys("50000")
        time.sleep(2)

        self.an.delete_first_row().click()
        time.sleep(1)
        self.an.click_new().click()

        branch2_val = branch2.first_selected_option.text
        print(branch2_val)
        gl2_val = gl2.first_selected_option.text
        print(gl2_val)

        transc_rem = self.an.transaction_remark_second().text
        lc_val = self.an.lc_amount_second()
        print(transc_rem, lc_val)

    def test_the_filter_is_working(self, setup):

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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        self.an.search_transaction_reference().send_keys("JRLVHR/02-20241028-102724-490/")
        time.sleep(2)
        branch_search = Select(self.an.search_branch())
        branch_search.select_by_index(2)

        gl_search = Select(self.an.search_Gl_account())
        gl_search.select_by_visible_text("Cabinet")

        self.an.from_date().send_keys("12082024")
        self.an.to_date().send_keys("01122024")

        self.an.filter_btn().click()

    def test_refresh_btn_working(self, setup):
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

         Journ_voucher = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
         Journ_voucher.click()

         time.sleep(2)
         self.an = Add_new(self.driver)
         time.sleep(2)
         self.an.search_transaction_reference().send_keys("JRLVHR/02-20241028-102724-490/")
         time.sleep(2)
         branch_search = Select(self.an.search_branch())
         branch_search.select_by_index(2)

         gl_search = Select(self.an.search_Gl_account())
         gl_search.select_by_visible_text("Cabinet")

         self.an.from_date().send_keys("12082024")
         self.an.to_date().send_keys("01122024")

         self.an.filter_btn().click()
         time.sleep(2)
         self.an.refresh_btn().click()

    def test_click_approve(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        approval_row = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[2]")
        approval_row.click()
        time.sleep(1)
        self.an.click_approve().click()

    def test_click_reject(self, setup):
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

        Journ_voucher = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[5]/div/span[3]")
        Journ_voucher.click()

        time.sleep(2)
        self.an = Add_new(self.driver)
        time.sleep(2)
        rejec_row = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[2]")
        rejec_row.click()
        time.sleep(1)
        self.an.click_reject().click()





