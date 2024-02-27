import pytest
from selenium import webdriver
import time

from PageObjects.Signup import signup


class Test_002_signup:
    baseurl = "https://dev.sqor.ai"
    emailid = "pepc@kreatifeo.com"
    code = "1234"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.sp = signup(self.driver)
        self.sp.clicksignup()
        self.sp.setemail(self.emailid)
        self.sp.setaccesscode(self.code)
        self.sp.clickcheckbox()
        self.sp.clicksignupbttn()
        time.sleep(30)
        self.sp.clickvalidatebttn()
