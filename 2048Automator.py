'''
Created on Mar 5, 2019

@author: darrenbean
'''
#goes to 2048 game and automates up right down left

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')
#since html tag encapsulates site, this is good way to get keys sent to general site

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    
# works but hits error when games ends