import sys
import os
			
class Pluginmno_go_search_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by mnoGoSearch .{3} free web search engine software},
			{ "certainty" : "75", "regexp" : "/<title>mnoGoSearch:},
		]
		return(self.rules)

