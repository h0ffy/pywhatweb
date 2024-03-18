import plugins
			
class Pluginpcextreme_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/img/header_normal.png", "md5" : "f6803df276fd181667f3e6975b12b3dc" },
			{ "text" : "<p class="content" align="center">Deze server is eigendom van <a href="http://www.pcextreme.nl/">PCextreme B.V.</a></p>" },
		]
		return(self.rules)
