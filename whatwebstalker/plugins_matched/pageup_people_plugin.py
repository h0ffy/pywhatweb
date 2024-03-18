import plugins
			
class Pluginpageup_people_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by PageUp People"", "certainty" : "75 },
			{ "text" : "<a class="pageupLink" href="http://www.pageuppeople.com" target="self">Powered by PageUp People</a>" },
		]
		return(self.rules)

