import plugins
			
class Pluginpluck_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by pluck" +admin inurl:"file=kop1.php"" },
			{ "version" : "/<meta name="generator" content="pluck ([^\s^"]+)" \/>/" },
			{ "text" : "powered by <a href="http://www.pluck-cms.org">pluck</a>" },
		]
		return(self.rules)
