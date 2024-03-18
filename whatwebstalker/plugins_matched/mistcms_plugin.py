import sys
import os
			
class Pluginmistcms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class="page">login</div><form method="post" action="mist.php">" },
			{ "text" : "<!-- Powered by MistCMS @ dvondrake.com -->" },
		]
		return(self.rules)

