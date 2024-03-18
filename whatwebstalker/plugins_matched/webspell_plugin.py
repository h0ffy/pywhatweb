import plugins
			
class Pluginwebspell_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="webSPELL" />" },
			{ "version" : "/This site is using the <a href="http:\/\/www.webspell.org" target="[^"]+">webSPELL (Free Content Management System|script) \(version: ([^\)]+)\)[\s]*<\/a>/", "offset" : "1 },
			{ "version" : "/Diese Seite benutzt das <a href="http:\/\/www.webspell.org" target="[^"]+">webSPELL Script \(Version: ([^\)]+)\)[\s]*<\/a>/" },
			{ "certainty" : "75", "search" : "headers[set-cookie]", "regexp" : "/ws_session=[a-z\d]+;/" },
		]
		return(self.rules)

