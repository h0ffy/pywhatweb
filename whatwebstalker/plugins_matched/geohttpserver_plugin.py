import plugins
			
class Plugingeohttpserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/Language.js", "md5" : "f98b7425f7ff4680ac7682ed61844a17" },
			{ "url" : "/Language.js", "md5" : "6682a8f95d0beb6524f0c08d2982654e" },
			{ "url" : "/Language.js", "md5" : "97cdb361307be266683bceb8c452927b" },
		]
	return(self.rules)

