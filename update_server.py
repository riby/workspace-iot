import urllib2
import webbrowser
import time
list_link=["https://45.33.89.37:8443/share/svtZz","https://s3.amazonaws.com/ribytests3/google.pdf","TRUE"]

def user_options():
        print "Press 1 for Video"
        print "Press 2 for PDF"
        print "Press 3 for getting last session"
	op=int(raw_input())
        return list_link[op-1],op-1

print urllib2.urlopen("http://testapp/ping/mac").read()
value=urllib2.urlopen("http://testapp/status/mac").read()
print value

list_current=None
uop,op=user_options()
if uop=="TRUE":
	op=urllib2.urlopen("http://testapp/getlaststate").read()
	uop=list_link[int(op)]
if list_current==None:
	list_current=uop
print uop

if value=="Good":
	print urllib2.urlopen("http://testapp/update/"+str(op)).read()
	webbrowser.open(uop)
