import sys
import os
			
class Plugindatum_tymserve_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "model" : "/<H2 ALIGN=CENTER>Datum TymServe ([^\s]+) Virtual Viewpoint<\/H2><P><!-- This is a clock that shows the system time -->/" },
			{ "search" : "headers[server]", "version" : "/^DATM\/([\d\.]{1,3})$/" },
		]

