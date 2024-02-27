from selenium import webdriver
from selenium.webdriver.common.by import By


class signup:
    signup_link_xpath= "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/form[1]/div[2]/div[4]/p[2]"
    email_xpath= "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    access_code_xpath= "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    checkbox_xpath= "//input[@type='checkbox']"
    signup_button= "//button[@type='submit']"
    validate_acc_bttn= "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/button[1]"
    first_lastname_xpath = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    enter_password = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    confirm_password = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/input[1]"
    signuptwo_button = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[6]/button[1]"
    add_company = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    country = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    state = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
    city = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]"




    def __init__(self, driver):
        self.driver = driver

    def clicksignup(self):
        self.driver.find_element(By.XPATH,(self.signup_link_xpath)).click()

    def setemail(self,emailid):
        self.driver.find_element(By.XPATH,(self.email_xpath)).send_keys(emailid)

    def setaccesscode(self,code):
        self.driver.find_element(By.XPATH,(self.access_code_xpath)).send_keys(code)

    def clickcheckbox(self):
        self.driver.find_element(By.XPATH,(self.checkbox_xpath)).click()

    def clicksignupbttn(self):
        self.driver.find_element(By.XPATH,(self.signup_button)).click()

    def clickvalidatebttn(self):
        self.driver.find_element(By.XPATH,(self.validate_acc_bttn)).click()

    def setfirstlastname(self):
        self.driver.find_element(By.XPATH,(self.first_lastname_xpath)).send_keys("Anuj R")

    def setpassword(self):
        self.driver.find_element(By.XPATH,(self.enter_password)).send_keys("Amit@123!!")

    def setconfirmpassword(self):
        self.driver.find_element(By.XPATH,(self.confirm_password)).send_keys("Amit@123!!")

    def clicksignupbutton(self):
        self.driver.find_element(By.XPATH,(self.signuptwo_button)).click()

    def setcompany(self):
        self.driver.find_element(By.XPATH,(self.add_company)).send_keys("Testing")

    def setcountry(self):
        self.driver.find_element(By.XPATH,(self.country)).send_keys("India")
