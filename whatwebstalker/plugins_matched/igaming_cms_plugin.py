import plugins
			
class Pluginigaming_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- iGaming CMS is free software", "please do not remove the copyright message. -->" },
			{ "text" : "Powered by <a href="http://www.igamingcms.com/" target="_blank">iGaming CMS</a>" },
		]
		return(self.rules)
