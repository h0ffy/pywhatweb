import plugins
			
class Pluginacarsd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^acarsd\/([^\s]+)$/" },
			{ "certainty" : "75", "text" : "<meta name="author" content="KjM <acarsd@acarsd.org>">" },
			{ "certainty" : "75", "regexp" : "/<title>[^<]*RealTime Web ACARS/" },
			{ "certainty" : "75", "text" : "<!-- MAIN PART OF WEBACARS -->" },
			{ "string" : /<meta name="description" content="Realtime Web ACARS - [^\s]+ Location: ([^\.^\"^>]+)\./" },
		]
		return(self.rules)
