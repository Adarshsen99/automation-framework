import time
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Customer_Registration import Persomal_Information, Contact_Information
from Dinero_automation.utilities.randomString import random_string_generator_max_30,random_string_generator_max_50,random_string_generator_max_28,random_string_generator_max_48,random_string_generator_max_31,random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort

class Test_Personal_Information:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()
    def test_personal_info_with_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        # time.sleep(2)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        # click action for customer registration
        self.nav.click_customer_registration()
        # time.sleep(2)

    #     # perform customer registration actions for id verification
        self.cur = Persomal_Information(self.driver)
        dob = self.cur.click_dob()
        dob.click()

        def select_year_and_month_day(target_year, target_month, target_day):
            # Loop until the desired year and month are displayed
            while True:
                # Assume we can locate the currently displayed year and month
                current_year = 2006 # Get current year element
                current_month = "September" # Get current month element

                # If the displayed month and year match the target, break out of the loop
                if current_year == target_year and current_month == target_month:
                    break

                # If current year is greater than target, click the 'previous' button
                if current_year > target_year or (
                        current_year == target_year and current_month_index(current_month) > current_month_index(
                    target_month)):
                    prev_button = self.cur.dob_previous_button()  # Previous button locator
                    prev_button.click()

                # If current year is less than target, click the 'next' button
                else:
                    next_button = self.cur.dob_next_button()  # Next button locator
                    next_button.click()

            # Once the correct month and year are displayed, select the day
            # Construct XPath based on the target day (assumes day elements are in <td> or similar structure)
            day_element = self.cur.select_date(target_day)  # A method to dynamically find the day element
            day_element.click()

        # Function to convert month names to index (assuming months are displayed as full names, e.g., "September")
        def current_month_index(month_name):
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
            return months.index(month_name) + 1

        # Example Usage: Select September 15, 2005
        select_year_and_month_day(2005, "September", 15)

