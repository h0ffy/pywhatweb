import sys
import os
			
class Pluginourdisclaimer_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a[^>]+href[\s]*=[\s]*"http:\/\/ourdisclaimer.com\/\?i=([^\"]+)/i },
			{ "version" : "/<iframe[^>]+src[\s]*=[\s]*"http:\/\/ourdisclaimer.com\/\?i=([^\"]+)/i },
		]
		return(self.rules)

