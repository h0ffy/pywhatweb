import sys
import os
			
class nabble_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div class="nabble" id="nabble">' }
			{ "text" : 'Powered by <a href="http://www.nabble.com/" target="_top" title="Free forum and other embeddable web apps">Nabble</a>' }
			{ "text" : '<table class="footer-table shaded-bg-color">' }
		]

