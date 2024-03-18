import sys
import os
			
class dota_openstats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="dota OpenStats" />' }
			{ "text" : '<meta name="copyright" content="openstats.iz.rs" />' }
			{ "text" : '<img alt='' width='16' height='16' style='vertical-align:middle' src='./style/dota/img/logo.png' />" }
			{ "string" : /&copy; (20[\d]{2}) Powered by <a target="_blank" href="http:\/\/openstats\.iz\.rs">DotA OpenStats<\/a>/ }
		]

