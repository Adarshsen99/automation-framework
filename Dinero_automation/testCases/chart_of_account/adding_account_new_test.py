import string
import time

from random import random

from selenium.webdriver.common.by import By

from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Chart_of_accounts import adding_account
from Dinero_automation.utilities.randomString import generate_random_email_new, random_string_generator_numbers, \
    random_string_generator_numbers_new, random_string_generator_new, random_string_generator, \
    random_string_generator_max_30, random_string_generator_max_50, generate_random_email, \
    random_string_generator_max_28, random_string_generator_max_48, random_string_generator_max_31, \
    random_string_generator_max_51
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities import screenShort
from Dinero_automation.utilities.readProperties import ReadConfig


class Test_adding_account:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    def test_sending_valid_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,100);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys("store")
        self.ad.arabic_name().send_keys("Purchase")
        time.sleep(2)
        self.ad.suffix().send_keys("322258225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.save_btn().click()

        save_messg = self.ad.save_messege()
        print(save_messg)

        if save_messg == "New chart of accounts added":
            assert True
        else:
            assert False

    def test_without_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,100);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        # self.ad.account_name().send_keys("store")
        # self.ad.arabic_name().send_keys("Purchase")
        # time.sleep(2)
        # self.ad.suffix().send_keys("322258225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.save_btn().click()

        error_messg = self.ad.error_messege()
        print(error_messg)

        if error_messg == "Required":
            assert True
        else:
            assert False

    def test_sending_invalid_data(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,100);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys("5448485484")
        self.ad.arabic_name().send_keys("654564654")
        time.sleep(2)
        self.ad.suffix().send_keys("dfaasasds")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.save_btn().click()

        error_messg = self.ad.error_messege()
        print(error_messg)

        if error_messg == "Required":
            assert True
        else:
            assert False

    def test_sending_spl_char_num_alph(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,300);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys("50!@#$%^&*()_+={}|:'""><.,?aev")
        self.ad.arabic_name().send_keys("50!@#$%^&*()_+={}|:'""><.,?aev")
        time.sleep(2)
        self.ad.suffix().send_keys("50!@#$%^&*()_+={}|:'""><.,?aev")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.save_btn().click()

        error_messg = self.ad.error_messege()
        print(error_messg)

        if error_messg == "Required":
            assert True
        else:
            assert False

    def test_maximum_length(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,300);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys(random_string_generator_numbers(100))
        self.ad.arabic_name().send_keys(random_string_generator_numbers(100))
        time.sleep(2)
        self.ad.suffix().send_keys(random_string_generator_numbers(100))

        time.sleep(3)

        account_name_value = self.ad.account_name().get_attribute("value")
        arabic_name_value = self.ad.arabic_name().get_attribute("value")
        print("Account Name:", account_name_value)
        print("Arabic Name:", arabic_name_value)

        # Print the WebElement itself (if needed for debugging)
        print("Account Name Element:", self.ad.account_name())

        # Retrieve and print the values of account number and parent account
        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")
        print("Account Number:", acc_number)
        print("Parent Account:", parent_acc)

        # Retrieve and print the maxlength attributes
        account_name_maxlength = self.ad.account_name().get_attribute("maxlength")
        arabic_name_maxlength = self.ad.arabic_name().get_attribute("maxlength")
        suffix_maxlength = self.ad.suffix().get_attribute("maxlength")  # Assuming suffix is part of self.ad

        print("Account Name Maxlength:", account_name_maxlength)
        print("Arabic Name Maxlength:", arabic_name_maxlength)
        print("Suffix Maxlength:", suffix_maxlength)

        error_messg = self.ad.error_messege()
        print(error_messg)

    def test_validating_Gl_coount_data(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,200);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys("Cabinet")
        self.ad.arabic_name().send_keys("Purchase")
        time.sleep(2)
        self.ad.suffix().send_keys("322646258225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.is_gl_acc().click()
        time.sleep(2)

        self.ad.fc_account().click()
        currency = Select(self.ad.drp_currency())
        currency.select_by_index(1)

        self.ad.rate().send_keys("3")

        self.ad.journal_voucher().click()

        self.ad.petty_cash().click()

        self.ad.receipt_voucher().click()

        self.ad.save_btn().click()

        save_messg = self.ad.save_messege()
        print(save_messg)

        if save_messg == "New chart of accounts added":
            assert True
        else:
            assert False

    def test_no_data_gl_account(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        new_btn = self.ad.new_btn()
        self.driver.execute_script("arguments[0].scrollIntoView(0,200);", new_btn)

        # Optionally, interact with the element after scrolling into view
        new_btn.click()

        time.sleep(2)
        self.ad.account_name().send_keys("Cabinet")
        self.ad.arabic_name().send_keys("Purchase")
        time.sleep(2)
        self.ad.suffix().send_keys("32264622258225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.is_gl_acc().click()
        time.sleep(2)

        # self.ad.fc_account().click()
        # currency = Select(self.ad.drp_currency())
        # currency.select_by_index(1)
        #
        # self.ad.rate().send_keys("3")
        #
        # self.ad.journal_voucher().click()
        #
        # self.ad.petty_cash().click()
        #
        # self.ad.receipt_voucher().click()
        #
        self.ad.save_btn().click()

        save_messg = self.ad.save_messege()
        print(save_messg)

        if save_messg == "New chart of accounts added":
            assert True
        else:
            assert False

    def test_deleting_a_chart_of_acct(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)
        #
        # new_btn = self.ad.new_btn()
        # self.driver.execute_script("arguments[0].scrollIntoView(0,100);", new_btn)
        #
        # # Optionally, interact with the element after scrolling into view
        # new_btn.click()
        #
        # time.sleep(2)
        # self.ad.account_name().send_keys("Dominozz")
        # self.ad.arabic_name().send_keys("Dominozz")
        # time.sleep(2)
        # self.ad.suffix().send_keys("300008225")
        # time.sleep(3)
        #
        # acc_number = self.ad.account_num().get_attribute("value")
        # parent_acc = self.ad.parent_account().get_attribute("value")
        #
        # print("acc_number:", acc_number)
        # print("parent_acc:", parent_acc)
        #
        # self.ad.save_btn().click()
        #
        # save_messg = self.ad.save_messege()
        # print(save_messg)

        deleting_chart_element = self.driver.find_element(By.XPATH,
                                                          "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[15]/div/div[2]")
        deleting_chart_element.click()

        time.sleep(2)

        self.ad.delete_btn().click()

    def test_updating_chart_of_accnt(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        updating_chart_element = self.driver.find_element(By.XPATH,

                                                          "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[16]/div/div[2]")
        time.sleep(1)
        updating_chart_element.click()
        time.sleep(2)

        acc_name_ = self.ad.account_name().get_attribute("value")
        print(acc_name_)

        arabic_name = self.ad.arabic_name().get_attribute("value")
        print(arabic_name)

        suffix = self.ad.suffix().get_attribute("value")
        print(suffix)

        acc_num = self.ad.account_num().get_attribute("value")
        print(acc_num)

        time.sleep(2)

        self.ad.updte_btn().click()

        time.sleep(2)
        print("values after updating")

        acc_name_2 = self.ad.account_name().get_attribute("value")
        print(acc_name_2)

        arabic_name2 = self.ad.arabic_name().get_attribute("value")
        print(arabic_name2)

        suffix2 = self.ad.suffix().get_attribute("value")
        print(suffix2)

        acc_num2 = self.ad.account_num().get_attribute("value")
        print(acc_num2)

        time.sleep(2)

        self.ad.updte_btn().click()

        if acc_name_ == acc_name_2:
            assert True
        else:
            assert False

        if acc_num == acc_num2:
            assert True
        else:
            assert False

        if arabic_name == arabic_name2:
            assert True
        else:
            assert False

        if suffix2 == suffix:
            assert True
        else:
            assert False

    def test_updating_with_value_change(self, setup):
        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        updating_chart_element = self.driver.find_element(By.XPATH,

                                                          "/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div[1]/div/div/div[16]/div/div[2]")
        time.sleep(1)
        updating_chart_element.click()
        time.sleep(2)

        acc_name_ = self.ad.account_name().get_attribute("value")
        print(acc_name_)

        arabic_name = self.ad.arabic_name().get_attribute("value")
        print(arabic_name)

        suffix = self.ad.suffix().get_attribute("value")
        print(suffix)

        acc_num = self.ad.account_num().get_attribute("value")
        print(acc_num)

        time.sleep(2)

        self.ad.updte_btn().click()

        time.sleep(2)
        print("values after updating")

        self.ad.account_name().send_keys("store")
        self.ad.arabic_name().send_keys("Purchase")
        time.sleep(2)

        acc_name_2 = self.ad.account_name().get_attribute("value")
        print(acc_name_2)

        arabic_name2 = self.ad.arabic_name().get_attribute("value")
        print(arabic_name2)

        suffix2 = self.ad.suffix().get_attribute("value")
        print(suffix2)

        acc_num2 = self.ad.account_num().get_attribute("value")
        print(acc_num2)

        time.sleep(2)

        self.ad.updte_btn().click()

        if acc_name_ != acc_name_2:
            assert True
        else:
            assert False

        if acc_num == acc_num2:
            assert True
        else:
            assert False

        if arabic_name != arabic_name2:
            assert True
        else:
            assert False

        if suffix2 == suffix:
            assert True
        else:
            assert False

    def test_adding_child_account_normal(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        adding_chart_element = self.driver.find_element(By.XPATH,

                                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[15]/div[1]/div[3]")
        time.sleep(1)
        adding_chart_element.click()
        time.sleep(2)

        self.ad.account_name().send_keys("stor21e")
        self.ad.arabic_name().send_keys("Purcqqhase")
        time.sleep(2)
        self.ad.suffix().send_keys("2228225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.save_btn().click()

        save_messg = self.ad.save_messege()
        print(save_messg)

        if save_messg == "New chart of accounts added":
            assert True
        else:
            assert False

    def test_adding_child_account_GL(self, setup):

        # login setup
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()
        # time.sleep(2)

        # click action for nav bar arrow
        self.nav = Navigation_Page(self.driver)
        self.nav.click_navbar()
        # time.sleep(2)

        sidebar = self.driver.find_element(By.XPATH, "//div[@class='sidebarMenuContainer open']")

        # Locate the "Remittance" element inside the sidebar container
        self.driver.execute_script("arguments[0].scrollIntoView(100, 100);", sidebar)
        time.sleep(2)
        self.nav.click_chart_of_account()
        time.sleep(3)

        self.ad = adding_account(self.driver)

        adding_chart_element = self.driver.find_element(By.XPATH,

                                                        "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[15]/div[1]/div[3]")
        time.sleep(1)
        adding_chart_element.click()
        time.sleep(2)

        self.ad.account_name().send_keys("stor21e")
        self.ad.arabic_name().send_keys("Purcqqhase")
        time.sleep(2)
        self.ad.suffix().send_keys("226448225")
        time.sleep(3)

        acc_number = self.ad.account_num().get_attribute("value")
        parent_acc = self.ad.parent_account().get_attribute("value")

        print("acc_number:", acc_number)
        print("parent_acc:", parent_acc)

        self.ad.is_gl_acc().click()
        time.sleep(2)

        self.ad.fc_account().click()
        currency = Select(self.ad.drp_currency())
        currency.select_by_index(1)

        self.ad.rate().send_keys("3")

        self.ad.journal_voucher().click()

        self.ad.petty_cash().click()

        self.ad.receipt_voucher().click()

        self.ad.save_btn().click()

        save_messg = self.ad.save_messege()
        print(save_messg)

        if save_messg == "New chart of accounts added":
            assert True
        else:
            assert False








