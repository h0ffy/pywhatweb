import sys
import os
			
class Plugindt_centrepiece_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "	<meta name="generator" content="DT Centrepiece - www.dt.net.nz/centrepiece/" />" },
			{ "text" : "<a href="http://www.dt.net.nz/centrepiece/" target="_blank">Powered By DT Centrepiece</a>" },
		]

