import plugins
			
class Pluginpiecrust_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="PieCrust" />" },
			{ "version" : "/<meta name="generator" content="PieCrust ([^\s^"]+)" \/>/" },
			{ "version" : "/Baked with <em><a href="http:\/\/bolt80\.com\/piecrust\/">PieCrust<\/a> ([^\s^<]+)<\/em>\.<\/p>/" },
		]
		return(self.rules)
