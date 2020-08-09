from urllib import request,parse
import urllib
import time

def postrequest(url,user,msg):
	data = bytes("{\"username\":\""+user+"\",\"avatar_url\":\"\",\"content\":\""+msg+"\"}","utf-8")
	headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
	req = request.Request(url,data=data,headers=headers)
	request.urlopen(req)

def deleterequest(url):
	headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
	req = request.Request(url,headers=headers,method="DELETE")
	request.urlopen(req)

def main():
	numberofrequest = 0
	print("""
 ██████  ██████   ██████  ██      ███████ ██████   █████  ███    ███ ███    ███ ███████ ██████  
██      ██    ██ ██    ██ ██      ██      ██   ██ ██   ██ ████  ████ ████  ████ ██      ██   ██ 
██      ██    ██ ██    ██ ██      ███████ ██████  ███████ ██ ████ ██ ██ ████ ██ █████   ██████  
██      ██    ██ ██    ██ ██           ██ ██      ██   ██ ██  ██  ██ ██  ██  ██ ██      ██   ██ 
 ██████  ██████   ██████  ███████ ███████ ██      ██   ██ ██      ██ ██      ██ ███████ ██   ██ 
                                                                                                
                                                                                                
		""")
	choice = input("""
	[1] Spam Webhook
	[2] Delete Webhook
	""")
	if(choice == "1"):
		webhook = input("webhook: ")
		username = input("username of the bot: ")
		subject = input("subject: ")
		try:
			for i in range(0,10000):
				numberofrequest+=1
				postrequest(webhook,username,subject)
				print(str(numberofrequest)+" | Request sended to the webhook.")
				time.sleep(2)
		except urllib.error.HTTPError:
			main()
	if(choice == "2"):
		webhook = input("webhook to delete: ")
		deleterequest(webhook)
		print("got deleted lol")
		input()
		main()
main()