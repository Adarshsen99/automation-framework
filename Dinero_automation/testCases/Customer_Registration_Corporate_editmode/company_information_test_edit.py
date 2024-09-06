import time
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Dashbord import Dashboard
from Dinero_automation.pageObjects.Customer_Registration_corporate_edit import Company_Information_Edit,Registration_Details_Edit,Beneficial_Owners_Details_Edit,Upload_Documents_Edit
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
