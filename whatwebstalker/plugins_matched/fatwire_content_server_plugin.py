import plugins
			
class Pluginfatwire_content_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[host_service]", "version" : "/^FutureTenseContentServer:([^\s]+)$/" },
			{ "text" : "<!-- this tag to be replaced with autogen stuff -->" },
			{ "text" : "<h1>FatWire Corporation<br />&nbsp;Content Server</h1>" },
			{ "text" : "<b>Open Market", "Inc.<br>&nbsp;ContentServer</b><hr>" },
			{ "certainty" : "75", "text" : "An error occurred during processing. Check the info log.<br" },
		]
	return(self.rules)

