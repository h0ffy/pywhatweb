import plugins
			
class Pluginmikrotik_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>mikrotik routeros > administration</title>"},
			{ "version" : "/<div class="top">mikrotik routeros ([^ ]+) configuration page</", "name" : "mikrotik routeros ([^ ]+) configuration page" },
			{ "md5" : "bacf8a0c6f3e702db9be393989b2a0b5", "name" : "401 page"},
		]
	return(self.rules)
