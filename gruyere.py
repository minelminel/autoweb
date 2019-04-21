# RUN OUTSIDE OF CONDA

import os
import re
from urllib3 as URL
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

print("\n[online]")
PWD = os.path.abspath(os.path.dirname(__file__))
driverPath = os.path.join(PWD,'chromedriver')
browser = webdriver.Chrome(driverPath)
browser.set_window_size(680,880)

root_url = 'https://google-gruyere.appspot.com'
start_page = 'start'
browser.get(os.path.join(root_url,start_page))

html = browser.find_element_by_xpath(".//html")
# extract contents from plaintext
pattern = '(?<=instance id is ).*(?=.)'
line = html.text

instanceID = re.findall(pattern, line)
instanceID = ''.join(instanceID)
instanceURL = os.path.join(root_url,instanceID)
print(instanceID)
print(instanceURL)

"""
Our driver is initialized and metadata collected.
We can now reference BACK to this point
    after future entry attemps.
"""

usernameInjection = 'admin'
passwordInjection = 'admin'

loginURL = os.path.join(instanceURL,'login')
browser.get(loginURL)
login = browser.find_element_by_class_name('content')
login.find_element_by_name('uid').send_keys(usernameInjection)
login.find_element_by_name('pw').send_keys(passwordInjection)
login.find_element_by_css_selector("[value='Login']").click()


print("\nFINISHED")
