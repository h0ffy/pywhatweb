import plugins
			
class Pluginalpha_five_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Alpha Five( Application Server)?\/([\d\.]+ Build\/[\d\-]+)/", "offset" : "1" },
			{ "search" : "headers[set-cookie]", "regexp" : "/A5wSessionId=[a-f\d]{32};/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/A5wBrowserId=[a-f\d]{32};/" },
		]
        return(self.rules)
