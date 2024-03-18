import sys
import os
			
class orca_platform_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '    <meta name="author" content="ORCA Websites"/>' }
			{ "text" : '    <meta name="generator" content="ORCA Platform - http://www.orcawebsites.com"/>' }
			{ "text" : '<a href="http://www.orcawebsites.com/" title="Powered By ORCA Websites">Powered By ORCA Websites</a>' }
			{ "text" : '                <p class="orca">Powered By <a href="http://www.orcawebsites.com/" title="ORCA Websites">ORCA Websites</a></p>' }
			{ "text" : '    <!-- Macro Initialisation - Don\'t Touch! -->' }
	]

