import sys
import os
			
class citrix_metaframe_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Copyright \(c\) [\d]+ - [\d]+ Citrix Systems", "Inc. All Rights Reserved./ }
			{ "text" : 'window.location="/Citrix/MetaFrame";' }
			{ "text" : '<title>MetaFrame Presentation Server Log In</title>" }
		]

