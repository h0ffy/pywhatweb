import plugins
			
class Pluginfirephp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-wf-1-plugin-1]", "version" : "/^http:\/\/meta\.firephp\.org\/Wildfire\/Plugin\/FirePHP\/Library-FirePHPCore\/([^\s]+)$/" },
			{ "search" : "headers[x-wf-1-structure-1]", "string" : /^http:\/\/meta\.firephp\.org\/Wildfire\/Structure\/FirePHP\/(FirebugConsole\/[^\s]+)$/" },
			{ "search" : "headers[x-wf-protocol-1]", "regexp" : "/^http:\/\/meta\.wildfirehq\.org\/Protocol\//" },
		]
	return(self.rules)

