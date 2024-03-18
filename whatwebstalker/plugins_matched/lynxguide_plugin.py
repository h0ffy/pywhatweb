import plugins
			
class Pluginlynxguide_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Login to LynxGuide Server</title>" },
			{ "text" : "Use subject to <a href="/cgi/help/license.htm">license agreement</a></span>" },
			{ "search" : "headers[set-cookie]", "regexp" : "/Access_Num=[^;]+;/" },
		]
	return(self.rules)

