import sys
import os
			
class yamamah_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<p>Copyright &copy; [\d]{4}  All rights reserved. Powered By : <a href="http:\/\/www.yamamah.org" title="Yamamah">Yamamah Version ([\d\.]{1,5})<\/a><\/p>/" },
			{ "text" : "<meta name="Author" content="Majed Al-Mulihani - majed@modernsys.net" />" },
			{ "text" : "<meta name="Description" content="Yamamah is free photo gallery cms" />" },
		]

