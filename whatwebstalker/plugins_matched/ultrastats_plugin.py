import sys
import os
			
class ultrastats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<DIV align=center>Powered by Ultrastats' },
			{ "text" : '<img src="./images/main/ultrastatslogo.png" width="300" height="200" name="ultrastats_logo" align="center">' },
			{ "regexp" : '/<title>Ultrastats :: [^<]+<\/title>/i },
			{ "text" : '<title>UltraStats :: Critical Error occured</title>' },
			{ "version" : '/ &nbsp;<a href="http:\/\/www.ultrastats.org[\/]?" target="_blank">Ultrastats<\/a> Version ([\d\.]+)/i },
		]

