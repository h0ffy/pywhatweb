import sys
import os
			
class Pluginamxmodx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "// *NOTE* amx_sql_type specifies the DEFAULT database type which admin.sma will use." },
		]

