#!/usr/bin/python2
#made by SAURABH LONDHE
import os
import urllib2
os.system("tput clear")
#-------------------------------------------------------------------------------
print "Base url means it must contain string till its domain it should not be extended with its pages or file extensions\nSuch as;\n\t\t'http://ritindia.edu'\n\n('http://ritindia.edu/index.html')such url is not valid\n"
print "both base url and url must be of same website" 
print "*************************************************************\n"
print "Use (https://website_name.com) format 'www.web_name.com' will give error\n'"
url=raw_input("Enter base url= ")
os.system("tput clear")
print "\ncopy link from browser it may or may not contain /name.html extensions\n"
base_url=raw_input("Enter page url= ")
#-------------------------------------------------------------------------------
cnt=0
test = urllib2.urlopen(base_url).read()
test2=test
os.system("touch web.html")
data=open("web.html","w")
#print test
data.write(test)
data.close()
#---------------------------------------------------------------------------------
choice=int(input("Enter method\n\t1)href\n\t2)src\n\t\t="))
if choice==1:
	sane = 0
	needlestack = []
	while sane == 0:
	  curpos = test.find("href")
	  if curpos >= 0:
		testlen = len(test)
		test = test[curpos:testlen]
		curpos = test.find('"')
		testlen = len(test)
		test = test[curpos+1:testlen]
		curpos = test.find('"')
		needle = test[0:curpos]
		if needle.startswith("http" or "www" or "/"):#and needle.endswith(".js"):
			needlestack.append(needle)
		elif needle.startswith(""):
			needlestack.append(url+"/"+needle)
	  else:
		sane = 1
		for item in needlestack:
			dwnld=str(cnt+1)+") "+item
			cnt+=1
			print dwnld
#--------------------------------------------------------------------------------
elif choice==2:
	sane = 0
	needlestack = []
	while sane == 0:
	  curpos = test.find("src")
	  if curpos >= 0:
		testlen = len(test)
		test = test[curpos:testlen]
		curpos = test.find('"')
		testlen = len(test)
		test = test[curpos+1:testlen]
		curpos = test.find('"')
		needle = test[0:curpos]
		if needle.startswith("http" or "www" or "/"):#and needle.endswith(".js"):
			needlestack.append(needle)
		elif needle.startswith(""):
			needlestack.append(url+"/"+needle)
	  else:
		sane = 1
		for item in needlestack:
			dwnld=str(cnt+1)+") "+item
			cnt+=1
			print dwnld
#--------------------------------------------------------------------------------
print "\nDo you Want to Download (",cnt,"files) (Y/N)"
ch=raw_input()
if ch=='y' or ch=='Y':	
	os.system("rm -rf Script_data")
	os.system("mkdir Script_data")
	for item in needlestack:
		
		dwnld="cd Script_data && "+"wget "+item
	#	print dwnld
		os.system(dwnld)
	#  print item
#------------------------------------------------------------------------------------
if ch=='n' or ch=='N':
	print "would you like to download selected items?(Y/n)"
	ch2=raw_input()
	if ch2=='y' or ch2=='y':
		while(True):
			filetodownload=int(input("Enter your choice number"))
			if filetodownload!=0:
				os.system("rm -rf Script_data")
				os.system("mkdir Script_data")
				dwnld="cd Script_data && "+"wget "+needlestack[filetodownload-1]
				os.system(dwnld)
			else:
				break
			
