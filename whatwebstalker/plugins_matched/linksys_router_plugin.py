import plugins
			
class Pluginlinksys_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "'WRT54GC", "md5" : "0b749361e0c9ab37b9f8875b0667d713", "url" : "/UI_Linksys.gif" },
		]
	return(self.rules)

