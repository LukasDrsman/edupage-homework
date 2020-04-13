# import stuff
from config import *
from functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# init
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", options = options)
date = dateGen(ndays)
homework = []

# login
driver.get(website+"/login/")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(uname)
password.send_keys(passwd)
driver.find_element_by_xpath("//input[@type='submit']").click()

# parse homework
driver.get(website+"/exam/?")
time.sleep(1)

for i in range(len(date)):
    path = "//li[@data-date='"+date[i]+"']/div[@class='hwItemInner']/div[@class='hwCnt']/div[@class='hwTitle']"
    hw = driver.find_elements_by_xpath(path)
    for n in range(len(hw)):
        homework.append((hw[n].text, date[i]))

driver.quit()

# print homework
if(printdata == True):
    print(separator)
    for i in range(len(homework)):
        print(homework[i][0] + "\n" + homework[i][1])
        print(separator)
