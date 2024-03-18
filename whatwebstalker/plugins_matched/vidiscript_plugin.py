import sys
import os
			
class Pluginvidiscript_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<span  style="font-size:12px"><a href="http://www.VidiScript.com"><b>Free Open Source Video Script</b></a>&nbsp;Powered By&nbsp;<a href="http://www.VidiScript.com"><b>VidiScript.com</b></a> |    <b>" },
			{ "text" : "<a href='http://www.VidiScript.com'><b>Free Video Script</b></a>&nbsp;Powered By&nbsp;<a href='http://www.VidiScript.com'><b>VidiScript.com</b></a>" },
		]

