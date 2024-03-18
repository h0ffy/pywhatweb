import sys
import os
			
class Pluginempirecms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : " - Powered by EmpireCMS</title>" },
		]

