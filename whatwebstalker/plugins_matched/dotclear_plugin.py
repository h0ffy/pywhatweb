import sys
import os
			
class dotclear_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p>Powered by <a href="http://dotclear.org/">Dotclear</a></p>' },
			{ "text" : '<!-- End #d-content -->' },
			{ "text" : '<!-- End #blogextra -->' },
			{ "text" : '<a href="#search">To search</a>' },
			{ "text" : '<p class="post-info-co">' },
		]

