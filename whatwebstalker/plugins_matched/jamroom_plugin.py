import sys
import os
			
class jamroom_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<input type="text" name="search_string" class="jform s_input" style="width:300px;">' }
			{ "text" : '<meta name="designer" content="Talldude Networks", "LLC.">' }
			{ "regexp" : '/<a href="http:\/\/www.jamroom.net"><img src="[^"]*" alt="Powered by Jamroom - the Powerful Social Media Platform" title="Powered by Jamroom - the Powerful Social Media Platform" border="0"><\/a>/ }
			{ "version" : '/<meta name="generator" content="Jamroom ([\d\.]+)">/ }
		]

