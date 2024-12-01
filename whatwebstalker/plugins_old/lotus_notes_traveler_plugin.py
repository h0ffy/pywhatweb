import plugins
			
class Pluginlotus_notes_traveler_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "string" : /^Basic realm="Lotus Notes Traveler \(([^\)]+)\)"$/" },
			{ "status" : "401", "text" : "<HTML><HEAD><TITLE>Unable to Process Request</TITLE></HEAD><BODY><P>Servlet Status Code: 401</P><P>Servlet Status Message: Unauthorized</P></BODY></HTML>" },
		]
	return(self.rules)
