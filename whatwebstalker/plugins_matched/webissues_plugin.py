import sys
import os
			
class Pluginwebissues_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="header-right">[\s]+WebIssues ([^\s]+) \| <a href=/" },
			{ "text" : "<div><input type="hidden" name="__formId" id="field-login-__formId" value="login" />" },
		]
		return(self.rules)

