import sys
import os
			
class Pluginlantronix_device_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "url" : "/summary.html", "version" : "/<TITLE>Lantronix ThinWeb Manager ([\d\.]+): Home<\/TITLE>/" },
			{ "url" : "/navigation.html", "version" : "/<img src="logo\.gif" width=129 height=84 border=0 alt="Lantronix ThinWeb Manager ([\d\.]+)"><br>/" },
			{ "url" : "/navigation.html", "model" : "/<font face="Arial,Helvetica" color="#660066"><b>([^<]+)<\/b><\/font><br><br>/" },
			{ "version" : "/^Gordian Embedded([\d\.]+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^Gordian Embedded/", "search" : "headers[server]" },
		]

