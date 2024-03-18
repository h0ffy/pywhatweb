import plugins
			
class Pluginmivamerchant_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="mmcategorytree">" },
			{ "ghdb" : "inurl:merchant.mvc filetype:mvc" },
			{ "search" : "headers[set-cookie]", "regexp" : "/htscallerid=/" },
		]
		return(self.rules)

