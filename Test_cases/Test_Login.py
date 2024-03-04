import pytest
from selenium import webdriver
from PageObjects.Login import Login
import time


class Test_001_Login:
    baseURL= "https://dev.sqor.ai"
    emailId= "sourabh@findids.net"
    password= "@Ss940661"



    def test_login(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.LP=Login(self.driver)
        self.LP.setusername(self.emailId)
        self.LP.setpassword(self.password)
        self.LP.clicklogin()
        time.sleep(5)
        self.LP.clicklogout()
        time.sleep(5)



