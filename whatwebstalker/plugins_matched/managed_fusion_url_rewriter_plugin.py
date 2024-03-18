import sys
import os
			
class managed_fusion_url_rewriter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-rewritten-by]", "regexp" : '/^ManagedFusion \(rewriter; reverse-proxy; +http:\/\/managedfusion\.com\/\)$/ },
			{ "search" : 'headers[x-managedfusion-rewriter-version]", "version" : '/^(.+)$/ },
		]

