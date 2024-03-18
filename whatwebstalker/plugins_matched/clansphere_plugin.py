import sys
import os
			
class clansphere_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>ClanSphere - News</title>' }
			{ "text" : '<meta name="generator" content="ClanSphere" />' }
			{ "regexp" : '/Powered by <a href="http:\/\/www.csphere.eu[^>]+>Clansphere[\ CSP]*/i }
			{ "regexp" : '/<a href="[\/]*index.php\?mod=clansphere&amp;action=about[^>]+>Powered by Clansphere[\ CSP]*/i }
			{ "regexp" : '/<a href="[\/]*index.php\?mod=clansphere&amp;action=about[^>]+>Clansphere[\ CSP]*/i }
			{ "regexp" : '/powered by <a href="http:\/\/www.clansphere.net[^>]+>ClanSphere Project<\/a>/ }
	]
