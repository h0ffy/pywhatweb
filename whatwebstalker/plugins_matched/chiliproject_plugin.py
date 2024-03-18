import plugins
			
class Pluginchiliproject_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="https://www.chiliproject.org/">ChiliProject</a>" },
			{ "text" : "<meta name="description" content="ChiliProject" />" },
			{ "text" : "<!-- page specific tags -->" },
			{ "version" : "/<li><a href="https:\/\/www\.chiliproject\.org\/help\/v([^\s^"]+)" class="help">/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/_chiliproject_session=/" },
		]
		return(self.rules)
