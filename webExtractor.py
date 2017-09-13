#!/usr/bin/python2
#Made by Saurabh Londhe
import os
import urllib2
url=raw_input("Enter url= http://")
url=("http://"+url)
test = urllib2.urlopen(url).read()
test2=test
os.system("touch web.html")
data=open("web.html","w")
#print test
data.write(test)
data.close()
#---------------------------------------------------------------------------------
choice=int(input("Enter method\n\t1)href\n\t2)src"))
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
			needlestack.append(url+needle)
	  else:
		sane = 1
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
			needlestack.append(url+needle)
	  else:
		sane = 1
#--------------------------------------------------------------------------------
for item in needlestack:
  print item
