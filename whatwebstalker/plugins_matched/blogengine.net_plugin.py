import sys
import os
			
class blogengine.net_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<link rel="shortcut icon" href="pics/blogengine.ico" type="image/x-icon" />' }
			{ "regexp" : '/Powered by[\r\n\s]*<a href="http:\/\/www.dotnetblogengine.net[\/]?"[^>]*>BlogEngine.NET<\/a>/ }
			{ "version" : '/Powered by[\r\n\s]*<a href="http:\/\/www.dotnetblogengine.net[\/]?"[^>]*>BlogEngine.NET<\/a>[\r\n\s]*([\d\.]+)/ }
		]

