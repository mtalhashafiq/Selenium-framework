from selenium.webdriver.common.by import By


class dashboard:

    def __init__(self,driver):
        self.driver=driver
        self.textbox_dashboard_xpath="//h6[normalize-space()='Dashboard']"
        self.button_admin_xpath="//li[1]//a[1]//span[1]"
        self.button_job_xpath="//span[normalize-space()='Job']"
        self.button_employment_status_xpath="//a[normalize-space()='Employment Status']"

    def dashboard_msg(self):
        return self.driver.find_element(By.XPATH, self.textbox_dashboard_xpath).text

    def click_admin(self):
        return self.driver.find_element(By.XPATH, self.button_admin_xpath).click()

    def click_job(self):
        return self.driver.find_element(By.XPATH, self.button_job_xpath).click()

    def click_emp_status(self):
        return self.driver.find_element(By.XPATH, self.button_employment_status_xpath).click()