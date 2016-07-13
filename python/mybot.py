#!/usr/bin/python

import time
import os
from selenium import webdriver

if os.args[1].find("new")
    driver = webdriver.Chrome('/disk4/WhatsappBot/chromedriver')  # Optional argument, if not specified will search path.

    url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
    session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
    print url
    print session_id
    exit()

url = "http://127.0.0.1:54450"
session_id = "57c36c13c14ec380b27816085ba4759c"

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id


driver.get('http://web.whatsapp.com');
time.sleep(8) # Let the user actually see something!

groups = driver.find_elements_by_class_name("chat-body")
for lnk in groups:
    link = lnk.text.decode("utf-8")
    if link.find("Harman")>=0:
        lnk.click()

# Find relevant chat
lnk.click();

time.sleep(2);

msg_groups = driver.find_elements_by_class_name("msg");


#serach_box = driver.find_element_by_link_text("HARMAN");
#search_box.send_keys('ChromeDriver')
#search_box.submit()
time.sleep(5) # Let the user actually see something!
#driver.quit()
