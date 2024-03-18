import sys
import os
			
class Pluginsyntaxcms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.syntaxcms.org">SyntaxCMS</a></div>" },
			{ "text" : "powered by <a href="http://www.syntaxcms.org/" title="SyntaxCMS">SyntaxCMS</a></div>" },
		]
		return(self.rules)

