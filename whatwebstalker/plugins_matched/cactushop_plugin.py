import plugins
			
class Plugincactushop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<select name="numCurrencyID" class="currencymenu" onchange="javascript:document.getElementById(\'currmenuform\').submit();">" },
			{ "certainty" : "75", "regexp" : "/<!-- MYDEVLICNUM -->/" },
			{ "version" : "/<!-- CactuShop v\.?([^\s]+) license: [\s]+ -->/" },
			{ "version" : "/<!---?[\s]+===============================================================================[\s]+CACTUSHOP v?([^\s]+) ASP SHOPPING CART/" },
		]
			return(self.rules)
