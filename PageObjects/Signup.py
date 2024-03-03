from selenium import webdriver
from selenium.webdriver.common.by import By


class signup:
    signup_link_xpath = "/html[1]/body[1]/div[1]/span[1]/div[1]/div[2]/div[3]/div[2]/div[1]/form[1]/div[2]/div[4]/p[2]"
    email_css = 'input[placeholder="Email"]'
    access_code_css = 'input[placeholder="Access Code"]'
    checkbox_xpath = 'input[type="checkbox"]'
    signup_button = 'button[type="submit"]'
    validate_acc_bttn = 'button[type="submit"]'
    first_lastname_css = 'input[placeholder="First and Last name"]'
    enter_password_css_selector = 'input[placeholder="Enter a password"]'
    confirm_password = 'input[placeholder="Confirm password"]'
    signuptwo_button = "button[type='submit']"



    def __init__(self, driver):
        self.driver = driver

    def clicksignup(self):
        self.driver.find_element(By.XPATH,(self.signup_link_xpath)).click()

    def setemail(self, emailid):
        self.driver.find_element(By.CSS_SELECTOR,(self.email_css)).send_keys(emailid)

    def setaccesscode(self, code):
        self.driver.find_element(By.CSS_SELECTOR,(self.access_code_css)).send_keys(code)

    def clickcheckbox(self):
        self.driver.find_element(By.CSS_SELECTOR,(self.checkbox_xpath)).click()

    def clicksignupbttn(self):
        self.driver.find_element(By.CSS_SELECTOR,(self.signup_button)).click()

    def clickvalidatebttn(self):
        self.driver.find_element(By.CSS_SELECTOR,(self.validate_acc_bttn)).click()

    def setfirstlastname(self, flname):
        self.driver.find_element(By.CSS_SELECTOR,(self.first_lastname_css)).send_keys(flname)

    def setpassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR,(self.enter_password_css_selector)).send_keys(password)

    def setconfirmpass(self, confirmpass):
        self.driver.find_element(By.CSS_SELECTOR,(self.confirm_password)).send_keys(confirmpass)

    def clicksignuptwo(self):
        self.driver.find_element(By.CSS_SELECTOR,(self.signuptwo_button)).click()



