import plugins
			
class Pluginempirecms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : " - Powered by EmpireCMS</title>" },
		]
		return(self.rules)
