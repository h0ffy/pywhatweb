import sys
import os
			
class 6kbbs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="6KBBS v([^"^>]+)" \/>/ }
			{ "regexp" : '/<meta name="copyright" content="2003-20[\d]{2} 6KBBS" \/>/ }
			{ "text" : '<meta name="author" content="www.6kbbs.com" />' }
			{ "version" : '/Powered by <a href="http:\/\/www\.6kbbs\.com" target="_blank">6kbbs V([^<^\s]+)<\/a> &copy; 2003-20[\d]{2}/ }
	]

