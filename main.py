#!/usr/bin/python
import urllib2   #module for http requests
import re 		#module for regular expression
import datetime  #module for time function
#fucntion to check the validity of the url
def checkUrl(url):
	a='((http://)|(https://))?(www.)?(github.com/)'  ##regular expression for valid url according to app
	a=re.compile(a)									
	if(a.match(url)):							
		return 1   									# return success if valid url
	else:
		return 0			
def useUrl(url):									##function to extract useful part of url
	a='((http://)|(https://))?(www.)?(github.com)'   
	url=re.sub(a,'',url)
	if(url[len(url)-7:]=='/issues'):  ##check if the url consist issue part or not
		pass	
	else:
		if(url[len(url)-1]=='/'):
			url+='issues'		
		else:
			url+='/issues'			
	return url

while(1):											#Infinite loop for cheking different urls						
	url=raw_input("Enter the public github profile to check open issues\n")    ##input from user for url
	if(checkUrl(url)):											##if url is valid
		url='https://github.com'+useUrl(url)					##modifying url according to our needs
		try:
			r=urllib2.urlopen(url)							
			bytecode=r.read()									##reading the response of the request
			r.close()											
		except urllib2.HTTPError,error:
			bytecode=error.read()

		bytecode=bytecode.split('\n')						##adjusting the response according to needs by removing new line
		newstr=''	
		for i in  bytecode:
			newstr+=i.strip()								##final response to match with our needs
		## pattern to match for finding open issues			
		openmatch=	'(<a href="'+useUrl(url)+'\?q=is%3Aopen\+is%3Aissue" class="btn-link selected"><span class="octicon octicon-issue-opened"></span>)([0-9]+)( Open</a>)'	
		total=0   ##total number of open issues
		a=re.search(openmatch,newstr)
		if(a):
			total=int(a.group(2))
		print "Number of total open issues :                        %d"%total
		j=1  ####index for checking next page of open issues
		today=0 ###number of issues opened in last 24 hours
		thisWeek=0  ##number of issues  opened in last week
		old=0 		###number of issues opened beforea week
		if(total!=0):		##if there are some opened issues
			while(1): 		###loop for checking all the opened issues	
				url=url+'?page='+str(j)+'&q=is%3Aissue+is%3Aopen'	##modifies url for going to next page of opened issues
				j+=1          ###incrementing the page by 1
				r=urllib2.urlopen(url)
				bytecode=r.read()
				r.close()
				url=''
				bytecode=bytecode.split('\n')
				newstr=''
				for i in  bytecode:
					newstr+=i.strip()
				openmatch='(<span class="issue-meta-section opened-by">#)'+'([0-9]+)'+'(opened <time datetime=")'+'(.{20})'+'(" is="relative-time">)'+'([a-zA-Z0-9,\s]+)'+'(</time>)'
				a=re.findall(openmatch,newstr)

				currentTime=datetime.datetime.now()  ###current datetime in GMT +5:30
				
				for k in a:
					###getting the time of the issue when it was last openedin GMT +00 
					openedTime=datetime.datetime(int(k[3][:4]),int(k[3][5:7]),int(k[3][8:10]),int(k[3][11:13]),int(k[3][14:16]),int(k[3][17:19]))
					###calcualting the time difference in hour
					timeDifference=(currentTime-openedTime).days*24+(currentTime-openedTime).seconds/3600-5.5
					###if number difference between current and last opened is under 24 hours
					if(timeDifference<=24):
						today+=1
					###if number difference between current and last opened is under 1 Week						
					elif(timeDifference>=24 and timeDifference<=168):
						thisWeek+=1
					###if number difference between current and last opened is older than 1 week						
					else:
						old=total-today-thisWeek
						break									
					
				if(old!=0):
					break
				elif(today+thisWeek+old==total):
					break
		print "Number of  issued  opened within 24 hours:           %d"	%today
		print "Number of issues opened between 24 hours and 7 days: %d"%thisWeek
		print "Number of issues opened more than 7 days ago:        %d"%old
	else:
		print "Wrong url Please try again"		
	###user response for continueing programm
	response=raw_input("press y/Y to continue or any other key to exit\n")
	if(response=='y' or response=='Y'):
		continue
	else:
		break				

		
		
			


