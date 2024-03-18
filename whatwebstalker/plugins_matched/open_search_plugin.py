import sys
import os
			
class Pluginopen_search_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<link[^>]+href[\s]*=[\s]*["']([^'^"^>]+)["'][^>]+type[\s]*=[\s]*["']?application\/opensearchdescription\+xml['"]?[^>]*>/i },
			{ "string" : /<link[^>]+type[\s]*=[\s]*["']?application\/opensearchdescription\+xml['"]?[^>]+href[\s]*=[\s]*["']([^'^"^>]+)["'][^>]*>/i },
		]

