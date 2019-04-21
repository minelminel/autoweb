# RUN OUTSIDE OF CONDA

import os
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

print("\n[online]")
PWD = os.path.abspath(os.path.dirname(__file__))
driverPath = os.path.join(PWD,'chromedriver')
browser = webdriver.Chrome(driverPath)
browser.set_window_size(680,680)
# browser.send_keys(Keys.chord(Keys.COMMAND, Keys.SUBTRACT));

root_url = 'https://www.twitter.com'
start_url = ''
browser.get(os.path.join(root_url,start_url))
loginLink = os.path.join(root_url,'login')
browser.get(loginLink)

"""
Our driver is initialized and metadata collected.
We can now reference BACK to this point
    after future entry attemps.
"""
usernameInjection = '*******'
passwordInjection = '*******'
tweetInjection = 'hello twitter'

browser.find_element_by_class_name('js-username-field').send_keys(usernameInjection)
browser.find_element_by_class_name('js-password-field').send_keys(passwordInjection, Keys.ENTER)
browser.find_element_by_id('global-new-tweet-button').click()
# browser.find_element_by_class_name('tweet-box').click() #send_keys(tweetInjection)
browser.find_element_by_class_name('tweet-box').send_keys(tweetInjection)

# login.find_element_by_name('pw').send_keys(passwordInjection)
# login.find_element_by_css_selector("[value='Login']").click()












# browser.findElement(By.name("")).sendKeys("")
# usename = browser.find_element_by_name('uid')
# username.click()
# username.send_keys('hello')















# browser.find_element_by_link('submit').click() # alternative to pressing ENTER
# searchBox = browser.find_element_by_id('searchform')
# searchBox.send_keys('hello')
# searchBox.send_keys(Keys.ENTER)



# loginForm = browser.find_element_by_id('signin-dropdown')
# userName = loginForm.find_element_by_name('session[username_or_email]')
# sleep(1)
# userName.send_keys('hello world')
# elem.send_keys('hello world')


"""
// enter a valid username
driver.findElement(By.<em>id</em>("username")).sendKeys("name");

// enter a valid email address
driver.findElement(By.<em>id</em>("email")).sendKeys("name@abc.com");

// enter a valid password
driver.findElement(By.<em>id</em>("password")).sendKeys("namepass");

// re-enter the password
driver.findElement(By.<em>id</em>("passwordConf")).sendKeys("namepass");

// submit the form
driver.findElement(By.<em>id</em>("submit")).submit();
"""












# elem = browser.find_element_by_link_text('Download')
# elem.click()

# loginButton = browser.find_element_by_name('session[username_or_email]')
# loginButton.click()

# searchBox = browser.find_element_by_id('q')
# searchBox.send_keys('download')
# searchBox.send_keys(Keys.ENTER)
# # browser.find_element_by_id('submit').click() # alternative to pressing ENTER




print("\nFINISHED")



# driver.current_url
"""
class Tweeter(object):
    # docstring for Tweeter
    # Selenium-based API workaround (thx a lot, Russia)
    # Calling an instance initializes environ variables & paths
    # * tweet will not be sent on obj init *

    def __init__(self, username='TWITTER_USERN', password='TWITTER_PASSW'):
        self.Height = 600
        self.Width = 300
        try:
            self.username = os.environ.get(username)
            self.password = os.environ.get(password)
        except:
            self.username = None
            self.password = None
        self.PWD = os.path.abspath(os.path.dirname(__file__))
        driverPath = os.path.join(self.PWD,'chromedriver')
        self.driverPath = driverPath if os.path.isfile(driverPath) else None
        self.root_url = 'https://twitter.com/'
        self.login_url = os.path.join(self.root_url, 'login')
        self.driver = self.driver_init()

    def driver_init(self):
        if self.driverPath is not None:
            print('driver initialized')
            driver = webdriver.Chrome(self.driverPath)
            driver.set_window_size(self.Height,self.Width)
            driver.execute_script("document.body.style.zoom='67%'")
            return driver
        else:
            return None

    def visit_url(self):
        self.driver.get(self.root_url)
"""
