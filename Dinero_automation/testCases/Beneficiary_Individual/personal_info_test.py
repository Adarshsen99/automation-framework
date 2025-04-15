import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details, Contact_Information, Bank_Information
from Dinero_automation.utilities.randomString import random_string_generator_max_30, random_string_generator, \
    random_string_generator_numbers_new, random_string_generator_max_50, random_string_generator_max_28, \
    random_string_generator_max_48, random_string_generator_max_31, random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Personal_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_with_valid_data(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
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
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        error_msg = self.pi.error_message()
        print(error_msg)

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_valid_data.png")
            assert True



    def test_without_data(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_visible_text("")
        fname.send_keys("")
        mname.send_keys("")
        lname.send_keys("")
        sname.send_keys("")
        cob.select_by_visible_text("")
        nationality.select_by_visible_text("")
        id_type.select_by_visible_text("")
        id_num.send_keys("")
        trans_type.select_by_visible_text("")

        self.pi.btn_next().click()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_without_data.png")
            assert False

        # self.driver.quit()

    def test_with_spchar_data(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        mname.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        lname.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        sname.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        id_type.select_by_index(2)
        id_num.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_spchar_data.png")
            assert False

        # self.driver.quit()

    def test_with_numbers_data(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("123456789")
        mname.send_keys("123456789")
        lname.send_keys("123456789")
        sname.send_keys("123456789")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        id_type.select_by_index(2)
        id_num.send_keys("123456789")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()
        # time.sleep(5)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_numbers_data.png")
            assert False

    def test_with_sp_char_num_data(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_index(1)
        fname.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        mname.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        lname.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        sname.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        cob.select_by_index(9)
        nationality.select_by_index(12)
        id_type.select_by_index(2)
        id_num.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        trans_type.select_by_index(3)

        self.pi.btn_next().click()

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_sp_char_num_data.png")
            assert True

        self.driver.quit()

    def test_with_validating_cancel(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        # Contact Information

        title.select_by_index(1)
        fname.send_keys(random_string_generator())
        mname.send_keys(random_string_generator())
        lname.send_keys(random_string_generator())
        sname.send_keys(random_string_generator())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        title_val = title.first_selected_option.text
        fname_val = fname.get_attribute('value')
        mname_val = mname.get_attribute('value')
        lname_val = lname.get_attribute('value')
        sname_val = sname.get_attribute('value')
        cob_val = cob.first_selected_option.text
        nationality_val = nationality.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_num_val = id_num.get_attribute('value')
        trans_type_val = trans_type.first_selected_option.text

        print(
            "title_val:", title_val,
            "fname_val:", fname_val,
            "mname_val:", mname_val,
            "lname_val:", lname_val,
            "sname_val:", sname_val,
            "cob_val:", cob_val,
            "nationality_val:", nationality_val,
            "id_type_val:", id_type_val,
            "id_num_val:", id_num_val,
            "trans_type_val:", trans_type_val

        )

        self.pi.btn_next().click()

        self.ci.btn_back()
        self.pi.btn_cancel().click()
        self.pi.btn_cancel_confirm().click()

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

        title_val_af = title.first_selected_option.text
        fname_val_af = fname.get_attribute('value')
        mname_val_af = mname.get_attribute('value')
        lname_val_af = lname.get_attribute('value')
        sname_val_af = sname.get_attribute('value')
        cob_val_af = cob.first_selected_option.text
        nationality_val_af = nationality.first_selected_option.text
        relation_val_af = relation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_num_val_af = id_num.get_attribute('value')
        trans_type_val_af = trans_type.first_selected_option.text

        print(
            "title_val_af:", title_val_af,
            "fname_val_af:", fname_val_af,
            "mname_val_af:", mname_val_af,
            "lname_val_af:", lname_val_af,
            "sname_val_af:", sname_val_af,
            "cob_val_af:", cob_val_af,
            "nationality_val_af:", nationality_val_af,
            "relation_val_af:", relation_val_af,
            "id_type_val_af:", id_type_val_af,
            "id_num_val_af:", id_num_val_af,
            "trans_type_val_af:", trans_type_val_af

        )

        time.sleep(2)

        if title_val != title_val_af:
            assert True
        else:
            assert False

        if fname_val != fname_val_af:
            assert True
        else:
            assert False

        if mname_val != mname_val_af:
            assert True
        else:
            assert False

        if lname_val != lname_val_af:
            assert True
        else:
            assert False

        if sname_val != sname_val_af:
            assert True
        else:
            assert False

        if cob_val != cob_val_af:
            assert True
        else:
            assert False

        if nationality_val != nationality_val_af:
            assert True
        else:
            assert False


        if id_type_val != id_type_val_af:
            assert True
        else:
            assert False

        if trans_type_val != trans_type_val_af:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_with_sending_data_have_spaces(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
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
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        self.pi.btn_next().click()
        time.sleep(4)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_sending_data_have_spaces.png")
            assert True

        self.driver.quit()

    def test_with_sending_data_only_required_fields(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
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
        # id_type.select_by_index(2)
        # id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        self.pi.btn_next().click()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BI_test_with_sending_data_have_spaces.png")
            assert True

        self.driver.quit()

    def test_with_sending_data_only_nonrequired_fields(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
        id_type = Select(self.pi.drp_id_type())
        id_num = self.pi.id_num()
        trans_type = Select(self.pi.drp_trans_type())

        title.select_by_visible_text("")
        fname.send_keys("")
        mname.send_keys(random_string_generator())
        lname.send_keys("")
        sname.send_keys("")
        cob.select_by_index(2)
        nationality.select_by_visible_text("")
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_visible_text("")

        self.pi.btn_next().click()
        time.sleep(2)

        error_msg = self.pi.error_message()

        if error_msg == "Required":
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BI_test_with_sending_data_only_nonrequired_fields.png")
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
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
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        title_val = title.first_selected_option.text
        fname_val = fname.get_attribute("value")
        mname_val = mname.get_attribute("value")
        lname_val = lname.get_attribute("value")
        sname_val = sname.get_attribute("value")
        cob_val = cob.first_selected_option.text
        nationality_val = nationality.first_selected_option.text

        id_type_val = id_type.first_selected_option.text
        id_num_val = id_num.get_attribute("value")
        trans_type_val = trans_type.first_selected_option.text

        print(
            f"title_val: {title_val}, fname_val: {fname_val}, mname_val: {mname_val}, lname_val: {lname_val}, sname_val: {sname_val}, cob_val: {cob_val}, nationality_val: {nationality_val},  id_type_val: {id_type_val}, id_num_val: {id_num_val}, trans_type_val: {trans_type_val}")

        self.pi.btn_next().click()

        self.ci.click_personal_info_preview()

        print(self.ci.title_pre(),
              self.ci.first_name_pre(),
              self.ci.middle_name_pre(),
              self.ci.last_name_pre(),
              self.ci.short_name_pre(),
              self.ci.country_of_birth_pre(),
              self.ci.nationality_pre(),
              self.ci.id_type_pre(),
              self.ci.id_number_pre(),
              self.ci.transaction_type_pre())

        time.sleep(2)

        if title_val == self.ci.title_pre():
            assert True
        else:
            assert False

        if fname_val == self.ci.first_name_pre():
            assert True
        else:
            assert False

        if mname_val == self.ci.middle_name_pre():
            assert True
        else:
            assert False

        if lname_val == self.ci.last_name_pre():
            assert True
        else:
            assert False

        if sname_val == self.ci.short_name_pre():
            assert True
        else:
            assert False

        if cob_val == self.ci.country_of_birth_pre():
            assert True
        else:
            assert False

        if nationality_val == self.ci.nationality_pre():
            assert True
        else:
            assert False


        if id_type_val == self.ci.id_type_pre():
            assert True
        else:
            assert False

        if self.ci.id_number_pre() == id_num_val:
            assert True
        else:
            assert False

        if self.ci.transaction_type_pre() == trans_type_val:
            assert True
        else:
            assert False
        self.driver.quit()

    def test_validating_preview_reqfields(self, setup):
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

        title = Select(self.pi.drp_title())
        fname = self.pi.fname()
        mname = self.pi.mname()
        lname = self.pi.lname()
        sname = self.pi.short_name()
        cob = Select(self.pi.drp_cob())
        nationality = Select(self.pi.drp_nationality())
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
        id_type.select_by_index(2)
        id_num.send_keys(random_string_generator_numbers_new())
        trans_type.select_by_index(3)

        title_val = title.first_selected_option.text
        fname_val = fname.get_attribute("value")
        mname_val = mname.get_attribute("value")
        lname_val = lname.get_attribute("value")
        sname_val = sname.get_attribute("value")
        cob_val = cob.first_selected_option.text
        nationality_val = nationality.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_num_val = id_num.get_attribute("value")
        trans_type_val = trans_type.first_selected_option.text

        print(
            f"title_val: {title_val}, fname_val: {fname_val}, mname_val: {mname_val}, lname_val: {lname_val}, sname_val: {sname_val}, cob_val: {cob_val}, nationality_val: {nationality_val}, id_type_val: {id_type_val}, id_num_val: {id_num_val}, trans_type_val: {trans_type_val}")

        self.pi.btn_next().click()

        self.ci.click_personal_info_preview()

        print(self.ci.title_pre(),
              self.ci.first_name_pre(),
              self.ci.middle_name_pre(),
              self.ci.last_name_pre(),
              self.ci.short_name_pre(),
              self.ci.country_of_birth_pre(),
              self.ci.nationality_pre(),
              self.ci.id_type_pre(),
              self.ci.id_number_pre(),
              self.ci.transaction_type_pre())

        time.sleep(2)

        if title_val == self.ci.title_pre():
            assert True
        else:
            assert False

        if fname_val == self.ci.first_name_pre():
            assert True
        else:
            assert False

        if mname_val == self.ci.middle_name_pre():
            assert True
        else:
            assert False

        if lname_val == self.ci.last_name_pre():
            assert True
        else:
            assert False

        if sname_val == self.ci.short_name_pre():
            assert True
        else:
            assert False

        if cob_val == self.ci.country_of_birth_pre():
            assert True
        else:
            assert False

        if nationality_val == self.ci.nationality_pre():
            assert True
        else:
            assert False


        if id_type_val == self.ci.id_type_pre():
            assert True
        else:
            assert False

        if self.ci.id_number_pre() == id_num_val:
            assert True
        else:
            assert False

        if self.ci.transaction_type_pre() == trans_type_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_validating_fields_maxlen(self, setup):
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
        fname.send_keys(random_string_generator_max_30())
        mname.send_keys(random_string_generator_max_30())
        lname.send_keys(random_string_generator_max_30())
        sname.send_keys(random_string_generator_max_30())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_visible_text("")
        id_num.send_keys(random_string_generator_max_30())
        trans_type.select_by_index(3)

        fname_len = int(fname.get_attribute("maxlength"))
        mname_len = int(mname.get_attribute("maxlength"))
        lname_len = int(lname.get_attribute("maxlength"))
        sname_len = int(sname.get_attribute("maxlength"))
        id_num_len = int(id_num.get_attribute("maxlength"))

        print(
            f"fname_val: {fname_len}, mname_val: {mname_len}, lname_val: {lname_len}, sname_val: {sname_len}, id_num_val: {id_num_len}")

        fname_val = len(fname.get_attribute("value"))
        mname_val = len(mname.get_attribute("value"))
        lname_val = len(lname.get_attribute("value"))
        sname_val = len(sname.get_attribute("value"))
        id_num_val = len(id_num.get_attribute("value"))
        print(
            f"fname_val: {fname_val}, mname_val: {mname_val}, lname_val: {lname_val}, sname_val: {sname_val}, id_num_val: {id_num_val}")

        if fname_len == fname_val:
            assert True
        else:
            assert False

        if mname_len == mname_val:
            assert True
        else:
            assert False

        if lname_len == lname_val:
            assert True
        else:
            assert False

        if sname_len == sname_val:
            assert True
        else:
            assert False

        if id_num_len == id_num_val:
            assert True
        else:
            assert False

        self.pi.btn_next().click()

    def test_validating_fields_maxlen_greater(self, setup):
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
        fname.send_keys(random_string_generator_max_30() + random_string_generator_max_30())
        mname.send_keys(random_string_generator_max_30() + random_string_generator_max_30())
        lname.send_keys(random_string_generator_max_30() + random_string_generator_max_30())
        sname.send_keys(random_string_generator_max_30() + random_string_generator_max_30())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_visible_text("")
        id_num.send_keys(random_string_generator_max_30() + random_string_generator_max_30())
        trans_type.select_by_index(3)

        fname_len = int(fname.get_attribute("maxlength"))
        mname_len = int(mname.get_attribute("maxlength"))
        lname_len = int(lname.get_attribute("maxlength"))
        sname_len = int(sname.get_attribute("maxlength"))
        id_num_len = int(id_num.get_attribute("maxlength"))

        print(
            f"fname_val: {fname_len}, mname_val: {mname_len}, lname_val: {lname_len}, sname_val: {sname_len}, id_num_val: {id_num_len}")

        fname_val = len(fname.get_attribute("value"))
        mname_val = len(mname.get_attribute("value"))
        lname_val = len(lname.get_attribute("value"))
        sname_val = len(sname.get_attribute("value"))
        id_num_val = len(id_num.get_attribute("value"))
        print(
            f"fname_val: {fname_val}, mname_val: {mname_val}, lname_val: {lname_val}, sname_val: {sname_val}, id_num_val: {id_num_val}")

        if fname_len == fname_val:
            assert True
        else:
            assert False

        if mname_len == mname_val:
            assert True
        else:
            assert False

        if lname_len == lname_val:
            assert True
        else:
            assert False

        if sname_len == sname_val:
            assert True
        else:
            assert False

        if id_num_len == id_num_val:
            assert True
        else:
            assert False

        self.pi.btn_next().click()

    def test_validating_fields_maxlen_lessthen(self, setup):
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
        fname.send_keys(random_string_generator_max_28())
        mname.send_keys(random_string_generator_max_28())
        lname.send_keys(random_string_generator_max_28())
        sname.send_keys(random_string_generator_max_28())
        cob.select_by_index(9)
        nationality.select_by_index(12)
        relation.select_by_index(3)
        id_type.select_by_visible_text("")
        id_num.send_keys(random_string_generator_max_28())
        trans_type.select_by_index(3)

        fname_len = int(fname.get_attribute("maxlength"))
        mname_len = int(mname.get_attribute("maxlength"))
        lname_len = int(lname.get_attribute("maxlength"))
        sname_len = int(sname.get_attribute("maxlength"))
        id_num_len = int(id_num.get_attribute("maxlength"))

        print(
            f"fname_val: {fname_len}, mname_val: {mname_len}, lname_val: {lname_len}, sname_val: {sname_len}, id_num_val: {id_num_len}")

        fname_val = len(fname.get_attribute("value"))
        mname_val = len(mname.get_attribute("value"))
        lname_val = len(lname.get_attribute("value"))
        sname_val = len(sname.get_attribute("value"))
        id_num_val = len(id_num.get_attribute("value"))
        print(
            f"fname_val: {fname_val}, mname_val: {mname_val}, lname_val: {lname_val}, sname_val: {sname_val}, id_num_val: {id_num_val}")

        if fname_len > fname_val:
            assert True
        else:
            assert False

        if mname_len > mname_val:
            assert True
        else:
            assert False

        if lname_len > lname_val:
            assert True
        else:
            assert False

        if sname_len > sname_val:
            assert True
        else:
            assert False

        if id_num_len > id_num_val:
            assert True
        else:
            assert False

        self.pi.btn_next().click()


