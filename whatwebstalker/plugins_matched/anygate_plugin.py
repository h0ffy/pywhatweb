import plugins
			
class Pluginanygate_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/index.asp", "text" : "<title>AnyGate" },
			{ "url" : "/index.asp", "text" : "사용자 암호가 설정되어 있지 않습니다.", "string" : "No Password"},
		]
		return(self.rules)
