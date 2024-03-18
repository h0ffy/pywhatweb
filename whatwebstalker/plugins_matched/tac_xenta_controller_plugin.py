import sys
import os
			
class tac_xenta_controller_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<html><body><script>var url="https://"+location.hostname+"/www/index/Slogin.html";location.href=url;</script></body></html>" },
			{ "regexp" : "/^TAC\/Xenta/", "search" : "headers[server]" },
			{ "model" : "/^TAC\/Xenta([\d]{3}|[\d]{3}-[A-Z]{3}) [\d\.]{4}/", "search" : "headers[server]" },
			{ "firmware" : "/^TAC\/Xenta[^\ ]+ ([\d\.]{4})/", "search" : "headers[server]" },
		]

