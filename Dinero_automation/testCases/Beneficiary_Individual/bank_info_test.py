import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Bank_Information,Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator,generate_random_email_new,random_string_generator_numbers_new,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Bank_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_with_add_bank(self, setup):
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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        bank_name.send_keys("icici")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_valid_data.png")
            assert True

        self.driver.quit()

    def test_with_add_bank_diff_ac_num(self, setup):
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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        bank_name.send_keys("icici")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("12345789")
        confirm_account_num.send_keys("32145789")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_diff_ac_num.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_spchar(self, setup):
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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        bank_name.send_keys("icici")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        confirm_account_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_with_spchar.png")
            assert True

        self.driver.quit()

    def test_with_add_bank_with_char(self, setup):
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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        account_num.send_keys("qwertyuiop")
        confirm_account_num.send_keys("qwertyuiop")
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
        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_add_bank_with_char.png")
            assert False

        self.driver.quit()

    def test_with_add_bank_with_only_account_number(self, setup):
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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_with_add_bank_with_only_account_num.png")
            assert False

        self.driver.quit()

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        account_num.send_keys("")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        #
        error_msg = self.bi.message_2()
        if error_msg == "Account numbers do not match":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "test_with_add_bank_with_only_account_num.png")
            assert False

        self.driver.quit()

    def test_click_next_without_adding_bank(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        # bank_name = self.bi.send_bank_name()
        # branch_name = self.bi.send_branch_name()
        # account_num = self.bi.account_number()
        # confirm_account_num = self.bi.confirm_account_numb()
        # acc_type = Select(self.bi.drp_account_type())
        # currency = Select(self.bi.drp_currency())
        # purpose = Select(self.bi.drp_purpose())
        #
        # bank_name.send_keys("sbi")
        # click_bank = self.bi.click_bank_name()
        # click_bank.click()
        # branch_name.send_keys("kaloor")
        # click_branch = self.bi.click_branch_name()
        # click_branch.click()
        # account_num.send_keys("4578965544")
        # confirm_account_num.send_keys("")
        # acc_type.select_by_index(2)
        # currency.select_by_index(2)
        # purpose.select_by_index(3)

        # time.sleep(2)
        # self.bi.btn_add_bank()
        self.bi.btn_next()
        time.sleep(2)
        #
        # error_msg = self.bi.message()

        # Assuming the rest of your code is correct, just update the print statement
        print(self.fp.btn_save().is_enabled())

        #
        if not self.fp.btn_save().is_enabled() == True:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_click_next_without_adding_bank.png")
            assert False

        self.driver.quit()

    def test_without_adding_bank(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        # bank_name = self.bi.send_bank_name()
        # branch_name = self.bi.send_branch_name()
        # account_num = self.bi.account_number()
        # confirm_account_num = self.bi.confirm_account_numb()
        # acc_type = Select(self.bi.drp_account_type())
        # currency = Select(self.bi.drp_currency())
        # purpose = Select(self.bi.drp_purpose())
        #
        # bank_name.send_keys("sbi")
        # click_bank = self.bi.click_bank_name()
        # click_bank.click()
        # branch_name.send_keys("kaloor")
        # click_branch = self.bi.click_branch_name()
        # click_branch.click()
        # account_num.send_keys("4578965544")
        # confirm_account_num.send_keys("")
        # acc_type.select_by_index(2)
        # currency.select_by_index(2)
        # purpose.select_by_index(3)
        self.bi.btn_add_bank()
        # self.bi.btn_next()
        time.sleep(2)

        # Assuming the rest of your code is correct, just update the print statement
        error_msg = self.bi.message()
        # print(error_msg)
        #
        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_without_adding_bank.png")
            assert False

        self.driver.quit()

    def test_adding_bank_next_back_clear(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text
        purpose_val = purpose.first_selected_option.text

        print(acc_type_val, currency_val, purpose_val)

        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_back().click()
        time.sleep(2)
        self.bi.btn_clear()

        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())
        acc_type_af = acc_type.first_selected_option.text
        currency_af = currency.first_selected_option.text
        purpose_af = purpose.first_selected_option.text

        print(acc_type_af, currency_af, purpose_af)

        time.sleep(2)


        if acc_type_val == acc_type_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_next_back_clear_acc_type.png")
            assert False

        if currency_val == currency_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_next_back_clear_currency.png")
            assert False

        if purpose_val == purpose_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_next_back_clear_purpose.png")
            assert False

        self.driver.quit()

    def test_adding_bank_without_bank_branch(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        # bank_name.send_keys("sbi")
        # click_bank = self.bi.click_bank_name()
        # click_bank.click()
        # branch_name.send_keys("kaloor")
        # click_branch = self.bi.click_branch_name()
        # click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(3)

        error_msg = self.bi.message()

        if error_msg == "Required fields must be filled.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_without_bank_branch.png")
            assert False


        self.driver.quit()

    def test_adding_bank_with_same_bank_branch(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()

        bank_name.send_keys("sbi")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("kaloor")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(3)

        error_msg = self.bi.meassage_text()

        if error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_with_same_bank_branch.png")
            assert False

        self.driver.quit()

    def test_adding_bank_with_same_account_diff_bank_branch(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()

        error_msg = self.bi.meassage_text()

        if not error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_adding_bank_with_same_bank_branch.png")
            assert False

        self.driver.quit()

    def test_adding_multilple_bank_account(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)

        error_msg = self.bi.meassage_text()

        if not error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_ test_adding_multilple_bank_account.png")
            assert False

        self.driver.quit()

    def test_updating_account_number(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        bank_name_val_bf = bank_name.get_attribute('value')
        branch_name_val_bf = branch_name.get_attribute('value')
        account_num_val_bf = account_num.get_attribute('value')
        confirm_account_num_val_bf = confirm_account_num.get_attribute('value')
        acc_type_val_bf = acc_type.first_selected_option.text
        currency_val_bf = currency.first_selected_option.text
        purpose_val__bf = purpose.first_selected_option.text

        print(
            bank_name_val_bf,
            branch_name_val_bf,
            account_num_val_bf,
            confirm_account_num_val_bf,
            acc_type_val_bf,
            currency_val_bf,
            purpose_val__bf

        )

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)

        self.bi.banks_data_1().click()

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        account_num.clear()
        account_num.send_keys("123456789")
        confirm_account_num.clear()
        confirm_account_num.send_keys("123456789")
        acc_type.select_by_index(1)
        currency.select_by_index(1)
        purpose.select_by_index(2)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text
        purpose_val = purpose.first_selected_option.text

        print(
            bank_name_val,
            branch_name_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val,
            purpose_val

        )

        if bank_name_val_bf == bank_name_val:
            assert True
        else:
            assert False

        if branch_name_val_bf == branch_name_val:
            assert True
        else:
            assert False

        if account_num_val_bf != account_num_val:
            assert True
        else:
            assert False

        if confirm_account_num_val_bf != confirm_account_num_val:
            assert True
        else:
            assert False

        if acc_type_val_bf != acc_type_val:
            assert True
        else:
            assert False

        if currency_val_bf != currency_val:
            assert True
        else:
            assert False

        if purpose_val__bf != purpose_val:
            assert True
        else:
            assert False


        self.driver.quit()

    def test_updating_account_number_with_same_bank_and_branch(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        bank_name_val_bf = bank_name.get_attribute('value')
        branch_name_val_bf = branch_name.get_attribute('value')
        account_num_val_bf = account_num.get_attribute('value')
        confirm_account_num_val_bf = confirm_account_num.get_attribute('value')
        acc_type_val_bf = acc_type.first_selected_option.text
        currency_val_bf = currency.first_selected_option.text
        purpose_val__bf = purpose.first_selected_option.text

        print(
            bank_name_val_bf,
            branch_name_val_bf,
            account_num_val_bf,
            confirm_account_num_val_bf,
            acc_type_val_bf,
            currency_val_bf,
            purpose_val__bf

        )

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)

        self.bi.banks_data_1().click()

        bank_name = self.bi.send_bank_name()
        branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        acc_type = Select(self.bi.drp_account_type())
        currency = Select(self.bi.drp_currency())
        purpose = Select(self.bi.drp_purpose())

        bank_name.clear()
        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.clear()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.clear()
        account_num.send_keys("4578965544")
        confirm_account_num.clear()
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(1)
        currency.select_by_index(1)
        purpose.select_by_index(2)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text
        purpose_val = purpose.first_selected_option.text

        print(
            bank_name_val,
            branch_name_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val,
            purpose_val

        )
        self.bi.btn_update()
        time.sleep(2)

        error_msg = self.bi.meassage_text()

        if not error_msg == "Bank already exists in the list.":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_updating_account_number_with_same_bank_and_branch.png")
            assert False

        self.driver.quit()

    def test_validating_preview(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        acc_no = random_string_generator_numbers_new()
        account_num.send_keys(acc_no)
        confirm_account_num.send_keys(acc_no)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text
        purpose_val = purpose.first_selected_option.text

        branch_val = self.bi.branch_address().get_attribute('value')
        branch_code_val = self.bi.branch_code().get_attribute('value')

        print(
            bank_name_val,
            branch_name_val,
            branch_val,
            branch_code_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val,
            purpose_val

        )

        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_back().click()
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.click_bank_info_preview()

        print(
            self.bi.bank_name_pre(),
            self.bi.branch_name_pre(),
            self.bi.branch_address_pre(),
            self.bi.branch_code_pre(),
            self.bi.account_num_pre(),
            self.bi.confirm_account_num_pre(),
            self.bi.account_type_pre(),
            self.bi.currency_pre(),
            self.bi.purpose_of_payment_pre())

        if bank_name_val == self.bi.bank_name_pre():
            assert True
        else:
            assert False

        if branch_name_val == self.bi.branch_name_pre():
            assert True
        else:
            assert False

        if branch_val == self.bi.branch_address_pre():
            assert True
        else:
            assert False

        if branch_code_val == self.bi.branch_code_pre():
            assert True
        else:
            assert False

        if account_num_val == self.bi.account_num_pre():
            assert True
        else:
            assert False

        if confirm_account_num_val == self.bi.confirm_account_num_pre():
            assert True
        else:
            assert False

        if acc_type_val == self.bi.account_type_pre():
            assert True
        else:
            assert False

        if currency_val == self.bi.currency_pre():
            assert True
        else:
            assert False

        if purpose_val == self.bi.purpose_of_payment_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_after_update_preview(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        bank_name_val = bank_name.get_attribute('value')
        branch_name_val = branch_name.get_attribute('value')
        account_num_val = account_num.get_attribute('value')
        confirm_account_num_val = confirm_account_num.get_attribute('value')
        acc_type_val = acc_type.first_selected_option.text
        currency_val = currency.first_selected_option.text
        purpose_val = purpose.first_selected_option.text

        branch_val = self.bi.branch_address().get_attribute('value')
        branch_code_val = self.bi.branch_code().get_attribute('value')

        print(
            bank_name_val,
            branch_name_val,
            branch_val,
            branch_code_val,
            account_num_val,
            confirm_account_num_val,
            acc_type_val,
            currency_val,
            purpose_val

        )

        self.bi.btn_add_bank()
        self.bi.btn_next()
        self.fp.btn_back().click()
        time.sleep(2)
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.btn_update()
        time.sleep(4)
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_back().click()
        time.sleep(2)
        self.bi.click_bank_info_preview()
        time.sleep(4)

        print(
            self.bi.bank_name_pre(),
            self.bi.branch_name_pre(),
            self.bi.branch_address_pre(),
            self.bi.branch_code_pre(),
            self.bi.account_num_pre(),
            self.bi.confirm_account_num_pre(),
            self.bi.account_type_pre(),
            self.bi.currency_pre(),
            self.bi.purpose_of_payment_pre())

        if bank_name_val == self.bi.bank_name_pre():
            assert True
        else:
            assert False

        if branch_name_val == self.bi.branch_name_pre():
            assert True
        else:
            assert False

        if branch_val == self.bi.branch_address_pre():
            assert True
        else:
            assert False

        if branch_code_val == self.bi.branch_code_pre():
            assert True
        else:
            assert False

        if account_num_val == self.bi.account_num_pre():
            assert True
        else:
            assert False

        if confirm_account_num_val == self.bi.confirm_account_num_pre():
            assert True
        else:
            assert False

        if acc_type_val == self.bi.account_type_pre():
            assert True
        else:
            assert False

        if currency_val == self.bi.currency_pre():
            assert True
        else:
            assert False

        if purpose_val == self.bi.purpose_of_payment_pre():
            assert True
        else:
            assert False

        self.driver.quit()

    def test_updating_second_bank(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back().click()
        self.bi.banks_data_1().click()
        time.sleep(2)
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        time.sleep(2)
        self.bi.banks_data_2().click()
        time.sleep(2)
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        time.sleep(2)
        click_branch = self.bi.click_branch_name()
        click_branch.click()

        if click_branch.click():
            assert True
        else:
            assert False


        self.driver.quit()

    def test_maxlength(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

        self.ci.btn_next()
        time.sleep(2)

        # bank_name = self.bi.send_bank_name()
        # branch_name = self.bi.send_branch_name()
        account_num = self.bi.account_number()
        confirm_account_num = self.bi.confirm_account_numb()
        # acc_type = Select(self.bi.drp_account_type())
        # currency = Select(self.bi.drp_currency())
        # purpose = Select(self.bi.drp_purpose())

        account_num = account_num.get_attribute('maxlength')
        confirm_account_num = confirm_account_num.get_attribute('maxlength')

        print("maxlength of account number:",account_num)
        print("maxlength of confirm account number:",confirm_account_num)

        if account_num == confirm_account_num:
            assert True
        else:
            assert False

        self.driver.quit()


        # self.bi.btn_add_bank()

    def test_click_update_and_click_save(self, setup):
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
        self.fp = Final_Preview(self.driver)

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
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(2)

        self.pi.btn_next().click()

        fh_num = self.ci.flat_house_number()
        hb_num = self.ci.house_building_name()
        street = self.ci.street()
        email = self.ci.email()
        city = self.ci.city()
        drp_contry = Select(self.ci.drp_country())
        drp_phone = Select(self.ci.drp_phone())
        phone = self.ci.phone()

        fh_num.send_keys(random_string_generator_numbers_new())
        hb_num.send_keys(random_string_generator_numbers_new())
        street.send_keys(random_string_generator())
        email.send_keys(generate_random_email_new())
        city.send_keys(random_string_generator())
        drp_contry.select_by_index(2)
        drp_phone.select_by_index(50)
        phone.send_keys(random_string_generator_numbers_new())

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
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()

        bank_name.send_keys("icic")
        click_bank = self.bi.click_bank_name()
        click_bank.click()
        branch_name.send_keys("icic")
        click_branch = self.bi.click_branch_name()
        click_branch.click()
        account_num.send_keys("4578965544")
        confirm_account_num.send_keys("4578965544")
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()
        self.fp.btn_back().click()
        self.bi.banks_data_1().click()
        time.sleep(2)
        self.bi.btn_update()
        self.bi.btn_next()
        time.sleep(2)
        self.fp.btn_save().click()
        time.sleep(2)

        print(self.fp.meassge_final())

        if not self.fp.meassge_final() == "Field 'id' expected a number but got ''.":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BI_test_click_update_and_click_save.png")
            assert False