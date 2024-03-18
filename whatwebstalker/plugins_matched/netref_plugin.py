import sys
import os
			
class netref_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "Annuaire Netref : http://www.netref.net" },
			{ "version" : "/<a href=['|"]?http:\/\/www.netref.(fr|net)['|"]? class=['|"]?lienp['|"]?[^>]*>Powered by Netref ([\d\.]+) &copy; [0-9]{4}<\/a>/", "offset" : "1 },
		]

