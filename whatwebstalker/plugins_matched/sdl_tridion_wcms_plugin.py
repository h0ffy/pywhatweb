import plugins
			
class Pluginsdl_tridion_wcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[product-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[product]", "string" : /^Tridion (20[\d]{2}) Dynamic Content Web Application$/" },
		]
	return(self.rules)
