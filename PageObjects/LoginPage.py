from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver=driver

        self.textbox_username_xpath="//input[@placeholder='Username']"
        self.textbox_password_xpath="//input[@placeholder='Password']"
        self.button_login_xpath="//button[@type='submit']"
        self.txt_invldmsg_xpath="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def input_username(self,Username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(Username)

    def input_password(self,Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def invalidmsg(self):
       return self.driver.find_element(By.XPATH, self.txt_invldmsg_xpath).text