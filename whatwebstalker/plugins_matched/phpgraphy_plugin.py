import sys
import os
			
class phpgraphy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>my phpGraphy site</title>' },
			{ "version" : '/This site is using <a href="http:\/\/phpgraphy\.sourceforge\.net\/">phpGraphy<\/a>\n([^\s]+) - Page generated in [\d\.]+s\.<\/div><!--\/\/footer-->/ },
		]

