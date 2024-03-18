import sys
import os
			
class mistcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div class="page">login</div><form method="post" action="mist.php">' }
			{ "text" : '<!-- Powered by MistCMS @ dvondrake.com -->' }
	]

