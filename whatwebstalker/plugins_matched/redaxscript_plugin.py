import plugins
			
class Pluginredaxscript_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://redaxscript.com">Redaxscript</a>" },
			{ "version" : "/<meta name="generator" content="Redaxscript ([^\s^"]+)" \/>/" },
			{ "version" : "/Powered by <a href="http:\/\/redaxscript\.com" title="Redaxscript">Redaxscript<\/a> ([^\s^<]+)</" },
		]
		return(self.rules)
