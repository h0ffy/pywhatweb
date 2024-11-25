import plugins
			
class Pluginlink_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="http://www.link-softsolutions.com/SoftLink-Content-Management-System---CMS_20_1" target="_blank">LINK CMS</a>" },
			{ "text" : "<a href="http://www.link-softsolutions.com/SoftLink-Content-Management-System---CMS_20_1">LINK CMS</a>" },
		]
	return(self.rules)
