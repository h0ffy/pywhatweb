import plugins
			
class Plugintreenews_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/vendor.js", "string" : /var _VENDOR_ = "([^"]+)";/" },
			{ "url" : "/vendor.js", "model" : "/var _OTHER_SYSTEM_MANAGEMENT_NAME_ = '([^']+)';/" },
			{ "search" : "headers[server]", "version" : "/^TreeNeWS\/([^\s]+)$/" },
		]
	return(self.rules)
