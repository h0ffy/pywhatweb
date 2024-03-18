import sys
import os
			
class Pluginnovell_ichain_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<td height="20" align="center"><img height="8" width="445" src="ICHAINErrors/alertbar.gif"></td>" },
			{ "text" : "<HTML><HEAD><TITLE>Novell iChain</TITLE></HEAD><BODY><b><p>Your old browser does not support a 302 Redirect.</b></BODY></HTML>" },
			{ "text" : "<HTML><HEAD><TITLE>Novell Proxy</TITLE></HEAD><BODY><b><p>HTTP request is being redirected to HTTPS.</b></BODY></HTML>" },
			{ "search" : "headers[X-Error-Info]", "regexp" : "/Host name received is not for this web site/" },
		]

