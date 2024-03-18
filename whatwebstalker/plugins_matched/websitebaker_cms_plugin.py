import sys
import os
			
class websitebaker_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="WebsiteBaker ([\d\.]+) CMS; www\.websitebaker2?\.org"[\s]?\/?>/ }
			{ "regexp" : '/[pP]owered by <a href="http:\/\/www\.websitebaker2?\.org"( target="_blank")?>WebsiteBaker<\/a>/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/wb_[\d]{4}_session_id=[^;]+;/ }
			{ "search" : 'headers[set-cookie]", "regexp" : '/wb_session_id=[^;]+;/", "certainty" : '75 }
	]
