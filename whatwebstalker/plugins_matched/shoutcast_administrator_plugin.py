import sys
import os
			
class Pluginshoutcast_administrator_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>SHOUTcast Administrator</title>" },
			{ "regexp" : "/<tr><td><font class=ltv>Written by Stephen 'Tag Loomis", "Tom Pepper and Justin Frankel<\/font><\/td><\/tr><\/table><\/td><\/tr><tr><td nowrap colspan=5 align=center><font class=ST><b><a href="http:\/\/www.shoutcast.com\/disclaimer.phtml">Copyright Nullsoft Inc<\/a>[<a href="\/llamacookie">.<\/a>]* 1998-[0-9]{4}<\/b><\/font><\/td><\/tr><\/table><\/font><\/body><\/html>/" },
		]
		return(self.rules)

