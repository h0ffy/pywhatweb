import sys
import os
			
class zoom_search_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<center><p><small>Search powered by <a href="http://www.wrensoft.com/zoom/" target="_blank"><b>Zoom Search Engine</b></a></small></p></center>' }
			{ "version" : '/<!--Zoom Search Engine Version ([\d\.]+ \([\d]+\) [A-Z]{3})-->/ }
			{ "version" : '/<!--Zoom Search Engine Version ([\d\.]+ \([\d]+\))-->/ }
		]

