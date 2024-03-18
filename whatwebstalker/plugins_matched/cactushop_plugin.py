import sys
import os
			
class Plugincactushop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<select name="numCurrencyID" class="currencymenu" onchange="javascript:document.getElementById(\'currmenuform\').submit();">" },
			{ "certainty" : "75", "regexp" : "/<!-- MYDEVLICNUM -->/" },
			{ "version" : "/<!-- CactuShop v\.?([^\s]+) license: [\s]+ -->/" },
			{ "version" : "/<!---?[\s]+===============================================================================[\s]+CACTUSHOP v?([^\s]+) ASP SHOPPING CART/" },
		]

