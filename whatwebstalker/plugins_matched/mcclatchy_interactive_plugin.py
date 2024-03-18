import sys
import os
			
class Pluginmcclatchy_interactive_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : " %r{<script type="text/javascript" src="http://media.\w+.com/mistats/mianalytics.js"></script>} },
			{ "text" :  'miAppControler contains master settings that can be used to quickly disable" },
		]

