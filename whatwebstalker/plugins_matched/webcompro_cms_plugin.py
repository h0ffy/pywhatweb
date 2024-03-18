import sys
import os
			
class webcompro_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-powered-by]", "version" : '/WEBCOMpro CMS (.+)$/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/wcp_userid=[\d]{10};/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/wcp_userid_temporary=[\d]{10};/ }
			{ "regexp" : '/<meta name="generator" content="WEBCOMpro CMS ([^\s]+) . Patrick Heyer", "www\.webcompro-cms\.com">/ }
		]

