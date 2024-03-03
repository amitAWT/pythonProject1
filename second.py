from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

#################Edge Browser ########################
#Serv_obj= Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
#driver=webdriver.Edge(service=Serv_obj)

###################### Chrome browser ###########################
Serv_obj= Service("C:\\Drivers\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=Serv_obj)

######################## Firefox Browser ###############

#Serv_obj= Service("C:\\Drivers\\geckodriver-v0.34.0-win32\\geckodriver.exe")
#driver=webdriver.Chrome(service=Serv_obj)

driver.get("https://dev.sqor.ai")

driver.find_element(By.NAME,"email").send_keys("sourabh@findids.net")
driver.find_element(By.ID,":r1:").send_keys("@Ss940661")
driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-daiv24']").click()
time.sleep(5)

act_tittle = driver.title
exp_tittle = "SQOR"
if act_tittle == exp_tittle:
    print("Login test pass")
else:
    print("Login test fail")


