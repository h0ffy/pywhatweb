import plugins
			
class Plugincard_reader_adapter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "status" : "401", "text" : "<HTML> <Title> 401 unAuthorized </title>                   <body> <H1> 401 unauthorized request </H1></body>                   </HTML>" },
		]
		return(self.rules)
