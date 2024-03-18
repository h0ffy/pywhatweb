import plugins
			
class Pluginphprechnung_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a class='slink' title='phpInvoice Home' href='http://www.ecorak.de/phpRechnung/' target='_blank'>" },
			{ "version" : "/<title>phpRechnung ([^-]+) - Login<\/title>/" },
			{ "version" : "/<title>phpInvoice ([^-]+) - Login<\/title>/" },
		]
		return(self.rules)

