import plugins
			
class Pluginearlyimpact_productcart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:custva.asp'},
			{ "text" : "<a href="fpassword.asp?redirectUrl=&frURL=Custva.asp"" },
			{ "text" : "<!-- end of password request -->" },
		]
	return(self.rules)
