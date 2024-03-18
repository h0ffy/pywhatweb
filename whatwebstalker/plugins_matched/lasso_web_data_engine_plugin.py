import sys
import os
			
class lasso_web_data_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "ghdb" : 'filetype:lasso" },
			{ "search" : 'headers[server]", "version" : '/Lasso\/([^\s]+)/ },
		]

