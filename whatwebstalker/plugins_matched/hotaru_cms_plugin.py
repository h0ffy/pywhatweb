import plugins
			
class Pluginhotaru_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Hotaru CMS ([^\s^"^>]+)" \/>/" },
		]
		return(self.rules)
