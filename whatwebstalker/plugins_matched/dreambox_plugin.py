import plugins
			
class Plugindreambox_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/web-data/img/favicon.ico", "md5" : "d9aa63661d742d5f7c7300d02ac18d69" },
			{ "version" : "/^Enigma2 WebInterface Server ([\d\.]+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^TwistedWeb/", "search" : "headers[server]" },
			{ "version" : "/^TwistedWeb\/([\d\.]+)/", "search" : "headers[server]" },
		]
		return(self.rules)

