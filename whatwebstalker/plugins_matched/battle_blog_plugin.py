import sys
import os
			
class Pluginbattle_blog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<br /><br /><font face="arial" size="1">Powered by <a href="http://www.battleblog.com">Battle Blog</a></font>" },
			{ "text" : "<title>Battle Blog Login</title> '},
			{ "text" : "<form name = "UserInfoCollect" action = "authenticate.asp" method = "post">" },
			{ "text" : "<table width = "10%" cellpadding = "5" style = "border-style: solid; border-color: #000000; border-width: 1px;">" },
		]

