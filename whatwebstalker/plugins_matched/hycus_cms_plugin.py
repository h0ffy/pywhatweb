import plugins
			
class Pluginhycus_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Hycus - Open Source PHP Based Content Management" />" },
			{ "text" : "Powered By <a href="http://www.hycus.com" target="_blank" >Hycus-CMS</a>. Developed By <a href="http://www.hycus.com" target="_blank" >Hycus Team</a>." },
		]
		return(self.rules)
