import sys
import os
			
class cloudfront_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "status" : '403", "text" : '<html><body>Sorry", "invalid request</body></html>" },
			{ "search" : 'headers[server]", "regexp" : '/^CloudFront/ },
			{ "search" : 'headers[x-cache]", "regexp" : '/^Error from cloudfront/ },
		]

