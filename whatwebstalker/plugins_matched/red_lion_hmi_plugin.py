import plugins
			
class Pluginred_lion_hmi_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td><font face=tahoma size="2">Display a view of the HMI\'s display and keyboard.&nbsp;&nbsp;&nbsp;</font></td>" },
			{ "text" : "<p><font face=tahoma size=1>Powered by <a href=http://www.redlion.net>Red Lion</a>.</font></p>" },
		]
		return(self.rules)
