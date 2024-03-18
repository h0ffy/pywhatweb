import plugins
			
class Pluginwhiteboard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "			&copy; <a href="http://www.powerwd.com">SaroSoftware</a><br />", "certainty" : "75 },
			{ "version" : "/Powered By WhiteBoard ([\d\.]+)<br \/>/" },
			{ "version" : "/Powered By WhiteBoard <span id="version">([\d\.]+)<\/span><br \/>/" },
		]
		return(self.rules)
