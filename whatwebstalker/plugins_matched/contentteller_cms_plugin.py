import sys
import os
			
class Plugincontentteller_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Esselbach Contentteller CMS" />" },
			{ "version" : "/Powered by <a href="http:\/\/www.contentteller.com">Contentteller&reg; (Business Edition|Standard Edition)<\/a><img src="index.php\?ct=core&amp;action=tasks" alt=" \/>/" },
		]

