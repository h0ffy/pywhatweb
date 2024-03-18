import sys
import os
			
class osticket_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id="nav">[\s]+<ul id="sub_nav">[\s]+<li>osTicket version ([^\-^<]+) - Basic installation<\/li>[\s]+<\/ul>[\s]+<\/div>/ },
			{ "regexp" : '/<title>osTicket Installer<\/title>[\s]+<link rel="stylesheet" href="style\.css" media="screen">/ },
			{ "regexp" : '/<a id="powered_by" href="http:\/\/osticket\.com"><img src="\.\/images\/poweredby\.jpg" width="126" height="23" alt="Powered by osTicket"><\/a><\/div>/ },
		]

