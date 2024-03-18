import plugins
			
class Pluginweb_calendar_system_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "+intitle:"Web Calendar system v" inurl:.asp" },
			{ "version" : "/<TITLE>Web Calendar system v ([\.\d]+)<\/TITLE>/" },
		]
		return(self.rules)

