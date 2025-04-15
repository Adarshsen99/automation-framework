from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from Dinero_automation.pageObjects.Customer_Registration_Corporate import Company_Information, Registration_Details, \
    Beneficial_Owners_Details
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18, \
    random_string_generator_numbers_22, random_string_generator_numbers_10, random_string_generator_numbers_20, \
    random_string_generator_max_52, random_string_generator_max_32, random_string_generator_max_22, \
    generate_random_email_lessthen_45, generate_random_email_lessthen_52, random_string_generator_numbers_max_10, \
    random_string_generator_max_18, random_string_generator_max_30, random_string_generator_max_50, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51, random_string_generator_max_20, random_string_generator_numbers, \
    generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort


class Test_Registration_Details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self, setup):
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
        capital.send_keys("20000")
        reg_pur.send_keys("Testing")
        est_an_income.send_keys("30000")
        auth_per.send_keys("CEO")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("2321232")
        id_exp.send_keys("20032004")
        cr_no.send_keys("597845612")
        comp_card_no.send_keys("211215445")
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        self.rg.btn_next()
        time.sleep(5)

        if self.comp_info.errorMessage() != "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_sending_valid_data.png")
            assert False
        self.driver.quit()

    def test_sending_without_data(self, setup):
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

        coun_of_incorp.select_by_visible_text("")
        lice_natu.select_by_visible_text("")
        ent_type.select_by_visible_text("")
        oper.select_by_visible_text("")
        tr_servi_sect.select_by_visible_text("")
        capital.send_keys("")
        reg_pur.send_keys("")
        est_an_income.send_keys("")
        auth_per.send_keys("")
        designat.select_by_visible_text("")
        nation.select_by_visible_text("")
        id_type.select_by_visible_text("")
        id_no.send_keys("")
        id_exp.send_keys("")
        cr_no.send_keys("")
        comp_card_no.send_keys("")
        cr_iss_dat.send_keys("")
        cr_exp_dat.send_keys("")
        cc_iss_date.send_keys("")
        cc_exp_dat.send_keys("")

        self.rg.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_sending_without_data.png")
            assert True
        #self.driver.quit()

    def test_special_char_data(self, setup):
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
        capital.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        reg_pur.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        est_an_income.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        auth_per.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        id_exp.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cr_no.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        comp_card_no.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cr_iss_dat.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cr_exp_dat.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cc_iss_date.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")
        cc_exp_dat.send_keys("!@#$%^&*()_+*/{}|]""-[:;',.?")

        self.rg.btn_next()
        time.sleep(5)

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_special_char_data.png")
            assert True
        self.driver.quit()

    def test_special_char_with_num_data(self, setup):
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
        capital.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        reg_pur.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        est_an_income.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        auth_per.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        id_exp.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        cr_no.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        comp_card_no.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        cr_iss_dat.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        cr_exp_dat.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        cc_iss_date.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")
        cc_exp_dat.send_keys("108765652!@#$%^&*()_+*/{}|]""-[:;',.?aewewdzcv")

        self.rg.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_special_char_with_num_data.png")
            assert True
        #self.driver.quit()

    def test_only_num_data(self, setup):
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
        capital.send_keys("123456789")
        reg_pur.send_keys("123456789")
        est_an_income.send_keys("123456789")
        auth_per.send_keys("123456789")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("123456789")
        id_exp.send_keys("123456789")
        cr_no.send_keys("123456789")
        comp_card_no.send_keys("123456789")
        cr_iss_dat.send_keys("123456789")
        cr_exp_dat.send_keys("123456789")
        cc_iss_date.send_keys("123456789")
        cc_exp_dat.send_keys("123456789")

        self.rg.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_only_num_data.png")
            assert True

        #self.driver.quit()

    def test_sending_only_char_data(self, setup):
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
        capital.send_keys("qwertyuioplkjhg")
        reg_pur.send_keys("qwertyuioplkjhg")
        est_an_income.send_keys("qwertyuioplkjhg")
        auth_per.send_keys("qwertyuioplkjhg")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("qwertyuioplkjhg")
        id_exp.send_keys("qwertyuioplkjhg")
        cr_no.send_keys("qwertyuioplkjhg")
        comp_card_no.send_keys("qwertyuioplkjhg")
        cr_iss_dat.send_keys("qwertyuioplkjhg")
        cr_exp_dat.send_keys("qwertyuioplkjhg")
        cc_iss_date.send_keys("qwertyuioplkjhg")
        cc_exp_dat.send_keys("qwertyuioplkjhg")

        self.rg.btn_next()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_sending_only_char_data.png")
            assert True
        self.driver.quit()

    def test_sending_bulk_data(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
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
        self.rg = Registration_Details(self.driver)
        self.bod = Beneficial_Owners_Details(self.driver)

        # Assigning Elements for Company Information
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

        # Assigning the data
        c_name = "Zen Tech"
        a_name = "Shaik"
        b_num = "1223"
        b_name = "monlash"
        stre = "nellore"
        po = "524309"
        dist = "Kerala"
        num = "7641524344"
        mai = "finnest@tech.com"

        # Filling Company Information
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

        capital = [50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000, 250000, 275000]
        registration_purpose = [
            'Business', 'Non-Profit', 'Educational', 'Government', 'Business',
            'Non-Profit', 'Educational', 'Government', 'Business', 'Non-Profit'
        ]
        estimated_annual_income = [200000, 150000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
        authorized_person = [
            'AUTH00123A', 'AUTH00234B', 'AUTH00345C', 'AUTH00456D', 'AUTH00567E',
            'AUTH00678F', 'AUTH00789G', 'AUTH00890H', 'AUTH00901I', 'AUTH01012J'
        ]
        id_no = [
            '123456789012', '234567890123', '345678901234', '456789012345', '567890123456',
            '678901234567', '789012345678', '890123456789', '901234567890', '012345678901'
        ]
        cr_no = [
            'CR123456', 'CR234567', 'CR345678', 'CR456789', 'CR567890',
            'CR678901', 'CR789012', 'CR890123', 'CR901234', 'CR012345'
        ]
        computer_card_no = [
            'CC12345678', 'CC23456789', 'CC34567890', 'CC45678901', 'CC56789012',
            'CC67890123', 'CC78901234', 'CC89012345', 'CC90123456', 'CC01234567'
        ]

        for i in range(10):
            # Assigning data from the lists
            capi = capital[i]
            regi_pur = registration_purpose[i]
            estim_anual_incom = estimated_annual_income[i]
            auth_person = authorized_person[i]
            id_num = id_no[i]
            cr_num = cr_no[i]
            comp_card_num = computer_card_no[i]

            # Assigning elements for Registration Details
            coun_of_incorp = Select(self.rg.drp_country_of_incorp())
            lice_natu = Select(self.rg.drp_licence_nature())
            ent_type = Select(self.rg.drp_entity_type())
            oper = Select(self.rg.drp_operation())
            tr_servi_sect = Select(self.rg.drp_trade_service_sector())
            capital_elem = self.rg.capital()
            reg_pur = self.rg.regisration_purpose()
            est_an_income = self.rg.estimated_annaul_incode()
            auth_per = self.rg.authorized_person()
            designat = Select(self.rg.drp_designation())
            nation = Select(self.rg.drp_nationality())
            id_type = Select(self.rg.drp_id_type())
            id_no_elem = self.rg.id_no()
            id_exp = self.rg.dpick_id_exp()
            cr_no_elem = self.rg.cr_no()
            comp_card_no_elem = self.rg.comp_card_no()
            cr_iss_dat = self.rg.dpick_cr_issue_date()
            cr_exp_dat = self.rg.dpick_cr_exp_date()
            cc_iss_date = self.rg.dpick_cc_issue_date()
            cc_exp_dat = self.rg.dpick_cc_expaire_date()

            # Filling Registration Details
            coun_of_incorp.select_by_index(2)
            lice_natu.select_by_index(2)
            ent_type.select_by_index(1)
            oper.select_by_index(2)
            tr_servi_sect.select_by_index(2)
            capital_elem.send_keys(capi)
            reg_pur.send_keys(regi_pur)
            est_an_income.send_keys(estim_anual_incom)
            auth_per.send_keys(auth_person)
            designat.select_by_index(2)
            nation.select_by_index(1)
            id_type.select_by_index(2)
            id_no_elem.send_keys(id_num)
            id_exp.send_keys("20032004")
            cr_no_elem.send_keys(cr_num)
            comp_card_no_elem.send_keys(comp_card_num)
            cr_iss_dat.send_keys("20032004")
            cr_exp_dat.send_keys("20032014")
            cc_iss_date.send_keys("20032006")
            cc_exp_dat.send_keys("20032026")

            self.rg.btn_next()
            self.bod.btn_back()

            # Validation and screenshot
            if self.comp_info.errorMessage() == "Required":
                assert False
            else:
                self.driver.save_screenshot(screenShort.screen_short() + f"RG_test_sending_bulk_data_success_{i}.png")
                assert True

            # coun_of_incorp = Select(self.rg.drp_country_of_incorp())
            # lice_natu = Select(self.rg.drp_licence_nature())
            # ent_type = Select(self.rg.drp_entity_type())
            # oper = Select(self.rg.drp_operation())
            # tr_servi_sect = Select(self.rg.drp_trade_service_sector())
            capital_elem = self.rg.capital()
            reg_pur = self.rg.regisration_purpose()
            est_an_income = self.rg.estimated_annaul_incode()
            auth_per = self.rg.authorized_person()
            # designat = Select(self.rg.drp_designation())
            # nation = Select(self.rg.drp_nationality())
            # id_type = Select(self.rg.drp_id_type())
            id_no_elem = self.rg.id_no()
            id_exp = self.rg.dpick_id_exp()
            cr_no_elem = self.rg.cr_no()
            comp_card_no_elem = self.rg.comp_card_no()
            cr_iss_dat = self.rg.dpick_cr_issue_date()
            cr_exp_dat = self.rg.dpick_cr_exp_date()
            cc_iss_date = self.rg.dpick_cc_issue_date()
            cc_exp_dat = self.rg.dpick_cc_expaire_date()

            # Clear fields for the next iteration
            capital_elem.clear()
            reg_pur.clear()
            est_an_income.clear()
            auth_per.clear()
            id_no_elem.clear()
            id_exp.clear()
            cr_no_elem.clear()
            comp_card_no_elem.clear()
            cr_iss_dat.clear()
            cr_exp_dat.clear()
            cc_iss_date.clear()
            cc_exp_dat.clear()

        self.driver.quit()

    def test_preview(self, setup):
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
        capital.send_keys("20000")
        reg_pur.send_keys("Testing")
        est_an_income.send_keys("30000")
        auth_per.send_keys("CEO")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("2321232")
        id_exp.send_keys("20032004")
        cr_no.send_keys("597845612")
        comp_card_no.send_keys("211215445")
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        coun_of_incorp_val = coun_of_incorp.first_selected_option.text
        print("coun_of_incorp_val", coun_of_incorp_val)
        lice_natu_val = lice_natu.first_selected_option.text
        print("lice_natu_val", lice_natu_val)
        ent_type_val = ent_type.first_selected_option.text
        print("ent_type_val", ent_type_val)
        oper_val = oper.first_selected_option.text
        print("oper_val", oper_val)
        tr_servi_sect_val = tr_servi_sect.first_selected_option.text
        print("tr_servi_sect_val", tr_servi_sect_val)
        capital_val = capital.get_attribute('value')
        print("capital_val", capital_val)
        reg_pur_val = reg_pur.get_attribute('value')
        print("reg_pur_val", reg_pur_val)
        est_an_income_val = est_an_income.get_attribute('value')
        print("est_an_income_val", est_an_income_val)
        auth_per_val = auth_per.get_attribute('value')
        print("auth_per_val", auth_per_val)
        designat_val = designat.first_selected_option.text
        print("designat_val", designat_val)
        nation_val = nation.first_selected_option.text
        print("nation_val", nation_val)
        id_type_val = id_type.first_selected_option.text
        print("id_type_val what i sent", id_type_val)
        id_no_val = id_no.get_attribute('value')
        print("id_no_val", id_no_val)
        id_exp_val = id_exp.get_attribute('value')
        print("id_exp_val", id_exp_val)
        cr_no_val = cr_no.get_attribute('value')
        print("cr_no_val", cr_no_val)
        comp_card_no_val = comp_card_no.get_attribute('value')
        print("comp_card_no_val", comp_card_no_val)
        cr_iss_dat_val = cr_iss_dat.get_attribute('value')
        print("cr_iss_dat_val", cr_iss_dat_val)
        cr_exp_dat_val = cr_exp_dat.get_attribute('value')
        print("cr_exp_dat_val", cr_exp_dat_val)
        cc_iss_date_val = cc_iss_date.get_attribute('value')
        print("cc_iss_date_val", cc_iss_date_val)
        cc_exp_dat_val = cc_exp_dat.get_attribute('value')
        print("cc_exp_dat_val", cc_exp_dat_val)

        self.rg.btn_next()
        self.bod.registration_preview()

        cop_pre = self.bod.cont_of_incorp_pre()
        print("cop_pre", cop_pre)
        lic_pre = self.bod.license_nature_pre()
        print("lic_pre", lic_pre)
        entity_pre = self.bod.entity_type_pre()
        print("entity_pre", entity_pre)
        oprta_pre = self.bod.operation_field_pre()
        print("oprta_pre", oprta_pre)
        trader_pre = self.bod.trade_service_sector_pre()
        print("trader_pre", trader_pre)
        capital_pre = self.bod.capital_pre()
        print("capital_pre", capital_pre)
        reg_pur_pre = self.bod.regisration_purpose_pre()
        print("reg_pur_pre", reg_pur_pre)
        est_anu_pre = self.bod.estimated_annaul_incode_pre()
        print("est_anu_pre", est_anu_pre)
        auth_per_pre = self.bod.authorized_person_pre()
        print("auth_per_pre", auth_per_pre)
        desig_pre = self.bod.drp_designation_id_pre()
        print("desig_pre", desig_pre)

        nati_pre = self.bod.nationality_pre()
        print(type(nati_pre))
        nati_pre_element = self.bod.nationality_pre()

        # Extract the text or value from the element (depending on your need)
        nati_pre = nati_pre_element.text
        print("nati_pre", nati_pre)
        id_type_pre = self.bod.id_type_pre()
        print("id_type_pre", id_type_pre)
        id_no_pre = self.bod.id_no_pre()
        print("id_no_pre", id_no_pre)
        id_exp_pre = self.bod.id_expiry_pre()
        print("id_exp_pre", id_exp_pre)
        comp_card_pre = self.bod.comp_card_no_pre()
        print("comp_card_pre", comp_card_pre)
        cr_iss_date_pre = self.bod.cr_iss_date_pre()
        print("cr_iss_date_pre", cr_iss_date_pre)
        cr_exp_date_pre = self.bod.cr_exp_date_pre()
        print("cr_exp_date_pre", cr_exp_date_pre)
        cc_iss_date_pre = self.bod.cc_iss_date_pre()
        print("cc_iss_date_pre", cc_iss_date_pre)
        cc_exp_date_pre = self.bod.cc_exp_date_pre()
        print("cc_exp_date_pre", cc_exp_date_pre)
        cr_no_pre = self.bod.cr_no_pre()
        print("cr_no_pre", cr_no_pre)

        if coun_of_incorp_val == cop_pre:
            assert True
        else:
            assert False

        if lice_natu_val == lic_pre:
            assert True
        else:
            assert False

        if ent_type_val == entity_pre:
            assert True
        else:
            assert False

        if oper_val == oprta_pre:
            assert True
        else:
            assert False

        if tr_servi_sect_val == trader_pre:
            assert True
        else:
            assert False

        if capital_val == capital_pre:
            assert True
        else:
            assert False

        if est_an_income_val == est_anu_pre:
            assert True
        else:
            assert False

        if reg_pur_val == reg_pur_pre:
            assert True
        else:
            assert False

        if auth_per_val == auth_per_pre:
            assert True
        else:
            assert False

        if designat_val == desig_pre:
            assert True
        else:
            assert False

        if nation_val == nati_pre:
            assert True
        else:
            assert False

        if id_type_val == id_type_pre:
            assert True
        else:
            assert False

        if id_no_val == id_no_pre:
            assert True
        else:
            assert False

        # if id_exp_val == id_exp_pre:
        #     assert True
        # else:
        #     assert False

        if cr_no_val == cr_no_pre:
            assert True
        else:
            assert False

        if comp_card_no_val == comp_card_pre:
            assert True
        else:
            assert False

        # if cr_iss_dat_val == cr_iss_date_pre:
        #     assert True
        # else:
        #     assert False

        # if cr_exp_dat_val == cr_exp_date_pre:
        #     assert True
        # else:
        #     assert False
        #
        # if cc_iss_date_val == cc_iss_date_pre:
        #     assert True
        # else:
        #     assert False
        #
        # if cc_exp_dat_val == cc_exp_date_pre:
        #     assert True
        # else:
        #     assert False
        #self.driver.quit()

    def test_validating_maxlen(self, setup):
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
        #       Assigning elements for registration details

        capital_len = int(self.rg.capital().get_attribute('maxlength'))
        reg_pur_len = int(self.rg.regisration_purpose().get_attribute('maxlength'))
        est_an_income_len = int(self.rg.estimated_annaul_incode().get_attribute('maxlength'))
        auth_per_len = int(self.rg.authorized_person().get_attribute('maxlength'))
        id_no_len = int(self.rg.id_no().get_attribute('maxlength'))
        cr_no_len = int(self.rg.cr_no().get_attribute('maxlength'))
        comp_card_no_len = int(self.rg.comp_card_no().get_attribute('maxlength'))

        print("capital", capital_len)
        print("reg_pur", reg_pur_len)
        print("est_an_income", est_an_income_len)
        print("auth_per", auth_per_len)
        print("id_no", id_no_len)
        print("cr_no", cr_no_len)
        print("comp_card_no", comp_card_no_len)

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
        capital.send_keys(random_string_generator_numbers_20())
        reg_pur.send_keys(random_string_generator_max_50())
        est_an_income.send_keys(random_string_generator_numbers_20())
        auth_per.send_keys(random_string_generator_max_50())
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys(random_string_generator_max_30())
        id_exp.send_keys("20032004")
        cr_no.send_keys(random_string_generator_numbers_20() + random_string_generator_numbers_10())
        comp_card_no.send_keys(random_string_generator_numbers_20() + random_string_generator_numbers_10())
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        capital_val = len(self.rg.capital().get_attribute('value'))
        reg_pur_val = len(self.rg.regisration_purpose().get_attribute('value'))
        est_an_income_val = len(self.rg.estimated_annaul_incode().get_attribute('value'))
        auth_per_val = len(self.rg.authorized_person().get_attribute('value'))
        id_no_val = len(self.rg.id_no().get_attribute('value'))
        cr_no_val = len(self.rg.cr_no().get_attribute('value'))
        print("cr_no_val", cr_no_val)
        comp_card_no_val = len(self.rg.comp_card_no().get_attribute('value'))

        if capital_val == capital_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_capital.png")
            assert False

        if reg_pur_val == reg_pur_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_reg_pur.png")
            assert False

        if est_an_income_val == est_an_income_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_est_an.png")
            assert False

        if auth_per_val == auth_per_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_auth_per.png")
            assert False

        if id_no_val == id_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_id_no.png")
            assert False

        if cr_no_val == cr_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_cr_no.png")
            assert False

        if comp_card_no_val == comp_card_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_comp_card.png")
            assert False
        self.driver.quit()

    def test_validating_maxlen_less(self, setup):
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
        #       Assigning elements for registration details

        capital_len = int(self.rg.capital().get_attribute('maxlength'))
        reg_pur_len = int(self.rg.regisration_purpose().get_attribute('maxlength'))
        est_an_income_len = int(self.rg.estimated_annaul_incode().get_attribute('maxlength'))
        auth_per_len = int(self.rg.authorized_person().get_attribute('maxlength'))
        id_no_len = int(self.rg.id_no().get_attribute('maxlength'))
        cr_no_len = int(self.rg.cr_no().get_attribute('maxlength'))
        comp_card_no_len = int(self.rg.comp_card_no().get_attribute('maxlength'))

        print("capital", capital_len)
        print("reg_pur", reg_pur_len)
        print("est_an_income", est_an_income_len)
        print("auth_per", auth_per_len)
        print("id_no", id_no_len)
        print("cr_no", cr_no_len)
        print("comp_card_no", comp_card_no_len)

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
        capital.send_keys(random_string_generator_numbers_18())
        reg_pur.send_keys(random_string_generator_max_48())
        est_an_income.send_keys(random_string_generator_numbers_18())
        auth_per.send_keys(random_string_generator_max_48())
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys(random_string_generator_max_28())
        id_exp.send_keys("20032004")
        cr_no.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_10())
        comp_card_no.send_keys(random_string_generator_numbers_18() + random_string_generator_numbers_10())
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        capital_val = len(self.rg.capital().get_attribute('value'))
        reg_pur_val = len(self.rg.regisration_purpose().get_attribute('value'))
        est_an_income_val = len(self.rg.estimated_annaul_incode().get_attribute('value'))
        auth_per_val = len(self.rg.authorized_person().get_attribute('value'))
        id_no_val = len(self.rg.id_no().get_attribute('value'))
        cr_no_val = len(self.rg.cr_no().get_attribute('value'))
        print("cr_no_val", cr_no_val)
        comp_card_no_val = len(self.rg.comp_card_no().get_attribute('value'))

        if capital_val < capital_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_capital.png")
            assert False

        if reg_pur_val < reg_pur_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_reg_pur.png")
            assert False

        if est_an_income_val < est_an_income_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_est_an.png")
            assert False

        if auth_per_val < auth_per_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_auth_per.png")
            assert False

        if id_no_val < id_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_id_no.png")
            assert False

        if cr_no_val < cr_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_cr_no.png")
            assert False

        if comp_card_no_val < comp_card_no_len:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_validating_maxlen_less_card.png")
            assert False
        self.driver.quit()

    def test_validating_cancel(self, setup):
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
        capital.send_keys("20000")
        reg_pur.send_keys("Testing")
        est_an_income.send_keys("30000")
        auth_per.send_keys("CEO")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("2321232")
        id_exp.send_keys("20032004")
        cr_no.send_keys("597845612")
        comp_card_no.send_keys("211215445")
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        coun_of_incorp_val = coun_of_incorp.first_selected_option.text
        lice_natu_val = lice_natu.first_selected_option.text
        ent_type_val = ent_type.first_selected_option.text
        oper_val = oper.first_selected_option.text
        tr_servi_sect_val = tr_servi_sect.first_selected_option.text
        capital_val = capital.get_attribute('value')
        reg_pur_val = reg_pur.get_attribute('value')
        est_an_income_val = est_an_income.get_attribute('value')
        auth_per_val = auth_per.get_attribute('value')
        designat_val = designat.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        id_exp_val = id_exp.get_attribute('value')
        cr_no_val = cr_no.get_attribute('value')
        comp_card_no_val = comp_card_no.get_attribute('value')
        cr_iss_dat_val = cr_iss_dat.get_attribute('value')
        cr_exp_dat_val = cr_exp_dat.get_attribute('value')
        cc_iss_date_val = cc_iss_date.get_attribute('value')
        cc_exp_dat_val = cc_exp_dat.get_attribute('value')

        print(
            "Values before the cancel"
            f"coun_of_incorp_val: {coun_of_incorp_val}, "
            f"lice_natu_val: {lice_natu_val}, "
            f"ent_type_val: {ent_type_val}, "
            f"oper_val: {oper_val}, "
            f"tr_servi_sect_val: {tr_servi_sect_val}, "
            f"capital_val: {capital_val}, "
            f"reg_pur_val: {reg_pur_val}, "
            f"est_an_income_val: {est_an_income_val}, "
            f"auth_per_val: {auth_per_val}, "
            f"designat_val: {designat_val}, "
            f"nation_val: {nation_val}, "
            f"id_type_val: {id_type_val}, "
            f"id_no_val: {id_no_val}, "
            f"id_exp_val: {id_exp_val}, "
            f"cr_no_val: {cr_no_val}, "
            f"comp_card_no_val: {comp_card_no_val}, "
            f"cr_iss_dat_val: {cr_iss_dat_val}, "
            f"cr_exp_dat_val: {cr_exp_dat_val}, "
            f"cc_iss_date_val: {cc_iss_date_val}, "
            f"cc_exp_dat_val: {cc_exp_dat_val}"
        )

        self.rg.btn_cancel()
        self.rg.btn_confirm()
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

        coun_of_incorp_af = coun_of_incorp.first_selected_option.text
        lice_natu_af = lice_natu.first_selected_option.text
        ent_type_af = ent_type.first_selected_option.text
        oper_af = oper.first_selected_option.text
        tr_servi_sect_af = tr_servi_sect.first_selected_option.text
        capital_af = capital.get_attribute('value')
        reg_pur_af = reg_pur.get_attribute('value')
        est_an_income_af = est_an_income.get_attribute('value')
        auth_per_af = auth_per.get_attribute('value')
        designat_af = designat.first_selected_option.text
        nation_af = nation.first_selected_option.text
        id_type_af = id_type.first_selected_option.text
        id_no_af = id_no.get_attribute('value')
        id_exp_af = id_exp.get_attribute('value')
        cr_no_af = cr_no.get_attribute('value')
        comp_card_no_af = comp_card_no.get_attribute('value')
        cr_iss_dat_af = cr_iss_dat.get_attribute('value')
        cr_exp_dat_af = cr_exp_dat.get_attribute('value')
        cc_iss_date_af = cc_iss_date.get_attribute('value')
        cc_exp_dat_af = cc_exp_dat.get_attribute('value')

        print(
            f"coun_of_incorp_af: {coun_of_incorp_af}, "
            f"lice_natu_af: {lice_natu_af}, "
            f"ent_type_af: {ent_type_af}, "
            f"oper_af: {oper_af}, "
            f"tr_servi_sect_af: {tr_servi_sect_af}, "
            f"capital_af: {capital_af}, "
            f"reg_pur_af: {reg_pur_af}, "
            f"est_an_income_af: {est_an_income_af}, "
            f"auth_per_af: {auth_per_af}, "
            f"designat_af: {designat_af}, "
            f"nation_af: {nation_af}, "
            f"id_type_af: {id_type_af}, "
            f"id_no_af: {id_no_af}, "
            f"id_exp_af: {id_exp_af}, "
            f"cr_no_af: {cr_no_af}, "
            f"comp_card_no_af: {comp_card_no_af}, "
            f"cr_iss_dat_af: {cr_iss_dat_af}, "
            f"cr_exp_dat_af: {cr_exp_dat_af}, "
            f"cc_iss_date_af: {cc_iss_date_af}, "
            f"cc_exp_dat_af: {cc_exp_dat_af}"
        )

        if coun_of_incorp_val != coun_of_incorp_af:
            assert True
        elif lice_natu_val != lice_natu_af:
            assert True
        elif ent_type_val != ent_type_af:
            assert True
        elif oper_val != oper_af:
            assert True
        elif tr_servi_sect_val != tr_servi_sect_af:
            assert True
        elif capital_val != capital_af:
            assert True
        elif reg_pur_val != reg_pur_af:
            assert True
        elif est_an_income_val != est_an_income_af:
            assert True
        elif auth_per_val != auth_per_af:
            assert True
        elif designat_val != designat_af:
            assert True
        elif nation_val != nation_af:
            assert True
        elif id_type_val != id_type_af:
            assert True
        elif id_no_val != id_no_af:
            assert True
        elif id_exp_val != id_exp_af:
            assert True
        elif cr_no_val != cr_no_af:
            assert True
        elif comp_card_no_val != comp_card_no_af:
            assert True
        elif cr_iss_dat_val != cr_iss_dat_af:
            assert True
        elif cr_exp_dat_val != cr_exp_dat_af:
            assert True
        elif cc_iss_date_val != cc_iss_date_af:
            assert True
        elif cc_exp_dat_val != cc_exp_dat_af:
            assert True
        else:
            assert False, "All values are equal"

        self.driver.quit()

    def test_modifying_data_clear(self, setup):
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
        # Assigning elements for registration details
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
        capital.send_keys("20000")
        reg_pur.send_keys("Testing")
        est_an_income.send_keys("30000")
        auth_per.send_keys("CEO")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("2321232")
        id_exp.send_keys("20032004")
        cr_no.send_keys("597845612")
        comp_card_no.send_keys("211215445")
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.send_keys("20032026")

        self.rg.btn_next()
        self.bod.btn_back()

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
        capital.clear()
        capital.send_keys("20000")
        reg_pur.clear()
        reg_pur.send_keys("Testing")
        est_an_income.clear()
        est_an_income.send_keys("30000")
        auth_per.clear()
        auth_per.send_keys("CEO")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.clear()
        id_no.send_keys("2321232")
        id_exp.clear()
        id_exp.send_keys("20032004")
        cr_no.clear()
        cr_no.send_keys("597845612")
        comp_card_no.clear()
        comp_card_no.send_keys("211215445")
        cr_iss_dat.clear()
        cr_iss_dat.send_keys("20032004")
        cr_exp_dat.clear()
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.clear()
        cc_iss_date.send_keys("20032006")
        cc_exp_dat.clear()
        cc_exp_dat.send_keys("20032026")

        coun_of_incorp_val = coun_of_incorp.first_selected_option.text
        print("coun_of_incorp_val", coun_of_incorp_val)
        lice_natu_val = lice_natu.first_selected_option.text
        print("lice_natu_val", lice_natu_val)
        ent_type_val = ent_type.first_selected_option.text
        print("ent_type_val", ent_type_val)
        oper_val = oper.first_selected_option.text
        print("oper_val", oper_val)
        tr_servi_sect_val = tr_servi_sect.first_selected_option.text
        print("tr_servi_sect_val", tr_servi_sect_val)
        capital_val = capital.get_attribute('value')
        print("capital_val", capital_val)
        reg_pur_val = reg_pur.get_attribute('value')
        print("reg_pur_val", reg_pur_val)
        est_an_income_val = est_an_income.get_attribute('value')
        print("est_an_income_val", est_an_income_val)
        auth_per_val = auth_per.get_attribute('value')
        print("auth_per_val", auth_per_val)
        designat_val = designat.first_selected_option.text
        print("designat_val", designat_val)
        nation_val = nation.first_selected_option.text
        print("nation_val", nation_val)
        id_type_val = id_type.first_selected_option.text
        print("id_type_val what i sent", id_type_val)
        id_no_val = id_no.get_attribute('value')
        print("id_no_val", id_no_val)
        id_exp_val = id_exp.get_attribute('value')
        print("id_exp_val", id_exp_val)
        cr_no_val = cr_no.get_attribute('value')
        print("cr_no_val", cr_no_val)
        comp_card_no_val = comp_card_no.get_attribute('value')
        print("comp_card_no_val", comp_card_no_val)
        cr_iss_dat_val = cr_iss_dat.get_attribute('value')
        print("cr_iss_dat_val", cr_iss_dat_val)
        cr_exp_dat_val = cr_exp_dat.get_attribute('value')
        print("cr_exp_dat_val", cr_exp_dat_val)
        cc_iss_date_val = cc_iss_date.get_attribute('value')
        print("cc_iss_date_val", cc_iss_date_val)
        cc_exp_dat_val = cc_exp_dat.get_attribute('value')
        print("cc_exp_dat_val", cc_exp_dat_val)

        self.rg.btn_next()
        self.bod.registration_preview()

        cop_pre = self.bod.cont_of_incorp_pre()
        print("cop_pre", cop_pre)
        lic_pre = self.bod.license_nature_pre()
        print("lic_pre", lic_pre)
        entity_pre = self.bod.entity_type_pre()
        print("entity_pre", entity_pre)
        oprta_pre = self.bod.operation_field_pre()
        print("oprta_pre", oprta_pre)
        trader_pre = self.bod.trade_service_sector_pre()
        print("trader_pre", trader_pre)
        capital_pre = self.bod.capital_pre()
        print("capital_pre", capital_pre)
        reg_pur_pre = self.bod.regisration_purpose_pre()
        print("reg_pur_pre", reg_pur_pre)
        est_anu_pre = self.bod.estimated_annaul_incode_pre()
        print("est_anu_pre", est_anu_pre)
        auth_per_pre = self.bod.authorized_person_pre()
        print("auth_per_pre", auth_per_pre)
        desig_pre = self.bod.drp_designation_id_pre()
        print("desig_pre", desig_pre)
        nati_pre_element = self.bod.nationality_pre()

        # Extract the text or value from the element (depending on your need)
        nati_pre = nati_pre_element.text

        print("nati_pre", nati_pre)
        id_type_pre = self.bod.id_type_pre()
        print("id_type_pre", id_type_pre)
        id_no_pre = self.bod.id_no_pre()
        print("id_no_pre", id_no_pre)
        id_exp_pre = self.bod.id_expiry_pre()
        print("id_exp_pre", id_exp_pre)
        comp_card_pre = self.bod.comp_card_no_pre()
        print("comp_card_pre", comp_card_pre)
        cr_iss_date_pre = self.bod.cr_iss_date_pre()
        print("cr_iss_date_pre", cr_iss_date_pre)
        cr_exp_date_pre = self.bod.cr_exp_date_pre()
        print("cr_exp_date_pre", cr_exp_date_pre)
        cc_iss_date_pre = self.bod.cc_iss_date_pre()
        print("cc_iss_date_pre", cc_iss_date_pre)
        cc_exp_date_pre = self.bod.cc_exp_date_pre()
        print("cc_exp_date_pre", cc_exp_date_pre)
        cr_no_pre = self.bod.cr_no_pre()
        print("cr_no_pre", cr_no_pre)

        if coun_of_incorp_val == cop_pre:
            assert True
        else:
            assert False

        if lice_natu_val == lic_pre:
            assert True
        else:
            assert False

        if ent_type_val == entity_pre:
            assert True
        else:
            assert False

        if oper_val == oprta_pre:
            assert True
        else:
            assert False

        if tr_servi_sect_val == trader_pre:
            assert True
        else:
            assert False

        if capital_val == capital_pre:
            assert True
        else:
            assert False

        if est_an_income_val == est_anu_pre:
            assert True
        else:
            assert False

        if reg_pur_val == reg_pur_pre:
            assert True
        else:
            assert False

        if auth_per_val == auth_per_pre:
            assert True
        else:
            assert False

        if designat_val == desig_pre:
            assert True
        else:
            assert False

        if nation_val == nati_pre:
            assert True
        else:
            assert False

        if id_type_val == id_type_pre:
            assert True
        else:
            assert False

        if id_no_val == id_no_pre:
            assert True
        else:
            assert False

        # if id_exp_val == id_exp_pre:
        #     assert True
        # else:
        #     assert False

        if cr_no_val == cr_no_pre:
            assert True
        else:
            assert False

        if comp_card_no_val == comp_card_pre:
            assert True
        else:
            assert False

        # if cr_iss_dat_val == cr_iss_date_pre:
        #     assert True
        # else:
        #     assert False

        # if cr_exp_dat_val == cr_exp_date_pre:
        #     assert True
        # else:
        #     assert False
        #
        # if cc_iss_date_val == cc_iss_date_pre:
        #     assert True
        # else:
        #     assert False
        #
        # if cc_exp_dat_val == cc_exp_date_pre:
        #     assert True
        # else:
        #     assert False
        self.driver.quit()

    def test_data_having_spaces(self, setup):

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
        a_name = "Sh aik"
        b_num = "12   23"
        b_name = "mon la sh"
        stre = "nel lo  re"
        po = "52  4  0 9"
        dist = "Ke r a  la"
        num = "7641 52 43 44"
        mai = " finnest@ te ch.com"

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
        capital.send_keys("20 0  00 ")
        reg_pur.send_keys("Test i  g")
        est_an_income.send_keys("3 0 0 00")
        auth_per.send_keys("C E   O")
        designat.select_by_index(2)
        nation.select_by_index(1)
        id_type.select_by_index(2)
        id_no.send_keys("2321  2  32")
        id_exp.send_keys("2003  2  00  4")
        cr_no.send_keys("597  8  456  12")
        comp_card_no.send_keys("2  112   154  45")
        cr_iss_dat.send_keys("200 320  04")
        cr_exp_dat.send_keys("20032014")
        cc_iss_date.send_keys("200 320  06")
        cc_exp_dat.send_keys("200 32  026")

        self.rg.btn_next()
        time.sleep(5)

        if self.comp_info.errorMessage() != "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "RG_test_sending_valid_data.png")
            assert False
        self.driver.quit()
