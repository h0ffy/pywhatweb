import plugins
			
class Pluginvsns_lemon_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by Vsns Lemon" intitle:"Vsns Lemon"'},
			{ "text" : "<p>Powered by <abbr title="very simple news system">'},
			{ "regexp" : "/<a[^>]+title="Blog powered by VSNS Lemon">},
			{ "certainty" : "50", "regexp" : "/<div id="vsns-(inner|container)">},
			{ "regexp" : "/<img[^>]+alt="VSNS Lemon"[^>]+title="Blog powered by VSNS Lemon"},
			{ "version" : "/<p>Powered by <abbr title="very simple news system">VSNS<\/abbr> (Lemon) ([0-9.a-z]*) by <a href="http:\/\/tachyondecay.net\/">Tachyon<\/a>/", "offset" : "1", "name" : "powered by link" },
		]
		return(self.rules)

