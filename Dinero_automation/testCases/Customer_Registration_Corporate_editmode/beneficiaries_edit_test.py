import time

from django.template.defaulttags import firstof
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Dashbord import Dashboard
from Dinero_automation.pageObjects.Customer_Registration_corporate_edit import Company_Information_Edit, \
    Registration_Details_Edit, Beneficial_Owners_Details_Edit, Beneficiaries, Upload_Documents_Edit, Delegate
from Dinero_automation.utilities import screenShort


class Test_Beneficiaries_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # def test_click_on_beneficiaries(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("sad")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     search_bene = self.be.search_bene()
    #     search_bene.send_keys("qwrqwrqwr  qwrqwq")
    #     time.sleep(2)
    #
    #     self.be.select_beneficiary().click()
    #     time.sleep(2)
    #
    #     self.be.click_beneficiaries().click()
    #     time.sleep(2)
    #
    #     ele = self.be.btn_next().is_displayed()
    #
    #     if ele == "True":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "Edit_BENEFICIARIES_test_clearing_bod_and_save_id.png")
    #         assert False
    #
    #     self.driver.quit()


    # def test_validating_fastcash_location_after_removing_beneficiary(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("sad")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     search_bene = self.be.search_bene()
    #     search_bene.send_keys("kendall kris jenner")
    #     time.sleep(2)
    #
    #     self.be.select_beneficiary().click()
    #     time.sleep(2)
    #
    #     self.be.click_beneficiaries().click()
    #     time.sleep(2)
    #
    #
    #     fc_bf = self.be.get_fastcash_locations()
    #     print("fc_bf:",fc_bf)
    #     time.sleep(2)
    #
    #     self.be.remove_beneficiaries()
    #     time.sleep(2)
    #
    #     fc_af = self.be.get_fastcash_locations()
    #     print("fc_af:", fc_af)
    #     time.sleep(2)
    #
    #     if fc_bf != fc_af:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "Edit_BENEFICIARIES_test_validating_fastcash_location_after_removing_beneficiary.png")
    #         assert False

    # def test_validating_sending_beneficiary_search_box(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("sad")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     search_bene = self.be.search_bene()
    #     search_bene.send_keys("kendall kris jenner")
    #     time.sleep(2)
    #
    #     search_bene_bf = search_bene.get_attribute('value')
    #     print("search_bene_bf:",search_bene_bf)
    #
    #     self.be.select_beneficiary().click()
    #     time.sleep(2)
    #
    #     search_bene_af = search_bene.get_attribute('value')
    #     print("search_bene_af:", search_bene_af)
    #
    #     time.sleep(2)
    #
    #     if search_bene_bf != search_bene_af:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "Edit_BENEFICIARIES_test_validating_sending_beneficiary_search_box.png")
    #         assert False

    def test_validating_sending_beneficiary_and_save(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize edit mode page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        self.ci = Company_Information_Edit(self.driver)
        self.rd = Registration_Details_Edit(self.driver)
        self.bod = Beneficial_Owners_Details_Edit(self.driver)
        self.ud = Upload_Documents_Edit(self.driver)
        self.de = Delegate(self.driver)
        self.be = Beneficiaries(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # time.sleep(10)

        self.da = Dashboard(self.driver)
        cust_type = Select(self.da.customer_type())
        cust_type.select_by_index(2)
        search_customer = self.da.sending_customers()
        search_customer.send_keys("MtTUFwaJlw")
        self.da.click_customers().click()
        self.da.click_edit_mode()
        time.sleep(2)

        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_next()
        time.sleep(2)
        self.bod.btn_next()
        time.sleep(2)

        search_bene = self.be.search_bene()
        search_bene.send_keys("karunakar")
        time.sleep(2)

        self.be.select_beneficiary().click()
        time.sleep(2)

        beneficiary_name_bf = self.be.bene_name()
        print("beneficiary_name_before:",beneficiary_name_bf)

        self.be.btn_next().click()
        time.sleep(2)

        self.de.btn_next().click()
        time.sleep(2)

        self.ud.btn_next()
        time.sleep(2)

        save = self.ud.btn_save()
        time.sleep(4)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save)
        time.sleep(2)
        save.click()

        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_next()
        time.sleep(2)
        self.bod.btn_next()
        time.sleep(2)

        beneficiary_name_af = self.be.bene_name()
        print("beneficiary_name_after:", beneficiary_name_af)
        time.sleep(2)

        if beneficiary_name_bf == beneficiary_name_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "Edit_BENEFICIARIES_test_validating_sending_beneficiary_and_save.png")
            assert False










