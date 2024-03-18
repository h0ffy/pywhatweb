import sys
import os
			
class brewblogger_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<div id="footer">Content &copy; 2011 [^\n]+ &mdash; BrewBlogger ([^\s]+) (Personal Edition|Club Edition) developed by <a href="http:\/\/www\.zkdigital\.com" target="_blank">zkdigital\.com<\/a>/" },
			{ "string" : /<div id="footer">Content &copy; 2011 [^\n]+ &mdash; BrewBlogger ([^\s]+) (Personal Edition|Club Edition) developed by <a href="http:\/\/www\.zkdigital\.com" target="_blank">zkdigital\.com<\/a>/", "offset" : "1 },
		]

