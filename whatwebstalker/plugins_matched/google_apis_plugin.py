import plugins
			
class Plugingoogle_apis_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script[^>]+src[\s]*=[\s]*["|']?http:\/\/www.google.com\/jsapi[^>]*>[\s]*<\/script[\s]*>/i", "string" : "Dynamic" },
			{ "string" : /<script[^>]+src[\s]*=[\s]*["|']?http:\/\/ajax.googleapis.com\/([a-zA-Z0-9\/\.-_]+)["|']?[^>]*>[\s]*<\/script[\s]*>/i },
		]
	return(self.rules)

