import plugins
			
class Pluginwanem_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<html><body><h1>WANem v([^\s^:]+): It works\!<\/h1><\/body><\/html>/" },
			{ "url" : "/WANem/about.html", "version" : "/<b>WANem v([^\s^<]+)<\/b><br>/" },
			{ "url" : "/WANem/title.html", "text" : "<TITLE>Welcome to WANem</TITLE>" },
		]
		return(self.rules)
