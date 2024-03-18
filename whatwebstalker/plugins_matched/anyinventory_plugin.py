import sys
import os
			
class anyinventory_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "		<title>anyInventory: Top</title>" },
			{ "regexp" : "/					 you have inventoried <b>[0-9]*<\/b>  items with <a href="http:\/\/anyinventory.sourceforge.net\/">anyInventory", "the most flexible and powerful web-based inventory system<\/a>/" },
			{ "version" : "/								anyInventory ([\d\.]+)/" },
		]

