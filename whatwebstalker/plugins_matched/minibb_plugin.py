import sys
import os
			
class Pluginminibb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<td class="tbTransparent txtR"><!--miniBB Copyright link. You are not allowed to remove it if you have not purchased the Commercial License. Refer to COPYING file for more-->" },
			{ "regexp" : "/Powered by <a[^>]+href="http:\/\/www.minibb.(com|net)"[^>]*>miniBB[^<]{0,15}<\/a>/i },
			{ "version" : "/Powered by <a[^>]+href="http:\/\/www.miniBB.(com|net)"[^>]*>miniBB ([^<]{1,7})<\/a>/i", "offset" : "1 },
		]

