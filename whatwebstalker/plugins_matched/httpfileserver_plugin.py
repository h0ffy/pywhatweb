import plugins
			
class Pluginhttpfileserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id=footer>[\s]+<a href="http:\/\/www\.rejetto\.com\/hfs\/">HttpFileServer ([^<]+)<\/a>[\s]+<br \/>Servertime/" },
			{ "version" : "/^HFS (\d\.\d.+)$/", "search" : "headers[server]" },
			{ "regexp" : "/^HFS /", "search" : "headers[server]" },
		]
		return(self.rules)
