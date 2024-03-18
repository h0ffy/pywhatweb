import sys
import os
			
class qcodo_development_framework_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<b>PHP Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Zend Engine Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Qcodo Version:<\/b> ([^\(]+) \([^\(]+\)<br \/>/", "string" : 'Error" }
		]

