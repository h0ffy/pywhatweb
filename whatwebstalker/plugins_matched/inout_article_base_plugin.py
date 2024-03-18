import sys
import os
			
class inout_article_base_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "function trim(stringValue){return stringValue.replace(/(^\s*|\s*$)/", "");}", "certainty" : "75 },
			{ "text" : "<title>Inout Article Base - Admin Area</title>" },
			{ "text" : "<title>Inout ArticleBase - Login</title>" },
			{ "text" : " href="http://www.inoutscripts.com/?r=0">Powered by Inoutscripts</a>", "certainty" : "75 },
		]

