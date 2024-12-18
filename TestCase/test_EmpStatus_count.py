import pytest
from selenium.webdriver.common.by import By
import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from PageObjects.EmploymentStatusPage import EmpStatus
from Utilities.logger import logclass
from Utilities.random_status import status_generator
import configparser
config=configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_001(self):
        log=self.getthelogs()
        lg=Login(self.driver)
        db=dashboard(self.driver)
        es=EmpStatus(self.driver)
        # self.driver.implicitly_wait(20)
        log.info("Adding status of log class has been started")
        lg.input_username(config.get("credential","corrct_username"))
        log.info("Username has been added")
        lg.input_password(config.get("credential","correct_password"))
        log.info("Password has been added")
        lg.click_login()
        log.info("Login button has been clicked")

        self.driver.implicitly_wait(5)
        db.click_admin()
        self.driver.implicitly_wait(5)
        db.click_job()
        db.click_emp_status()

        old_status_count=0
        for i in es.total_status():
            old_status_count=old_status_count+1
        print(old_status_count)
        log.info("Total count is "+str(old_status_count))
        es.click_add_button()
        log.info("Proces of adding new status has been started")
        # self.driver.implicitly_wait(40)
        es.input_new_status(status_generator())
        # es.input_new_status("Mian gg")
        # self.driver.implicitly_wait(20)
        time.sleep(4)
        es.click_save_button()
        log.info("Save button clicked")
        New_status_count=0
        for j in es.total_status():
            New_status_count=New_status_count+1
        print(New_status_count)
        log.info("Status do not save")
        log.info("And total count after addition is " + str(New_status_count))
        self.driver.save_screenshot('Screenshots\\Test_Employment_failed.png')
        # time.sleep(3)

        # if old_status_count +1 == New_status_count:
        #     log.info("Status has been successfully added")
        #     log.info("ANd total count after addition is "+str(New_status_count))
        #     self.driver.save_screenshot('Screenshots\\Test_Employment_passed.png')
        #     assert True
        #
        # else:
        #     log.info("Status do not save")
        #     log.info("ANd total count after addition is " + str(New_status_count))
        #     self.driver.save_screenshot('Screenshots\\Test_Employment_failed.png')
        #     assert False


        time.sleep(10)
