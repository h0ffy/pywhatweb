import sys
import os
			
class geeklog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered By <a href="http://www.geeklog.net/">Geeklog</a>' },
			{ "text" : 'Powered By <a class="footer" href="http://www.geeklog.net/">GeekLog</a>' },
			{ "text" : '<!--If you want the splash", "uncomment the last line. If you want no splash", "make sure it is commented out.-->' },
			{ "version" : '/Powered by <a href="http:\/\/www.geeklog.net\/">Geeklog ([\d\.a-z]{1,10})<\/a>/ },
		]

