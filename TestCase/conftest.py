# driver=webdriver.Chrome(executable_path="E:\\chromedriver.exe")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import configparser
config=configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.fixture
def setup(request):
    service = Service("Driver\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    request.cls.driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver.get(config.get("Url","base_url"))
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    yield
    request.cls.driver.quit()