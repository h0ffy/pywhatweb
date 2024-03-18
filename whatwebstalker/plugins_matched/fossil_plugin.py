import plugins
			
class Pluginfossil_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div class="footer">\s+(<a href="http:\/\/fossil-scm\.org">Fossil<\/a>|Fossil) version \[([^\]]+)\] [\d]{4}\-[\d]{2}\-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}/", "offset" : "1 },
			{ "string" : /<div class="footer">\s+(<a href="http:\/\/fossil-scm\.org">Fossil<\/a>|Fossil) version \[[^\]]+\] ([\d]{4}\-[\d]{2}\-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2})/", "offset" : "1 },
		]
	return(self.rules)

