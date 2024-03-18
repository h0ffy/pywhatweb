import sys
import os
			
class maxmind_geoip_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script type="(JavaScript|text\/javascript)" src="(http:\/\/)?j\.maxmind\.com\/app\/(country|geoip)\.js"><\/script>/ },
		]

