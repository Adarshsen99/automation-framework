from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
import time
from Dinero_automation.pageObjects.Customer_Registration_Corporate import Company_Information,Registration_Details
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_numbers_22,random_string_generator_numbers_10,random_string_generator_numbers_20,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Contact_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

#       assign the data
        c_name = "Zen Tech"
        a_name = "Shaik"
        b_num = "1223"
        b_name = "monlash"
        stre = "nellore"
        po = "524309"
        dist = "Kerala"
        num = "7641524344"
        mai = "finnest@tech.com"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        self.comp_info.btn_next()

        if self.comp_info.errorMessage() != "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_sending_valid_data.png")
            assert False

    def test_sending_without_data(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

#       assign the data
        c_name = ""
        a_name = ""
        b_num = ""
        b_name = ""
        stre = ""
        po = ""
        dist = ""
        num = ""
        mai = ""

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(1)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        self.comp_info.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_sending_without_data.png")
            assert False




    def test_sending_spchar_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        #       assign the data
        c_name = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        a_name = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        b_num = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        b_name = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        stre = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        po = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        dist = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        num = "!@#$%^&*()_+*/{}|]""-[:;',.?"
        mai = "!@#$%^&*()_+*/{}|]""-[:;',.?"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(1)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        self.comp_info.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_sending_spchar_data.png")
            assert False

        self.driver.quit()

    def test_sending_char_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        #       assign the data
        c_name = "qwertyuioplkjhgfd"
        a_name = "qwertyuioplkjhgfd"
        b_num = "qwertyuioplkjhgfd"
        b_name = "qwertyuioplkjhgfd"
        stre = "qwertyuioplkjhgfd"
        po = "qwertyuioplkjhgfd"
        dist = "qwertyuioplkjhgfd"
        num = "qwertyuioplkjhgfd"
        mai = "qwertyuioplkjhgfd"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(1)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        self.comp_info.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_sending_char_data_data.png")
            assert False

        self.driver.quit()

    def test_sending_bulk_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # Click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assigning submodules
        self.comp_info = Company_Information(self.driver)
        self.rg_detail = Registration_Details(self.driver)

        # Define fixed data for fields
        company_names = ["Company A", "Company B", "Company C", "Company D", "Company E", "Company F", "Company G", "Company H", "Company I", "Company J"]
        arabic_names = ["اسم الشركة A", "اسم الشركة B", "اسم الشركة C", "اسم الشركة D", "اسم الشركة E", "اسم الشركة F", "اسم الشركة G", "اسم الشركة H", "اسم الشركة I", "اسم الشركة J"]
        building_numbers = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]
        building_names = ["Building 1", "Building 2", "Building 3", "Building 4", "Building 5", "Building 6", "Building 7", "Building 8", "Building 9", "Building 10"]
        streets = ["Street A", "Street B", "Street C", "Street D", "Street E", "Street F", "Street G", "Street H", "Street I", "Street J"]
        post_codes = ["10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010"]
        districts = ["District A", "District B", "District C", "District D", "District E", "District F", "District G", "District H", "District I", "District J"]
        mobile_numbers = ["0500000001", "0500000002", "0500000003", "0500000004", "0500000005", "0500000006", "0500000007", "0500000008", "0500000009", "0500000010"]
        emails = ["test1@example.com", "test2@example.com", "test3@example.com", "test4@example.com", "test5@example.com", "test6@example.com", "test7@example.com", "test8@example.com", "test9@example.com", "test10@example.com"]

        for i in range(10):  # Loop for bulk data generation
            # Get the fixed data
            c_name = company_names[i]
            a_name = arabic_names[i]
            b_num = building_numbers[i]
            b_name = building_names[i]
            stre = streets[i]
            po = post_codes[i]
            dist = districts[i]
            num = mobile_numbers[i]
            mai = emails[i]

            # Assigning Elements
            comp_name = self.comp_info.company_name()
            ara_name = self.comp_info.arabic_name()
            build_num = self.comp_info.building_number()
            build_name = self.comp_info.building_name()
            stree = self.comp_info.street()
            post = self.comp_info.postal_code()
            distc = self.comp_info.city_district()
            drp_country = Select(self.comp_info.country())
            drp_mob = Select(self.comp_info.drp_mobile())
            numb = self.comp_info.mobile_num()
            mail = self.comp_info.email()

            # Fill out the form with fixed data
            comp_name.send_keys(c_name)
            ara_name.send_keys(a_name)
            build_num.send_keys(b_num)
            build_name.send_keys(b_name)
            stree.send_keys(stre)
            post.send_keys(po)
            distc.send_keys(dist)
            drp_country.select_by_index(1)
            drp_mob.select_by_index(2)
            numb.send_keys(num)
            mail.send_keys(mai)

            self.comp_info.btn_next()

            # Verify and handle error message
            if self.comp_info.errorMessage() == "Required":
                assert False
            else:
                self.driver.save_screenshot(screenShort.screen_short() + f"CRC_test_sending_bulk_data_success_{i}.png")
                assert True

            # Go back and clear the fields for the next iteration
            self.rg_detail.btn_back()

            # Reinitialize elements
            self.comp_info = Company_Information(self.driver)

            # Clear the fields
            comp_name = self.comp_info.company_name()
            ara_name = self.comp_info.arabic_name()
            build_num = self.comp_info.building_number()
            build_name = self.comp_info.building_name()
            stree = self.comp_info.street()
            post = self.comp_info.postal_code()
            distc = self.comp_info.city_district()
            numb = self.comp_info.mobile_num()
            mail = self.comp_info.email()

            comp_name.clear()
            ara_name.clear()
            build_num.clear()
            build_name.clear()
            stree.clear()
            post.clear()
            distc.clear()
            numb.clear()
            mail.clear()

        self.driver.quit()

    def test_validating_preview(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

#       assign the data
        c_name = "zen Tech"
        a_name = "shaik"
        b_num = "1223"
        b_name = "monlash"
        stre = "nellore"
        po = "524309"
        dist = "Kerala"
        num = "7641524344"
        mai = "finnest@tech.com"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        # c = comp_name.get_attribute('value')
        # a = ara_name.get_attribute('value')
        # b_nu = build_num.get_attribute('value')
        b_na = build_name.get_attribute('value')
        print("buildingname what i sent:",b_na)
        # st = stree.get_attribute('value')
        # # po = post.get_attribute('value')
        # di = distc.get_attribute('value')
        # ma = mail.get_attribute('value')
        print(drp_country.first_selected_option.text)
        co = drp_country.first_selected_option.text


        self.comp_info.btn_next()
        self.regi_details.comp_info_pre()

        print(self.regi_details.company_pre())
        print(self.regi_details.arabic_pre())
        print(self.regi_details.building_num_pre())
        print("buildingname what i get:",self.regi_details.building_name_pre())
        print("street:",self.regi_details.street_pre())
        print(self.regi_details.postal_code_pre())
        print(self.regi_details.city_district_pre())
        print(self.regi_details.country_pre())
        print("mail",self.regi_details.email_pre())




        if c_name == self.regi_details.company_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_comp.png")
            assert False

        if a_name == self.regi_details.arabic_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_arab.png")
            assert False

        if b_num == self.regi_details.building_num_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_buildnum.png")
            assert False

        if b_name == self.regi_details.building_name_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_buildname.png")
            assert False

        if stre == self.regi_details.street_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_street.png")
            assert False

        if po == self.regi_details.postal_code_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_post.png")
            assert False

        if dist == self.regi_details.city_district_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_dist.png")
            assert False

        if mai == self.regi_details.email_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_email.png")
            assert False

        if co == self.regi_details.country_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_preview_country.png")
            assert False

        self.driver.quit()

    def test_validating_maxlen(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        comp_int = int(comp_name.get_attribute('maxlength'))
        arab_int = int(ara_name.get_attribute('maxlength'))
        build_num_int = int(build_num.get_attribute('maxlength'))
        build_name_int = int(build_name.get_attribute('maxlength'))
        street_int = int(stree.get_attribute('maxlength'))
        post_int = int(post.get_attribute('maxlength'))
        distc_int = int(distc.get_attribute('maxlength'))
        numb_int = int(numb.get_attribute('maxlength'))
        mail_int = int(mail.get_attribute('maxlength'))

        max_20 = random_string_generator_max_20()
        print("maxlenght_20:", max_20)
        max_30 = random_string_generator_max_30()
        print("maxlenght_30:", max_30)
        max_50 = random_string_generator_max_50()
        print("maxlenght_50:", max_50)
        max_num_20 = random_string_generator_numbers_20()
        print("maxlennumber20",max_num_20)
        max_mail_50 = generate_random_email()
        print("maxmail:",max_mail_50)

#       assign the data
        c_name = max_50
        a_name = max_50
        b_num = max_50
        b_name = max_50
        stre = max_50
        po = max_num_20
        dist = max_30
        num = random_string_generator_numbers()
        mai = max_mail_50

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        c = len(comp_name.get_attribute('value'))
        a = len(ara_name.get_attribute('value'))
        b_nu = len(build_num.get_attribute('value'))
        b_na = len(build_name.get_attribute('value'))
        st = len(stree.get_attribute('value'))
        post_val = len(post.get_attribute('value'))
        di = len(distc.get_attribute('value'))
        ma = len(mail.get_attribute('value'))
        num = len(numb.get_attribute('value'))


        self.comp_info.btn_next()


        if c == comp_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_comp.png")
            assert False

        if a == arab_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_arab.png")
            assert False

        if b_nu == build_num_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_buildnum.png")
            assert False

        if b_na == build_name_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_buildname.png")
            assert False

        if st == street_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_street.png")
            assert False

        if post_val == post_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_post.png")
            assert False

        if di == distc_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_dist.png")
            assert False

        if ma == mail_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_email.png")
            assert False

        if num == numb_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_country.png")
            assert False

        self.driver.quit()

    def test_validating_maxlen_lessthen(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        comp_int = int(comp_name.get_attribute('maxlength'))
        arab_int = int(ara_name.get_attribute('maxlength'))
        build_num_int = int(build_num.get_attribute('maxlength'))
        build_name_int = int(build_name.get_attribute('maxlength'))
        street_int = int(stree.get_attribute('maxlength'))
        post_int = int(post.get_attribute('maxlength'))
        distc_int = int(distc.get_attribute('maxlength'))
        numb_int = int(numb.get_attribute('maxlength'))
        print(numb_int,"numb_int")
        mail_int = int(mail.get_attribute('maxlength'))

        # max_20 = random_string_generator_max_20()
        # print("maxlenght_20:", max_20)
        # max_30 = random_string_generator_max_30()
        # print("maxlenght_30:", max_30)
        # max_50 = random_string_generator_max_50()
        # print("maxlenght_50:", max_50)
        # max_num_20 = random_string_generator_numbers_20()
        # print("maxlennumber20", max_num_20)
        # max_mail_50 = generate_random_email()
        # print("maxmail:", max_mail_50)

        #       assign the data
        c_name = random_string_generator_max_52()
        a_name = random_string_generator_max_52()
        b_num = random_string_generator_max_52()
        b_name = random_string_generator_max_52()
        stre = random_string_generator_max_52()
        po = random_string_generator_numbers_22()
        dist = random_string_generator_max_28()
        num = random_string_generator_numbers_10()
        mai = generate_random_email_lessthen_45()

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        c = len(comp_name.get_attribute('value'))
        a = len(ara_name.get_attribute('value'))
        b_nu = len(build_num.get_attribute('value'))
        b_na = len(build_name.get_attribute('value'))
        st = len(stree.get_attribute('value'))
        post_val = len(post.get_attribute('value'))
        di = len(distc.get_attribute('value'))
        ma = len(mail.get_attribute('value'))
        num = len(numb.get_attribute('value'))
        print(num,"numbers")

        self.comp_info.btn_next()

        if c < comp_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_comp.png")
            assert False

        if a < arab_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_arab.png")
            assert False

        if b_nu < build_num_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_buildnum.png")
            assert False

        if b_na < build_name_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_buildname.png")
            assert False

        if st < street_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_street.png")
            assert False

        if post_val < post_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_post.png")
            assert False

        if di < distc_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_dist.png")
            assert False

        if ma < mail_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_email.png")
            assert False

        if num < numb_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_lessthen_num.png")
            assert False

        self.driver.quit()

    def test_validating_maxlen_greaterthen(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        comp_int = int(comp_name.get_attribute('maxlength'))
        print(comp_int,"comp_int")
        arab_int = int(ara_name.get_attribute('maxlength'))
        build_num_int = int(build_num.get_attribute('maxlength'))
        build_name_int = int(build_name.get_attribute('maxlength'))
        street_int = int(stree.get_attribute('maxlength'))
        post_int = int(post.get_attribute('maxlength'))
        distc_int = int(distc.get_attribute('maxlength'))
        numb_int = int(numb.get_attribute('maxlength'))
        print(numb_int,"numb_int")
        mail_int = int(mail.get_attribute('maxlength'))

        # max_20 = random_string_generator_max_20()
        # print("maxlenght_20:", max_20)
        # max_30 = random_string_generator_max_30()
        # print("maxlenght_30:", max_30)
        # max_50 = random_string_generator_max_50()
        # print("maxlenght_50:", max_50)
        # max_num_20 = random_string_generator_numbers_20()
        # print("maxlennumber20", max_num_20)
        # max_mail_50 = generate_random_email()
        # print("maxmail:", max_mail_50)

        #       assign the data
        c_name = random_string_generator_max_52()
        a_name = random_string_generator_max_52()
        b_num = random_string_generator_max_52()
        b_name = random_string_generator_max_52()
        stre = random_string_generator_max_52()
        po = random_string_generator_numbers_22()
        dist = random_string_generator_max_32()
        num = random_string_generator_numbers_22()
        mai = generate_random_email_lessthen_52()

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        c = len(comp_name.get_attribute('value'))
        print("c",c)
        a = len(ara_name.get_attribute('value'))
        b_nu = len(build_num.get_attribute('value'))
        b_na = len(build_name.get_attribute('value'))
        st = len(stree.get_attribute('value'))
        post_val = len(post.get_attribute('value'))
        di = len(distc.get_attribute('value'))
        ma = len(mail.get_attribute('value'))
        num = len(numb.get_attribute('value'))
        print(num,"numbers")

        self.comp_info.btn_next()

        if c == comp_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_comp.png")
            assert False

        if a == arab_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_arab.png")
            assert False

        if b_nu == build_num_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_buildnum.png")
            assert False

        if b_na == build_name_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_buildname.png")
            assert False

        if st == street_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_street.png")
            assert False

        if post_val == post_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_post.png")
            assert False

        if di == distc_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_dist.png")
            assert False

        if ma == mail_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_email.png")
            assert False

        if num == numb_int:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_validating_maxlen_greaterthen_num.png")
            assert False

        self.driver.quit()

    def test_cancel(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        #       assign the data
        c_name = "Zen Tech"
        a_name = "Shaik"
        b_num = "1223"
        b_name = "monlash"
        stre = "nellore"
        po = "524309"
        dist = "Kerala"
        num = "7641524344"
        mai = "finnest@tech.com"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        company_val = comp_name.get_attribute('value')
        arabic_val = ara_name.get_attribute('value')
        b_nu_val = build_num.get_attribute('value')
        b_na_val = build_name.get_attribute('value')
        steet_val = stree.get_attribute('value')
        post_val = post.get_attribute('value')
        dist_val = distc.get_attribute('value')
        mail_val = mail.get_attribute('value')
        num_val = numb.get_attribute('value')
        country_val = drp_country.first_selected_option.text
        mob_val = drp_mob.first_selected_option.text
        print(company_val,arabic_val,b_nu_val,b_na_val,steet_val,post_val,dist_val,mail_val,num_val,country_val,mob_val)

        self.comp_info.btn_cancel()
        self.comp_info.btn_cancel_confirm()
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        company_val_after = comp_name.get_attribute('value')
        arabic_val_after = ara_name.get_attribute('value')
        b_nu_val_after = build_num.get_attribute('value')
        b_na_val_after = build_name.get_attribute('value')
        steet_val_after = stree.get_attribute('value')
        post_val_after = post.get_attribute('value')
        dist_val_after = distc.get_attribute('value')
        mail_val_after = mail.get_attribute('value')
        num_val_after = numb.get_attribute('value')
        country_val_after = drp_country.first_selected_option.text
        mob_val_after = drp_mob.first_selected_option.text
        print(company_val_after,arabic_val_after,b_nu_val_after,b_na_val_after,steet_val_after,post_val_after,dist_val_after,mail_val_after,num_val_after,country_val_after,mob_val_after)

        if company_val != company_val_after and arabic_val != arabic_val_after and b_nu_val != b_nu_val_after and b_na_val != b_na_val_after and steet_val != steet_val_after and post_val != post_val_after and dist_val != dist_val_after and mail_val != mail_val_after and num_val != num_val_after and country_val != country_val_after and mob_val != mob_val_after:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_cancel.png")
            assert False

    def test_addingdata_without_clear(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        #       assign the data
        c_name = "Zen Tech"
        a_name = "Shaik"
        b_num = "1223"
        b_name = "monlash"
        stre = "nellore"
        po = "524309"
        dist = "Kerala"
        num = "7641524"
        mai = "finnest@tech.com"

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        self.comp_info.btn_next()
        self.regi_details.btn_back()

        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = Select(self.comp_info.country())
        drp_mob = Select(self.comp_info.drp_mobile())
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()
        c_name = "Pvt"
        a_name = "Basha"
        b_num = "9876"
        b_name = "building"
        stre = "palem"
        po = "76352"
        dist = "stories"
        num = "983633"
        mai = ""

        comp_name.send_keys(c_name)
        ara_name.send_keys(a_name)
        build_num.send_keys(b_num)
        build_name.send_keys(b_name)
        stree.send_keys(stre)
        post.send_keys(po)
        distc.send_keys(dist)
        drp_country.select_by_index(4)
        drp_mob.select_by_index(2)
        numb.send_keys(num)
        mail.send_keys(mai)

        comp_val = comp_name.get_attribute('value')
        print("comp_val",comp_val)
        arb_val = ara_name.get_attribute('value')
        print("arb_val",arb_val)
        buil_num_val = build_num.get_attribute('value')
        print("buil_num_val",buil_num_val)
        build_name_val = build_name.get_attribute('value')
        print("build_name_val", build_name_val)
        stree_val = stree.get_attribute('value')
        print("stree_val",stree_val)
        post_val = post.get_attribute('value')
        print("post_val",post_val)
        dist_val = distc.get_attribute('value')
        print("dist_val",dist_val)
        mail_val = mail.get_attribute('value')
        print("mail_val",mail_val)
        country_val = drp_country.first_selected_option.text
        print("country_val",country_val)
        mobil = drp_mob.first_selected_option.text
        print("mobil",mobil)

        self.comp_info.btn_next()
        self.regi_details.comp_info_pre()

        print(self.regi_details.company_pre())
        print(self.regi_details.arabic_pre())
        print(self.regi_details.building_num_pre())
        print("buildingname what i get:", self.regi_details.building_name_pre())
        print("street:", self.regi_details.street_pre())
        print(self.regi_details.postal_code_pre())
        print(self.regi_details.city_district_pre())
        print(self.regi_details.country_pre())
        print("mail", self.regi_details.email_pre())

        if comp_val == self.regi_details.company_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_comp.png")
            assert False

        if arb_val == self.regi_details.arabic_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_arab.png")
            assert False

        if buil_num_val == self.regi_details.building_num_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_buildnum.png")
            assert False

        if build_name_val == self.regi_details.building_name_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_buildname.png")
            assert False

        if stree_val == self.regi_details.street_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_street.png")
            assert False

        if post_val == self.regi_details.postal_code_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_post.png")
            assert False

        if dist_val == self.regi_details.city_district_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_dist.png")
            assert False

        if mail_val == self.regi_details.email_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_email.png")
            assert False

        if country_val == self.regi_details.country_pre():
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "CRC_test_addingdata_without_clear_country.png")
            assert False

        self.driver.quit()

    def test_get_size(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()

        # click action for customer registration
        self.nav.click_customer_registration_corporate()

        # Assinging submodules
        self.comp_info = Company_Information(self.driver)
        self.regi_details = Registration_Details(self.driver)

        # Assinging Elements
        comp_name = self.comp_info.company_name()
        ara_name = self.comp_info.arabic_name()
        build_num = self.comp_info.building_number()
        build_name = self.comp_info.building_name()
        stree = self.comp_info.street()
        post = self.comp_info.postal_code()
        distc = self.comp_info.city_district()
        drp_country = self.comp_info.country()
        drp_mob = self.comp_info.drp_mobile()
        numb = self.comp_info.mobile_num()
        mail = self.comp_info.email()

        print("comp_name", comp_name.size)
        print("ara_name", ara_name.size)
        print("build_num", build_num.size)
        print("build_name", build_name.size)
        print("stree", stree.size)
        print("post", post.size)
        print("distc", distc.size)
        print("drp_country", drp_country.size)
        print("drp_mob", drp_mob.size)
        print("numb", numb.size)
        print("mail", mail.size)







