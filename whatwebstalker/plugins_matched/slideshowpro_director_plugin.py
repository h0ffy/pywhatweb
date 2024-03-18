import sys
import os
			
class Pluginslideshowpro_director_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<div id="simple-footer">\s+<span>SlideShowPro Director ([^<]+)<\/span>/" },
			{ "text" : "</div> <!--close login-container-->	</body>" },
		]

