import plugins


class Plugintraffic_inspector_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[server]",
     "version": "/^Traffic [Ii]nspector HTTP\\/FTP\\/Proxy server \\(([^\\)]+)\\)$/"},
			{"url": "/", "string": / <title > Error <\/title><\/head><body><h1>403 - Forbidden<\/h1><hr( class="footer")?>Traffic [Ii]nspector HTTP\/FTP\/Proxy server \([^\)]+\)<br>([^<^\/]+)\s*\/?\s*[\d]{2}\.[\d]{2}\.[\d]{2}/", "offset" : "1 },
		]
	return(self.rules)
