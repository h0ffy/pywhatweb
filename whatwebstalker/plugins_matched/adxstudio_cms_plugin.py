import sys
import os
			
class Pluginadxstudio_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "Set-cookie Header", "search" : "headers[set-cookie]", "regexp" : "/anonprofile/i},
			{ "text" : "/PoweredByADX.gif'},
			{ "text" : "alt="Powered by Adxstudio"'},
			{ "text" : "/poweredbyadx.png'},
		]
		return(self.rules)

