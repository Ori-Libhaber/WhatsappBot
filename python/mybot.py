#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')


GROUP_NAME = "KOKO"
dico = {}
##GROUP_NAME = "כדורסל מטומי-שלישי 19:00"


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


#driver.get('http://web.whatsapp.com');

time.sleep(8) # Let the user actually see something!

str = "//*[@title='"+GROUP_NAME + "']"
driver.find_element_by_xpath(str).click()

# Send message in current chat
def sendMessage(message):
	msgbox = driver.find_element_by_class_name("input-container")
	msgbox.click()
	msgbox.send_keys(message)
	driver.find_element_by_class_name("icon-send").click()

def parser():
	txt = driver.find_element_by_class_name("message-list").get_attribute("innerHTML")
	txt_find= "inverse-text-direction selectable-text"+'"'+ " dir=" +'"'+"rtl"+'"'+">"
	txt_other_find = "class="+'"'+"emojitext selectable-text"+'"'+" dir="+'"'+"ltr"+'"'+">"
	authour_txt = "<span class="+'"'+"emojitext"+'"'+">"
	prev_auth = ""

	for elem in txt.split("bubble bubble"):
		authour = ""
		txt_find_len = 50
		strt = elem.find(txt_find)
		if (strt<0):
			strt = elem.find(txt_other_find)
			if (strt<0):
				continue
			txt_find_len = 44
		new_txt = elem[strt+txt_find_len:]
		if (new_txt.find("href")>=0):
			continue
		end = new_txt.find("<")
		if (elem.find(authour_txt)>=0):
			tmp_authour = elem[elem.find(authour_txt)+24:]
			end_tmp = tmp_authour.find("<")
			authour = tmp_authour[:end_tmp]
			prev_auth = authour
		print elem[elem.find("[")+1:elem.find("]")]
		print new_txt[0:end]
		if (authour==""):
			if (elem.find("+972 54-772-0957")>=0):
				authour = "צחי לפידות"
			elif (elem.find("+972 52-616-3001")>=0):
				authour = "יואב"
			else:
				authour = prev_auth
		print authour
		arr = dico.get(authour,[authour])
	   arr.append(new_txt[0:end])
	   dico[authour]=arr
	   print "========================================"
	  ##  if dico.__contains__(authour):

		print "========================================"
>>>>>>> fix


time.sleep(2)

def scorllUp():
	# Scroll up to get more messages
	try:
		icon_refresh = driver.find_element_by_class_name("icon-refresh")
	except:
		pass
	else:
		icon_refresh.click()


scorllUp()

# Main loop
while True:
	parser()

	time.sleep(2)

	# Check last message

	# Send relevant message
	sendMessage("Hello World!!!")

	time.sleep(5)
	#driver.quit()
