import plugins
			
class Plugincustom_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : " - Powered by CCMS</title>", "certainty" : "75 },
			{ "text" : "<meta name="generator" content="CustomCMS Gaming" />" },
			{ "version" : "/power.png" border="0" style="margin-top: 7px;" alt=" title="Powered by CCMS v([\d\.]+)" \/><\/a>/" },
		]
		return(self.rules)
