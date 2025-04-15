from selenium.webdriver.common.by import By


class Add_new:

    def __init__(self, driver):
        self.driver = driver

    def create_new(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Create New Rule']")

    def settings(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Settings']")

    def search_bar(self):
        return self.driver.find_element(By.XPATH, "//input[@id='aml_wl_int_search']")

    def process_status(self):
        return self.driver.find_element(By.XPATH, "//span[@class='AMLWIntTab ']")

    def title(self):
        return self.driver.find_element(By.XPATH, "//select[@name='aml_wl_int_ttl']")

    def full_name(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Type & Hit Enter to add Full Name')]")

    def date_of_birtth(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add Date of Birth']")

    def state(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add State']")

    def nationality(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add Nationality']")

    def id_number(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add ID Number']")

    def action_remarks(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='aml_wl_int_actn_rmrks']")

    def gender(self):
        return self.driver.find_element(By.XPATH, "//select[@name='aml_wl_int_gndr']")

    def alias_name(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add Aliases Name']")

    def city(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add City']")

    def country_of_residence(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add Country of Residence']")

    def country_of_birth (self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Type & Hit Enter to add Country of Birth'] ")

    def id_type(self):
        return self.driver.find_element(By.XPATH, "//select[@name='aml_wl_int_id_tp']")

    def is_pep(self):
        return self.driver.find_element(By.XPATH, "//input[@id='aml_wl_int_is_pep']")

    def save_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    def cancel_btn(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")

    def close_btn(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='Close Hover']")









