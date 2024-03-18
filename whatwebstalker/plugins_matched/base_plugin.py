import sys
import os
			
class base_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- Basic Analysis and Security Engine (BASE) -->' },
			{ "version" : '/<!-- Basic Analysis and Security Engine \(BASE\) ([\d\.]+ \([^\)]+\)) -->/ },
		]

