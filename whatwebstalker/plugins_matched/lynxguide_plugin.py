import sys
import os
			
class lynxguide_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Login to LynxGuide Server</title>' },
			{ "text" : 'Use subject to <a href="/cgi/help/license.htm">license agreement</a></span>' },
			{ "search" : 'headers[set-cookie]", "regexp" : '/Access_Num=[^;]+;/ },
		]

