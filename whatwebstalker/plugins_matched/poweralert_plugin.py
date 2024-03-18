import plugins
			
class Pluginpoweralert_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<h1>Protected Object</h1>This object on the Netsilicon is protected.<p>Return to <A TARGET="_top" HREF="index.html">Last page</A><p>" },
		]
			return(self.rules)
