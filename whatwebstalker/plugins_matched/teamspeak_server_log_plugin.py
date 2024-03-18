import plugins
			
class Pluginteamspeak_server_log_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/^[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},ALL,Info,server,[\s]+Server version: ([^\r^\n]+)/" },
		]
	return(self.rules)

