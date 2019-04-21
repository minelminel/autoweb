## RUN OUTSIDE OF CONDA
import os
import re
import random
import urllib3 as URL
from time import time, sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def randomWord():
    URL.disable_warnings(URL.exceptions.InsecureRequestWarning)
    http = URL.PoolManager()
    r = http.request('GET','https://randomword.com/')
    pattern = '(?<=<div id="random_word">).*(?=<)'
    line = r.data.decode('utf-8')
    word = re.findall(pattern,line)
    word = ''.join(word)
    return word


def generateTweet(tweetType=None):
    defaultText = 'hello, world'
    if tweetType is None:
        return defaultText
    elif tweetType == 'time':
        return datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')
    elif tweetType == 'int':
        return random.randint(0,100)
    elif tweetType == 'char':
        return chr(random.randint(33,126))
    elif tweetType == 'word':
        return randomWord()
    elif tweetType == 'msg':
        return 'debug'
    else:
        return defaultText


tic = time()
actually_send_tweet = False

print("\n[Running: {} as {}]".format(__file__,__name__))
if actually_send_tweet is True:
    print("[online]\n")
else:
    print("[debug]\n")
root_url = "https://twitter.com"
login_url = os.path.join(root_url, 'login')
userName = os.environ.get('TWITTER_USERN')
passWord = os.environ.get('TWITTER_PASSW')


print("Initializing driver")
chrome_options = Options()
chrome_options.add_argument("--headless")
PWD = os.path.abspath(os.path.dirname(__file__))
driverPath = os.path.join(PWD,'chromedriver')
driver = webdriver.Chrome(executable_path=driverPath,options=chrome_options)
driver.set_window_size(580,680)
# driver.execute_script("document.body.style.zoom='70%'")


print("Accessing {}".format(login_url))
driver.get(login_url)
print("Logging in as @{}".format(userName))
username = driver.find_element_by_css_selector("input[placeholder='Phone, email or username']")
password= driver.find_element_by_css_selector("input[class='js-password-field']")
username.send_keys(userName)
password.send_keys(passWord)
submit = driver.find_element_by_xpath("//button[text()='Log in']")
submit.click()


if driver.current_url != login_url:
    print("Pasting text...")
# Focus on tweet box
    autotw1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='tweet-box-home-timeline']")))
# Generate/Insert TWEET text
    tweetMsg = generateTweet('time')
    print("\t@{}: {}".format(userName,tweetMsg))
    autotw1.send_keys(str(tweetMsg))
# Click to submit
    tweet = driver.find_element_by_xpath("//span[@class='add-tweet-button ']//following-sibling::button[contains(@class,'tweet-action')]")
    if actually_send_tweet is True: tweet.click()
    print("\t[success]")
else:
    print("Unable to login @{}".format(userName))
    print("\t[failure]")


# Exit browser
driver.close()
toc = time()
print("\n[offline]\n[duration :: {} s]".format(toc-tic))
