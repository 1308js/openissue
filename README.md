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
	Number of total open issues :                        somenumber
	Number of  issued  opened within 24 hours:           somenumber
	Number of issues opened between 24 hours and 7 days: somenumber
	Number of issues opened more than 7 days ago:        somenumber
	
Next:
	After this it will ask you whether you want to continue or not
#############################################
This is a command line utility, this can be tested on any system having python 2.7 installed.
########################################
Changes or modification that can be made for this
	1. Make a working web app for the same as it's command line utility
	2. This method uses web scrapping, but github APIs can be used for this purpose as well.
	

