import sys
import os
			
class Pluginmanageengine_applications_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- This comment is for Instant Gratification to work applications.do -->" },
			{ "text" : "<SCRIPT LANGUAGE="JavaScript1.2" SRC="/template/appmanager.js"></SCRIPT>" },
			{ "text" : "<title>Applications Manager Login Screen</title>" },
			{ "version" : "/<td>Applications Manager \((Build No:[\d]+)\) &nbsp;&nbsp;&nbsp;&nbsp;Number of Monitor\(s\) : /" },
			{ "url" : "images/am_logo.gif", "md5" : "4454cf4db9355b0e26b98cc354213c56" },
		]

