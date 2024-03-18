import sys
import os
			
class esvon_classifieds_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- DO NOT REMOVE OR EDIT THIS LINE", "DOING SO WILL RESULT IN COPYRIGHT VIOLATIONS UNLESS YOU PURCHASED "POWERED BY" REMOVAL OPTION -->' }
			{ "regexp" : '/Powered by Esvon <a href='http:\/\/www.esvon.com\/pg\/products\/p_classifieds\/' target="_blank"[^>]+>Classifieds<\/a>/ }
	]

