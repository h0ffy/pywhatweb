import sys
import os
			
class Plugincitrix_metaframe_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Copyright \(c\) [\d]+ - [\d]+ Citrix Systems", "Inc. All Rights Reserved./" },
			{ "text" : "window.location="/Citrix/MetaFrame";" },
			{ "text" : "<title>MetaFrame Presentation Server Log In</title>" },
		]
		return(self.rules)

