import plugins
			
class Pluginescenic_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Start Escenic Analysis Engine client script -->" },
			{ "certainty" : "75", "text" : "<meta name="author" content="Escenic AS"/>" },
			{ "certainty" : "25", "regexp" : "/<form action="\/sok\/" id="[^"]+" method="get" accept-charset="utf-8"[^>]*>/" },
			{ "certainty" : "75", "ghdb" : "filetype:ece inurl:article" },
			{ "certainty" : "25", "regexp" : "/<img[^>]+src="[^"^>]+\/archive\/\d{5}\/[^"^>]+"[^>]*>/" },
			{ "certainty" : "25", "regexp" : "/<a[^>]+href="[^"^>]+\/article[\d]{5,10}\.ece">[^<]*<\/a>/" },
		]
		return(self.rules)
