import plugins
			
class Pluginowl_intranet_engine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/owl_sessid=/" },
			{ "version" : "/<a class="version2" href="http:\/\/owl\.sourceforge\.net\/" target="_blank">Owl Intranet Engine", "Version Owl ([^<]+)<\/a>/" },
			{ "version" : "/<title>[^<]+ Owl ([\d\.]+ [\d]{8})<\/title>/" },
		]
		return(self.rules)
