import sys
import os
			
class qcubed_development_framework_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<div id="codeVersion">QCubed Development Framework ([^\(]+) \([^\)]+\)<\/div>/" },
			{ "version" : "/<b>PHP Version:<\/b> [^;]+;&nbsp;&nbsp;<b>Zend Engine Version:<\/b> [^;]+;&nbsp;&nbsp;<b>QCubed Version:<\/b> ([^\(]+) \([^\(]+\)<br \/>/" },
		]

