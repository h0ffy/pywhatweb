import sys
import os
			
class Pluginwebcompro_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-powered-by]", "version" : "/WEBCOMpro CMS (.+)$/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/wcp_userid=[\d]{10};/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/wcp_userid_temporary=[\d]{10};/" },
			{ "regexp" : "/<meta name="generator" content="WEBCOMpro CMS ([^\s]+) . Patrick Heyer", "www\.webcompro-cms\.com">/" },
		]
		return(self.rules)

