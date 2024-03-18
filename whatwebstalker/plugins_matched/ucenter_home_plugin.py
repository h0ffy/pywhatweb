import sys
import os
			
class ucenter_home_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by UCenter Home</title>' }
			{ "version" : '/Powered by <a  href="http:\/\/u.discuz.net" target="_blank"><strong>UCenter Home<\/strong><\/a> <span title="[0-9]{8}">([\d\.]+)<\/span>/ }
		]

