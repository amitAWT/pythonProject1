from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

Serv_obj= Service("C:\\Users\\dell\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=Serv_obj)

driver.get("https://dev.sqor.ai")

driver.find_element(By.XPATH, "//input[@id=':r0:']").clear()
driver.find_element(By.XPATH, "//input[@id=':r0:']").send_keys("sourabh@findids.net")
driver.find_element(By.XPATH, "//input[@id=':r1:']").send_keys("@Ss940661")
time.sleep(5)
driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-daiv24']").click()
time.sleep(10)