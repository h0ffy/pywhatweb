import sys
import os
			
class wordpress_spamfree_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<!-- Protected by \(WP-SpamFree\) v([\d\.]+) :: JS BEGIN -->/ }
		]

