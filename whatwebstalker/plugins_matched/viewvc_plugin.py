import sys
import os
			
class viewvc_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>ViewVC Repository Listing</title>" },
			{ "text" : "<!-- ViewVC :: http://www.viewvc.org/ -->" },
			{ "text" : "<!-- ViewCVS -- http://viewcvs.sourceforge.net/" },
			{ "version" : "%r{Powered by <a href="http://(viewcvs.sourceforge.net|viewvc.tigris.org)/">(ViewCVS|ViewVC) ([^<]+)</a></td>}", "offset" : "2 },
			{ "version" : "/<meta name="generator" content="View(VC|CVS) ([^"]+)"/", "offset" : "1 },
		]

