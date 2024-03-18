import plugins
			
class Pluginanecms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="Author" content="Erwin Aligam - ealigam@gmail.com" />" },
			{ "ghdb" : "powered by anecms"", "certainty" : "75 },
			{ "regexp" : "/&copy; [\d]{4} <strong><a href="http:\/\/anecms.com[^\>]*>anecms.com<\/a><\/strong>/" },
			{ "regexp" : "/<title>[^<^\-]+- Powered By ANECMS<\/title>/" },
		]
		return(self.rules)
