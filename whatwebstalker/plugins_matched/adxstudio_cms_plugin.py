import sys
import os
			
class adxstudio_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'Set-cookie Header", "search" : 'headers[set-cookie]", "regexp" : '/anonprofile/i}
			{ "text" : '/PoweredByADX.gif'}
			{ "text" : 'alt="Powered by Adxstudio"'}
			{ "text" : '/poweredbyadx.png'}
	]

