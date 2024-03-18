import plugins
			
class Pluginopenwrt_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>OpenWrt Administrative Console</title>" },
			{ "text" : "OpenWrt Administrative Console<br />Redirecting to : <a style="color: inherit;" href="/cgi-bin/webif.sh">main page</a></p>" },
		]
		return(self.rules)
