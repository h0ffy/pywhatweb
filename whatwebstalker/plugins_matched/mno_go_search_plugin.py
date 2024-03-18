import sys
import os
			
class mno_go_search_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by mnoGoSearch .{3} free web search engine software}
			{ "certainty" : '75", "regexp" : '/<title>mnoGoSearch:}
	]

