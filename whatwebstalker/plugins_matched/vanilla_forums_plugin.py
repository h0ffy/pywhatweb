import plugins
			
class Pluginvanilla_forums_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-garden-version]", "version" : "/^Vanilla ([^\s]+)$/" },
			{ "version" : "/Powered by <a href="(http:\/\/)?getvanilla\.com\/?">Vanilla ([^\s^<]+)<\/a>/", "offset" : "1 },
			{ "search" : "headers[set-cookie]", "regexp" : "/Vanilla=deleted; expires=/" },
			{ "certainty" : "25", "regexp" : "/<body id=["'](DiscussionsPage|vanilla)/i },
		]
		return(self.rules)

