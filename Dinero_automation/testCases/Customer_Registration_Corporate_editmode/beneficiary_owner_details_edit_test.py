import time

from django.template.defaulttags import firstof
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Dashbord import Dashboard
from Dinero_automation.pageObjects.Customer_Registration_corporate_edit import Company_Information_Edit,Registration_Details_Edit,Beneficial_Owners_Details_Edit,Upload_Documents_Edit
from Dinero_automation.utilities import screenShort


class Test_Registration_Details_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_clearing_bod_and_save(self,setup):
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

        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_next()
        time.sleep(2)
        self.bod.click_bod()
        time.sleep(2)

        first_name = self.bod.first_name()
        middle_name = self.bod.middle_name()
        last_name = self.bod.last_name()
        pob = self.bod.place_of_birth()
        fh_num = self.bod.flat_house_number()
        hb_num = self.bod.house_building_name()
        street = self.bod.street()
        city = self.bod.city()
        id_no = self.bod.id_no()

        first_name_val_bf = first_name.get_attribute("value")
        print("first_name_val_bf:", first_name_val_bf)
        middle_name_val_bf = hb_num.get_attribute("value")
        print("middle_name_val_before:",middle_name_val_bf)
        last_name_val_bf = last_name.get_attribute("value")
        print("last_name_val_bf:", last_name_val_bf)
        pob_val_bf = pob.get_attribute("value")
        print("pob_val_bf:", pob_val_bf)
        fh_num_val_bf = fh_num.get_attribute("value")
        print("fh_num_val_bf:", fh_num_val_bf)
        street_val_bf = street.get_attribute("value")
        print("street_val_bf:", street_val_bf)
        city_val_bf = city.get_attribute("value")
        print("city_val_bf:", city_val_bf)
        id_no_bf = id_no.get_attribute("value")
        print("id_no_bf:", id_no_bf)

        first_name.clear()
        middle_name.clear()
        last_name.clear()
        pob.clear()
        fh_num.clear()
        hb_num.clear()
        street.clear()
        city.clear()
        id_no.clear()
        time.sleep(2)

        # Scroll to the bottom of the page
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.bod.btn_update()

        time.sleep(2)

        self.bod.click_bod()
        time.sleep(2)

        first_name_val_af = first_name.get_attribute("value")
        print("first_name_val_af:", first_name_val_af)
        middle_name_val_af = hb_num.get_attribute("value")
        print("middle_name_val_af:", middle_name_val_af)
        last_name_val_af = last_name.get_attribute("value")
        print("last_name_val_af:", last_name_val_af)
        pob_val_af = pob.get_attribute("value")
        print("pob_val_af:", pob_val_af)
        fh_num_val_af = fh_num.get_attribute("value")
        print("fh_num_val_af:", fh_num_val_af)
        street_val_af = street.get_attribute("value")
        print("street_val_af:", street_val_af)
        city_val_af = city.get_attribute("value")
        print("city_val_af:", city_val_af)
        id_no_af = id_no.get_attribute("value")
        print("id_no_bf:", id_no_af)

        if first_name_val_bf == first_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_fname.png")
            assert False

        if middle_name_val_bf != middle_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_middle.png")
            assert False

        if last_name_val_bf != last_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_last.png")
            assert False

        if pob_val_bf != pob_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_pob.png")
            assert False

        if fh_num_val_bf != fh_num_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_fh.png")
            assert False

        if street_val_bf != street_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_street.png")
            assert False

        if city_val_bf != city_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_city.png")
            assert False

        if id_no_bf != id_no_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "Edit_REGISTRATION_DETAILS_test_clearing_bod_and_save_id.png")
            assert False





