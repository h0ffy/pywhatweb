import sys
import os
			
class blogger_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta content='blogger' name='generator'/>"}
			{ "name" : 'Powered by link", "regexp" : '/<a href="http:\/\/www.blogger.com"><img [^>]* alt="Powered by Blogger"><\/a>}
	]

