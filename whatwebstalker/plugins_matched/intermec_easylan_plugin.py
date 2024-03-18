import plugins
			
class Pluginintermec_easylan_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/imec.jpg", "md5" : "d0204544f2a9ec61184efb62d0b51515" },
		]
		return(self.rules)
