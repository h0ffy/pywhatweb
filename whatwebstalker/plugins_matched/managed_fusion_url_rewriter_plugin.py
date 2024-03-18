import plugins
			
class Pluginmanaged_fusion_url_rewriter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-rewritten-by]", "regexp" : "/^ManagedFusion \(rewriter; reverse-proxy; +http:\/\/managedfusion\.com\/\)$/" },
			{ "search" : "headers[x-managedfusion-rewriter-version]", "version" : "/^(.+)$/" },
		]
		return(self.rules)
