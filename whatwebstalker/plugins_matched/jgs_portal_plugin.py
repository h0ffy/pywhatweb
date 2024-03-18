import plugins
			
class Pluginjgs_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Powered by JGS-Portal Version"" },
			{ "version" : "/Powered by <b>JGS-Portal Version ([\d\.]+)<\/b> &copy; /" },
		]
		return(self.rules)
