import sys
import os
			
class Pluginsocial_strata_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "ghdb" : "inurl:"/eve/personal?x_myspace_page=profile" "Powered by Social Strata"" },
			{ "text" : "<a href="http://socialstrata.com/landing/goto.php?a=eve" target="_blank">Powered by Social Strata</a>" },
			{ "version" : "/Powered by: <a target="_blank" href="http:\/\/eveforenterprise\.com">Groupee<\/a><SUP>TM<\/SUP> \(version ([\d\.]+)\) from Groupee Inc\./" },
		]

