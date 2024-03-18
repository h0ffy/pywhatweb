import plugins
			
class Pluginoracle_access_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p id="footerVersion">Oracle Access Manager Version: ([^\s]+)<\/p>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/ObSSOCookie=[^;]+;/", "certainty" : "75 },
			{ "search" : "headers[location]", "regexp" : "/obrareq\.cgi/", "certainty" : "75 },
		]
		return(self.rules)
