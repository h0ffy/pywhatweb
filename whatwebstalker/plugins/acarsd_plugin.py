import plugins
			
class Pluginacarsd_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : r"^acarsd\/([^\s]+)$" },
			{ "certainty" : "75", "text" : "<meta name=\"author\" content=\"KjM <acarsd@acarsd.org>\">" },
			{ "certainty" : "75", "regexp" : r"<title>[^<]*RealTime Web ACARS" },
			{ "certainty" : "75", "text" : "<!-- MAIN PART OF WEBACARS -->" },
			{ "string" : r"<meta name=\"description\" content=\"Realtime Web ACARS - [^\s]+ Location: ([^\.^\"^>]+)\." },
		]
        return self.rules