import sys
import os
			
class entrans_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<li ><a href="list.php?category=all&amp;page=1" >View All Strings</a> </li>" },
			{ "certainty" : "25", "text" : "<title>Entrans</title>" },
		]

