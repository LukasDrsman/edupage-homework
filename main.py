# import stuff
from bs4 import BeautifulSoup
import requests
from config import *
from functions import *
from selenium import webdriver
import time
import pprint

# init
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", options = options)
date = dateGen(ndays)
homework = []

# login
driver.get("https://seslm.edupage.org/login/")
username = driver.find_element_by_id("login_Login_1e1")
password = driver.find_element_by_id("login_Login_1e2")
username.send_keys(uname)
password.send_keys(passwd)
driver.find_element_by_class_name("skgdFormSubmit").click()

# parse homework
driver.get("https://seslm.edupage.org/exam/?")
time.sleep(1)

for i in range(len(date)):
    path = "//li[@data-date='"+date[i]+"']/div[@class='hwItemInner']/div[@class='hwCnt']/div[@class='hwTitle']"
    hw = driver.find_elements_by_xpath(path)
    for n in range(len(hw)):
        homework.append((hw[n].text, date[i]))

# print homework
print("-------------------------------------------")
for i in range(len(homework)):
    print(homework[i][0] + "\n" + homework[i][1])
    print("-------------------------------------------")
