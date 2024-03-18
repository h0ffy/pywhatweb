import plugins
			
class Plugincontao_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "This website is powered by Contao Open Source CMS :: Licensed under GNU/LGPL'},
			{ "text" : "<!-- indexer::continue -->'},
		]
		return(self.rules)

