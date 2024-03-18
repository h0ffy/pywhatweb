import sys
import os
			
class sabros.us_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "	<title>sabros.us/" },
			{ "text" : "		<p class="powered">powered by: <a title="sabros.us" href="http://sabros.us/">sabros.us</a></p>", "version" : "1.8" },
			{ "text" : "		<p class="powered">powered by: <a title="sabros.us" href="http://sourceforge.net/projects/sabrosus/">sabros.us</a></p>", "version" : "1.7" },
			{ "version" : "/	<meta name="generator" content="sabros.us ([\d\.]+)" \/>/" },
		]

