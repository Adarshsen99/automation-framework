from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
import time
from Dinero_automation.pageObjects.Customer_Registration_Corporate import Company_Information,Registration_Details,Beneficial_Owners_Details
from Dinero_automation.utilities.randomString import random_string_generator_numbers_18,random_string_generator_numbers_22,random_string_generator_numbers_10,random_string_generator_numbers_20,random_string_generator_max_52,random_string_generator_max_32,random_string_generator_max_22,generate_random_email_lessthen_45,generate_random_email_lessthen_52,random_string_generator_numbers_max_10,random_string_generator_max_18,random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51,random_string_generator_max_20,random_string_generator_numbers,generate_random_email
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Beneficial_Owners_Details:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_add_beneficial_owners(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("Tester")
        m_name.send_keys("QA")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners.png")
            assert True

        self.driver.quit()

    def test_add_beneficial_owners_and_check_values(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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

        # Get values before click on add details

        ti_val = tit.first_selected_option.text
        f_name_val = f_name.get_attribute('value')
        m_name_val = m_name.get_attribute('value')
        l_name_val = l_name.get_attribute('value')
        dob_val = dob.get_attribute('value')
        pob_val = pob.get_attribute('value')
        gend_val = gend.first_selected_option.text
        fh_no_val = fh_no.get_attribute('value')
        hb_name_val = hb_name.get_attribute('value')
        street_val = street.get_attribute('value')
        ci_val = ci.get_attribute('value')
        count_val = count.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        pla_of_iss_val = pla_of_iss.first_selected_option.text
        id_exp_val = id_exp.get_attribute('value')

        print(
            "Before:",
            ti_val,
            f_name_val,
            m_name_val,
            l_name_val,
            dob_val,
            pob_val,
            gend_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            count_val,
            nation_val,
            id_type_val,
            id_no_val,
            pla_of_iss_val,
            id_exp_val)

        tit.select_by_index(2)
        f_name.send_keys("Tester")
        m_name.send_keys("QA")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()

        ti_val_af = tit.first_selected_option.text
        f_name_val_af = f_name.get_attribute('value')
        m_name_val_af = m_name.get_attribute('value')
        l_name_val_af = l_name.get_attribute('value')
        dob_val_af = dob.get_attribute('value')
        pob_val_af = pob.get_attribute('value')
        gend_val_af = gend.first_selected_option.text
        fh_no_val_af = fh_no.get_attribute('value')
        hb_name_val_af = hb_name.get_attribute('value')
        street_val_af = street.get_attribute('value')
        ci_val_af = ci.get_attribute('value')
        count_val_af = count.first_selected_option.text
        nation_val_af = nation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_no_val_af = id_no.get_attribute('value')
        pla_of_iss_val_af = pla_of_iss.first_selected_option.text
        id_exp_val_af = id_exp.get_attribute('value')

        print(
            "After:",
            ti_val_af,
            f_name_val_af,
            m_name_val_af,
            l_name_val_af,
            dob_val_af,
            pob_val_af,
            gend_val_af,
            fh_no_val_af,
            hb_name_val_af,
            street_val_af,
            ci_val_af,
            count_val_af,
            nation_val_af,
            id_type_val_af,
            id_no_val_af,
            pla_of_iss_val_af,
            id_exp_val_af

        )

        if (ti_val == ti_val_af and f_name_val == f_name_val_af and m_name_val == m_name_val_af and l_name_val == l_name_val_af and
            dob_val == dob_val_af and pob_val == pob_val_af and gend_val == gend_val_af and fh_no_val == fh_no_val and hb_name_val == hb_name_val and
            street_val == street_val_af and ci_val == ci_val_af and count_val == count_val_af and nation_val == nation_val_af and id_type_val == id_type_val and id_no_val == id_no_val and pla_of_iss_val == pla_of_iss_val_af and id_exp_val == id_exp_val_af):

            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_and_check_values.png")
            assert False

        self.driver.quit()

    def test_add_multiple_beneficial_owners(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        # Define a list of dictionaries, each containing the user details
        users = [
            {
                "title_index": 2,
                "first_name": "Tester",
                "middle_name": "QA",
                "last_name": "Automation",
                "dob": "20022000",
                "place_of_birth": "Kerala",
                "gender_index": 1,
                "flat_house_number": "12457888",
                "house_building_name": "65445665",
                "street": "kochi",
                "city": "Nellore",
                "country_index": 3,
                "nationality_index": 4,
                "id_type_index": 2,
                "id_no": "2145221",
                "place_of_id_issu_index": 2,
                "id_expiry": "06072008"
            },
            {
                "title_index": 1,
                "first_name": "John",
                "middle_name": "Doe",
                "last_name": "Smith",
                "dob": "15081990",
                "place_of_birth": "Chennai",
                "gender_index": 1,
                "flat_house_number": "55566677",
                "house_building_name": "12345678",
                "street": "Chennai Street",
                "city": "Hyderabad",
                "country_index": 2,
                "nationality_index": 3,
                "id_type_index": 1,
                "id_no": "98765432",
                "place_of_id_issu_index": 1,
                "id_expiry": "15082025"
            },
            {
                "title_index": 1,
                "first_name": "Alice",
                "middle_name": "Mary",
                "last_name": "Johnson",
                "dob": "08031985",
                "place_of_birth": "Bangalore",
                "gender_index": 2,
                "flat_house_number": "12345000",
                "house_building_name": "AB Apartments",
                "street": "MG Road",
                "city": "Bangalore",
                "country_index": 1,
                "nationality_index": 2,
                "id_type_index": 2,
                "id_no": "65432100",
                "place_of_id_issu_index": 3,
                "id_expiry": "08032025"
            },
            {
                "title_index": 1,
                "first_name": "Michael",
                "middle_name": "Edward",
                "last_name": "Brown",
                "dob": "24071975",
                "place_of_birth": "Mumbai",
                "gender_index": 1,
                "flat_house_number": "78901234",
                "house_building_name": "Ocean View",
                "street": "Marine Drive",
                "city": "Mumbai",
                "country_index": 4,
                "nationality_index": 5,
                "id_type_index":2,
                "id_no": "11223344",
                "place_of_id_issu_index": 4,
                "id_expiry": "24072030"
            },
            {
                "title_index": 1,
                "first_name": "Emma",
                "middle_name": "Grace",
                "last_name": "Williams",
                "dob": "12061995",
                "place_of_birth": "Delhi",
                "gender_index": 2,
                "flat_house_number": "99887766",
                "house_building_name": "Rose Villa",
                "street": "Green Park",
                "city": "Delhi",
                "country_index": 2,
                "nationality_index": 3,
                "id_type_index": 2,
                "id_no": "12398765",
                "place_of_id_issu_index": 2,
                "id_expiry": "12062030"
            },
            {
                "title_index": 2,
                "first_name": "Oliver",
                "middle_name": "James",
                "last_name": "Davis",
                "dob": "17041980",
                "place_of_birth": "Pune",
                "gender_index": 1,
                "flat_house_number": "44332211",
                "house_building_name": "Skyline Towers",
                "street": "Baner Road",
                "city": "Pune",
                "country_index": 1,
                "nationality_index": 4,
                "id_type_index": 2,
                "id_no": "76543210",
                "place_of_id_issu_index": 1,
                "id_expiry": "17042025"
            },
            {
                "title_index": 1,
                "first_name": "Sophia",
                "middle_name": "Isabella",
                "last_name": "Martinez",
                "dob": "02121985",
                "place_of_birth": "Kolkata",
                "gender_index": 2,
                "flat_house_number": "55667788",
                "house_building_name": "Sunshine Apartments",
                "street": "Park Street",
                "city": "Kolkata",
                "country_index": 4,
                "nationality_index": 5,
                "id_type_index": 1,
                "id_no": "33445566",
                "place_of_id_issu_index": 4,
                "id_expiry": "02122030"
            },
            {
                "title_index": 3,
                "first_name": "Liam",
                "middle_name": "Alexander",
                "last_name": "Garcia",
                "dob": "05101992",
                "place_of_birth": "Ahmedabad",
                "gender_index": 1,
                "flat_house_number": "99887755",
                "house_building_name": "Lakeview Residency",
                "street": "CG Road",
                "city": "Ahmedabad",
                "country_index": 3,
                "nationality_index": 2,
                "id_type_index": 2,
                "id_no": "11224433",
                "place_of_id_issu_index": 3,
                "id_expiry": "05102030"
            },
            {
                "title_index": 2,
                "first_name": "Isabella",
                "middle_name": "Sophia",
                "last_name": "Rodriguez",
                "dob": "07071988",
                "place_of_birth": "Chandigarh",
                "gender_index": 2,
                "flat_house_number": "33221100",
                "house_building_name": "Maple Gardens",
                "street": "Sector 22",
                "city": "Chandigarh",
                "country_index": 1,
                "nationality_index": 3,
                "id_type_index": 2,
                "id_no": "55443322",
                "place_of_id_issu_index": 2,
                "id_expiry": "07072028"
            },
            {
                "title_index": 1,
                "first_name": "William",
                "middle_name": "Henry",
                "last_name": "Lopez",
                "dob": "23031979",
                "place_of_birth": "Lucknow",
                "gender_index": 1,
                "flat_house_number": "77665544",
                "house_building_name": "Heritage Homes",
                "street": "Hazratganj",
                "city": "Lucknow",
                "country_index": 4,
                "nationality_index": 5,
                "id_type_index": 1,
                "id_no": "99887766",
                "place_of_id_issu_index": 4,
                "id_expiry": "23032029"
            }
        ]

        for user in users:
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

            tit.select_by_index(user["title_index"])
            f_name.send_keys(user["first_name"])
            m_name.send_keys(user["middle_name"])
            l_name.send_keys(user["last_name"])
            dob.send_keys(user["dob"])
            pob.clear()
            pob.send_keys(user["place_of_birth"])
            gend.select_by_index(user["gender_index"])
            fh_no.send_keys(user["flat_house_number"])
            hb_name.send_keys(user["house_building_name"])
            street.send_keys(user["street"])
            ci.send_keys(user["city"])
            count.select_by_index(user["country_index"])
            nation.select_by_index(user["nationality_index"])
            id_type.select_by_index(user["id_type_index"])
            id_no.send_keys(user["id_no"])
            pla_of_iss.select_by_index(user["place_of_id_issu_index"])
            id_exp.send_keys(user["id_expiry"])

            self.bod.btn_add_details()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_multiple_beneficial_owners.png")
            assert True

        self.driver.quit()

    def test_add_beneficial_owners_and_check_clear(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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

        # Get values before click on add details
        tit.select_by_index(2)
        f_name.send_keys("Tester")
        m_name.send_keys("QA")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()
        time.sleep(5)

        ti_val = tit.first_selected_option.text
        f_name_val = f_name.get_attribute('value')
        m_name_val = m_name.get_attribute('value')
        l_name_val = l_name.get_attribute('value')
        dob_val = dob.get_attribute('value')
        pob_val = pob.get_attribute('value')
        gend_val = gend.first_selected_option.text
        fh_no_val = fh_no.get_attribute('value')
        hb_name_val = hb_name.get_attribute('value')
        street_val = street.get_attribute('value')
        ci_val = ci.get_attribute('value')
        count_val = count.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        pla_of_iss_val = pla_of_iss.first_selected_option.text
        id_exp_val = id_exp.get_attribute('value')

        print(
            "Before:",
            ti_val,
            f_name_val,
            m_name_val,
            l_name_val,
            dob_val,
            pob_val,
            gend_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            count_val,
            nation_val,
            id_type_val,
            id_no_val,
            pla_of_iss_val,
            id_exp_val)

        self.bod.btn_update()
        self.bod.click_update_bod()
        self.bod.btn_clear()
        # time.sleep(5)

        ti_val_af = tit.first_selected_option.text
        f_name_val_af = f_name.get_attribute('value')
        m_name_val_af = m_name.get_attribute('value')
        l_name_val_af = l_name.get_attribute('value')
        dob_val_af = dob.get_attribute('value')
        pob_val_af = pob.get_attribute('value')
        gend_val_af = gend.first_selected_option.text
        fh_no_val_af = fh_no.get_attribute('value')
        hb_name_val_af = hb_name.get_attribute('value')
        street_val_af = street.get_attribute('value')
        ci_val_af = ci.get_attribute('value')
        count_val_af = count.first_selected_option.text
        nation_val_af = nation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_no_val_af = id_no.get_attribute('value')
        pla_of_iss_val_af = pla_of_iss.first_selected_option.text
        id_exp_val_af = id_exp.get_attribute('value')

        print(
            "After:",
            ti_val_af,
            f_name_val_af,
            m_name_val_af,
            l_name_val_af,
            dob_val_af,
            pob_val_af,
            gend_val_af,
            fh_no_val_af,
            hb_name_val_af,
            street_val_af,
            ci_val_af,
            count_val_af,
            nation_val_af,
            id_type_val_af,
            id_no_val_af,
            pla_of_iss_val_af,
            id_exp_val_af

        )

        time.sleep(5)


        if (ti_val != ti_val_af and f_name_val != f_name_val_af and m_name_val != m_name_val_af and l_name_val != l_name_val_af and
            dob_val != dob_val_af and pob_val != pob_val_af and gend_val != gend_val_af and fh_no_val != fh_no_val and hb_name_val != hb_name_val and
            street_val != street_val_af and ci_val != ci_val_af and count_val != count_val_af and nation_val != nation_val_af and id_type_val != id_type_val and id_no_val != id_no_val and pla_of_iss_val != pla_of_iss_val_af and id_exp_val != id_exp_val_af):

            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_and_check_clear.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_update(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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

        # Get values before click on add details
        tit.select_by_index(2)
        f_name.send_keys("Tester")
        m_name.send_keys("QA")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()
        time.sleep(5)

        ti_val = tit.first_selected_option.text
        f_name_val = f_name.get_attribute('value')
        m_name_val = m_name.get_attribute('value')
        l_name_val = l_name.get_attribute('value')
        dob_val = dob.get_attribute('value')
        pob_val = pob.get_attribute('value')
        gend_val = gend.first_selected_option.text
        fh_no_val = fh_no.get_attribute('value')
        hb_name_val = hb_name.get_attribute('value')
        street_val = street.get_attribute('value')
        ci_val = ci.get_attribute('value')
        count_val = count.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        pla_of_iss_val = pla_of_iss.first_selected_option.text
        id_exp_val = id_exp.get_attribute('value')

        print(
            "Before:",
            ti_val,
            f_name_val,
            m_name_val,
            l_name_val,
            dob_val,
            pob_val,
            gend_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            count_val,
            nation_val,
            id_type_val,
            id_no_val,
            pla_of_iss_val,
            id_exp_val)

        self.bod.btn_update()
        self.bod.click_update_bod()

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

        tit.select_by_index(1)
        f_name.send_keys("Testers")
        m_name.send_keys("QAa")
        l_name.send_keys("Automationn")
        dob.send_keys("20022001")
        pob.send_keys("Keralaa")
        gend.select_by_index(2)
        fh_no.send_keys("124578887")
        hb_name.send_keys("654456657")
        street.send_keys("kochii")
        ci.send_keys("Nelloree")
        count.select_by_index(1)
        nation.select_by_index(2)
        id_type.select_by_index(1)
        id_no.send_keys("21452213")
        pla_of_iss.select_by_index(1)
        id_exp.send_keys("06072009")

        self.bod.btn_update()
        self.bod.click_update_bod()

        ti_val_af = tit.first_selected_option.text
        f_name_val_af = f_name.get_attribute('value')
        m_name_val_af = m_name.get_attribute('value')
        l_name_val_af = l_name.get_attribute('value')
        dob_val_af = dob.get_attribute('value')
        pob_val_af = pob.get_attribute('value')
        gend_val_af = gend.first_selected_option.text
        fh_no_val_af = fh_no.get_attribute('value')
        hb_name_val_af = hb_name.get_attribute('value')
        street_val_af = street.get_attribute('value')
        ci_val_af = ci.get_attribute('value')
        count_val_af = count.first_selected_option.text
        nation_val_af = nation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_no_val_af = id_no.get_attribute('value')
        pla_of_iss_val_af = pla_of_iss.first_selected_option.text
        id_exp_val_af = id_exp.get_attribute('value')

        print(
            "After:",
            ti_val_af,
            f_name_val_af,
            m_name_val_af,
            l_name_val_af,
            dob_val_af,
            pob_val_af,
            gend_val_af,
            fh_no_val_af,
            hb_name_val_af,
            street_val_af,
            ci_val_af,
            count_val_af,
            nation_val_af,
            id_type_val_af,
            id_no_val_af,
            pla_of_iss_val_af,
            id_exp_val_af

        )

        if ti_val != ti_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_ti_val.png")
            assert False

        if f_name_val != f_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_f_name_val.png")
            assert False

        if m_name_val != m_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_m_name_val.png")
            assert False

        if l_name_val != l_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_l_name_val.png")
            assert False

        if dob_val != dob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_dob_val.png")
            assert False

        if pob_val != pob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_pob_val.png")
            assert False

        if gend_val != gend_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_gend_val.png")
            assert False

        if fh_no_val != fh_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_fh_no_val.png")
            assert False

        if hb_name_val != hb_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_hb_name_val.png")
            assert False

        if street_val != street_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_street_val.png")
            assert False

        if ci_val != ci_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_ci_val.png")
            assert False

        if count_val != count_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_count_val.png")
            assert False

        if nation_val != nation_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_nation_val.png")
            assert False

        if id_type_val != id_type_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_type_val.png")
            assert False

        if id_no_val != id_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_no_val.png")
            assert False

        if pla_of_iss_val != pla_of_iss_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_pla_of_iss_val.png")
            assert False

        if id_exp_val != id_exp_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_exp_val.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_update_clear(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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

        # Get values before click on add details
        tit.select_by_index(2)
        f_name.send_keys("Tester")
        m_name.send_keys("QA")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()
        time.sleep(5)

        ti_val = tit.first_selected_option.text
        f_name_val = f_name.get_attribute('value')
        m_name_val = m_name.get_attribute('value')
        l_name_val = l_name.get_attribute('value')
        dob_val = dob.get_attribute('value')
        pob_val = pob.get_attribute('value')
        gend_val = gend.first_selected_option.text
        fh_no_val = fh_no.get_attribute('value')
        hb_name_val = hb_name.get_attribute('value')
        street_val = street.get_attribute('value')
        ci_val = ci.get_attribute('value')
        count_val = count.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        pla_of_iss_val = pla_of_iss.first_selected_option.text
        id_exp_val = id_exp.get_attribute('value')

        print(
            "Before:",
            ti_val,
            f_name_val,
            m_name_val,
            l_name_val,
            dob_val,
            pob_val,
            gend_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            count_val,
            nation_val,
            id_type_val,
            id_no_val,
            pla_of_iss_val,
            id_exp_val)

        self.bod.btn_update()
        self.bod.click_update_bod()

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


        tit.select_by_index(1)
        f_name.clear()
        f_name.send_keys("Karunakar")
        m_name.clear()
        m_name.send_keys("Tester")
        l_name.clear()
        l_name.send_keys("Asus")
        dob.clear()
        dob.send_keys("20022001")
        pob.clear()
        pob.send_keys("Tamilnadu")
        gend.select_by_index(2)
        fh_no.clear()
        fh_no.send_keys("5478415")
        hb_name.clear()
        hb_name.send_keys("1244555")
        street.clear()
        street.send_keys("Ernakulam")
        ci.clear()
        ci.send_keys("Hyderabad")
        count.select_by_index(1)
        nation.select_by_index(2)
        id_type.select_by_index(1)
        id_no.clear()
        id_no.send_keys("784596523")
        pla_of_iss.select_by_index(1)
        id_exp.clear()
        id_exp.send_keys("06072009")

        self.bod.btn_update()
        self.bod.click_update_bod()

        ti_val_af = tit.first_selected_option.text
        f_name_val_af = f_name.get_attribute('value')
        m_name_val_af = m_name.get_attribute('value')
        l_name_val_af = l_name.get_attribute('value')
        dob_val_af = dob.get_attribute('value')
        pob_val_af = pob.get_attribute('value')
        gend_val_af = gend.first_selected_option.text
        fh_no_val_af = fh_no.get_attribute('value')
        hb_name_val_af = hb_name.get_attribute('value')
        street_val_af = street.get_attribute('value')
        ci_val_af = ci.get_attribute('value')
        count_val_af = count.first_selected_option.text
        nation_val_af = nation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_no_val_af = id_no.get_attribute('value')
        pla_of_iss_val_af = pla_of_iss.first_selected_option.text
        id_exp_val_af = id_exp.get_attribute('value')

        print(
            "After:",
            ti_val_af,
            f_name_val_af,
            m_name_val_af,
            l_name_val_af,
            dob_val_af,
            pob_val_af,
            gend_val_af,
            fh_no_val_af,
            hb_name_val_af,
            street_val_af,
            ci_val_af,
            count_val_af,
            nation_val_af,
            id_type_val_af,
            id_no_val_af,
            pla_of_iss_val_af,
            id_exp_val_af

        )

        if ti_val != ti_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_ti_val.png")
            assert False

        if f_name_val != f_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_f_name_val.png")
            assert False

        if m_name_val != m_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_m_name_val.png")
            assert False

        if l_name_val != l_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_l_name_val.png")
            assert False

        if dob_val != dob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_dob_val.png")
            assert False

        if pob_val != pob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_pob_val.png")
            assert False

        if gend_val != gend_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_gend_val.png")
            assert False

        if fh_no_val != fh_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_fh_no_val.png")
            assert False

        if hb_name_val != hb_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_hb_name_val.png")
            assert False

        if street_val != street_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_street_val.png")
            assert False

        if ci_val != ci_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_ci_val.png")
            assert False

        if count_val != count_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_count_val.png")
            assert False

        if nation_val != nation_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_nation_val.png")
            assert False

        if id_type_val != id_type_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_type_val.png")
            assert False

        if id_no_val != id_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_no_val.png")
            assert False

        if pla_of_iss_val != pla_of_iss_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_pla_of_iss_val.png")
            assert False

        if id_exp_val != id_exp_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_update_id_exp_val.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_onlymand_fields(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        # m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        # pla_of_iss = Select(self.bod.place_of_id_issu())
        # id_exp = self.bod.id_expiry()

        tit.select_by_index(2)
        f_name.send_keys("Tester")
        l_name.send_keys("Automation")
        dob.send_keys("20022000")
        pob.send_keys("Kerala")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi")
        ci.send_keys("Nellore")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221")


        self.bod.btn_add_details()

        if self.comp_info.errorMessage() == "Required":
            assert False
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_onlymand_fields.png")
            assert True

        self.driver.quit()

    def test_add_beneficial_owners_nonmand_fields(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        m_name = self.bod.middle_name()
        pla_of_iss = Select(self.bod.place_of_id_issu())
        id_exp = self.bod.id_expiry()

        m_name.send_keys("middle")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("20022001")

        self.bod.btn_add_details()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.execute_script("document.body.scrollHeight")
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_nonmand_fields.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners(self,setup):
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

        self.rg.btn_next()

        # time.sleep(2)
        self.bod.btn_next()
        msg = self.bod.message_info()
        time.sleep(2)

        print(msg.text)

        if msg.text == "Add atleast 1 beneficial owner":
            assert True
        else:
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_spaces(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("Tester Bala")
        m_name.send_keys("QA Senior")
        l_name.send_keys("Automation Tester")
        dob.send_keys("20022000")
        pob.send_keys("Kerala university")
        gend.select_by_index(1)
        fh_no.send_keys("12457888 5432")
        hb_name.send_keys("65445665 4321")
        street.send_keys("kochi airport")
        ci.send_keys("Nellore Dist")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221 0987")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        ti_val = tit.first_selected_option.text
        f_name_val = f_name.get_attribute('value')
        m_name_val = m_name.get_attribute('value')
        l_name_val = l_name.get_attribute('value')
        dob_val = dob.get_attribute('value')
        pob_val = pob.get_attribute('value')
        gend_val = gend.first_selected_option.text
        fh_no_val = fh_no.get_attribute('value')
        hb_name_val = hb_name.get_attribute('value')
        street_val = street.get_attribute('value')
        ci_val = ci.get_attribute('value')
        count_val = count.first_selected_option.text
        nation_val = nation.first_selected_option.text
        id_type_val = id_type.first_selected_option.text
        id_no_val = id_no.get_attribute('value')
        pla_of_iss_val = pla_of_iss.first_selected_option.text
        id_exp_val = id_exp.get_attribute('value')

        print(
            "Before:",
            ti_val,
            f_name_val,
            m_name_val,
            l_name_val,
            dob_val,
            pob_val,
            gend_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            count_val,
            nation_val,
            id_type_val,
            id_no_val,
            pla_of_iss_val,
            id_exp_val)

        self.bod.btn_add_details()
        self.bod.click_update_bod()

        ti_val_af = tit.first_selected_option.text
        f_name_val_af = f_name.get_attribute('value')
        m_name_val_af = m_name.get_attribute('value')
        l_name_val_af = l_name.get_attribute('value')
        dob_val_af = dob.get_attribute('value')
        pob_val_af = pob.get_attribute('value')
        gend_val_af = gend.first_selected_option.text
        fh_no_val_af = fh_no.get_attribute('value')
        hb_name_val_af = hb_name.get_attribute('value')
        street_val_af = street.get_attribute('value')
        ci_val_af = ci.get_attribute('value')
        count_val_af = count.first_selected_option.text
        nation_val_af = nation.first_selected_option.text
        id_type_val_af = id_type.first_selected_option.text
        id_no_val_af = id_no.get_attribute('value')
        pla_of_iss_val_af = pla_of_iss.first_selected_option.text
        id_exp_val_af = id_exp.get_attribute('value')

        print(
            "After:",
            ti_val_af,
            f_name_val_af,
            m_name_val_af,
            l_name_val_af,
            dob_val_af,
            pob_val_af,
            gend_val_af,
            fh_no_val_af,
            hb_name_val_af,
            street_val_af,
            ci_val_af,
            count_val_af,
            nation_val_af,
            id_type_val_af,
            id_no_val_af,
            pla_of_iss_val_af,
            id_exp_val_af

        )

        if ti_val == ti_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if f_name_val == f_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if m_name_val == m_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if l_name_val == l_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if dob_val == dob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if pob_val == pob_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if gend_val == gend_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if fh_no_val == fh_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if hb_name_val == hb_name_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if street_val == street_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if ci_val == ci_val_af:
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if count_val == count_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if nation_val == nation_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if id_type_val == id_type_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if id_no_val == id_no_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if pla_of_iss_val == pla_of_iss_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        if id_exp_val == id_exp_val_af:
            assert True
        else:
            self.driver.save_screenshot(
                screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_spaces_val.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_specialchar_num_char(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        m_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        l_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        dob.send_keys("20022000")
        pob.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        gend.select_by_index(1)
        fh_no.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        hb_name.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        street.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        ci.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("1!@#$%^&*()_+*/{}|]""-[:;',.?a")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            # self.driver.execute_script("window.scrollBy(0, -500);")
            # time.sleep(1)
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_specialchar_num_char.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_numbers(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("123456789")
        m_name.send_keys("123456789")
        l_name.send_keys("1234567890")
        dob.send_keys("20022000")
        pob.send_keys("123456789")
        gend.select_by_index(1)
        fh_no.send_keys("123456789")
        hb_name.send_keys("123456789")
        street.send_keys("123456789")
        ci.send_keys("123456789")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("123456789")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            # self.driver.execute_script("window.scrollBy(0, -500);")
            # time.sleep(1)
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_numbers.png")
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_char(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("qwertyuiop")
        m_name.send_keys("poiuytrewq")
        l_name.send_keys("poiuytrewq")
        dob.send_keys("20022000")
        pob.send_keys("poiuytrewq")
        gend.select_by_index(1)
        fh_no.send_keys("poiuytr")
        hb_name.send_keys("poiuytrewq")
        street.send_keys("poiuytre")
        ci.send_keys("poiuytre")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("poiuytrew")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        self.bod.click_update_bod()

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.execute_script("window.scrollBy(0, 500);")
            # time.sleep(1)
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_with_char.png")
            assert False
        self.driver.quit()

    def test_add_beneficial_owners_with_maxlen(self,setup):
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

        f_name_val = int(f_name.get_attribute('maxlength'))
        m_name_val = int(m_name.get_attribute('maxlength'))
        l_name_val = int(l_name.get_attribute('maxlength'))
        pob_val = int(pob.get_attribute('maxlength'))
        fh_no_val = int(fh_no.get_attribute('maxlength'))
        hb_name_val = int(hb_name.get_attribute('maxlength'))
        street_val = int(street.get_attribute('maxlength'))
        ci_val = int(ci.get_attribute('maxlength'))
        id_no_val = int(id_no.get_attribute('maxlength'))

        print(
            "Max length",
            f_name_val,
            m_name_val,
            l_name_val,
            pob_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            id_no_val
        )

        tit.select_by_index(2)
        f_name.send_keys(random_string_generator_max_30())
        m_name.send_keys(random_string_generator_max_30())
        l_name.send_keys(random_string_generator_max_30())
        dob.send_keys(20022000)
        pob.send_keys(random_string_generator_max_50())
        gend.select_by_index(1)
        fh_no.send_keys(random_string_generator_max_50())
        hb_name.send_keys(random_string_generator_max_50())
        street.send_keys(random_string_generator_max_50())
        ci.send_keys(random_string_generator_max_30())
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys(random_string_generator_numbers_20()+random_string_generator_numbers_10())
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        time.sleep(2)
        self.bod.btn_add_details()
        self.bod.click_update_bod()

        time.sleep(2)
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name = self.bod.last_name()
        pob = self.bod.place_of_birth()
        fh_no = self.bod.flat_house_number()
        hb_name = self.bod.house_building_name()
        street = self.bod.street()
        ci = self.bod.city()
        id_no = self.bod.id_no()

        f_name_af = len(f_name.get_attribute('value'))
        m_name_af = len(m_name.get_attribute('value'))
        l_name_af = len(l_name.get_attribute('value'))
        pob_af = len(pob.get_attribute('value'))
        fh_no_af = len(fh_no.get_attribute('value'))
        hb_name_af = len(hb_name.get_attribute('value'))
        street_af = len(street.get_attribute('value'))
        ci_af = len(ci.get_attribute('value'))
        id_no_af = len(id_no.get_attribute('value'))

        # Assuming you've already located the elements and retrieved their maxlength and current value lengths

        # Compare actual length with maxlength and assert if they are equal

        if f_name_af == f_name_val:
            assert True
        else:
            assert False

        if m_name_af == m_name_val:
            assert True
        else:
            assert False

        if l_name_af == l_name_val:
            assert True
        else:
            assert False

        if pob_af == pob_val:
            assert True
        else:
            assert False

        if fh_no_af == fh_no_val:
            assert True
        else:
            assert False

        if hb_name_af == hb_name_val:
            assert True
        else:
            assert False

        if street_af == street_val:
            assert True
        else:
            assert False

        if ci_af == ci_val:
            assert True
        else:
            assert False

        if id_no_af == id_no_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_maxlen_lessthen(self,setup):
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

        f_name_val = int(f_name.get_attribute('maxlength'))
        m_name_val = int(m_name.get_attribute('maxlength'))
        l_name_val = int(l_name.get_attribute('maxlength'))
        pob_val = int(pob.get_attribute('maxlength'))
        fh_no_val = int(fh_no.get_attribute('maxlength'))
        hb_name_val = int(hb_name.get_attribute('maxlength'))
        street_val = int(street.get_attribute('maxlength'))
        ci_val = int(ci.get_attribute('maxlength'))
        id_no_val = int(id_no.get_attribute('maxlength'))

        print(
            "Max length",
            f_name_val,
            m_name_val,
            l_name_val,
            pob_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            id_no_val
        )

        tit.select_by_index(2)
        f_name.send_keys(random_string_generator_max_28())
        m_name.send_keys(random_string_generator_max_28())
        l_name.send_keys(random_string_generator_max_28())
        dob.send_keys(20022000)
        pob.send_keys(random_string_generator_max_18())
        gend.select_by_index(1)
        fh_no.send_keys(random_string_generator_max_48())
        hb_name.send_keys(random_string_generator_max_48())
        street.send_keys(random_string_generator_max_48())
        ci.send_keys(random_string_generator_max_28())
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys(random_string_generator_numbers_18()+random_string_generator_numbers_10())
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        time.sleep(2)
        self.bod.btn_add_details()
        self.bod.click_update_bod()

        time.sleep(2)
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name = self.bod.last_name()
        pob = self.bod.place_of_birth()
        fh_no = self.bod.flat_house_number()
        hb_name = self.bod.house_building_name()
        street = self.bod.street()
        ci = self.bod.city()
        id_no = self.bod.id_no()

        f_name_af = len(f_name.get_attribute('value'))
        m_name_af = len(m_name.get_attribute('value'))
        l_name_af = len(l_name.get_attribute('value'))
        pob_af = len(pob.get_attribute('value'))
        fh_no_af = len(fh_no.get_attribute('value'))
        hb_name_af = len(hb_name.get_attribute('value'))
        street_af = len(street.get_attribute('value'))
        ci_af = len(ci.get_attribute('value'))
        id_no_af = len(id_no.get_attribute('value'))

        if f_name_af < f_name_val:
            assert True
        else:
            assert False

        if m_name_af < m_name_val:
            assert True
        else:
            assert False

        if l_name_af < l_name_val:
            assert True
        else:
            assert False

        if pob_af < pob_val:
            assert True
        else:
            assert False

        if fh_no_af < fh_no_val:
            assert True
        else:
            assert False

        if hb_name_af < hb_name_val:
            assert True
        else:
            assert False

        if street_af < street_val:
            assert True
        else:
            assert False

        if ci_af < ci_val:
            assert True
        else:
            assert False

        if id_no_af < id_no_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_with_maxlen_graterthen(self,setup):
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

        f_name_val = int(f_name.get_attribute('maxlength'))
        m_name_val = int(m_name.get_attribute('maxlength'))
        l_name_val = int(l_name.get_attribute('maxlength'))
        pob_val = int(pob.get_attribute('maxlength'))
        fh_no_val = int(fh_no.get_attribute('maxlength'))
        hb_name_val = int(hb_name.get_attribute('maxlength'))
        street_val = int(street.get_attribute('maxlength'))
        ci_val = int(ci.get_attribute('maxlength'))
        id_no_val = int(id_no.get_attribute('maxlength'))

        print(
            "Max length",
            f_name_val,
            m_name_val,
            l_name_val,
            pob_val,
            fh_no_val,
            hb_name_val,
            street_val,
            ci_val,
            id_no_val
        )

        tit.select_by_index(2)
        f_name.send_keys(random_string_generator_max_32())
        m_name.send_keys(random_string_generator_max_32())
        l_name.send_keys(random_string_generator_max_32())
        dob.send_keys(20022000)
        pob.send_keys(random_string_generator_max_22())
        gend.select_by_index(1)
        fh_no.send_keys(random_string_generator_max_52())
        hb_name.send_keys(random_string_generator_max_52())
        street.send_keys(random_string_generator_max_52())
        ci.send_keys(random_string_generator_max_32())
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys(random_string_generator_numbers_20()+random_string_generator_numbers_10())
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        time.sleep(2)
        self.bod.btn_add_details()
        self.bod.click_update_bod()

        time.sleep(2)
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name = self.bod.last_name()
        pob = self.bod.place_of_birth()
        fh_no = self.bod.flat_house_number()
        hb_name = self.bod.house_building_name()
        street = self.bod.street()
        ci = self.bod.city()
        id_no = self.bod.id_no()

        f_name_af = len(f_name.get_attribute('value'))
        m_name_af = len(m_name.get_attribute('value'))
        l_name_af = len(l_name.get_attribute('value'))
        pob_af = len(pob.get_attribute('value'))
        fh_no_af = len(fh_no.get_attribute('value'))
        hb_name_af = len(hb_name.get_attribute('value'))
        street_af = len(street.get_attribute('value'))
        ci_af = len(ci.get_attribute('value'))
        id_no_af = len(id_no.get_attribute('value'))

        if f_name_af == f_name_val:
            assert True
        else:
            assert False

        if m_name_af == m_name_val:
            assert True
        else:
            assert False

        if l_name_af == l_name_val:
            assert True
        else:
            assert False

        if pob_af == pob_val:
            assert True
        else:
            assert False

        if fh_no_af == fh_no_val:
            assert True
        else:
            assert False

        if hb_name_af == hb_name_val:
            assert True
        else:
            assert False

        if street_af == street_val:
            assert True
        else:
            assert False

        if ci_af == ci_val:
            assert True
        else:
            assert False

        if id_no_af == id_no_val:
            assert True
        else:
            assert False

        self.driver.quit()

    def test_add_beneficial_owners_spaces(self,setup):
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

        self.rg.btn_next()

        # Assigning BOD

        tit = Select(self.bod.title())
        f_name = self.bod.first_name()
        m_name = self.bod.middle_name()
        l_name =self.bod.last_name()
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
        f_name.send_keys("Tester Test")
        m_name.send_keys("QA QA")
        l_name.send_keys("Automation Engineer")
        dob.send_keys("20022000")
        pob.send_keys("Kerala Stories")
        gend.select_by_index(1)
        fh_no.send_keys("12457888")
        hb_name.send_keys("65445665")
        street.send_keys("kochi street")
        ci.send_keys("Nellore Corporation")
        count.select_by_index(3)
        nation.select_by_index(4)
        id_type.select_by_index(2)
        id_no.send_keys("2145221 35455")
        pla_of_iss.select_by_index(2)
        id_exp.send_keys("06072008")

        self.bod.btn_add_details()
        time.sleep(7)

        if self.comp_info.errorMessage() == "Required":
            assert True
        else:
            self.driver.save_screenshot(screenShort.screen_short() + "BOD_test_add_beneficial_owners_spaces.png")
            assert False

        self.driver.quit()



