#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, SoupStrainer
import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')

GROUP_NAME = "כדורסל מטומי-שלישי 19:00"

print "input",sys.argv[1]
if sys.argv[1].find("new")>=0:
	driver = webdriver.Chrome('/home/redbend/Desktop/Hackathon/chromedriver')  # Optional argument, if not specified will search path.
	print "python",sys.argv[0],driver.command_executor._url,driver.session_id
	exit()

if sys.argv.__len__()>2:
	url = str(sys.argv[1])
	session_id = str(sys.argv[2])
else:
	exit()

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id


driver.get('http://web.whatsapp.com');

time.sleep(8) # Let the user actually see something!

str = "//*[@title='"+GROUP_NAME + "']"
driver.find_element_by_xpath(str).click()


stam = driver.find_element_by_class_name("message-list").find_elements_by_class_name("message-text")
for pices in stam:
    print pices.text
    inr_txt = pices.get_attribute("innerHTML")
    strt = inr_txt.find("[")
    end = inr_txt.find("]")
    print inr_txt[strt:end]

time.sleep(2)
# Scroll up to get more messages
icon_refresh = driver.find_element_by_class_name("icon-refresh")
icon_refresh.click()


msg_groups = driver.find_elements_by_class_name("msg");

time.sleep(5) 
#driver.quit()
