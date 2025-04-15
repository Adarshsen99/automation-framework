import string
import time
from random import random

import self
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Pulldownmenu import AML_MENU
from Dinero_automation.pageObjects.AML_MENU.internal_watchlist import Add_new
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.randomString import random_string_generator_max_50
from Dinero_automation.utilities.readProperties import ReadConfig
import pyautogui


class Test_add_new:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_customer_data(self, setup):
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

        # click action for nav bar arrow
        self.aml = AML_MENU(self.driver)

        # Locate the customer pull-down element
        Aml_pull_element = self.driver.find_element(By.XPATH,
                                                    "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[7]/div[1]")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Aml_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        int_watch_element = self.driver.find_element(By.XPATH,
                                                     "//div[normalize-space()='Watch list-Internal']")
        int_watch_element.click()
        time.sleep(2)

        self.an = Add_new(self.driver)

        self.an.create_new().click()
        time.sleep(2)

        title = Select(self.an.title())
        title.select_by_index(1)
        full_name = self.an.full_name()
        full_name.send_keys("chris alias jericho")
        time.sleep(1)
        pyautogui.press('enter')
        dob = self.an.date_of_birtth()
        dob.send_keys("12081989")
        time.sleep(1)
        pyautogui.press('enter')
        state = self.an.state()
        state.send_keys("Kerala")
        time.sleep(1)
        pyautogui.press('enter')
        nationality = self.an.nationality()
        nationality.send_keys("India")
        time.sleep(1)
        pyautogui.press('enter')
        id_num = self.an.id_number()
        id_num.send_keys("54125454")
        time.sleep(1)
        pyautogui.press('enter')
        self.an.action_remarks().send_keys("customer fraud")
        time.sleep(2)

        gender = Select(self.an.gender())
        gender.select_by_index(1)
        alias_name = self.an.alias_name()
        alias_name.send_keys("y2j")
        time.sleep(1)
        pyautogui.press('enter')
        city = self.an.city()
        city.send_keys("Trivandrum")
        time.sleep(1)
        pyautogui.press('enter')
        country_of_residence = self.an.country_of_residence()
        country_of_residence.send_keys("India")
        time.sleep(1)
        pyautogui.press('enter')
        cob = self.an.country_of_birth()
        cob.send_keys("India")
        time.sleep(1)
        pyautogui.press('enter')
        id_type = Select(self.an.id_type())
        id_type.select_by_index(2)
        pep = self.an.is_pep()
        pep.click()
        time.sleep(2)

        self.an.save_btn().click()

    def test_add_multiple_internal_watch(self, setup):
        full_names = ["Priya Sharma", "Liam O'Connor", "Sofia Rodríguez", "Chen Wei",
                    ]
        dates_of_birth = ["25041995", "08072000", "01121989", "30061992",
                          ]

        states = ["Maharashtra", "New York", "Madrid", "Guangdong",
                  ]

        nationalities = [ "Indian", "United States of America", "Spain", "China",
                         ]

        id_numbers = [ "IN456789012", "US987654321", "ES345678901", "CN234567890",
                      ]
        alias_names = ["Pree", "Lio", "Sofi", "Wei", "Mara", "Dan", "Fati", "Carlito", "Em"]
        cities = [ "New York City", "Madrid", "Shenzhen",
                  "Lagos", "Munich", "Dubai", "São Paulo", "Austin"]

        countries_of_residence = ["India", "United States of America", "Spain", "China"]

        countries_of_birth = ["India", "Ireland", "Spain", "China"]

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

        # click action for nav bar arrow
        self.aml = AML_MENU(self.driver)

        # Locate the customer pull-down element
        Aml_pull_element = self.driver.find_element(By.XPATH,
                                                    "/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[7]/div[1]")

        # Hover over the customer pull-down menu
        actions = ActionChains(self.driver)
        actions.move_to_element(Aml_pull_element).perform()

        # Locate and click the "Individual Customers" submenu
        int_watch_element = self.driver.find_element(By.XPATH,
                                                     "//div[normalize-space()='Watch list-Internal']")
        int_watch_element.click()
        time.sleep(2)
        for i in range(4):
            self.an = Add_new(self.driver)

            self.an.create_new().click()
            time.sleep(2)

            title = Select(self.an.title())
            title.select_by_index(1)
            full_name = self.an.full_name()
            full_name.send_keys(full_names[i])
            time.sleep(1)
            pyautogui.press('enter')
            dob = self.an.date_of_birtth()
            dob.send_keys(dates_of_birth[i])
            time.sleep(1)
            pyautogui.press('enter')
            state = self.an.state()
            state.send_keys(states[i])
            time.sleep(1)
            pyautogui.press('enter')
            nationality = self.an.nationality()
            nationality.send_keys(nationalities[i])
            time.sleep(1)
            pyautogui.press('enter')
            id_num = self.an.id_number()
            id_num.send_keys(id_numbers[i])
            time.sleep(1)
            pyautogui.press('enter')
            self.an.action_remarks().send_keys("customer fraud")
            time.sleep(2)

            gender = Select(self.an.gender())
            gender.select_by_index(1)
            alias_name = self.an.alias_name()
            alias_name.send_keys(alias_names[i])
            time.sleep(1)
            pyautogui.press('enter')
            city = self.an.city()
            city.send_keys(cities[i])
            time.sleep(1)
            pyautogui.press('enter')
            country_of_residence = self.an.country_of_residence()
            country_of_residence.send_keys(countries_of_residence[i])
            time.sleep(1)
            pyautogui.press('enter')
            cob = self.an.country_of_birth()
            cob.send_keys(countries_of_birth[i])
            time.sleep(1)
            pyautogui.press('enter')
            id_type = Select(self.an.id_type())
            id_type.select_by_index(2)
            pep = self.an.is_pep()
            pep.click()
            time.sleep(2)

            self.an.save_btn().click()
            time.sleep(3
                       )
