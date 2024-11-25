import plugins
			
class Pluginamiro_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href='http://www.amirocms.com' target=_blank>Powered by: Amiro CMS</a>" },
			{ "text" : "<a href="http://www.amirocms.com/" target=_blank><FONT size=1><B>Powered by: Amiro CMS</B></FONT></A>" },
		]
	return(self.rules)
