import sys
import os
			
class cgit_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id='cgit'><table id='header'>" },
			{ "text" : '<link rel='stylesheet' type='text/css' href='/cgit.css'/>" },
			{ "text" : '<div class='footer'>Copyright &copy; 2000 &ndash; 20[\d]{2} Jason A. Donenfeld. All Rights Reserved.</div>" },
		]

