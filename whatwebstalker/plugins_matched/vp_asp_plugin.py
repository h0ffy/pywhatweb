import sys
import os
			
class vp_asp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "ghdb" : "filetype:asp inurl:"shopdisplayproducts.asp"'},
			{ "certainty" : "75", "text" : "src="vs350.js"'},
			{ "text" : "<a href="http://www.vpasp.com">Shopping Cart</a> powered by VP-ASP</p>'},
			{ "text" : "<a href="http://www.vpasp.com">Powered By VP-ASP Shopping Cart</a>'},
			{ "certainty" : "75", "text" : "shopdisplayproducts.asp?id='},
			{ "version" : "/<title>VP-ASP Shopping Cart ([^ <]*)/", "name" : "powered by title" },
		]

