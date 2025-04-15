from selenium.webdriver.common.by import By


class Navigation_Page():
    btn_nav_open_xpath = "//img[@class='icon-styles arrow-closed']"
    btn_nav_close_xpath = "//img[@class='icon-styles arrow-open']"
    dashboard_xpath = "//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[1]/span"
    customer_Registration_xpath = "//span[@class='sidebarRouteLabel'][normalize-space()='Customer Registration']"
    corporate_customer_link_text = "//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[3]/span"
    benificiary_link_text = "//span[normalize-space()='Beneficiary']"
    corporate_beneficiary_link_text = "//span[normalize-space()='Corporate Beneficiary']"
    remittance_link_text = "//span[normalize-space()='Remittance']"
    currency_trade_link_text = "//span[contains(@class,'sidebarRouteLabel')][normalize-space()='Currency Trade']"
    bank_link_text = "//span[normalize-space()='Banks']"
    service_provider_link_text = "//span[@class='sidebarRouteLabel'][normalize-space()='Service Provider']"
    fund_manger_link_text = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[8]/span[1]"
    deal_Manager_link_text = "//span[@class='sidebarRouteLabel'][normalize-space()='Deal Manager']"

    def __init__(self, driver):
        self.driver = driver

    def click_navbar(self):
        self.driver.find_element(By.XPATH, self.btn_nav_open_xpath).click()

    def close_navbar(self):
        self.driver.find_element(By.XPATH, self.btn_nav_close_xpath).click()

    def click_dashboard(self):
        self.driver.find_element(By.LINK_TEXT, self.dashboard_xpath)

    def click_customer_registration(self):
        self.driver.find_element(By.XPATH, self.customer_Registration_xpath).click()

    def click_customer_registration_corporate(self):
        self.driver.find_element(By.XPATH, self.corporate_customer_link_text).click()

    def click_benificiary_individual(self):
        self.driver.find_element(By.XPATH, self.benificiary_link_text).click()

    def click_benificiary_corporate(self):
        self.driver.find_element(By.XPATH, self.corporate_beneficiary_link_text).click()

    def click_remitance(self):
        self.driver.find_element(By.XPATH, self.remittance_link_text).click()

    def click_bank(self):
        self.driver.find_element(By.XPATH, self.bank_link_text).click()

    def click_service_provider(self):
        self.driver.find_element(By.XPATH, self.service_provider_link_text).click()

    def click_fund_manger(self):
        self.driver.find_element(By.XPATH, self.fund_manger_link_text).click()

    def click_side_bar(self):
        self.driver.find_element(By.XPATH, "//div[@class='sideBarRoutesContainer ']")

    def click_currency_trade(self):
        self.driver.find_element(By.XPATH, self.currency_trade_link_text).click()

    def click_deal_manger(self):
        self.driver.find_element(By.XPATH, self.deal_Manager_link_text).click()

    def click_rate_control(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[1]/div/div[10]/span").click()

    def click_chart_of_account(self):
        self.driver.find_element(By.XPATH, "//span[@class='sidebarRouteLabel'][normalize-space()='Chart of Account']").click()

    def pulldownmenu_accounts(self):
        self.driver.find_element(By.XPATH, "(//div[@class='pullDwnMenu_Head pullDwnMenu_Dropdown'])[5]").click()

    def click_withdrawal(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Withdrawal']").click()