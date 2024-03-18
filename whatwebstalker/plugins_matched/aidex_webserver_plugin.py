import plugins
			
class Pluginaidex_webserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^aidex\/([^\s]+)/" },
			{ "text" : "<br><small>Powered by <a href="http://www.aidex.de/software/webserver/" target="_blank">AIDeX Webserver</a></small></div></div><br><br><br>" },
		]
		return(self.rules)
