import sys
import os
			
class putty_log_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/=~=~=~=~=~=~=~=~=~=~=~= PuTTY log [0-9]{4}.[0-9]{2}.[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} =~=~=~=~=~=~=~=~=~=~=~=/ }
	]

