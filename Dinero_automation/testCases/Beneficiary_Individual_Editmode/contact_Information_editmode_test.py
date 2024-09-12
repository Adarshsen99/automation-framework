import time
from dataclasses import asdict
from time import sleep

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Beneficiary_Individual import Personal_Details,Contact_Information,Fastcash_Location,Bank_Information,Final_Preview
from Dinero_automation.utilities.randomString import random_string_generator,generate_random_email_new,random_string_generator_numbers_new,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_numbers,generate_random_email,random_string_generator_numbers_10,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.pageObjects.Beneficiary_Individual_editmode import Personal_Details_Editmode,Contact_Information_Editmode,Bank_Information_Editmode,Fastcash_Location_Editmode,Final_Preview_Editmode

class Test_Personal_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # def test_validating_mobile_number(self,setup):
    #     responce = []
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
    #     self.fi = Fastcash_Location(self.driver)
    #     self.bi = Bank_Information(self.driver)
    #     self.fp = Final_Preview(self.driver)
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
    #     fname.send_keys(random_string_generator())
    #     mname.send_keys(random_string_generator())
    #     lname.send_keys(random_string_generator())
    #     sname.send_keys(random_string_generator())
    #     cob.select_by_index(9)
    #     nationality.select_by_index(12)
    #     relation.select_by_index(3)
    #     id_type.select_by_index(2)
    #     id_num.send_keys(random_string_generator_numbers_new())
    #     trans_type.select_by_index(3)
    #
    #     title_val = title.first_selected_option.text
    #     fname_val = fname.get_attribute("value")
    #     mname_val = mname.get_attribute("value")
    #     lname_val = lname.get_attribute("value")
    #     sname_val = sname.get_attribute("value")
    #     cob_val = cob.first_selected_option.text
    #     nationality_val = nationality.first_selected_option.text
    #     relation_val = relation.first_selected_option.text
    #     id_type_val = id_type.first_selected_option.text
    #     id_num_val = id_num.get_attribute("value")
    #     trans_type_val = trans_type.first_selected_option.text
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
    #     fh_num.send_keys(random_string_generator_numbers_new())
    #     hb_num.send_keys(random_string_generator_numbers_new())
    #     street.send_keys(random_string_generator())
    #     email.send_keys(generate_random_email_new())
    #     city.send_keys(random_string_generator())
    #     drp_contry.select_by_index(2)
    #     drp_phone.select_by_index(50)
    #     phone.send_keys(random_string_generator_numbers_new())
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
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
    #     acc = random_string_generator_numbers_10()
    #     account_num.send_keys(acc)
    #     confirm_account_num.send_keys(acc)
    #     acc_type.select_by_index(2)
    #     currency.select_by_index(2)
    #     purpose.select_by_index(3)
    #
    #     time.sleep(2)
    #     self.bi.btn_add_bank()
    #     time.sleep(2)
    #     self.bi.btn_next()
    #
    #     self.fi.click_specific_location()
    #     counrty = Select(self.fi.drp_country_splocation())
    #     countrt_num = Select(self.fi.drp_num_country_splocation())
    #     number = self.fi.mobile_number_splocation()
    #     addr_1 = self.fi.address_1_splocation()
    #     addr_2 = self.fi.address_2_splocation()
    #     addr_3 = self.fi.address_3_splocation()
    #     city = self.fi.city_splocation()
    #
    #     counrty.select_by_index(2)
    #     countrt_num.select_by_index(4)
    #     number.send_keys("9876543210")
    #     addr_1.send_keys("kochi")
    #     addr_2.send_keys("ernakulam")
    #     addr_3.send_keys("habbel")
    #     city.send_keys("ernakulam")
    #
    #     time.sleep(2)
    #     self.fi.btn_add_location_splocation()
    #     time.sleep(2)
    #     self.fi.btn_next()
    #     time.sleep(4)
    #
    #     time.sleep(2)
    #
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    #     self.driver.implicitly_wait(10)
    #
    #     self.fp.btn_save().click()
    #     time.sleep(2)
    #     # print(self.fp.editmode_message())
    #
    #     document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
    #
    #     if self.fp.editmode_message() == "You're in edit mode":
    #         responce.append(document)
    #         self.return_url = document['root']['baseURL']
    #         assert True
    #
    #     self.driver.get(self.return_url)
    #
    #     self.pi = Personal_Details_Editmode(self.driver)
    #     self.ci = Contact_Information_Editmode(self.driver)
    #     self.bi = Bank_Information_Editmode(self.driver)
    #     self.fc = Fastcash_Location_Editmode(self.driver)
    #     self.fp = Final_Preview_Editmode(self.driver)
    #
    #     self.pi.btn_next().click()
    #     time.sleep(4)
    #
    #     phone_drp = Select(self.ci.drp_phone())
    #     phone_drp_val = phone_drp.first_selected_option.text
    #     phone = self.ci.phone().get_attribute('value')
    #
    #     print("phone_drp_val:",phone_drp_val)
    #     print("phone:",phone)
    #
    #     phone_drp_val_af = phone_drp.first_selected_option.text
    #     phone = self.ci.phone()
    #     phone.clear()
    #     time.sleep(2)
    #     phone_af = phone.get_attribute('value')
    #
    #     print("phone_drp_val_af:", phone_drp_val_af)
    #     print("phone_af:", phone_af)
    #
    #     if phone_drp_val != phone_drp_val_af:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "EDIT_BENEFICIARY_INDIVIDUAL_CONTACT_INFO_test_adding_beneficiary_only_mandatory_fields_checking_pre_countrycode.png")
    #         assert False
    #
    #     if phone != phone_af:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "EDIT_BENEFICIARY_INDIVIDUAL_CONTACT_INFO_test_adding_beneficiary_only_mandatory_fields_checking_pre_phonenumb.png")
    #         assert False

    def test_validating_mobile_number(self,setup):
        responce = []
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
        self.fi = Fastcash_Location(self.driver)
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
        trans_type.select_by_index(3)

        title_val = title.first_selected_option.text
        fname_val = fname.get_attribute("value")
        mname_val = mname.get_attribute("value")
        lname_val = lname.get_attribute("value")
        sname_val = sname.get_attribute("value")
        cob_val = cob.first_selected_option.text
        nationality_val = nationality.first_selected_option.text
        relation_val = relation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_num_val = id_num.get_attribute("value")
        trans_type_val = trans_type.first_selected_option.text

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
        acc = random_string_generator_numbers_10()
        account_num.send_keys(acc)
        confirm_account_num.send_keys(acc)
        acc_type.select_by_index(2)
        currency.select_by_index(2)
        purpose.select_by_index(3)

        time.sleep(2)
        self.bi.btn_add_bank()
        time.sleep(2)
        self.bi.btn_next()

        self.fi.click_specific_location()
        counrty = Select(self.fi.drp_country_splocation())
        countrt_num = Select(self.fi.drp_num_country_splocation())
        number = self.fi.mobile_number_splocation()
        addr_1 = self.fi.address_1_splocation()
        addr_2 = self.fi.address_2_splocation()
        addr_3 = self.fi.address_3_splocation()
        city = self.fi.city_splocation()

        counrty.select_by_index(2)
        countrt_num.select_by_index(4)
        number.send_keys("9876543210")
        addr_1.send_keys("kochi")
        addr_2.send_keys("ernakulam")
        addr_3.send_keys("habbel")
        city.send_keys("ernakulam")

        time.sleep(2)
        self.fi.btn_add_location_splocation()
        time.sleep(2)
        self.fi.btn_next()
        time.sleep(4)

        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.implicitly_wait(10)

        self.fp.btn_save().click()
        time.sleep(2)
        # print(self.fp.editmode_message())

        document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

        if self.fp.editmode_message() == "You're in edit mode":
            responce.append(document)
            self.return_url = document['root']['baseURL']
            assert True

        self.driver.get(self.return_url)

        self.pi = Personal_Details_Editmode(self.driver)
        self.ci = Contact_Information_Editmode(self.driver)
        self.bi = Bank_Information_Editmode(self.driver)
        self.fc = Fastcash_Location_Editmode(self.driver)
        self.fp = Final_Preview_Editmode(self.driver)

        self.pi.btn_next().click()
        time.sleep(2)

        # phone_drp = Select(self.ci.drp_phone())
        # phone_drp_val = phone_drp.first_selected_option.text
        # phone = self.ci.phone().get_attribute('value')
        #
        # print("phone_drp_val:",phone_drp_val)
        # print("phone:",phone)
        #
        # phone_drp_val_af = phone_drp.first_selected_option.text
        # phone = self.ci.phone()
        # phone.clear()
        # time.sleep(2)
        # phone_af = phone.get_attribute('value')
        #
        # print("phone_drp_val_af:", phone_drp_val_af)
        # print("phone_af:", phone_af)
        #
        # if phone_drp_val != phone_drp_val_af:
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "EDIT_BENEFICIARY_INDIVIDUAL_CONTACT_INFO_test_adding_beneficiary_only_mandatory_fields_checking_pre_countrycode.png")
        #     assert False
        #
        # if phone != phone_af:
        #     assert True
        # else:
        #     self.driver.save_screenshot(
        #         screenShort.screen_short() + "EDIT_BENEFICIARY_INDIVIDUAL_CONTACT_INFO_test_adding_beneficiary_only_mandatory_fields_checking_pre_phonenumb.png")
        #     assert False
        #


