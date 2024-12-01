import plugins
			
class Plugin1024_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id='otatfpowered'><a href='http://www.1024cms.com' target='_blank'>Powered by 1024 CMS</a></div></div>" },
			{ "text" : "<meta name=\"generator\" content=\"1024 CMS (c) 2008 Treble Designs. This is free software\"" }
		]
        return(self.rules)
