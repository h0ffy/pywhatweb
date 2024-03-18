import sys
import os
			
class Pluginempirecms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : " - Powered by EmpireCMS</title>" },
		]
		return(self.rules)

