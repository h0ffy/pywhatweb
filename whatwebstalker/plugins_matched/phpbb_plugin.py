import sys
import os
			
class Pluginphpbb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- link rel="stylesheet" href="templates/subSilver/subSilver.css'},
			{ "text" : "/images/logo_phpBB.gif", "certainty" : "75},
			{ "text" : "We request you retain the full copyright notice below including the link to www.phpbb.com.'},
			{ "search" : "headers[set-cookie]", "version" : "/phpbb([\d])mysql_(data=a%3A|sid=[a-f\d]{32};)/" },
		]

