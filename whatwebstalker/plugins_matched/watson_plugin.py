import plugins
			
class Pluginwatson_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Watson Management Console</TITLE>" },
			{ "text" : "<!--- Page(page_login)=[Login] ---><HTML>"},
		]
		return(self.rules)
