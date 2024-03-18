import sys
import os
			
class red_lion_hmi_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<td><font face=tahoma size="2">Display a view of the HMI\'s display and keyboard.&nbsp;&nbsp;&nbsp;</font></td>" },
			{ "text" : "<p><font face=tahoma size=1>Powered by <a href=http://www.redlion.net>Red Lion</a>.</font></p>" },
		]

