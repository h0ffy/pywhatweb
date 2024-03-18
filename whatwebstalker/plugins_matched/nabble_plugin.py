import sys
import os
			
class Pluginnabble_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class="nabble" id="nabble">" },
			{ "text" : "Powered by <a href="http://www.nabble.com/" target="_top" title="Free forum and other embeddable web apps">Nabble</a>" },
			{ "text" : "<table class="footer-table shaded-bg-color">" },
		]
		return(self.rules)

