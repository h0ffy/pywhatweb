import sys
import os
			
class Pluginsyntaxcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.syntaxcms.org">SyntaxCMS</a></div>" },
			{ "text" : "powered by <a href="http://www.syntaxcms.org/" title="SyntaxCMS">SyntaxCMS</a></div>" },
		]

