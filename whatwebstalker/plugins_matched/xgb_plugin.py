import sys
import os
			
class xgb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '	<title>xGB</title>' }
			{ "text" : '<!-- start xGB dynamic content -->' }
			{ "text" : 'powered by <a href='http://www.x-gfx.de' target='blank' title='Script by x-gfx.de'>xGB" }
			{ "version" : '/<p align='center'><span id='copyright'>\[ powered by <a href='http:\/\/www.x-gfx.de' target='blank' title='Script by x-gfx.de'>xGB ([\d\.]+)<\/a>/ }
	]

