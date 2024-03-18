import plugins
			
class Pluginsystem_shop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "      powered by System4you.com internet solutions" },
			{ "text" : "                powered by System-Shop" },
			{ "text" : "               http://www.system-shop.at" },
			{ "text" : "<a href="http://www.systemshop.at" target="_blank">Powered by System" },
		]
			return(self.rules)
