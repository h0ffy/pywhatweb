import sys
import os
			
class open_graph_protocol_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<meta[^>]+property="og:title"[^>]*>/i }
			{ "version" : '/<meta[^>]+property="og:type"[^>]+content="([^"^>]+)"/ }
			{ "account" : '/<meta[^>]+property="fb:admins"[^>]+content="([^"^>]+)"/ }
			{ "module" : /<meta[^>]+property="fb:app_id"[^>]+content="([^"^>]+)"/ }
	]

