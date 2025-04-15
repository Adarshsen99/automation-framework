import time
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Dashbord import Dashboard
from Dinero_automation.pageObjects.Customer_Registration_corporate_edit import Company_Information_Edit, \
    Registration_Details_Edit, Beneficial_Owners_Details_Edit, Beneficiaries, Upload_Documents_Edit, Delegate
from Dinero_automation.utilities import screenShort

class Test_Company_Information_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_comapany_information_editmode(self,setup):
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

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # time.sleep(10)

        self.da = Dashboard(self.driver)
        cust_type = Select(self.da.customer_type())
        cust_type.select_by_index(2)
        search_customer = self.da.sending_customers()
        search_customer.send_keys("sad")
        self.da.click_customers().click()
        self.da.click_edit_mode()
        time.sleep(2)

        comp = self.ci.company_name()
        arabic = self.ci.arabic_name()
        build_numb = self.ci.building_number()
        build_name = self.ci.building_name()
        street = self.ci.street()
        post_code = self.ci.postal_code()
        city_dist = self.ci.city_district()
        country = self.ci.country()
        drp_country_code = Select(self.ci.drp_mobile())
        drp_mobile_numb = self.ci.mobile_num()
        drp_email = self.ci.email()

        drp_country_code_val_bf = drp_country_code.first_selected_option.text
        drp_mobile_numb_val_bf = drp_mobile_numb.get_attribute('value')

        print("drp_country_code_val_bf:",drp_country_code_val_bf)
        print("drp_mobile_numb_val_bf:",drp_mobile_numb_val_bf)
        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_back()
        time.sleep(2)
        drp_mobile_numb = self.ci.mobile_num()
        drp_mobile_numb.clear()

        drp_country_code = Select(self.ci.drp_mobile())
        drp_mobile_numb = self.ci.mobile_num()
        drp_country_code_val_af = drp_country_code.first_selected_option.text
        drp_mobile_numb_val_af = drp_mobile_numb.get_attribute('value')

        print("drp_country_code_val_af:", drp_country_code_val_af)
        print("drp_mobile_numb_val_af:", drp_mobile_numb_val_af)

        if drp_country_code_val_bf != drp_country_code_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "EDIT_CUST_REG_CORP_test_comapany_information_editmode_country_code.png")
            assert False

        if drp_mobile_numb_val_bf != drp_mobile_numb_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "EDIT_CUST_REG_CORP_test_comapany_information_editmode_mob_num.png")
            assert False

    def test_comapany_information_preview_editmode(self,setup):

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

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # time.sleep(10)

        self.da = Dashboard(self.driver)
        cust_type = Select(self.da.customer_type())
        cust_type.select_by_index(2)
        search_customer = self.da.sending_customers()
        search_customer.send_keys("sad")
        self.da.click_customers().click()
        self.da.click_edit_mode()
        time.sleep(2)

        comp = self.ci.company_name()
        arabic = self.ci.arabic_name()
        build_numb = self.ci.building_number()
        build_name = self.ci.building_name()
        street = self.ci.street()
        post_code = self.ci.postal_code()
        city_dist = self.ci.city_district()
        country = Select(self.ci.country())
        drp_country_code = Select(self.ci.drp_mobile())
        drp_mobile_numb = self.ci.mobile_num()
        drp_email = self.ci.email()

        comp_val = comp.get_attribute('value')
        arabic_val = arabic.get_attribute('value')
        build_numb_val = build_numb.get_attribute('value')
        build_name_val = build_name.get_attribute('value')
        street_val = street.get_attribute('value')
        post_code_val = post_code.get_attribute('value')
        city_dist_val = city_dist.get_attribute('value')
        country_val = country.first_selected_option.text
        drp_country_code_val = drp_country_code.first_selected_option.text
        drp_mobile_numb_val = drp_mobile_numb.get_attribute('value')
        drp_email_val = drp_email.get_attribute('value')


        print("comp_val:", comp_val)
        print("arabic_val:", arabic_val)
        print("build_numb_val:", build_numb_val)
        print("build_name_val:", build_name_val)
        print("street_val:", street_val)
        print("post_code_val:", post_code_val)
        print("city_dist_val:",city_dist_val)
        print("country_val:", country_val)
        print("drp_country_code_val:",drp_country_code_val)
        print("drp_mobile_numb_val:",drp_mobile_numb_val)
        print("drp_email_val:", drp_email_val)

        self.ci.btn_next()
        self.rd.comp_info_pre()
        time.sleep(2)
        print(self.rd.company_pre())
        print(self.rd.arabic_pre())
        print(self.rd.building_num_pre())
        print(self.rd.building_name_pre())
        print(self.rd.street_pre())
        print(self.rd.postal_code_pre())
        print(self.rd.city_district_pre())
        print(self.rd.country_pre())
        print(self.rd.mobile_pre())
        print(self.rd.email_pre())

        if comp_val == self.rd.company_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_comapany_information_preview_editmode.png")
            assert False

        if arabic_val == self.rd.arabic_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_arab.png")
            assert False

        if build_numb_val == self.rd.building_num_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_buildnum.png")
            assert False

        if build_name_val == self.rd.building_name_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_buildname.png")
            assert False

        if street_val == self.rd.street_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_street.png")
            assert False

        if post_code_val == self.rd.postal_code_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_post.png")
            assert False

        if city_dist_val == self.rd.city_district_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_dist.png")
            assert False

        if drp_email_val == self.rd.email_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_email.png")
            assert False

        if country_val == self.rd.country_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_country.png")
            assert False

        if drp_mobile_numb_val == self.rd.mobile_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_mobile.png")
            assert False

    def test_mobile_numb_editmode(self,setup):
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
        search_customer.send_keys("gWEYrGPvYA")
        self.da.click_customers().click()
        self.da.click_edit_mode()
        time.sleep(2)

        drp_country_code = Select(self.ci.drp_mobile())
        drp_mobile_numb = self.ci.mobile_num()

        time.sleep(2)

        drp_country_code.select_by_value("TCA")
        drp_mobile_numb.send_keys("958785")

        time.sleep(2)
        drp_country_code_val_bf = drp_country_code.first_selected_option.text
        drp_mobile_numb_val_bf = drp_mobile_numb.get_attribute('value')

        print("drp_country_code_val_bf:",drp_country_code_val_bf)
        print("drp_mobile_numb_val_bf:",drp_mobile_numb_val_bf)
        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_next()
        time.sleep(2)
        self.bod.btn_next()
        time.sleep(2)
        self.be.btn_next().click()
        time.sleep(2)
        self.de.btn_next().click()
        time.sleep(2)
        self.ud.btn_next()
        time.sleep(2)
        self.ud.btn_save().click()

        drp_country_code = Select(self.ci.drp_mobile())
        drp_mobile_numb = self.ci.mobile_num()

        time.sleep(4)

        drp_country_code_val_af = drp_country_code.first_selected_option.text
        drp_mobile_numb_val_af = drp_mobile_numb.get_attribute('value')

        print("drp_country_code_val_af:", drp_country_code_val_af)
        print("drp_mobile_numb_val_af:", drp_mobile_numb_val_af)

        if not drp_country_code_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "EDIT_CUST_REG_CORP_test_mobile_numb_editmode_countrycode.png")
            assert False

        if not drp_mobile_numb_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "EDIT_CUST_REG_CORP_test_mobile_numb_editmode_mobilenumber.png")
            assert False





