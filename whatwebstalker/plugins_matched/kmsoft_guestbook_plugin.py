import sys
import os
			
class kmsoft_guestbook_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<div id="footer">KMSoft Guestbook v ([\d\.]+) Powered by <a href="http:\/\/www.kmsoft.org[\/]*">KMSoft<\/a><\/div>/" },
			{ "version" : "/<title>KMSoft Guestbook v([\d\.]+)[^<]+<\/title>/" },
		]

