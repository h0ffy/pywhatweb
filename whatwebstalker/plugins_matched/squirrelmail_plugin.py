import sys
import os
			
class squirrelmail_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'default title", "text" : '<title>SquirrelMail - Login</title>"}
			{ "name" : 'js function", "text" : 'function squirrelmail_loginpage_onload()"}
			{ "name" : 'css comment", "text" : '/* avoid stupid IE6 bug with frames and scrollbars */'}
			{ "text" : '<b>SquirrelMail Login</b>'}
		]

