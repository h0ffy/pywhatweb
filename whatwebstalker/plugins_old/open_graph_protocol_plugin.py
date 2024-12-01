import plugins
			
class Pluginopen_graph_protocol_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta[^>]+property="og:title"[^>]*>/i },
			{ "version" : "/<meta[^>]+property="og:type"[^>]+content="([^"^>]+)"/" },
			{ "account" : "/<meta[^>]+property="fb:admins"[^>]+content="([^"^>]+)"/" },
			{ "module" : /<meta[^>]+property="fb:app_id"[^>]+content="([^"^>]+)"/" },
		]
	return(self.rules)
