import sys
import os
			
class solidyne_inet_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Solidyne iNET Server</title>' },
			{ "text" : '<frame name="frLeft" scrolling="NO" id="frLeft" src="QFrLeft.aspx">' },
			{ "text" : '<META HTTP-EQUIV="refresh" content="0; url=/hmi/">' },
			{ "url" : '/hmi/sysapp/QLogin.aspx", "text" : '<form name="form1" method="post" action="QLogin.aspx" id="form1">' },
		]

