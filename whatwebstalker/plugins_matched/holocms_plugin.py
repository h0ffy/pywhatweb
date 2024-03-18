import sys
import os
			
class holocms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="build" content="([^\ ]+) - [^-]+- HoloCMS" \/>/ }
			{ "text" : '<div id="remember-me-notification" class="bottom-bubble" style="display:none;">' }
			{ "regexp" : '/^Powered by HoloCMS &copy[;]* 2008 Meth0d & Parts by Yifan", "sisija/ }
	]

