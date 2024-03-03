import pytest
from selenium import webdriver
import time

from PageObjects.Signup import signup


class Test_002_signup:
    baseurl = "https://dev.sqor.ai"
    emailid = "surogato@gifts4homes.com"
    code = "1234"
    flname = "Anuj R"
    password = "Amit@123!!"
    confirmpass = "Amit@123!!"
    companyname = "Testing"

    if password == confirmpass:
        print("Password matched")
    else:
        print("Please enter valid Confirm Password")
    def test_signup (self, setup):
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
        time.sleep(5)
        self.sp.setfirstlastname(self.flname)
        self.sp.setpassword(self.password)
        self.sp.setconfirmpass(self.confirmpass)
        self.sp.clicksignuptwo()
        time.sleep(5)


