import sys
import os
			
class Pluginqcodo_development_framework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<b>PHP Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Zend Engine Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Qcodo Version:<\/b> ([^\(]+) \([^\(]+\)<br \/>/", "string" : "Error" },
		]
		return(self.rules)

