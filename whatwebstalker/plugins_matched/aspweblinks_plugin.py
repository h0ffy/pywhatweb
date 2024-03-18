import sys
import os
			
class aspweblinks_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered By aspWebLinks ([\d\.]+) from <A[^>]*HREF=["']http:\/\/www.fullrevolution.com[^>]*>Full Revolution", "Inc.<\/A>/ }
			{ "version" : '/<A[^>]*HREF=["']http:\/\/www.fullrevolution.com[^>]*>Powered By aspWebLinks ([\d\.]+)<\/A>/ }
			{ "version" : '/<title>aspWebLinks ([\d\.]+)<\/title>/ }
		]

