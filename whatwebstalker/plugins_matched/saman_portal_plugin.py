import plugins
			
class Pluginsaman_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="Generator" content="Saman Information Structure" />" },
			{ "version" : "/<script  type="text\/javascript" language="JavaScript" src="\/portlets\/sisRapid\/dream\/libs\/(V[\d\.]+)\/core\/sisValidationAPI\.js">/" },
			{ "regexp" : "/<script  type="text\/javascript" language="JavaScript">[\s]+var sisTHEMEPATH_HTTP = "/" },
			{ "search" : "headers[server]", "regexp" : "/sisRapid Framework/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/SAMANPORTALSID=[^;]+;/" },
		]
		return(self.rules)

