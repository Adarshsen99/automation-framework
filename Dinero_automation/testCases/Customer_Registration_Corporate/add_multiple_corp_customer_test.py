import os

from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
import random
import string
import time

import controller
import pyautogui
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib3.exceptions import MaxRetryError

from DineroQa.Dinero_automation.utilities.randomString import random_string_generator_numbers_18, \
    random_string_generator_max_28, random_string_generator_max_31, random_string_generator_numbers
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Customer_Registration_Corporate import Company_Information, Registration_Details, \
    Beneficial_Owners_Details, Upload_Documents
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig

from selenium import webdriver


def generate_random_digits(length=8):
    return ''.join(random.choices(string.digits, k=length))


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_random_email():
    return generate_random_string(5) + "@example.com"


class Test_sending_docs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_add_documents(self, setup):
        # Sample data
        company_names = [


            
            "Atlas Construction Group"
        ]

        building_names = [
            "Maplewood", "Silverbrook", "Ridgeview", "Eastwood",
            "Brightwater", "Greenfield", "Stonebridge", "Westvale", "Clearwater"
        ]

        cities = [
            "Rivertown", "Crestwood", "Maple Valley", "Oceanview",
            "Silver Springs", "Pinehill", "Amberfield", "Sunridge", "Greenleaf"
        ]

        authorized_persons = [
            "Alice Johnson", "David Smith", "Maria Garcia", "James Brown",
            "Linda Wilson", "Michael Taylor", "Elizabeth Davis", "Robert Martinez", "Patricia Anderson"
        ]

        beneficiary_owners = [
            "Emma Clark", "Liam Johnson", "Sophia Lewis", "Noah Walker",
            "Olivia Hall", "Elijah Allen", "Ava Young", "Lucas Hernandez", "Mia King"
        ]

        # Loop through each company registration

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        # Navigate to Customer Registration
        self.nav = Navigation_Page(self.driver)

        for i in range(3):
            self.nav.click_navbar()
            self.nav.click_customer_registration_corporate()

            # Assigning submodules
            self.comp_info = Company_Information(self.driver)
            self.rg = Registration_Details(self.driver)
            self.bod = Beneficial_Owners_Details(self.driver)
            self.ud = Upload_Documents(self.driver)

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

            # Fill in the company information
            comp_name.send_keys(company_names[i])
            ara_name.send_keys(company_names[i])
            build_num.send_keys(random_string_generator_numbers(5))
            build_name.send_keys(building_names[i])
            stree.send_keys(random_string_generator_max_28())
            post.send_keys(random_string_generator_numbers(6))
            distc.send_keys(cities[i])
            drp_country.select_by_index(4 + i % len(drp_country.options))  # Prevent out of range
            drp_mob.select_by_index(2 + i % len(drp_mob.options))  # Prevent out of range
            numb.send_keys(random_string_generator_numbers(10))
            mail.send_keys(generate_random_email())
            time.sleep(2)

            self.comp_info.btn_next()  # Click the next button to proceed

            # Fill in registration details
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

            # Fill in registration details
            coun_of_incorp.select_by_index(2)
            lice_natu.select_by_index(2)
            ent_type.select_by_index(1)
            oper.select_by_index(2)
            tr_servi_sect.select_by_index(2)
            capital.send_keys("20000")
            reg_pur.send_keys("Testing")
            est_an_income.send_keys("30000")
            auth_per.send_keys(authorized_persons[i])
            designat.select_by_index(2)
            nation.select_by_index(i + 6)
            id_type.select_by_index(2)
            id_no.send_keys(random_string_generator_numbers(6))
            id_exp.send_keys("20032004")
            cr_no.send_keys(random_string_generator_numbers(5))
            comp_card_no.send_keys(random_string_generator_numbers(6))
            cr_iss_dat.send_keys("20032004")
            cr_exp_dat.send_keys("20032014")
            cc_iss_date.send_keys("20032006")
            cc_exp_dat.send_keys("20032026")
            time.sleep(2)

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
            perc_hol = Select(self.bod.perc_hold())

            # Fill in BOD details
            tit.select_by_index(2)
            f_name.send_keys(beneficiary_owners[i])
            m_name.send_keys("QA")
            l_name.send_keys("Automation")
            dob.send_keys("20022000")
            pob.send_keys("Kerala")
            gend.select_by_index(1)
            fh_no.send_keys(random_string_generator_numbers(5))
            hb_name.send_keys(random_string_generator_numbers(5))
            street.send_keys(cities[i])
            ci.send_keys(random_string_generator_max_28())
            count.select_by_index(3)
            nation.select_by_index(4)
            id_type.select_by_index(2)
            id_no.send_keys(random_string_generator_numbers(8))
            pla_of_iss.select_by_index(2)
            id_exp.send_keys("06072008")
            perc_hol.select_by_index(65)
            time.sleep(1)

            self.bod.btn_add_details()
            time.sleep(2)
            self.bod.btn_next()

            # Upload document
            self.ud.click_muncipal()
            element = self.ud.send_front()
            element.click()

            base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
            file_name = "Screenshot 2024-07-22 162441.png"
            full_path = os.path.join(base_dir, file_name)
            time.sleep(2)

            # Use PyAutoGUI to handle file dialog
            pyautogui.click(100, 50)  # Adjust coordinates as necessary
            time.sleep(4)
            pyautogui.write(full_path)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(3)

            self.ud.btn_next()
            time.sleep(2)
            self.ud.btn_save()
            time.sleep(4)

            # Get response from the document
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
            print(document)  # You can adjust this as needed

        self.driver.quit()
