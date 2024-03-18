import plugins
			
class Pluginvirtuemart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/<div id=["']vmMainPage/" },
			{ "certainty" : "75", "text" : "href="/index.php?option=com_virtuemart&amp;page=shop.registration">" },
		]
		return(self.rules)
