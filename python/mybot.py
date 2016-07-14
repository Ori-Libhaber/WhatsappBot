#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from selenium import webdriver
from whatsapp_poll import run_poll
reload(sys)
sys.setdefaultencoding('utf-8')


GROUP_NAME = ["KOKO", "Mybot"]
dico = {}
last_text_g = ["","",""]
last_author_g = ["","",""]
admin="Tzachi"

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

def React(id):
	if(id == 0 and last_author_g[id] != admin):
		if(last_text_g[id] == ""):
			sendMessage("HeziDaBot:  Hi")
		if(last_text_g[id] == "When you arrive"):
			sendMessage("HeziDaBot:  I dont know")
			sendMessage("HeziDaBot:  Are you done with showers ?")
		if(last_text_g[id] == "yes"):
			sendMessage("HeziDaBot:  Ohh I am in the kitchen")

	if (id == 1 and last_text_g[id] == "Can play?"):
		sendMessage("HeziDaBot: Checking....")
		sendMessage("HeziDaBot: Please be patient")
		time.sleep(1)
		run_poll(driver)
		gotoChat(GROUP_NAME[id])
		sendMessage("HeziDaBot: Done!")

def gotoChat(chat):
	str = "//*[@title='" + chat + "']"
	driver.find_element_by_xpath(str).click()
	time.sleep(2)


# Send message in current chat
def sendMessage(message):
	msgbox = driver.find_element_by_class_name("input-container")
	msgbox.click()
	msgbox.send_keys(message)
	driver.find_element_by_class_name("icon-send").click()

def parser():
	txt = driver.find_element_by_class_name("message-list").get_attribute("innerHTML")
	txt_find= "inverse-text-direction selectable-text"
	txt_other_find = "class=\"emojitext selectable-text\" dir="
	authour_txt = "<span class=\"emojitext\">"
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
	#	print elem[elem.find("[")+1:elem.find("]")]
	#	print new_txt[0:end]
		if (authour==""):
			if (elem.find("+972 54-772-0957")>=0):
				authour = admin
			elif (elem.find("+972 52-616-3001")>=0):
				authour = admin
			else:
				authour = prev_auth
	#	print "A: " + authour
		arr = dico.get(authour,[authour])
		arr.append(new_txt[0:end])
		dico[authour]=arr


		last_text_l=new_txt[0:end]
		last_author_l=authour
	return last_author_l,last_text_l

def scorllUp():
	# Scroll up to get more messages
	try:
		icon_refresh = driver.find_element_by_class_name("icon-refresh")
	except:
		pass
	else:
		icon_refresh.click()


scorllUp()

message_bank = ["hello", "how r u", "why dont u talk to me","i know u r out there", "this is very rude", "hello"]
iter = 0
# Main loop
id = 0
while True:

	gotoChat(GROUP_NAME[id])

	cur_author,cur_text=last_author_g[id],last_text_g[id]

	last_author_g[id],last_text_g[id] = parser()

	if(last_author_g[id] != cur_author or last_text_g[id] != cur_text):
		React(id)

	id = id + 1
	if(id == 2):
		id = 0

	time.sleep(4)
	#driver.quit()
