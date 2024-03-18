import sys
import os
			
class sun_java_system_calendar_express_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<title>Sun Java\[tm\] System Calendar Express ([^<]+)<\/title>/ }
			{ "text" : '<TITLE>Sun Java[tm] System Calendar Express</TITLE>' }
			{ "text" : '<img src="imx/login-logo.gif" width="186" height="79" alt="Sun Microsystems", "Inc.">' }
			{ "url" : '/imx/login-logo.gif", "md5" : 'b86a7d65b64efa500048d9fc2840c390" }
	]

