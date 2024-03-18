import sys
import os
			
class Pluginentrans_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<li ><a href="list.php?category=all&amp;page=1" >View All Strings</a> </li>" },
			{ "certainty" : "25", "text" : "<title>Entrans</title>" },
		]
		return(self.rules)

