import sys
import os
			
class Pluginqcubed_development_framework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="codeVersion">QCubed Development Framework ([^\(]+) \([^\)]+\)<\/div>/" },
			{ "version" : "/<b>PHP Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Zend Engine Version:<\/b> [^;]+;&nbsp;&nbsp;<b>QCubed Version:<\/b> ([^\(]+) \([^\(]+\)<br \/>/" },
		]
		return(self.rules)

