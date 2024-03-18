import sys
import os
			
class phpatm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<frame name="viewer_bottom" src="viewer_bottom.php?file=' },
			{ "version" : '/<div id="phpatm">(<br>)?<a href="http:\/\/phpatm\.org\/" target="_blank" title="Powered by PHP Advanced Transfer Manager v([^"]+)">Powered by phpATM<\/a><br><\/div>/", "offset" : '1 },
		]

