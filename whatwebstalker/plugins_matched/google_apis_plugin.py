import sys
import os
			
class google_apis_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<script[^>]+src[\s]*=[\s]*["|']?http:\/\/www.google.com\/jsapi[^>]*>[\s]*<\/script[\s]*>/i", "string" : "Dynamic" },
			{ "string" : /<script[^>]+src[\s]*=[\s]*["|']?http:\/\/ajax.googleapis.com\/([a-zA-Z0-9\/\.-_]+)["|']?[^>]*>[\s]*<\/script[\s]*>/i },
		]

