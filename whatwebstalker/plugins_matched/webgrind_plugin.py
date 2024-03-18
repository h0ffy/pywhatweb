import sys
import os
			
class Pluginwebgrind_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<span id="invocation_sum"></span> different functions called in <span id="runtime_sum"></span> milliseconds (<span id="runs"></span> runs", "<span id="shown_sum"></span> shown)" },
			{ "text" : "<img class="list_reload" src="img/reload.png" onclick="reloadFilelist()">" },
			{ "version" : "/<h1>webgrind<sup style="font-size:10px">v([^<]+)<\/sup><\/h1>/" },
		]

