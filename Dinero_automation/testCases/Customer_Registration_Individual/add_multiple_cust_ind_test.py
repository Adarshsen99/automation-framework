import os
import random
import string
from selenium.webdriver.support import expected_conditions as EC

import controller
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait, Select
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information, Id_details, \
    Other_Information, Upload_documents, Final_Preview
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key
from Dinero_automation.pageObjects.Pulldownmenu import CustPulldownmenu

from Dinero_automation.pageObjects.Customer_Registration_Individual_edit import Personal_Information_Edit, \
    Contact_Information_Edit, Id_details_Edit, Add_Beneficiaries_Edit, Add_Delegates_Edit, Other_Information_Edit, \
    Upload_documents_Edit, Final_Preview_Edit
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
import time
from selenium.common import ElementClickInterceptedException, TimeoutException, NoSuchElementException


class TestSendingDocs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_digits(self, length=8):
        return ''.join(random.choices(string.digits, k=length))

    def test_sending_docs(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)
        for i in range(4):
            first_names = ["Ravindran", "Shawn", "Adam", "Jacob"
                           ]

            last_names = ["Michaels", "Henry", "Edge", "Johnson"]

            nationalities = ["India", "Pakistan", "China", "United States of America"]

            responce = []
            # Static sleep to wait for the page to load

            # Initialize page objects
            self.cust = CustPulldownmenu(self.driver)

            # Locate the customer pull-down element
            cust_pull_element = self.driver.find_element(By.XPATH,
                                                         "//div[normalize-space()='Customers & Beneficiaries']")

            # Hover over the customer pull-down menu
            actions = ActionChains(self.driver)
            actions.move_to_element(cust_pull_element).perform()

            # Locate and click the "Individual Customers" submenu
            ind_customer_element = self.driver.find_element(By.XPATH,
                                                            "//div[contains(text(),'Individual Customers')]")
            ind_customer_element.click()
            time.sleep(2)

            # Login

            # Navigate to customer registration

            self.cur = Persomal_Information(self.driver)
            self.cur.click_new()

            self.ci = Contact_Information(self.driver)
            self.id = Id_details(self.driver)
            self.oi = Other_Information(self.driver)
            self.ud = Upload_documents(self.driver)
            self.fp = Final_Preview(self.driver)
            time.sleep(2)
            if not first_names or not last_names:
                print("Ran out of names.")
                break

            fname = first_names.pop(random.randint(0, len(first_names) - 1))  # Remove and pick a random first name
            lname = last_names.pop(random.randint(0, len(last_names) - 1))

            # Personal Information

            dob = 31032000

            self.cur.firstNameField_required(fname)
            self.cur.lastNameField_required(lname)
            self.cur.arabicNameFiels_required(fname[i])
            self.cur.shortNameField_not_required(fname[i])
            self.cur.maidenNameFiels_not_required(fname[i])
            self.cur.dobpicker_required(dob)

            # Dropdown selections
            Select(self.cur.cobDropdown_required()).select_by_index(2)
            nationality = nationalities[i % len(nationalities)]  # Cycle through the list
            Select(self.cur.nationality()).select_by_visible_text(nationality)
            Select(self.cur.citizenship()).select_by_index(2)
            Select(self.cur.countryofresidence()).select_by_visible_text("India")
            Select(self.cur.residentialstatus()).select_by_index(2)
            Select(self.cur.gender()).select_by_index(2)
            Select(self.cur.maritalstatus()).select_by_index(2)
            Select(self.cur.profession()).select_by_index(2)
            self.cur.btnnext()

            # Contact Information
            fh_number = self.generate_random_digits(3)
            hb_name = "Finnest Group"
            stre = "Godavrai"
            cit_dis = "Kalamassery"
            emi_sta = "Kerala"
            mob = self.generate_random_digits(8)

            self.ci.field_fh_num_required(fh_number)
            self.ci.field_hb_name_required(hb_name)
            self.ci.field_street_required(stre)
            self.ci.field_city_dist_required(cit_dis)
            self.ci.field_emin_dist(emi_sta)
            Select(self.ci.drp_country_required()).select_by_visible_text("India")
            Select(self.ci.drp_mobile_required()).select_by_index(69)
            self.ci.field_mobile_required(mob)
            self.ci.field_email_required(first_names[i] + "@finnest.io")
            self.ci.btn_next()

            # ID Details
            Select(self.id.id_type_field_req()).select_by_index(1)
            self.id.place_of_id_issue_field_req().send_keys(nationalities[i])
            self.id.id_number_field_req().send_keys(self.generate_random_digits(8))
            self.id.id_issue_date_dpick_req().send_keys("30042004")
            self.id.id_expaire_date_dpick_req().send_keys("30042025")
            self.id.place_of_passport_isse_drp_req().send_keys("delhi")
            self.id.passport_numb_field_req().send_keys(self.generate_random_digits(6))
            self.id.passport_issue_date_dpick_req().send_keys("30042010")
            self.id.passport_expi_date_dpick_req().send_keys("30052025")

            # Dual Nation
            # self.id.toggle().click()
            # Select(self.id.nationality_drp_req_dual()).select_by_index(3)
            # self.id.place_of_pass_issue_drp_req_dual().send_keys("qatar")
            # self.id.passport_num_req_dual().send_keys(self.generate_random_digits(6))
            # self.id.passport_issue_date_dpick_req_dual().send_keys("30042011")
            # self.id.passport_expai_date_dpick_req_dual().send_keys("30052025")
            self.id.btn_next()

            # Other Information
            self.oi.toggle_other_source_of_income().click()
            Select(self.oi.req_drp_organzation_category()).select_by_index(2)
            Select(self.oi.drp_designation()).select_by_index(2)
            self.oi.employer().send_keys("FINNEST")
            self.oi.employer_description().send_keys("Software")
            Select(self.oi.drp_source_of_income()).select_by_index(1)
            Select(self.oi.drp_salary_range()).select_by_index(2)
            Select(self.oi.drp_purpose()).select_by_index(2)
            self.oi.loyalty_card_no().send_keys(self.generate_random_digits(12))
            Select(self.oi.drp_categoty()).select_by_index(2)
            self.oi.req_points().send_keys("100")

            # Additional details
            #
            Select(self.oi.drp_demographics()).select_by_index(1)
            Select(self.oi.drp_industry_type()).select_by_index(2)
            Select(self.oi.drp_employment()).select_by_index(1)
            Select(self.oi.drp_employee_type()).select_by_index(2)
            self.oi.professional_email().send_keys(first_names[i] + "@finnest.io")
            Select(self.oi.drp_cb_purpose()).select_by_index(2)
            Select(self.oi.drp_customer_nearest_airport()).select_by_index(1)
            self.oi.fax().send_keys(self.generate_random_digits(7))
            Select(self.oi.drp_cusomer_segment()).select_by_index(2)
            Select(self.oi.drp_role()).select_by_index(1)
            self.oi.additional_remarks().send_keys("No remarks")
            self.oi.check_special_needs().click()
            Select(self.oi.drp_details_of_spcial_needs()).select_by_index(2)

            Select(self.oi.drp_application_priority()).select_by_index(2)
            self.oi.whatsapp().send_keys(self.generate_random_digits(7))
            self.oi.facebook().send_keys(first_names[i] + " " + last_names[i])
            self.oi.x().send_keys(first_names[i] + " " + last_names[i])
            self.oi.insta().send_keys(first_names[i] + " " + last_names[i])
            self.oi.linkedin().send_keys(first_names[i] + " " + last_names[i])
            self.oi.website().send_keys("https://example.com/")
            self.oi.institution_name().send_keys("finnest")
            Select(self.oi.drp_institution_type()).select_by_index(2)
            Select(self.oi.drp_mebmership()).select_by_index(2)
            self.oi.check_email().click()
            self.oi.check_sms().click()
            self.oi.check_whatsapp().click()
            self.oi.check_phone().click()
            self.oi.check_fax().click()
            self.oi.check_postid().click()
            self.oi.check_privacy_info().click()
            time.sleep(2)
            self.oi.btn_next().click()

            # Document Upload
            self.ud.passport()
            self.ud.front()
            time.sleep(5)
            keyword = controller
            base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
            file_name = "Screenshot 2024-07-22 162441.png"

            # Create the full path
            full_path = os.path.join(base_dir, file_name)

            # Automate with pyautogui
            pyautogui.click(x=50, y=50)
            time.sleep(4)  # Wait for 4 seconds

            # Write the file path
            pyautogui.write(full_path)
            time.sleep(2)  # Wait for 2 seconds

            # Press enter (fix typo)
            pyautogui.press("enter")
            time.sleep(5)  # Wait for 5 seconds

            self.ud.btn_next()
            time.sleep(4)
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(2)  # Add delay to ensure the element is ready to click
            self.fp.btn_save()
            time.sleep(2)
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

            responce.append(document)
            # for res in responce:
            #     print(res['root']['baseURL'])

        # self.driver.quit()

    def test_finding_nationality(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)
        for i in range(1):
            first_names = ["Ravindran", "Shawn", "Mark", "Orton", "Adam"
                           ]

            last_names = ["Pillai", "Michaels", "Henry", "Randy", "Edge"]

            nationalities = ["India", "Pakistan", "China", "United States of America"]

            responce = []
            # Static sleep to wait for the page to load

            # Initialize page objects
            self.cust = CustPulldownmenu(self.driver)

            # Locate the customer pull-down element
            cust_pull_element = self.driver.find_element(By.XPATH,
                                                         "//div[normalize-space()='Customers & Beneficiaries']")

            # Hover over the customer pull-down menu
            actions = ActionChains(self.driver)
            actions.move_to_element(cust_pull_element).perform()

            # Locate and click the "Individual Customers" submenu
            ind_customer_element = self.driver.find_element(By.XPATH,
                                                            "//div[contains(text(),'Individual Customers')]")
            ind_customer_element.click()

            # Login

            # Navigate to customer registration

            self.cur = Persomal_Information(self.driver)
            self.cur.click_new()

            self.ci = Contact_Information(self.driver)
            self.id = Id_details(self.driver)
            self.oi = Other_Information(self.driver)
            self.ud = Upload_documents(self.driver)
            self.fp = Final_Preview(self.driver)
            time.sleep(2)
            if not first_names or not last_names:
                print("Ran out of names.")
                break

            fname = first_names.pop(random.randint(0, len(first_names) - 1))  # Remove and pick a random first name
            lname = last_names.pop(random.randint(0, len(last_names) - 1))

            # Personal Information

            arbname = first_names.pop(random.randint(0, len(first_names) - 1))
            shname = first_names.pop(random.randint(0, len(first_names) - 1))
            mainame = first_names.pop(random.randint(0, len(first_names) - 1))
            dob = 31032000

            self.drp = Select(self.cur.titleDropdown_required())
            time.sleep(2)
            self.drp.select_by_index(1)
            self.cur.firstNameField_required(fname)
            self.cur.lastNameField_required(lname)
            self.cur.arabicNameFiels_required(arbname)
            self.cur.shortNameField_not_required(shname)
            self.cur.maidenNameFiels_not_required(mainame)
            self.cur.dobpicker_required(dob)

            # Dropdown selections
            Select(self.cur.cobDropdown_required()).select_by_index(2)
            nationality = nationalities[i % len(nationalities)]  # Cycle through the list
            Select(self.cur.nationality()).select_by_visible_text(nationality)
            Select(self.cur.citizenship()).select_by_index(2)
            Select(self.cur.countryofresidence()).select_by_visible_text("India")
            Select(self.cur.residentialstatus()).select_by_index(2)
            Select(self.cur.gender()).select_by_index(2)
            Select(self.cur.maritalstatus()).select_by_index(2)
            Select(self.cur.profession()).select_by_index(2)
            dropdown = Select(self.cur.nationality())  # Replace with your actual dropdown locator

            # Get all nationality options
            nationalities = [option.text for option in dropdown.options]

            # Print the full list
            print("List of Nationalities:")
            for nationality in nationalities:
                print(nationality)
            self.cur.btnnext()

    def test_edd_external_watch_customers(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)
        for i in range(4):
            first_names = ["Petar", "Vladimir", "Manuel Helder", "Mahmud"
                           ]

            last_names = ["DJOKIC", "FILIPPOV", "VIEIRA DIAS", "HOJATI NAJAFABADI"]

            dates_of_birth = ["29071961", "15041951", "10101955", "01121989"
                              ]

            street = ["California", "Maharashtra", "New York", "Madrid"
                      ]

            nationalities = ["Bosnia & Herzegovina", "Russia", "Angola", "Iran"
                             ]

            id_numbers = ["{US-OSDN}4636822", "{RU-INN}772822436164", "{US-OSDN}34132229", "ES345678901"
                          ]

            cities = ["~ Banja Luka", " Moscow", "Luanda", "Tehran"]

            countries_of_residence = ["Bosnia & Herzegovina", "Russia", "Angola", "Iran"]

            countries_of_birth = ["Bosnia & Herzegovina", "Russia", "Angola", "Iran"]

            responce = []
            # Static sleep to wait for the page to load

            # Initialize page objects
            self.cust = CustPulldownmenu(self.driver)

            # Locate the customer pull-down element
            cust_pull_element = self.driver.find_element(By.XPATH,
                                                         "//div[normalize-space()='Customers & Beneficiaries']")

            # Hover over the customer pull-down menu
            actions = ActionChains(self.driver)
            actions.move_to_element(cust_pull_element).perform()

            # Locate and click the "Individual Customers" submenu
            ind_customer_element = self.driver.find_element(By.XPATH,
                                                            "//div[contains(text(),'Individual Customers')]")
            ind_customer_element.click()
            time.sleep(2)

            # Login

            # Navigate to customer registration

            self.cur = Persomal_Information(self.driver)
            self.cur.click_new()

            self.ci = Contact_Information(self.driver)
            self.id = Id_details(self.driver)
            self.oi = Other_Information(self.driver)
            self.ud = Upload_documents(self.driver)
            self.fp = Final_Preview(self.driver)
            time.sleep(2)
            if not first_names or not last_names:
                print("Ran out of names.")
                break



            # Personal Information

            self.cur.firstNameField_required(first_names[i])
            self.cur.lastNameField_required(last_names[i])
            self.cur.arabicNameFiels_required(first_names[i])
            self.cur.shortNameField_not_required(first_names[i])
            self.cur.maidenNameFiels_not_required(first_names[i])
            self.cur.dobpicker_required(dates_of_birth[i])

            # Dropdown selections

            Select(self.cur.cobDropdown_required()).select_by_visible_text(countries_of_birth[i])
              # Cycle through the list
            Select(self.cur.nationality()).select_by_visible_text(nationalities[i])
            Select(self.cur.citizenship()).select_by_index(2)

            Select(self.cur.countryofresidence()).select_by_visible_text(countries_of_residence[i])
            Select(self.cur.residentialstatus()).select_by_index(2)
            Select(self.cur.gender()).select_by_index(2)
            Select(self.cur.maritalstatus()).select_by_index(2)
            Select(self.cur.profession()).select_by_index(2)
            self.cur.btnnext()

            # Contact Information
            fh_number = self.generate_random_digits(3)
            hb_name = "Finnest Group"

            emi_sta = "Kerala"
            mob = self.generate_random_digits(8)

            self.ci.field_fh_num_required(fh_number)
            self.ci.field_hb_name_required(hb_name)
            self.ci.field_street_required(street[i])
            self.ci.field_city_dist_required(cities[i])
            self.ci.field_emin_dist(emi_sta)
            Select(self.ci.drp_country_required()).select_by_visible_text("India")
            Select(self.ci.drp_mobile_required()).select_by_index(69)
            self.ci.field_mobile_required(mob)
            self.ci.field_email_required(first_names[i] + "@squad.io")
            self.ci.btn_next()

            # ID Details
            Select(self.id.id_type_field_req()).select_by_index(1)
            self.id.place_of_id_issue_field_req().send_keys(nationalities[i])
            self.id.id_number_field_req().send_keys(id_numbers[i])
            self.id.id_issue_date_dpick_req().send_keys("30042004")
            self.id.id_expaire_date_dpick_req().send_keys("30042025")
            self.id.place_of_passport_isse_drp_req().send_keys("delhi")
            self.id.passport_numb_field_req().send_keys(self.generate_random_digits(6))
            self.id.passport_issue_date_dpick_req().send_keys("30042010")
            self.id.passport_expi_date_dpick_req().send_keys("30052025")


            self.id.btn_next()

            # Other Information
            self.oi.toggle_other_source_of_income().click()
            Select(self.oi.req_drp_organzation_category()).select_by_index(2)
            Select(self.oi.drp_designation()).select_by_index(2)
            self.oi.employer().send_keys("FINNEST")
            self.oi.employer_description().send_keys("Software")
            Select(self.oi.drp_source_of_income()).select_by_index(1)
            Select(self.oi.drp_salary_range()).select_by_index(2)
            Select(self.oi.drp_purpose()).select_by_index(2)
            self.oi.loyalty_card_no().send_keys(self.generate_random_digits(12))
            Select(self.oi.drp_categoty()).select_by_index(2)
            self.oi.req_points().send_keys("100")

            # Additional details
            #
            Select(self.oi.drp_demographics()).select_by_index(1)
            Select(self.oi.drp_industry_type()).select_by_index(2)
            Select(self.oi.drp_employment()).select_by_index(1)
            Select(self.oi.drp_employee_type()).select_by_index(2)
            self.oi.professional_email().send_keys(first_names[i] + "@assasin.io")
            Select(self.oi.drp_cb_purpose()).select_by_index(2)
            Select(self.oi.drp_customer_nearest_airport()).select_by_index(1)
            self.oi.fax().send_keys(self.generate_random_digits(7))
            Select(self.oi.drp_cusomer_segment()).select_by_index(2)
            Select(self.oi.drp_role()).select_by_index(1)
            self.oi.additional_remarks().send_keys("No remarks")
            self.oi.check_special_needs().click()
            Select(self.oi.drp_details_of_spcial_needs()).select_by_index(2)

            Select(self.oi.drp_application_priority()).select_by_index(2)
            self.oi.whatsapp().send_keys(self.generate_random_digits(7))
            self.oi.facebook().send_keys(first_names[i] + " " + last_names[i])
            self.oi.x().send_keys(first_names[i] + " " + last_names[i])
            self.oi.insta().send_keys(first_names[i] + " " + last_names[i])
            self.oi.linkedin().send_keys(first_names[i] + " " + last_names[i])
            self.oi.website().send_keys("https://example.com/")
            self.oi.institution_name().send_keys("Terrorist ")
            Select(self.oi.drp_institution_type()).select_by_index(2)
            Select(self.oi.drp_mebmership()).select_by_index(2)
            self.oi.check_email().click()
            self.oi.check_sms().click()
            self.oi.check_whatsapp().click()
            self.oi.check_phone().click()
            self.oi.check_fax().click()
            self.oi.check_postid().click()
            self.oi.check_privacy_info().click()
            time.sleep(2)
            self.oi.btn_next().click()

            # Document Upload
            self.ud.passport()
            self.ud.front()
            time.sleep(5)
            keyword = controller
            base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
            file_name = "Screenshot 2024-07-22 162441.png"

            # Create the full path
            full_path = os.path.join(base_dir, file_name)

            # Automate with pyautogui
            pyautogui.click(x=50, y=50)
            time.sleep(4)  # Wait for 4 seconds

            # Write the file path
            pyautogui.write(full_path)
            time.sleep(2)  # Wait for 2 seconds

            # Press enter (fix typo)
            pyautogui.press("enter")
            time.sleep(5)  # Wait for 5 seconds

            self.ud.btn_next()
            time.sleep(4)
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(2)  # Add delay to ensure the element is ready to click
            self.fp.btn_save()
            time.sleep(2)
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

            responce.append(document)

    def test_add_customers_internal_watch(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)
        for i in range(4):
            first_names = [   'Sofia', 'Chen']

            last_names = [ 'Rodríguez', 'Wei']

            dates_of_birth = [  "01121989", "30061992",
                              ]

            states = [ "Madrid", "Guangdong",
                      ]

            nationalities = ["Spain", "China",
                             ]

            id_numbers = [  "ES345678901", "CN234567890",
                          ]

            cities = [ "Madrid", "Shenzhen"]

            countries_of_residence = [ "Spain", "China"]

            countries_of_birth = [  "Spain", "China"]

            responce = []
            # Static sleep to wait for the page to load

            # Initialize page objects
            self.cust = CustPulldownmenu(self.driver)

            # Locate the customer pull-down element
            cust_pull_element = self.driver.find_element(By.XPATH,
                                                         "//div[normalize-space()='Customers & Beneficiaries']")

            # Hover over the customer pull-down menu
            actions = ActionChains(self.driver)
            actions.move_to_element(cust_pull_element).perform()

            # Locate and click the "Individual Customers" submenu
            ind_customer_element = self.driver.find_element(By.XPATH,
                                                            "//div[contains(text(),'Individual Customers')]")
            ind_customer_element.click()
            time.sleep(2)

            # Login

            # Navigate to customer registration

            self.cur = Persomal_Information(self.driver)
            self.cur.click_new()

            self.ci = Contact_Information(self.driver)
            self.id = Id_details(self.driver)
            self.oi = Other_Information(self.driver)
            self.ud = Upload_documents(self.driver)
            self.fp = Final_Preview(self.driver)
            time.sleep(2)
            if not first_names or not last_names:
                print("Ran out of names.")
                break

            # Personal Information

            self.cur.firstNameField_required(first_names[i])
            self.cur.lastNameField_required(last_names[i])
            self.cur.arabicNameFiels_required(first_names[i])
            self.cur.shortNameField_not_required(first_names[i])
            self.cur.maidenNameFiels_not_required(first_names[i])
            self.cur.dobpicker_required(dates_of_birth[i])

            # Dropdown selections

            Select(self.cur.cobDropdown_required()).select_by_visible_text(countries_of_birth[i])
            # Cycle through the list
            Select(self.cur.nationality()).select_by_visible_text(nationalities[i])
            Select(self.cur.citizenship()).select_by_index(2)

            Select(self.cur.countryofresidence()).select_by_visible_text(countries_of_residence[i])
            Select(self.cur.residentialstatus()).select_by_index(2)
            Select(self.cur.gender()).select_by_index(2)
            Select(self.cur.maritalstatus()).select_by_index(2)
            Select(self.cur.profession()).select_by_index(2)
            self.cur.btnnext()

            # Contact Information
            fh_number = self.generate_random_digits(3)
            hb_name = "Finnest Group"
            street = "jam"

            mob = self.generate_random_digits(8)

            self.ci.field_fh_num_required(fh_number)
            self.ci.field_hb_name_required(hb_name)
            self.ci.field_street_required(street)
            self.ci.field_city_dist_required(cities[i])
            self.ci.field_emin_dist(states[i])
            Select(self.ci.drp_country_required()).select_by_visible_text("India")
            Select(self.ci.drp_mobile_required()).select_by_index(69)
            self.ci.field_mobile_required(mob)
            self.ci.field_email_required(first_names[i] + "@squad.io")
            self.ci.btn_next()

            # ID Details
            Select(self.id.id_type_field_req()).select_by_index(2)
            self.id.place_of_id_issue_field_req().send_keys(nationalities[i])
            self.id.id_number_field_req().send_keys(id_numbers[i])
            self.id.id_issue_date_dpick_req().send_keys("30042004")
            self.id.id_expaire_date_dpick_req().send_keys("30042025")
            self.id.place_of_passport_isse_drp_req().send_keys("delhi")
            self.id.passport_numb_field_req().send_keys(self.generate_random_digits(6))
            self.id.passport_issue_date_dpick_req().send_keys("30042010")
            self.id.passport_expi_date_dpick_req().send_keys("30052025")

            self.id.btn_next()

            # Other Information
            self.oi.toggle_other_source_of_income().click()
            Select(self.oi.req_drp_organzation_category()).select_by_index(2)
            Select(self.oi.drp_designation()).select_by_index(2)
            self.oi.employer().send_keys("FINNEST")
            self.oi.employer_description().send_keys("Software")
            Select(self.oi.drp_source_of_income()).select_by_index(1)
            Select(self.oi.drp_salary_range()).select_by_index(2)
            Select(self.oi.drp_purpose()).select_by_index(2)
            self.oi.loyalty_card_no().send_keys(self.generate_random_digits(12))
            Select(self.oi.drp_categoty()).select_by_index(2)
            self.oi.req_points().send_keys("100")

            # Additional details
            #
            Select(self.oi.drp_demographics()).select_by_index(1)
            Select(self.oi.drp_industry_type()).select_by_index(2)
            Select(self.oi.drp_employment()).select_by_index(1)
            Select(self.oi.drp_employee_type()).select_by_index(2)
            self.oi.professional_email().send_keys(first_names[i] + "@assasin.io")
            Select(self.oi.drp_cb_purpose()).select_by_index(2)
            Select(self.oi.drp_customer_nearest_airport()).select_by_index(1)
            self.oi.fax().send_keys(self.generate_random_digits(7))
            Select(self.oi.drp_cusomer_segment()).select_by_index(2)
            Select(self.oi.drp_role()).select_by_index(1)
            self.oi.additional_remarks().send_keys("No remarks")
            self.oi.check_special_needs().click()
            Select(self.oi.drp_details_of_spcial_needs()).select_by_index(2)

            Select(self.oi.drp_application_priority()).select_by_index(2)
            self.oi.whatsapp().send_keys(self.generate_random_digits(7))
            self.oi.facebook().send_keys(first_names[i] + " " + last_names[i])
            self.oi.x().send_keys(first_names[i] + " " + last_names[i])
            self.oi.insta().send_keys(first_names[i] + " " + last_names[i])
            self.oi.linkedin().send_keys(first_names[i] + " " + last_names[i])
            self.oi.website().send_keys("https://example.com/")
            self.oi.institution_name().send_keys("Terrorist ")
            Select(self.oi.drp_institution_type()).select_by_index(2)
            Select(self.oi.drp_mebmership()).select_by_index(2)
            self.oi.check_email().click()
            self.oi.check_sms().click()
            self.oi.check_whatsapp().click()
            self.oi.check_phone().click()
            self.oi.check_fax().click()
            self.oi.check_postid().click()
            self.oi.check_privacy_info().click()
            time.sleep(2)
            self.oi.btn_next().click()

            # Document Upload
            self.ud.passport()
            self.ud.front()
            time.sleep(5)
            keyword = controller
            base_dir = "C:\\Users\\adars\\OneDrive\\Pictures\\Screenshots"
            file_name = "Screenshot 2024-07-22 162441.png"

            # Create the full path
            full_path = os.path.join(base_dir, file_name)

            # Automate with pyautogui
            pyautogui.click(x=50, y=50)
            time.sleep(4)  # Wait for 4 seconds

            # Write the file path
            pyautogui.write(full_path)
            time.sleep(2)  # Wait for 2 seconds

            # Press enter (fix typo)
            pyautogui.press("enter")
            time.sleep(5)  # Wait for 5 seconds

            self.ud.btn_next()
            time.sleep(4)
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(2)  # Add delay to ensure the element is ready to click
            # self.fp.btn_save()
            time.sleep(3)
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})

            self.fp.btn_save()
            time.sleep(2)

            responce.append(document)
