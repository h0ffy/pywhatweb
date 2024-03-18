import plugins
			
class Pluginoracle_http_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/Oracle[ -]HTTP[ -]Server/" },
			{ "search" : "headers[server]", "version" : "/Oracle_Web_[Ll]istener(_NT_)?([\d\.]+\/[^\s]+)/", "offset" : "1 },
			{ "search" : "headers[server]", "version" : "/Oracle_Web_[Ll]istener(_NT_)?\/([^\s]+)/", "offset" : "1 },
		]
		return(self.rules)
