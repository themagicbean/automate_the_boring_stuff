'''
Created on Mar 5, 2019

@author: darrenbean
'''
# search for a category, then download all results
# imgur blocked, Flickr was not
# Flickr needed log-in via yahoo
# shutterstock? works, but they have their own API too

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, os

# second try changed search term
browser = webdriver.Firefox()
browser.get('https://www.shutterstock.com/')

searchField = browser.find_element_by_name('searchterm')
searchField.send_keys('eggplant')
WebDriverWait(browser, 10)
searchField.send_keys(Keys.ENTER)
#works to here

# need to wait for load ???? !!!!!!!!!!!!!!!!!!!!!

#result is https://www.shutterstock.com/search/taquitos?site=image&searchterm=taquitos&studio=1
#direct link works


# above works, redid to test logo
#browser = webdriver.Firefox()
#browser.get('https://www.shutterstock.com/search/taquitos?site=image&searchterm=taquitos&studio=1')

os.makedirs('eggplant_images', exist_ok=True)

# works to here but needs to wait for load 
current_url = browser.current_url
WebDriverWait(browser, 300).until(EC.url_changes(current_url))

# somewhat working, hits exception on one of the imgs being stale? 
imagesToGet =  browser.find_elements_by_tag_name('img')

for image in imagesToGet:
    
    imageUrl = image.get_attribute('src') 
    res = requests.get(imageUrl)
        
    imageFile = open(os.path.join('eggplant_images', os.path.basename(imageUrl)), 'wb')
        
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close
    
#above works!
