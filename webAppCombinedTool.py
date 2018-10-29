#AUthor: Shrutirupa Banerjiee
#Aim: The tool will be scanning the url, will check for any directories within it and perform some basic enumeration of the web application
#Date: 29.10.2018

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

#modules to be imported
import os.path
import os
import sys
import getopt
from sys import argv, stdout
import validators
import requests
import nmap
import re
import subprocess

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def usage(script):
	"how to use the tool"

	print ("Please use the following way to scan the url \n")
	print ("<python> %s -u <url to be scanned>" %script)

	return script
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def urlValid(url):
	"We need to check if the url entered is in a correct format or not"
	validTest = validators.url(url)
	if validTest == True :
		webExist(url)
	else:
		print ("Please enter a valid url \n:")
	pass

	return url 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def webExist(url):
	"We need to first check if the url is working or not"
	req = requests.get(url)
	if req.status_code == 200:
		urlScan(url)
	else:
		print("Seems either the url is wrong or its unavailable \n")
		print("Please enter an exiting url or wait for a while \n")

	return (url)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def urlScan(url):
	"We will be simply scanning the url using nmap command"
	if url.startswith('https'):
		url1 = url.replace("https://","")
	elif url.startswith('http'):
		url1 = url.replace("http://","")
	nmScan = nmap.PortScanner()
	nmResult = nmScan.scan(url1,'1-65535','-A')	
	print ("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________")
	print ("Scan result for scanning ports and services are shown below: \n")
	print nmResult
	
	webAppCheck(url)

	return (url)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def webAppCheck(url):
	"Using nikto scanner to scan the web application"
	print ("Let's see what all options are open for us in here")
	print ("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________")
	#res = os.popen('nikto'+' ' + '--host' +' '+  url).read()
	res = os.popen('nikto ' + '--host'+' ' + url).read()
	print res
	directoryCheck(url)
	return (url)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def directoryCheck(url):
	"This option is here to check if there are any directories which can be of any use to us"
	print ("The directories listed are as follows: \n")
	print ("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________")
	res = os.popen('dirb'+' '+' '+ url).read()
	print res
	return (url)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main(argv):
	"enter url to scan"
	script = argv[0]
	urlToScan = ""
	if len(argv) < 2:
		usage(script)

	try:
		opts, args = getopt.getopt(argv[1:],"u:",["url="])
	except getopt.GetoptError:
		usage(script)
		sys.exit(3)

	for opt, arg in opts:

		if opt in ("-u", "--url"):
			urlToScan = arg

		pass

	pass

	if (urlToScan == ""):
		print("\n PLease enter the url \n")
		#usage(script)
		return(3)

	urlValid(urlToScan)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__=="__main__":
	print("""

		 (`-').->             (`-')  _  <-. (`-')_      (`-')  _  (`-')                     <-. (`-')_             (`-')  _ 
		 ( OO)_    _          (OO ).-/     \( OO) )     (OO ).-/  ( OO).->            .->      \( OO) ) _          ( OO).-/ 
		(_)--\_)   \-,-----.  / ,---.   ,--./ ,--/      / ,---.   /    '._       (`-')----. ,--./ ,--/  \-,-----. (,------. 
		/    _ /    |  .--./  | \ /`.\  |   \ |  |      | \ /`.\  |'--...__)     ( OO).-.  '|   \ |  |   |  .--./  |  .---' 
		\_..`--.   /_) (`-')  '-'|_.' | |  . '|  |)     '-'|_.' | `--.  .--'     ( _) | |  ||  . '|  |) /_) (`-') (|  '--.  
		.-._)   \  ||  |OO ) (|  .-.  | |  |\    |     (|  .-.  |    |  |         \|  |)|  ||  |\    |  ||  |OO )  |  .--'  
		\       / (_'  '--'\  |  | |  | |  | \   |      |  | |  |    |  |          '  '-'  '|  | \   | (_'  '--'\  |  `---. 
		 `-----'     `-----'  `--' `--' `--'  `--'      `--' `--'    `--'           `-----' `--'  `--'    `-----'  `------' 


		#Coded by cryptFreak aka Shrutirupa
    	""" )
	
	print ("Scan At once \n")
	main(sys.argv[0:])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
