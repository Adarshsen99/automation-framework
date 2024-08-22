import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Bank_Information
from Dinero_automation.utilities.randomString import random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Bank_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # def test_with_add_bank(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Nayana")
    #     mname.send_keys("Benergy")
    #     lname.send_keys("Pool")
    #     sname.send_keys("Nayana Benergy Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("123456789")
    #     trans_type.select_by_index(3)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("123456789")
    #     hb_num.send_keys("123456789")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal@gmail.com")
    #     city.send_keys("Ernakulam")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("9876543210")
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #
    #     bank_name = self.bi.send_bank_name()
    #     branch_name = self.bi.send_branch_name()
    #     account_num = self.bi.account_number()
    #     confirm_account_num = self.bi.confirm_account_numb()
    #     acc_type = Select(self.bi.drp_account_type())
    #     currency = Select(self.bi.drp_currency())
    #     purpose = Select(self.bi.drp_purpose())
    #
    #     bank_name.send_keys("icici")
    #     click_bank = self.bi.click_bank_name()
    #     click_bank.click()
    #     branch_name.send_keys("icic")
    #     click_branch = self.bi.click_branch_name()
    #     click_branch.click()
    #     account_num.send_keys("1234567890")
    #     confirm_account_num.send_keys("1234567890")
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #
    #     error_msg = self.pi.error_message()
    #
    #     if error_msg == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_valid_data.png")
    #         assert True
    #
    #     self.driver.quit()

    # def test_with_add_bank_diff_ac_num(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Nayana")
    #     mname.send_keys("Benergy")
    #     lname.send_keys("Pool")
    #     sname.send_keys("Nayana Benergy Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("123456789")
    #     trans_type.select_by_index(3)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("123456789")
    #     hb_num.send_keys("123456789")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal@gmail.com")
    #     city.send_keys("Ernakulam")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("9876543210")
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #
    #     bank_name = self.bi.send_bank_name()
    #     branch_name = self.bi.send_branch_name()
    #     account_num = self.bi.account_number()
    #     confirm_account_num = self.bi.confirm_account_numb()
    #     acc_type = Select(self.bi.drp_account_type())
    #     currency = Select(self.bi.drp_currency())
    #     purpose = Select(self.bi.drp_purpose())
    #
    #     bank_name.send_keys("icici")
    #     click_bank = self.bi.click_bank_name()
    #     click_bank.click()
    #     branch_name.send_keys("icic")
    #     click_branch = self.bi.click_branch_name()
    #     click_branch.click()
    #     account_num.send_keys("1234567890")
    #     confirm_account_num.send_keys("1234567899")
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #
    #     error_msg = self.pi.error_message()
    #
    #     if error_msg == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_diff_ac_num.png")
    #         assert True
    #
    #     self.driver.quit()

    # def test_with_add_bank_with_spchar(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Nayana")
    #     mname.send_keys("Benergy")
    #     lname.send_keys("Pool")
    #     sname.send_keys("Nayana Benergy Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("123456789")
    #     trans_type.select_by_index(3)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("123456789")
    #     hb_num.send_keys("123456789")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal@gmail.com")
    #     city.send_keys("Ernakulam")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("9876543210")
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #
    #     bank_name = self.bi.send_bank_name()
    #     branch_name = self.bi.send_branch_name()
    #     account_num = self.bi.account_number()
    #     confirm_account_num = self.bi.confirm_account_numb()
    #     acc_type = Select(self.bi.drp_account_type())
    #     currency = Select(self.bi.drp_currency())
    #     purpose = Select(self.bi.drp_purpose())
    #
    #     bank_name.send_keys("icici")
    #     click_bank = self.bi.click_bank_name()
    #     click_bank.click()
    #     branch_name.send_keys("icic")
    #     click_branch = self.bi.click_branch_name()
    #     click_branch.click()
    #     account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     confirm_account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #
    #     error_msg = self.pi.error_message()
    #
    #     if error_msg == "Required":
    #         assert False
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_with_spchar.png")
    #         assert True
    #
    #     self.driver.quit()

    # def test_with_add_bank_with_char(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Nayana")
    #     mname.send_keys("Benergy")
    #     lname.send_keys("Pool")
    #     sname.send_keys("Nayana Benergy Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("123456789")
    #     trans_type.select_by_index(3)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("123456789")
    #     hb_num.send_keys("123456789")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal@gmail.com")
    #     city.send_keys("Ernakulam")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("9876543210")
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #
    #     bank_name = self.bi.send_bank_name()
    #     branch_name = self.bi.send_branch_name()
    #     account_num = self.bi.account_number()
    #     confirm_account_num = self.bi.confirm_account_numb()
    #     acc_type = Select(self.bi.drp_account_type())
    #     currency = Select(self.bi.drp_currency())
    #     purpose = Select(self.bi.drp_purpose())
    #
    #     bank_name.send_keys("sbi")
    #     click_bank = self.bi.click_bank_name()
    #     click_bank.click()
    #     branch_name.send_keys("kaloor")
    #     click_branch = self.bi.click_branch_name()
    #     click_branch.click()
    #     account_num.send_keys("qwertyuiop")
    #     confirm_account_num.send_keys("qwertyuiop")
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #     #
    #     error_msg = self.bi.message()
    #     print(error_msg)
    #     #
    #     if error_msg == "Required fields must be filled.":
    #         assert True
    #     else:
    #         self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_with_char.png")
    #         assert False
    #
    #     self.driver.quit()

    # def test_with_add_bank_with_only_account_num(self, setup):
    #     # login setup
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #     # time.sleep(2)
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #     # time.sleep(2)
    #
    #     # click action for customer registration
    #     self.nav.click_benificiary_individual()
    #
    #     self.pi = Personal_Details(self.driver)
    #     self.ci = Contact_Information(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #
    #     title = Select(self.pi.drp_title())
    #     fname = self.pi.fname()
    #     mname = self.pi.mname()
    #     lname = self.pi.lname()
    #     sname = self.pi.short_name()
    #     cob = Select(self.pi.drp_cob())
    #     nationality = Select(self.pi.drp_nationality())
    #     relation = Select(self.pi.drp_relation())
    #     id_type = Select(self.pi.drp_id_type())
    #     id_num = self.pi.id_num()
    #     trans_type = Select(self.pi.drp_trans_type())
    #
    #     title.select_by_index(1)
    #     fname.send_keys("Nayana")
    #     mname.send_keys("Benergy")
    #     lname.send_keys("Pool")
    #     sname.send_keys("Nayana Benergy Pool")
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys("123456789")
    #     trans_type.select_by_index(3)
    #
    #     self.pi.btn_next().click()
    #
    #     fh_num = self.ci.flat_house_number()
    #     hb_num = self.ci.house_building_name()
    #     street = self.ci.street()
    #     email = self.ci.email()
    #     city = self.ci.city()
    #     drp_contry = Select(self.ci.drp_country())
    #     drp_phone = Select(self.ci.drp_phone())
    #     phone = self.ci.phone()
    #
    #     fh_num.send_keys("123456789")
    #     hb_num.send_keys("123456789")
    #     street.send_keys("Kochi")
    #     email.send_keys("personal@gmail.com")
    #     city.send_keys("Ernakulam")
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys("9876543210")
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #
    #     bank_name = self.bi.send_bank_name()
    #     branch_name = self.bi.send_branch_name()
    #     account_num = self.bi.account_number()
    #     confirm_account_num = self.bi.confirm_account_numb()
    #     acc_type = Select(self.bi.drp_account_type())
    #     currency = Select(self.bi.drp_currency())
    #     purpose = Select(self.bi.drp_purpose())
    #
    #     bank_name.send_keys("sbi")
    #     click_bank = self.bi.click_bank_name()
    #     click_bank.click()
    #     branch_name.send_keys("kaloor")
    #     click_branch = self.bi.click_branch_name()
    #     click_branch.click()
    #     account_num.send_keys("4578965544")
    #     confirm_account_num.send_keys("")
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #     #
    #     error_msg = self.bi.message()
    #     print(error_msg)
    #     #
    #     # if error_msg == "Required fields must be filled.":
    #     #     assert True
    #     # else:
    #     #     self.driver.save_screenshot(screenShort.screen_short() + "test_with_add_bank_with_only_account_num.png")
    #     #     assert False
    #
    #     self.driver.quit()

    def test_with_add_bank_with_only_account_num(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer registration
        self.nav.click_benificiary_individual()

        self.pi = Personal_Details(self.driver)
        self.ci = Contact_Information(self.driver)
        self.bi = Bank_Information(self.driver)

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        relation = Select(self.pi.drp_relation())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("Nayana")
        mname.send_keys("Benergy")
        lname.send_keys("Pool")
        sname.send_keys("Nayana Benergy Pool")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys("123456789")
        hb_num.send_keys("123456789")
        street.send_keys("Kochi")
        email.send_keys("personal@gmail.com")
        city.send_keys("Ernakulam")
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys("9876543210")

        self.ci.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        #
        error_msg = self.bi.message()
        print(error_msg)
        #
        # if error_msg == "Required fields must be filled.":
        #     assert True
        # else:
        #     self.driver.save_screenshot(screenShort.screen_short() + "test_with_add_bank_with_only_account_num.png")
        #     assert False

        self.driver.quit()

