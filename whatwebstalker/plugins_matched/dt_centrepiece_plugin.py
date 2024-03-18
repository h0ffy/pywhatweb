import plugins
			
class Plugindt_centrepiece_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<meta name="generator" content="DT Centrepiece - www.dt.net.nz/centrepiece/" />" },
			{ "text" : "<a href="http://www.dt.net.nz/centrepiece/" target="_blank">Powered By DT Centrepiece</a>" },
		]
			return(self.rules)
