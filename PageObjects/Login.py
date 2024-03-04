from selenium import webdriver
from selenium.webdriver.common.by import By



class Login:
    textbox_Email_id = 'input[placeholder="Email"]'
    textbox_password_id = 'input[placeholder="Enter a password"]'
    button_Login_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-daiv24']"
    link_logout_linktext = "//*[@id='root']/span/div/div[1]/div[1]/div/div[2]/ul/li/div/div[2]/span"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self,emailId):
        self.driver.find_element(By.CSS_SELECTOR,(self.textbox_Email_id)).clear()
        self.driver.find_element(By.CSS_SELECTOR,(self.textbox_Email_id)).send_keys(emailId)

    def setpassword(self,password):
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_password_id)).clear()
        self.driver.find_element(By.CSS_SELECTOR, (self.textbox_password_id)).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, (self.button_Login_xpath)).click()

        act_title = self.driver.title
        exp_title = "SQOR"
        if act_title == exp_title:
            print("Login test case passed")
        else:
            print("Login test case failed")

    def clicklogout(self):
        self.driver.find_element(By.XPATH,(self.link_logout_linktext)).click()

