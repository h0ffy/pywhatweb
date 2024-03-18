import sys
import os
			
class lotus_notes_traveler_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[www-authenticate]", "string" : /^Basic realm="Lotus Notes Traveler \(([^\)]+)\)"$/ }
			{ "status" : '401", "text" : '<HTML><HEAD><TITLE>Unable to Process Request</TITLE></HEAD><BODY><P>Servlet Status Code: 401</P><P>Servlet Status Message: Unauthorized</P></BODY></HTML>' }
	]

