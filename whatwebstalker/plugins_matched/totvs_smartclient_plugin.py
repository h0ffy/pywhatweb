import plugins
			
class Plugintotvs_smartclient_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<object\s+classid="clsid:[a-f\d\-]+"\s+codebase="TotvsSmartClientax\.cab#version=([^"]+)"/" },
			{ "string" : /<param name="StartProgram" value="([^"]+)"> <<= Programa/" },
			{ "string" : /<param name="Environment" value="([^"]+)"> <<= Ambiente/" },
			{ "search" : "headers[TotvsSmartClient]", "regexp" : "/^TotvsSmartClient$/" },
		]
		return(self.rules)
