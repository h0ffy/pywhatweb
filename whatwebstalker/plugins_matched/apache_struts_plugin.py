import sys
import os
			
class apache_struts_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/org\.apache\.struts\.action\.LOCALE=[^\s]+;/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/org\.apache\.struts\.[^\s]+=[^\s]+;/", "certainty" : '75 },
			{ "search" : 'body", "regexp" : '/<a\s+href=[^>]+org.apache.struts},
			{ "search" : 'all", "version" : '2", "text" : 'org.apache.struts2", "certainty" : '25},
			{ "search" : 'all", "version" : '1", "text" : 'org.apache.struts.", "certainty" : '25},
			{ "regexp" : '/Development mode", "or devMode", "enables extra\s+debugging behaviors and reports to assist developers.  To disable this mode", "set:\s+<pre>\s+  struts.devMode=false/", "string" : 'Development Mode"},
		]

