import plugins
			
class Pluginweb_crossing_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Web Crossing\/([^\s]+)$/" },
			{ "search" : "headers[server]", "version" : "/^Web Crossing\(r\) [^\s]+-v([\d\.]+) built/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/webxSess=[\d]+\.[^\s]+;/" },
		]
		return(self.rules)
