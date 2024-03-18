import plugins
			
class Pluginsilex_print_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/troy_large_bw.gif", "md5" : "ba4feb9ffb5d77f9c72269549d07b78e" },
			{ "url" : "/silex_logo.gif", "md5" : "ba4feb9ffb5d77f9c72269549d07b78e" },
		]
	return(self.rules)

