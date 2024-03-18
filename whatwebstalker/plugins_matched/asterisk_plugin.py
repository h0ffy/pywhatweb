import sys
import os
			
class Pluginasterisk_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/static/index.html", "regexp" : "/Your browser should automatically go to the configuration page\.[\s]+<br>[\s]+Or you can <a href="config\/cfgbasic\.html">click here<\/a>[\s]+<br>/" },
			{ "search" : "headers[server]", "regexp" : "/^Asterisk\//" },
			{ "search" : "headers[server]", "version" : "/^Asterisk\/(.+)$/" },
			{ "regexp" : "/<!--[\s]+\* Asterisk-GUI -[\s]+an Asterisk configuration interface/" },
			{ "text" : "<link href="stylesheets/cfgbasic.css" media="all" rel="Stylesheet" type="text/css" />" },
			{ "url" : "/static/config/index.html", "text" : "<div id="ACTIVE_CONTENT"><noscript>You need to enable Javascript in your browser !!</noscript></div>" },
			{ "url" : "/static/config/js/astman.js", "module" : /		version : "([^']+)' \/\/ gui version/" },
		]
		return(self.rules)

