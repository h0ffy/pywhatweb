import sys
import os
			
class Pluginmaxmind_geoip_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script type="(JavaScript|text\/javascript)" src="(http:\/\/)?j\.maxmind\.com\/app\/(country|geoip)\.js"><\/script>/" },
		]
		return(self.rules)

