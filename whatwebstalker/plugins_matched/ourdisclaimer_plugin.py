import sys
import os
			
class ourdisclaimer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<a[^>]+href[\s]*=[\s]*"http:\/\/ourdisclaimer.com\/\?i=([^\"]+)/i },
			{ "version" : "/<iframe[^>]+src[\s]*=[\s]*"http:\/\/ourdisclaimer.com\/\?i=([^\"]+)/i },
		]

