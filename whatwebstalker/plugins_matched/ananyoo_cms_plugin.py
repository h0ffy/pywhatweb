import plugins
			
class Pluginananyoo_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="copyright" content="Copyright 2003-2008", "Ananyoo CMS", "a Anblik.com Project." />" },
			{ "certainty" : "75", "text" : "<meta name="generator" content="http://www.ananyoo.com" />" },
		]
		return(self.rules)

