import sys
import os
			
class comersus_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<meta NAME="DESCRIPTION" CONTENT="Powered by Comersus http:\/\/www.comersus.com">/i },
			{ "regexp" : "/<title>[^<]*Powered by Comersus ASP Shopping Cart Open Source[^<]*<\/title>/i },
			{ "regexp" : "/<a href="[^"]*comersus_showCart.asp">/i },
			{ "regexp" : "/Powered by <[^>]*>Comersus<\/a>/i },
		]

