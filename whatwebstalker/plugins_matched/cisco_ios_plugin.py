import sys
import os
			
class Plugincisco_ios_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : "Dir", "    "regexp" : "/<input type="hidden" name="DIRINFO" value="\s+Directory of archive:\//" },
			{ "string" : "DirFail", "regexp" : "/<input type="hidden" name="DIRINFO" value="\s*(Command authorization failed|% Authorization failed)/" },
			{ "search" : "headers[server]", "regexp" : "/^cisco-IOS/" },
		]

