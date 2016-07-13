#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')

GROUP_NAME = "עדי"

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

groups = driver.find_elements_by_class_name("chat-body")
for lnk in groups:
    link = lnk.text.decode("utf-8")
    if link.find(GROUP_NAME.decode("utf-8"))>=0:
        lnk.click()
        break

time.sleep(2);

# Scroll up to get more messages
icon_refresh = driver.find_element_by_class_name("icon-refresh")
icon_refresh.click()

msg_groups = driver.find_elements_by_class_name("msg");

time.sleep(5) 
#driver.quit()
