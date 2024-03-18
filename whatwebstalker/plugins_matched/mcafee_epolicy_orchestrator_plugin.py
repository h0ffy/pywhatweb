import plugins
			
class Pluginmcafee_epolicy_orchestrator_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>\s+ePolicy Orchestrator ([^\s]+ \(Build: \d+\))\s+<\/title>/" },
			{ "url" : "/EPOCore/images/epo-logo-login.gif", "md5" : "aa4beb20b354c761257271e86e9ec92b", "version" : "4.x" },
			{ "search" : "headers[server]", "regexp" : "/^Undefined$/" },
		]
		return(self.rules)
