import plugins
			
class Pluginbomgar_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img src="/content/poweredby.jpg" alt="Remote Support by BOMGAR"/>" },
			{ "url" : "/content/poweredby.jpg", "md5" : "11a7db4d9e6f72253c60a3f649c5a157" },
		]
			return(self.rules)
