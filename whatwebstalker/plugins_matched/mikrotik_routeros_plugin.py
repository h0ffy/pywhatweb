import plugins
			
class Pluginmikrotik_routeros_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/webfig/iframe.html", "text" : "<body onload="parent.generateContent(parent.location.hash.substr(1));">" },
		]
		return(self.rules)
