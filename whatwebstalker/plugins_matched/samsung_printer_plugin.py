import plugins
			
class Pluginsamsung_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "var debugMode = ("$$GSI_TCPIP_IP_ADDR$$".indexOf(".")" },
		]
	return(self.rules)

