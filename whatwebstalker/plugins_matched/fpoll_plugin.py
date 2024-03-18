import sys
import os
			
class fpoll_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<title>Fpoll v([^\s^>]+) AdminCP<\/title>[\s]+<link rel="stylesheet" href="admincp\/css\.css" media="all"\/>/" },
			{ "version" : "/<title>Fpoll v([^\s^>]+) AdminCP<\/title>[\s]+<link rel="stylesheet" href="css\.css" media="all"\/>/" },
			{ "version" : "/<br \/><br \/><hr \/><div style="text-align: center;">&copy 20[\d]{2} Fpoll v([^\s^>]+) \(<a href="http:\/\/www\.phpfront\.com">PHPfront\.com<\/a>\) <\/div><\/body>/" },
		]

