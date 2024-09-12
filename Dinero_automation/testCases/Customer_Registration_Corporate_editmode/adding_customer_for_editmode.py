from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
import os
from Dinero_automation.pageObjects.Customer_Registration_Corporate import Company_Information,Registration_Details,Beneficial_Owners_Details,Upload_Documents
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from pynput.keyboard import Controller, Key
import random
import string

class Test_Beneficial_Owners_Details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def random_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def random_number(self, length):
        return ''.join(random.choice(string.digits) for _ in range(length))

    def random_email(self):
        return f"{self.random_string(5)}@{self.random_string(5)}.com"

    # def test_validating_id_num(self,setup):
    #     responce = []
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # click action for nav bar arrow
    #     self.nav = Navigation_Page(self.driver)
    #     self.nav.click_navbar()
    #
    #     # click action for customer registration
    #     self.nav.click_customer_registration_corporate()
    #
    #     # Assinging submodules
    #     self.comp_info = Company_Information(self.driver)
    #     self.rg = Registration_Details(self.driver)
    #     self.bod = Beneficial_Owners_Details(self.driver)
    #     self.ud = Upload_Documents(self.driver)
    #
    #     # Assinging Elements
    #     comp_name = self.comp_info.company_name()
    #     ara_name = self.comp_info.arabic_name()
    #     build_num = self.comp_info.building_number()
    #     build_name = self.comp_info.building_name()
    #     stree = self.comp_info.street()
    #     post = self.comp_info.postal_code()
    #     distc = self.comp_info.city_district()
    #     drp_country = Select(self.comp_info.country())
    #     drp_mob = Select(self.comp_info.drp_mobile())
    #     numb = self.comp_info.mobile_num()
    #     mail = self.comp_info.email()
    #
    #     #       assign the data
    #     c_name = self.random_string(10)
    #     a_name = self.random_string(7)
    #     b_num = self.random_number(4)
    #     b_name = self.random_string(8)
    #     stre = self.random_string(12)
    #     po = self.random_number(6)
    #     dist = self.random_string(6)
    #     num = self.random_number(10)
    #     mai = self.random_email()
    #
    #     comp_name.send_keys(c_name)
    #     ara_name.send_keys(a_name)
    #     build_num.send_keys(b_num)
    #     build_name.send_keys(b_name)
    #     stree.send_keys(stre)
    #     post.send_keys(po)
    #     distc.send_keys(dist)
    #     drp_country.select_by_index(4)
    #     drp_mob.select_by_index(2)
    #     numb.send_keys(num)
    #     mail.send_keys(mai)
    #
    #     self.comp_info.btn_next()
    #     #       Assigning elements for registration details
    #     coun_of_incorp = Select(self.rg.drp_country_of_incorp())
    #     lice_natu = Select(self.rg.drp_licence_nature())
    #     ent_type = Select(self.rg.drp_entity_type())
    #     oper = Select(self.rg.drp_operation())
    #     tr_servi_sect = Select(self.rg.drp_trade_service_sector())
    #     capital = self.rg.capital()
    #     reg_pur = self.rg.regisration_purpose()
    #     est_an_income = self.rg.estimated_annaul_incode()
    #     auth_per = self.rg.authorized_person()
    #     designat = Select(self.rg.drp_designation())
    #     nation = Select(self.rg.drp_nationality())
    #     id_type = Select(self.rg.drp_id_type())
    #     id_no = self.rg.id_no()
    #     id_exp = self.rg.dpick_id_exp()
    #     cr_no = self.rg.cr_no()
    #     comp_card_no = self.rg.comp_card_no()
    #     cr_iss_dat = self.rg.dpick_cr_issue_date()
    #     cr_exp_dat = self.rg.dpick_cr_exp_date()
    #     cc_iss_date = self.rg.dpick_cc_issue_date()
    #     cc_exp_dat = self.rg.dpick_cc_expaire_date()
    #
    #     coun_of_incorp.select_by_index(2)
    #     lice_natu.select_by_index(2)
    #     ent_type.select_by_index(1)
    #     oper.select_by_index(2)
    #     tr_servi_sect.select_by_index(2)
    #     capital.send_keys(self.random_number(4))
    #     reg_pur.send_keys(self.random_string(10))
    #     est_an_income.send_keys(self.random_number(4))
    #     auth_per.send_keys(self.random_string(4))
    #     designat.select_by_index(2)
    #     nation.select_by_index(1)
    #     id_type.select_by_index(2)
    #     id_no.send_keys(self.random_number(8))
    #     id_exp.send_keys("20032004")
    #     cr_no.send_keys(self.random_number(8))
    #     comp_card_no.send_keys(self.random_number(8))
    #     cr_iss_dat.send_keys("20032004")
    #     cr_exp_dat.send_keys("20032014")
    #     cc_iss_date.send_keys("20032006")
    #     cc_exp_dat.send_keys("20032026")
    #
    #     self.rg.btn_next()
    #
    #     # Assigning BOD
    #     tit = Select(self.bod.title())
    #     f_name = self.bod.first_name()
    #     m_name = self.bod.middle_name()
    #     l_name = self.bod.last_name()
    #     dob = self.bod.dob()
    #     pob = self.bod.place_of_birth()
    #     gend = Select(self.bod.gender())
    #     fh_no = self.bod.flat_house_number()
    #     hb_name = self.bod.house_building_name()
    #     street = self.bod.street()
    #     ci = self.bod.city()
    #     count = Select(self.bod.country())
    #     nation = Select(self.bod.nationality())
    #     id_type = Select(self.bod.id_type())
    #     id_no = self.bod.id_no()
    #     pla_of_iss = Select(self.bod.place_of_id_issu())
    #     id_exp = self.bod.id_expiry()
    #
    #     tit.select_by_index(2)
    #     f_name.send_keys(self.random_string(5))
    #     m_name.send_keys(self.random_string(5))
    #     l_name.send_keys(self.random_string(5))
    #     dob.send_keys(22042003)
    #     pob.send_keys(self.random_string(5))
    #     gend.select_by_index(1)
    #     fh_no.send_keys(self.random_number(5))
    #     hb_name.send_keys(self.random_number(5))
    #     street.send_keys(self.random_string(5))
    #     ci.send_keys(self.random_string(5))
    #     count.select_by_index(3)
    #     nation.select_by_index(4)
    #     id_type.select_by_index(2)
    #     id_no.send_keys(self.random_number(5))
    #     pla_of_iss.select_by_index(2)
    #     id_exp.send_keys(self.random_number(5))
    #
    #     self.bod.btn_add_details()
    #     self.bod.btn_next()
    #     # time.sleep(2)
    #
    #     self.ud.click_passport()
    #     # time.sleep(2)
    #
    #     element = self.ud.send_front()
    #     element.click()
    #
    #     keyboard = Controller()
    #     time.sleep(2)
    #     self.driver.implicitly_wait(10)
    #     keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-08-19 11-43-05.png")
    #     time.sleep(2)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)
    #     time.sleep(2)
    #     self.ud.btn_next()
    #     time.sleep(2)
    #     self.ud.btn_save()
    #     time.sleep(2)
    #
    #     document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
    #
    #     if self.ud.editmode_message() == "You're in edit mode":
    #         responce.append(document)
    #         self.return_url = document['root']['baseURL']
    #         assert True
    #
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "test_adding_cust_corp_edit_test_validating_date.png")
    #         assert False
    #
    #     self.driver.quit()

    def test_adding_cust_corp_edit(self,setup):
        responce = []
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
        self.rg = Registration_Details(self.driver)
        self.bod = Beneficial_Owners_Details(self.driver)
        self.ud = Upload_Documents(self.driver)

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
        c_name = self.random_string(10)
        a_name = self.random_string(7)
        b_num = self.random_number(4)
        b_name = self.random_string(8)
        stre = self.random_string(12)
        po = self.random_number(6)
        dist = self.random_string(6)
        num = self.random_number(10)
        mai = self.random_email()

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
        #       Assigning elements for registration details
        coun_of_incorp = Select(self.rg.drp_country_of_incorp())
        lice_natu = Select(self.rg.drp_licence_nature())
        ent_type = Select(self.rg.drp_entity_type())
        oper = Select(self.rg.drp_operation())
        tr_servi_sect = Select(self.rg.drp_trade_service_sector())
        capital = self.rg.capital()
        reg_pur = self.rg.regisration_purpose()
        est_an_income = self.rg.estimated_annaul_incode()
        auth_per = self.rg.authorized_person()
        designat = Select(self.rg.drp_designation())
        nation = Select(self.rg.drp_nationality())
        id_type = Select(self.rg.drp_id_type())
        id_no = self.rg.id_no()
        id_exp = self.rg.dpick_id_exp()
        cr_no = self.rg.cr_no()
        comp_card_no = self.rg.comp_card_no()
        cr_iss_dat = self.rg.dpick_cr_issue_date()
        cr_exp_dat = self.rg.dpick_cr_exp_date()
        cc_iss_date = self.rg.dpick_cc_issue_date()
        cc_exp_dat = self.rg.dpick_cc_expaire_date()

        coun_of_incorp.select_by_index(2)
        lice_natu.select_by_index(2)
        ent_type.select_by_index(1)
        oper.select_by_index(2)
        tr_servi_sect.select_by_index(2)
        capital.send_keys(self.random_number(4))
        reg_pur.send_keys(self.random_string(10))
        est_an_income.send_keys(self.random_number(4))
        auth_per.send_keys(self.random_string(4))
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys(self.random_number(8))
        id_exp.send_keys("20032004")
        cr_no.send_keys(self.random_number(8))
        comp_card_no.send_keys(self.random_number(8))
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        self.rg.btn_next()

        # Assigning BOD
        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name = self.bod.last_name()
        dob = self.bod.dob()
        pob = self.bod.place_of_birth()
        gend = Select(self.bod.gender())
        fh_no = self.bod.flat_house_number()
        hb_name = self.bod.house_building_name()
        street = self.bod.street()
        ci = self.bod.city()
        count = Select(self.bod.country())
        nation = Select(self.bod.nationality())
        id_type = Select(self.bod.id_type())
        id_no = self.bod.id_no()
        pla_of_iss = Select(self.bod.place_of_id_issu())
        id_exp = self.bod.id_expiry()

        tit.select_by_index(2)
        f_name.send_keys(self.random_string(5))
        m_name.send_keys(self.random_string(5))
        l_name.send_keys(self.random_string(5))
        dob.send_keys(22042003)
        pob.send_keys(self.random_string(5))
        gend.select_by_index(1)
        fh_no.send_keys(self.random_number(5))
        hb_name.send_keys(self.random_number(5))
        street.send_keys(self.random_string(5))
        ci.send_keys(self.random_string(5))
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys(self.random_number(10))
        pla_of_iss.select_by_index(2)
        id_exp.send_keys(self.random_number(5))

        self.bod.btn_add_details()
        self.bod.btn_next()
        # time.sleep(2)

        self.ud.click_passport()
        # time.sleep(2)

        element = self.ud.send_front()
        element.click()

        keyboard = Controller()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-08-19 11-43-05.png")
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)
        self.ud.btn_next()
        time.sleep(2)
        self.ud.btn_save()
        time.sleep(2)

        document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

        if self.ud.editmode_message() == "You're in edit mode":
            responce.append(document)
            self.return_url = document['root']['baseURL']
            assert True

        else:
            responce = []
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
            self.rg = Registration_Details(self.driver)
            self.bod = Beneficial_Owners_Details(self.driver)
            self.ud = Upload_Documents(self.driver)

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
            c_name = self.random_string(10)
            a_name = self.random_string(7)
            b_num = self.random_number(4)
            b_name = self.random_string(8)
            stre = self.random_string(12)
            po = self.random_number(6)
            dist = self.random_string(6)
            num = self.random_number(10)
            mai = self.random_email()

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
            #       Assigning elements for registration details
            coun_of_incorp = Select(self.rg.drp_country_of_incorp())
            lice_natu = Select(self.rg.drp_licence_nature())
            ent_type = Select(self.rg.drp_entity_type())
            oper = Select(self.rg.drp_operation())
            tr_servi_sect = Select(self.rg.drp_trade_service_sector())
            capital = self.rg.capital()
            reg_pur = self.rg.regisration_purpose()
            est_an_income = self.rg.estimated_annaul_incode()
            auth_per = self.rg.authorized_person()
            designat = Select(self.rg.drp_designation())
            nation = Select(self.rg.drp_nationality())
            id_type = Select(self.rg.drp_id_type())
            id_no = self.rg.id_no()
            id_exp = self.rg.dpick_id_exp()
            cr_no = self.rg.cr_no()
            comp_card_no = self.rg.comp_card_no()
            cr_iss_dat = self.rg.dpick_cr_issue_date()
            cr_exp_dat = self.rg.dpick_cr_exp_date()
            cc_iss_date = self.rg.dpick_cc_issue_date()
            cc_exp_dat = self.rg.dpick_cc_expaire_date()

            coun_of_incorp.select_by_index(2)
            lice_natu.select_by_index(2)
            ent_type.select_by_index(1)
            oper.select_by_index(2)
            tr_servi_sect.select_by_index(2)
            capital.send_keys(self.random_number(4))
            reg_pur.send_keys(self.random_string(10))
            est_an_income.send_keys(self.random_number(4))
            auth_per.send_keys(self.random_string(4))
            designat.select_by_index(2)
            nation.select_by_index(1)
            id_type.select_by_index(2)
            id_no.send_keys(self.random_number(8))
            id_exp.send_keys("20032004")
            cr_no.send_keys(self.random_number(8))
            comp_card_no.send_keys(self.random_number(8))
            cr_iss_dat.send_keys("20032004")
            cr_exp_dat.send_keys("20032014")
            cc_iss_date.send_keys("20032006")
            cc_exp_dat.send_keys("20032026")

            self.rg.btn_next()

            # Assigning BOD
            tit = Select(self.bod.title())
            f_name = self.bod.first_name()
            m_name = self.bod.middle_name()
            l_name = self.bod.last_name()
            dob = self.bod.dob()
            pob = self.bod.place_of_birth()
            gend = Select(self.bod.gender())
            fh_no = self.bod.flat_house_number()
            hb_name = self.bod.house_building_name()
            street = self.bod.street()
            ci = self.bod.city()
            count = Select(self.bod.country())
            nation = Select(self.bod.nationality())
            id_type = Select(self.bod.id_type())
            id_no = self.bod.id_no()
            pla_of_iss = Select(self.bod.place_of_id_issu())
            id_exp = self.bod.id_expiry()

            tit.select_by_index(2)
            f_name.send_keys(self.random_string(5))
            m_name.send_keys(self.random_string(5))
            l_name.send_keys(self.random_string(5))
            dob.send_keys(22042003)
            pob.send_keys(self.random_string(5))
            gend.select_by_index(1)
            fh_no.send_keys(self.random_number(5))
            hb_name.send_keys(self.random_number(5))
            street.send_keys(self.random_string(5))
            ci.send_keys(self.random_string(5))
            count.select_by_index(3)
            nation.select_by_index(4)
            id_type.select_by_index(2)
            id_no.send_keys(self.random_number(10))
            pla_of_iss.select_by_index(2)
            id_exp.send_keys(20042029)

            self.bod.btn_add_details()
            self.bod.btn_next()
            # time.sleep(2)

            self.ud.click_passport()
            # time.sleep(2)

            element = self.ud.send_front()
            element.click()

            keyboard = Controller()
            time.sleep(2)
            self.driver.implicitly_wait(10)
            keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-08-19 11-43-05.png")
            time.sleep(2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(2)
            self.ud.btn_next()
            time.sleep(2)
            self.ud.btn_save()
            time.sleep(2)

            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

            if self.ud.editmode_message() == "You're in edit mode":
                responce.append(document)
                self.return_url = document['root']['baseURL']
                assert True

        print(self.return_url)
        self.driver.quit()




