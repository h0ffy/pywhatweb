import sys
import os
			
class sphinx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/Created using <a href="http:\/\/sphinx\.pocoo\.org\/">Sphinx<\/a> ([^\s]+)\./" },
			{ "regexp" : "/<div class="sphinxsidebar">[\s]+<div class="sphinxsidebarwrapper">/" },
		]

