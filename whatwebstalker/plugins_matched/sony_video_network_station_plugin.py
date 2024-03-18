import sys
import os
			
class Pluginsony_video_network_station_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>SONY SNT-V304 Video Network Station</TITLE>", "version" : "SNT-V304" },
			{ "text" : "<TITLE>SONY Video Network Station</TITLE>" },
		]
		return(self.rules)

