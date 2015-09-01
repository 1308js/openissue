# openissue
Python utility to get the information about open issues from a public github profile
######################################
Uses :
:~run the file main.py
:~ This will ask you for the github directory link.
Valid directory links that can be given 
	https://github.com/user/directory/issues
	http://github.com/user/directory/issues
	https://www.github.com/user/directory/issues
	http://www.github.com/user/directory/issues
	https://github.com/user/directory
	https://github.com/user/directory/

Output format:
	Number of total open issues :                        234
	Number of  issued  opened within 24 hours:           2
	Number of issues opened between 24 hours and 7 days: 8
	Number of issues opened more than 7 days ago:        224
	
Next:
	After this it will ask you whether you want to continue or not
#############################################
This is a command line utility so I don't have any link for running application
But this can be tested on any system having python 2.7 installed
########################################
Changes or modification I would make if I am given more time:
	1. I will make a working web app for the same	
	2. I have used urllib2 for scrapping the html reponse page and then used regular expressions to extract the desired data But I would like to try using APIs provided bu github if possible to get the desired output.
	

