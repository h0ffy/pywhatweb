import plugins
			
class Pluginopen_search_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<link[^>]+href[\s]*=[\s]*["']([^'^"^>]+)["'][^>]+type[\s]*=[\s]*["']?application\/opensearchdescription\+xml['"]?[^>]*>/i },
			{ "string" : /<link[^>]+type[\s]*=[\s]*["']?application\/opensearchdescription\+xml['"]?[^>]+href[\s]*=[\s]*["']([^'^"^>]+)["'][^>]*>/i },
		]
	return(self.rules)
