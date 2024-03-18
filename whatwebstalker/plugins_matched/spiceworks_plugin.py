import sys
import os
			
class spiceworks_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="author" content="Spiceworks", "Inc." />' }
			{ "text" : '<p>Spiceworks is compatible with <a href="http://community.spiceworks.com/help/Spiceworks_Requirements#Browser">modern browsers</a>", "and requires JavaScript", "Cookies", "and Stylesheets (CSS) to function correctly.</p>' }
			{ "text" : '<title>Spiceworks - Login Required</title>' }
	]

