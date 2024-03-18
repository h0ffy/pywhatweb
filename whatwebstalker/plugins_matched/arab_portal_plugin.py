import sys
import os
			
class arab_portal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<META NAME="COPYRIGHT" CONTENT="Copyright[^\>]*by Arab[\s]*Portal"/ },
			{ "version" : '/<META content="[^>]*Powered by: Arab Portal v([\d\.]+)", "Copyright[^>]*" name="description">/ },
			{ "version" : '/<center><font size=2>Powered by: Arab[\s]*Portal v([\d\.]+)[\s]*", "Copyright/ },
		]

