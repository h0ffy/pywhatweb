import plugins
			
class Pluginnetref_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Annuaire Netref : http://www.netref.net" },
			{ "version" : "/<a href=['|"]?http:\/\/www.netref.(fr|net)['|"]? class=['|"]?lienp['|"]?[^>]*>Powered by Netref ([\d\.]+) &copy; [0-9]{4}<\/a>/", "offset" : "1 },
		]
	return(self.rules)
