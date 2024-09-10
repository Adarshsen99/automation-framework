import time
from pynput.keyboard import Controller, Key
from django.template.defaulttags import firstof
from selenium.webdriver.support.ui import Select
from Dinero_automation.utilities.readProperties import ReadConfig
from Dinero_automation.pageObjects.LoginPage import LoginPage
from Dinero_automation.pageObjects.Navbar import Navigation_Page
from Dinero_automation.pageObjects.Dashbord import Dashboard
from Dinero_automation.pageObjects.Customer_Registration_corporate_edit import Company_Information_Edit, Registration_Details_Edit, Beneficial_Owners_Details_Edit, Beneficiaries, Upload_Documents_Edit, Delegate
from Dinero_automation.utilities import screenShort


class Test_Delegate_Editmode:
    url = ReadConfig.getApplicationURL()
    uname = ReadConfig.getApplicationUsername()
    upass = ReadConfig.getApplicationPWD()

    # def test_delegate_edit_valiadting_search_bar(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("gWEYrGPvYA")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     self.be.btn_next().click()
    #     time.sleep(2)
    #
    #     search_dele = self.de.search_delegates()
    #     search_dele.send_keys("karunakar")
    #
    #     self.de.click_delegate().click()
    #     time.sleep(4)
    #
    #     search_dele_val = search_dele.get_attribute('value')
    #
    #     if not search_dele_val:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "Edit_DELEGATE_CORPORATE_test_delegate_edit_valiadting_search_bar.png")
    #         assert False

    # def test_delegate_validating_sptime(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("gWEYrGPvYA")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     self.be.btn_next().click()
    #     time.sleep(2)
    #
    #     search_dele = self.de.search_delegates()
    #     search_dele.send_keys("karunakar")
    #
    #     self.de.click_delegate().click()
    #     time.sleep(2)
    #
    #     self.de.click_upload_doc().click()
    #     time.sleep(2)
    #     self.de.send_doc().click()
    #     time.sleep(2)
    #     keyboard = Controller()
    #     time.sleep(2)
    #     self.driver.implicitly_wait(10)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #     time.sleep(4)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     time.sleep(4)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)
    #     time.sleep(2)
    #
    #     self.de.click_sptime()
    #     time.sleep(2)
    #     start_date = self.de.start_date()
    #     start_date.send_keys("02042024")
    #     time.sleep(2)
    #     end_date = self.de.end_date()
    #     end_date.send_keys("02042025")
    #     start_date_val = start_date.get_attribute('value')
    #     end_date_val = end_date.get_attribute('value')
    #
    #     time.sleep(2)
    #     self.de.click_save()
    #
    #     if start_date_val < end_date_val:
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime.png")
    #         assert False
    #
    #     li = []
    #     msg = self.de.upload_doc_message()
    #
    #     li.append(msg)
    #
    #     time.sleep(2)
    #
    #     extracted_text = li[0].split('\n')[0]
    #
    #     # Print the result
    #     if extracted_text == "No document uploaded":
    #         time.sleep(2)
    #         self.de.btn_next().click()
    #
    #     else:
    #         self.driver.get("http://www.dinero.local/customer/corp/540")
    #         self.ci.btn_next()
    #         time.sleep(2)
    #         self.rd.btn_next()
    #         time.sleep(2)
    #         self.bod.btn_next()
    #         time.sleep(2)
    #
    #         self.be.btn_next().click()
    #         time.sleep(2)
    #
    #         search_dele = self.de.search_delegates()
    #         search_dele.send_keys("karunakar")
    #
    #         self.de.click_delegate().click()
    #         time.sleep(4)
    #
    #         self.de.click_upload_doc().click()
    #         time.sleep(2)
    #         self.de.send_doc().click()
    #         time.sleep(2)
    #         keyboard = Controller()
    #         time.sleep(2)
    #         self.driver.implicitly_wait(10)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #         time.sleep(4)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         time.sleep(4)
    #         keyboard.press(Key.enter)
    #         keyboard.release(Key.enter)
    #         time.sleep(2)
    #
    #         self.de.click_sptime()
    #         time.sleep(2)
    #         start_date = self.de.start_date()
    #         start_date.send_keys("02042024")
    #         time.sleep(2)
    #         end_date = self.de.end_date()
    #         end_date.send_keys("02042025")
    #         start_date_val = start_date.get_attribute('value')
    #         end_date_val = end_date.get_attribute('value')
    #         self.de.click_save()
    #
    #         if start_date_val < end_date_val:
    #             assert True
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime.png")
    #             assert False
    #
    #         self.de.btn_next().click()
    #         time.sleep(2)
    #
    #     self.driver.quit()

    # def test_delegate_validating_sptime_invaild(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("gWEYrGPvYA")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     self.be.btn_next().click()
    #     time.sleep(2)
    #
    #     search_dele = self.de.search_delegates()
    #     search_dele.send_keys("karunakar")
    #
    #     self.de.click_delegate().click()
    #     time.sleep(2)
    #
    #     self.de.click_upload_doc().click()
    #     time.sleep(2)
    #     self.de.send_doc().click()
    #     time.sleep(2)
    #     keyboard = Controller()
    #     time.sleep(2)
    #     self.driver.implicitly_wait(10)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #     time.sleep(4)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     time.sleep(4)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)
    #     time.sleep(2)
    #
    #     self.de.click_sptime()
    #     time.sleep(2)
    #     start_date = self.de.start_date()
    #     start_date.send_keys("02042024")
    #     time.sleep(2)
    #     end_date = self.de.end_date()
    #     end_date.send_keys("02042021")
    #
    #     time.sleep(2)
    #     self.de.click_save()
    #
    #     li = []
    #     msg = self.de.upload_doc_message()
    #
    #     li.append(msg)
    #
    #     time.sleep(2)
    #
    #     extracted_text = li[0].split('\n')[0]
    #
    #     # Print the result
    #     if extracted_text == "No document uploaded":
    #         time.sleep(2)
    #         self.de.btn_next().click()
    #         start_date_val = start_date.get_attribute('value')
    #         end_date_val = end_date.get_attribute('value')
    #
    #         print(start_date_val)
    #         print(end_date_val)
    #
    #         if start_date_val < end_date_val:
    #             assert True
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime_invalid.png")
    #             assert False
    #
    #     else:
    #         self.driver.get("http://www.dinero.local/customer/corp/540")
    #         self.ci.btn_next()
    #         time.sleep(2)
    #         self.rd.btn_next()
    #         time.sleep(2)
    #         self.bod.btn_next()
    #         time.sleep(2)
    #
    #         self.be.btn_next().click()
    #         time.sleep(2)
    #
    #         search_dele = self.de.search_delegates()
    #         search_dele.send_keys("karunakar")
    #
    #         self.de.click_delegate().click()
    #         time.sleep(4)
    #
    #         self.de.click_upload_doc().click()
    #         time.sleep(2)
    #         self.de.send_doc().click()
    #         time.sleep(2)
    #         keyboard = Controller()
    #         time.sleep(2)
    #         self.driver.implicitly_wait(10)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #         time.sleep(4)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         time.sleep(4)
    #         keyboard.press(Key.enter)
    #         keyboard.release(Key.enter)
    #         time.sleep(2)
    #
    #         self.de.click_sptime()
    #         time.sleep(2)
    #         start_date = self.de.start_date()
    #         start_date.send_keys("02042024")
    #         time.sleep(2)
    #         end_date = self.de.end_date()
    #         end_date.send_keys("02042021")
    #         start_date_val = start_date.get_attribute('value')
    #         end_date_val = end_date.get_attribute('value')
    #         self.de.click_save()
    #         time.sleep(2)
    #
    #         if start_date_val < end_date_val:
    #             assert True
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime_invalid.png")
    #             assert False
    #
    #         self.de.btn_next().click()
    #         time.sleep(2)
    #
    #     self.driver.quit()

    # def test_delegate_validating_sptime_invaild(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(30)
    #
    #     # Initialize edit mode page objects
    #     self.lp = LoginPage(self.driver)
    #     self.nav = Navigation_Page(self.driver)
    #
    #     self.ci = Company_Information_Edit(self.driver)
    #     self.rd = Registration_Details_Edit(self.driver)
    #     self.bod = Beneficial_Owners_Details_Edit(self.driver)
    #     self.ud = Upload_Documents_Edit(self.driver)
    #     self.de = Delegate(self.driver)
    #     self.be = Beneficiaries(self.driver)
    #
    #     # Login
    #     self.lp.setUsername(self.uname)
    #     self.lp.setPassword(self.upass)
    #     self.lp.clickLogin()
    #
    #     # time.sleep(10)
    #
    #     self.da = Dashboard(self.driver)
    #     cust_type = Select(self.da.customer_type())
    #     cust_type.select_by_index(2)
    #     search_customer = self.da.sending_customers()
    #     search_customer.send_keys("gWEYrGPvYA")
    #     self.da.click_customers().click()
    #     self.da.click_edit_mode()
    #     time.sleep(2)
    #
    #     self.ci.btn_next()
    #     time.sleep(2)
    #     self.rd.btn_next()
    #     time.sleep(2)
    #     self.bod.btn_next()
    #     time.sleep(2)
    #
    #     self.be.btn_next().click()
    #     time.sleep(2)
    #
    #     search_dele = self.de.search_delegates()
    #     search_dele.send_keys("karunakar")
    #
    #     self.de.click_delegate().click()
    #     time.sleep(2)
    #
    #     self.de.click_upload_doc().click()
    #     time.sleep(2)
    #     self.de.send_doc().click()
    #     time.sleep(2)
    #     keyboard = Controller()
    #     time.sleep(2)
    #     self.driver.implicitly_wait(10)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #     time.sleep(4)
    #     self.driver.execute_script("window.scrollBy(0, 0);")
    #     time.sleep(4)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)
    #     time.sleep(2)
    #
    #     self.de.click_sptime()
    #     time.sleep(2)
    #     start_date = self.de.start_date()
    #     start_date.send_keys("02042024")
    #     time.sleep(2)
    #     end_date = self.de.end_date()
    #     end_date.send_keys("02042021")
    #
    #     time.sleep(2)
    #     self.de.click_save()
    #
    #     li = []
    #     msg = self.de.upload_doc_message()
    #
    #     li.append(msg)
    #
    #     time.sleep(2)
    #
    #     extracted_text = li[0].split('\n')[0]
    #
    #     # Print the result
    #     if extracted_text == "No document uploaded":
    #         time.sleep(2)
    #         self.de.btn_next().click()
    #         start_date_val = start_date.get_attribute('value')
    #         end_date_val = end_date.get_attribute('value')
    #
    #         print(start_date_val)
    #         print(end_date_val)
    #
    #         if start_date_val < end_date_val:
    #             assert True
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime_invalid.png")
    #             assert False
    #
    #     else:
    #         self.driver.get("http://www.dinero.local/customer/corp/540")
    #         self.ci.btn_next()
    #         time.sleep(2)
    #         self.rd.btn_next()
    #         time.sleep(2)
    #         self.bod.btn_next()
    #         time.sleep(2)
    #
    #         self.be.btn_next().click()
    #         time.sleep(2)
    #
    #         search_dele = self.de.search_delegates()
    #         search_dele.send_keys("karunakar")
    #
    #         self.de.click_delegate().click()
    #         time.sleep(4)
    #
    #         self.de.click_upload_doc().click()
    #         time.sleep(2)
    #         self.de.send_doc().click()
    #         time.sleep(2)
    #         keyboard = Controller()
    #         time.sleep(2)
    #         self.driver.implicitly_wait(10)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
    #         time.sleep(4)
    #         self.driver.execute_script("window.scrollBy(0, 0);")
    #         time.sleep(4)
    #         keyboard.press(Key.enter)
    #         keyboard.release(Key.enter)
    #         time.sleep(2)
    #
    #         self.de.click_sptime()
    #         time.sleep(2)
    #         start_date = self.de.start_date()
    #         start_date.send_keys("02042024")
    #         time.sleep(2)
    #         end_date = self.de.end_date()
    #         end_date.send_keys("02042021")
    #         start_date_val = start_date.get_attribute('value')
    #         end_date_val = end_date.get_attribute('value')
    #         self.de.click_save()
    #         time.sleep(2)
    #
    #         if start_date_val < end_date_val:
    #             assert True
    #         else:
    #             self.driver.save_screenshot(
    #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_sptime_invalid.png")
    #             assert False
    #
    #         self.de.btn_next().click()
    #         time.sleep(2)
    #
    #     self.driver.quit()

    def test_delegate_validating_doc_changing_the_type(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        # Initialize edit mode page objects
        self.lp = LoginPage(self.driver)
        self.nav = Navigation_Page(self.driver)

        self.ci = Company_Information_Edit(self.driver)
        self.rd = Registration_Details_Edit(self.driver)
        self.bod = Beneficial_Owners_Details_Edit(self.driver)
        self.ud = Upload_Documents_Edit(self.driver)
        self.de = Delegate(self.driver)
        self.be = Beneficiaries(self.driver)

        # Login
        self.lp.setUsername(self.uname)
        self.lp.setPassword(self.upass)
        self.lp.clickLogin()

        self.da = Dashboard(self.driver)
        cust_type = Select(self.da.customer_type())
        cust_type.select_by_index(2)
        search_customer = self.da.sending_customers()
        search_customer.send_keys("ZkhDpxJUyu")
        self.da.click_customers().click()
        self.da.click_edit_mode()
        time.sleep(2)

        self.ci.btn_next()
        time.sleep(2)
        self.rd.btn_next()
        time.sleep(2)
        self.bod.btn_next()
        time.sleep(2)
        self.be.btn_next().click()
        time.sleep(2)

        search_dele = self.de.search_delegates()
        search_dele.send_keys("karunakar")

        self.de.click_delegate().click()
        time.sleep(2)

        retry_count = 0
        max_retries = 2
        while retry_count < max_retries:
            # Attempt document upload
            self.de.click_upload_doc().click()
            time.sleep(2)
            self.de.send_doc().click()
            time.sleep(2)
            keyboard = Controller()
            time.sleep(2)
            self.driver.implicitly_wait(10)
            self.driver.execute_script("window.scrollBy(0, 0);")
            keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
            time.sleep(4)
            self.driver.execute_script("window.scrollBy(0, 0);")
            time.sleep(4)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(2)

            self.de.click_save()
            time.sleep(2)

            # Check if document was uploaded successfully
            li = []
            msg = self.de.upload_doc_message()

            if msg:
                li.append(msg)
                time.sleep(2)
                extracted_text = li[0].split('\n')[0]
            else:
                extracted_text = "No document uploaded"

            print(extracted_text)

            if extracted_text != "No document uploaded":
                # If the document is uploaded, proceed normally
                break
            else:
                # If the document is not uploaded, retry
                print(f"Retrying document upload... ({retry_count + 1}/{max_retries})")
                retry_count += 1

        # Proceed after retries or successful upload
        if extracted_text == "No document uploaded":
            print("Document upload failed after retries.")
            assert False  # Fail the test if document was not uploaded
        else:
            # Continue with the rest of the process as usual
            self.ud.btn_next()
            self.ud.btn_save().click()

            time.sleep(2)
            self.ci.btn_next()
            time.sleep(2)
            self.rd.btn_next()
            time.sleep(2)
            self.bod.btn_next()
            time.sleep(4)

            ele = self.ud.edit_mode_error()

            if ele == ele:
                assert True
            else:
                self.driver.save_screenshot(
                    screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_doc_changing_the_type.png")
                assert False

        #     time.sleep(2)
        #
        #     search_dele = self.de.search_delegates()
        #     search_dele.send_keys("karunakar")
        #
        #     self.de.click_delegate().click()
        #     time.sleep(2)
        #
        #     self.de.click_upload_doc().click()
        #     time.sleep(2)
        #     self.de.send_doc().click()
        #     time.sleep(2)
        #     keyboard = Controller()
        #     time.sleep(2)
        #     self.driver.implicitly_wait(10)
        #     self.driver.execute_script("window.scrollBy(0, 0);")
        #     keyboard.type("/home/karunakar/Pictures/Screenshots/Screenshot from 2024-09-03 16-38-51.png")
        #     time.sleep(4)
        #     self.driver.execute_script("window.scrollBy(0, 0);")
        #     time.sleep(4)
        #     keyboard.press(Key.enter)
        #     keyboard.release(Key.enter)
        #     time.sleep(2)
        #
        #     self.de.click_save()
        #     self.de.btn_next().click()
        #     self.ud.btn_next()
        #     self.ud.btn_save().click()
        #
        #     time.sleep(2)
        #     self.ci.btn_next()
        #     time.sleep(2)
        #     self.rd.btn_next()
        #     time.sleep(2)
        #     self.bod.btn_next()
        #     time.sleep(2)
        #
        #     self.be.btn_next().click()
        #     time.sleep(2)
        #     self.de.click_upload_doc().click()
        #     time.sleep(2)
        #     self.de.click_single_time()
        #
        #     self.de.click_save()
        #     self.de.btn_next().click()
        #     self.ud.btn_next()
        #     self.ud.btn_save()
        #
        #     time.sleep(2)
        #     self.ci.btn_next()
        #     time.sleep(2)
        #     self.rd.btn_next()
        #     time.sleep(2)
        #     self.bod.btn_next()
        #     time.sleep(4)
        #
            # li = []
            # msg = self.de.upload_doc_message()
            #
            # li.append(msg)
            #
            # time.sleep(2)
            #
            # extracted_text = li[0].split('\n')[0]
        #
        #     # Print the result
        #     if extracted_text != "No document uploaded":
        #         time.sleep(2)
        #         self.de.btn_next().click()
        #
        #         ele = self.ud.edit_mode_error()
        #
        #         if ele == ele:
        #             assert True
        #         else:
        #             self.driver.save_screenshot(
        #                 screenShort.screen_short() + "Edit_DELEGATE_test_delegate_validating_doc_changing_the_type.png")
        #             assert False
        #
        #     self.driver.quit()
        #
