import sys
import os
			
class Pluginip_logger_pro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Logdaten - Bitte hier klicken." inurl:"iplog.php?action=show"" },
			{ "version" : "/<br \/><br \/>&nbsp;debilsoft IP-Logger PRO Version ([\d\.]{1,5}) is licensed to [^<]+<\/div><\/body><\/html>/" },
			{ "text" : "<title>debilsoft IP-Logger PRO Besucherdaten</title>" },
		]
		return(self.rules)

