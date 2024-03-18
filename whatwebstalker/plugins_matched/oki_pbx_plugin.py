import sys
import os
			
class Pluginoki_pbx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>IPstageMaintenanceConsole(PBX)</title>" },
			{ "text" : "<APPLET CODE="DavisBar.class" ARCHIVE="ipstage.jar"" },
			{ "text" : "<PARAM NAME="systype"    value="OKI">" },
		]

