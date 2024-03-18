import sys
import os
			
class Pluginoracle_primerva_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<!-- @#\$ Copyright Start\s+. 1999 - (20[\d]{2}) Primavera Systems", "Inc\.  All rights reserved\./" },
			{ "text" : "<!-- use the default style sheet only.... we do not know the users locale at this time -->" },
			{ "version" : "/<div class="IntroAreaBuildId" id="BuildId">Version ([^,^\s]+", "Build \d+)(&nbsp;)*<\/div>/" },
			{ "version" : "/<div align="right" id="BuildId">Version ([^,^\s]+", "Build \d+)(&nbsp;)*<\/div>/" },
			{ "text" : "<img src="img/process_meter.gif" border=0 id="progressimage"><br><br>Loading Java Plugin and Security Certificate" },
		]

