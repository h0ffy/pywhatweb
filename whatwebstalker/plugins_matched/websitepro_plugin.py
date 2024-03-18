import plugins
			
class Pluginwebsitepro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^WebSitePro\/([^\s]+)/" },
		]
		return(self.rules)
