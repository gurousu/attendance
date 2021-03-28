from selenium import webdriver
import time

#pre settings
driver = webdriver.Chrome(executable_path='G:\\project\\attendance\\driver\\chromedriver.exe')

driver.get("https://workcloud.jp/")
time.sleep(5)

#log in
user_id = driver.find_element_by_id("user_login")
user_id.send_keys("") 

user_password = driver.find_element_by_id("user_password")
user_password.send_keys("")

driver.find_element_by_name("commit").submit()

#Attendance and departure