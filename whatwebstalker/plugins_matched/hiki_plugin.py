import plugins
			
class Pluginhiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Hiki ([^"^\s]+)">/" },
			{ "text" : "<html><head><title>Hiki Error</title></head><body>" },
			{ "version" : "/<div class="footer">Generated by <a href="http:\/\/hikiwiki.org\/">Hiki<\/a> ([^\s]+) \([\d]{4}-[\d]{2}-[\d]{2}\)/" },
		]
		return(self.rules)

