import plugins
			
class Plugin3dcart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!--START: 3dcart stats-->" },
			{ "text" : "<!--END: 3dcart stats-->" },
			{ "search" : "headers[set-cookie]", "regexp" : "/3dvisit/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^affiliate\s/", "name" : "affiliate cookie", "certainty" : "25 },
		]
		return(self.rules)
