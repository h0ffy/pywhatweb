import sys
import os
			
class teamviewer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<html><body>This site is running <a href='http://www.TeamViewer.com'>TeamViewer</a>.</body></html>" },
		]

