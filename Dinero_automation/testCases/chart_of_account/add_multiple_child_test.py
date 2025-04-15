import string
import time
from random import random

from selenium.webdriver.common.by import By
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Chart_of_accounts import adding_account
from Dinero_automation.utilities.randomString import (
    generate_random_email_new, random_string_generator_numbers,
    random_string_generator_numbers_new, random_string_generator_new,
    random_string_generator, random_string_generator_max_30,
    random_string_generator_max_50, generate_random_email,
    random_string_generator_max_28, random_string_generator_max_48,
    random_string_generator_max_31, random_string_generator_max_51
)
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig


class TestSendingDocs:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_docs(self, setup):
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

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")
        # Scroll to the sidebar
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        # List of chart of account XPaths
        chart_of_accounts_xpath = [

            "//body/div[@id='root']/div/div[@class='d-flex']/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/img[1]",
            # Service Revenue
            "//body/div[@id='root']/div/div[contains(@class,'d-flex')]/div[contains(@class,'dir-ltr')]/div[contains(@class,'page-layout')]/div[contains(@class,'justify-content-center')]/form/div[contains(@class,'d-flex flex-row')]/div[contains(@class,'w-50 p-2')]/div[contains(@class,'chartaccounttreecontainer')]/div[contains(@class,'chartaccounttreebody')]/div/div[contains(@class,'grpAndPrmContainer')]/div/div[2]/div[1]/div[3]/img[1]",
            # Interest Income
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[7]/div/div[3]/img",
            # Rental Income
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[9]/div/div[3]/img",
            # Commission Income
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[7]/div/div[3]/img",
            # Cost of Goods Sold
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[8]/div/div[3]/img",
            # Salaries and Wages
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[9]/div/div[3]/img",
            # Rent Expense
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[10]/div/div[3]/img",
            # Utilities Expense
            "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[11]/div/div[3]/img"
            # Marketing and Advertising
        ]

        # List of child account names for each main chart of account
        child_names = [
            "Domestic Sales",  # Child of Sales Revenue
            "Consulting Services",  # Child of Service Revenue
            "Bank Interest",  # Child of Interest Income
            "Office Rental",  # Child of Rental Income
            "Brokerage Commissions",  # Child of Commission Income
            "Direct Material Costs",  # Child of Cost of Goods Sold
            "Employee Salaries",  # Child of Salaries and Wages
            "Office Rent",  # Child of Rent Expense
            "Electricity Expense",  # Child of Utilities Expense
            "Digital Marketing"  # Child of Marketing and Advertising
        ]

        for i in range(len(child_names)):
            # Click on the corresponding chart of account
            self.driver.find_element(By.XPATH, chart_of_accounts_xpath[i]).click()
            time.sleep(2)  # Wait for the action to complete

            # Set account name and Arabic name for each main account
            account_name = child_names[i]
            self.ad.account_name().send_keys(account_name)
            self.ad.arabic_name().send_keys(account_name)  # Arabic name matches account name
            time.sleep(2)

            # Assign the suffix for each account
            self.ad.suffix().send_keys(random_string_generator_numbers(5))
            time.sleep(2)

            # Click save button
            self.ad.save_btn().click()
            time.sleep(2)  # Wait for save action to complete

            # Capture and print document URL
            document = self.driver.execute_cdp_cmd(cmd="DOM.getDocument", cmd_args={})
            print(document['root']['baseURL'])

        self.driver.quit()
