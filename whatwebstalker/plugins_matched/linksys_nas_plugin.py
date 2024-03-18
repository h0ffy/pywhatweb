import plugins
			
class Pluginlinksys_nas_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html><head><title>Ethernet Network Attached Storage  Utility</title>" },
			{ "text" : "	<td nowrap colspan="3"><img src="Admin_top.JPG" width="750" height="52" alt=" border="0" hspace="0" vspace="0"></td>" },
		]
		return(self.rules)

