from HTMLParser import HTMLParser
import urllib.request 
while(1):
	url=raw_input("Enter the public github profile to check open issues")
	r=request.urlopen(url)
	bytecode=r.read()
	print bytecode


