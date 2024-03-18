import sys
import os
			
class Pluginsamsung_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "var debugMode = ("$$GSI_TCPIP_IP_ADDR$$".indexOf(".")" },
		]

