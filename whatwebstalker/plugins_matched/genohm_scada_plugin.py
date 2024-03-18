import plugins
			
class Plugingenohm_scada_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>GenOHM Scada Launcher</title>" },
			{ "url" : "/favicon.ico", "md5" : "311df4268641ef7c01f43a077ff2c9fe" },
			{ "url" : "/cgi-bin/scada-vis/index.cgi", "version" : "/var LMVersion = '([^\s^']+)';/" },
		]
		return(self.rules)

