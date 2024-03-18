import plugins
			
class Plugintaurus_server_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>The Taurus Server Appliance</title>" },
			{ "text" : "<b><font color=#FFFFFF>Welcome to Taurus </font></b>" },
			{ "version" : "/<div align=center><font size=-2 color=#FFFFFF>Software Version : CeLinuX-([\d\.]+)<\/font><\/div>/" },
		]
		return(self.rules)
