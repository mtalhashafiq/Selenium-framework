import pytest
from selenium.webdriver.common.by import By
import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from Utilities.logger import logclass
@pytest.mark.usefixtures("setup")
class Testlogin(logclass):

    def test_001(self):
        log=self.getthelogs()
        lg=Login(self.driver)
        db=dashboard(self.driver)
        log.info("Test case 001")
        log.info("Test case starting")
        lg.input_username("Admin")
        log.info(("Username has been entered"))
        lg.input_password("admin123")
        log.info("Password has been entered")
        lg.click_login()
        log.info("CLicked login button")
        # driver.find_element(By.NAME,value='username').send_keys("Admin")
       # self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        # driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
       # self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
       #  self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

        if 'Dashboard' in db.dashboard_msg():
            assert True
            log.info("Taet case 001 Pass")
        else:
            log.critical("Test case failed")
            assert False
       # driver.quit()
        time.sleep(7)



    def test_002(self):

        lg = Login(self.driver)
        lg.input_username("Amin")
        lg.input_password("admin123")
        lg.click_login()

        if 'Invalid credentials' in lg.invalidmsg():
            assert True

        else:
            assert False
        # driver.quit()
        time.sleep(7)

    def test_003(self):
        lg = Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("amin123")
        lg.click_login()

        if 'Invalid credentials' in lg.invalidmsg():
            assert True
        else:
            assert False
        # driver.quit()
        time.sleep(7)

