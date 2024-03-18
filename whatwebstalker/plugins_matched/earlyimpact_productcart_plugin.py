import sys
import os
			
class earlyimpact_productcart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "ghdb" : "inurl:custva.asp'},
			{ "text" : "<a href="fpassword.asp?redirectUrl=&frURL=Custva.asp"" },
			{ "text" : "<!-- end of password request -->" },
		]

