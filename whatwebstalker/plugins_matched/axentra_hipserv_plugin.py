import plugins
			
class Pluginaxentra_hipserv_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="author" content="Axentra">" },
			{ "text" : "<title id="document_title">Axentra :: Digital Home/SOHO Software Platform for Internet Gateway and NAS Devices</title>" },
			{ "regexp" : "//", "search" : "headers[x-axentra-version]" },
			{ "name" : "HOMEBASEID Cookie", "regexp" : "/HOMEBASEID=/", "search" : "headers[set-cookie]" },
		]
		return(self.rules)

