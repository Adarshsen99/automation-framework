from selenium.webdriver.common.by import By


class LoginPage:

    fields_username_xpath = "//input[@id='Login']"
    fields_password_xpath = "//input[@id='Password']"
    btn_login_xpath = "//button[@type='submit']"
    dropdown_xpath = "//select[@id='languageSelect']"
    view_password = "//img[@alt='Open Eye']"


    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,uname):

        username_field = self.driver.find_element(By.XPATH, self.fields_username_xpath)
        # username_field.clear()
        username_field.send_keys(uname)

    def setPassword(self,password):
        password_field = self.driver.find_element(By.XPATH,self.fields_password_xpath)
        # password_field.clear()
        password_field.send_keys(password)

    def clickDropdown(self):
        return self.driver.find_element(By.XPATH,self.dropdown_xpath)

    def viewPassword(self):
        self.driver.find_element(By.XPATH, self.view_password).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
