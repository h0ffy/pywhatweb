import plugins
			
class Pluginteamviewer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html><body>This site is running <a href='http://www.TeamViewer.com'>TeamViewer</a>.</body></html>" },
		]
		return(self.rules)
