import sys
import os
			
class m2soft_rdserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>M2Soft Report Designer Server</title>' }
			{ "url" : '/RDServer/rdagent.jsp", "version" : '/<font face="Verdana" size=2>\s+<li>Server version : ([^\s]+)/ }
			{ "search" : 'headers[writereportlog]", "regexp" : '/^FALSE$/ }
			{ "search" : 'headers[server]", "version" : '/^RDServer\/([^\s]+)$/ }
	]

