import sys
import os
			
class phpfm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/Powered by <a href='http:\/\/phpfm.zalon.dk\/' target='_new' class='bottom'>PHPFM<\/a> ([\d\.]+)<\/td>/" },
		]

