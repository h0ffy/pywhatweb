import sys
import os
			
class pivot_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "25", "text" : "<!-- Includes for Thickbox script -->" },
			{ "text" : "<title>Pivot &#187; setup</title>" },
			{ "text" : "<td width=\'75%\'><input type="text" name="sitename" value="Pivot Powered" size="40" class="input" /></td>" },
			{ "version" : "/<a href="http:\/\/www\.pivotlog\.net\/\?ver=Pivot[^"]+" target="_blank" title="Pivot - ([^:]+): "[^']+'"><img[^>]+alt="Pivot - [^"]+" \/><\/a>/" },
		]

