import plugins
			
class Pluginallnewsmanager_net_plugin(plugins.Base):
    def __init__(self):
    	super().__init__()
    def start(self):
        self.rules = [
			{ "regexp" : r"/(kujeme|Powered by) <a id=\"[^\"]+\" href=\"http:\/\/www.allnewsmanager.net\">AllNewsManager.NET<\/a>/" },
		]
        return self.rules