import sys
import os
			
class Pluginsmartcds_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<img border=0 src="http://www.globaldawin.com/capcds/refresh.gif" width="13" height="16"" },
			{ "regexp" : "/^smartcds/", "search" : "headers[server]" },
			{ "version" : "/^smartcds\/([^\s]+)/", "search" : "headers[server]" },
			{ "version" : "/^Version:([^\s]+)$/", "search" : "headers[smartcds]" },
			{ "string" : /^(.*)$/", "search" : "headers[x-smartcds-error]" },
		]

