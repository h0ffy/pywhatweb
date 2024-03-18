import sys
import os
			
class revsense_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '				<li><a href="http://www.revsense.com.au/"><strong>RevSense</strong> - Powered by RevSense Ads</a></li>' },
			{ "text" : '	<!-- You cannot remove this powered by link without receiving permission from W3matter.com -->' },
			{ "regexp" : '/	<font size=1><a>Powered by Revsense &trade;<\/a> &copy; [0-9]{4} W3matter LLC<\/font>/ },
			{ "regexp" : '/	<font size=1><a href="http:\/\/www.w3matter.com">Powered by Revsense &trade;<\/a> &copy; [0-9]{4} W3matter LLC<\/font>/ },
		]

