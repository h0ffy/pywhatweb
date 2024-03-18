import sys
import os
			
class Pluginopenconf_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.OpenConf.org" target="_blank">OpenConf</a>" },
			{ "version" : "/<div class="powered">Powered by <a href="http:\/\/www\.OpenConf\.com" target="_blank">OpenConf<\/a>(<sup>&reg;<\/sup>)?<!--([^\s]+)-->/", "offset" : "1 },
			{ "version" : "/<script type="text\/javascript" src="openconf\.js\?v=([^\s^"]+)"><\/script>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/OPENCONF=[^;]+;/" },
		]

