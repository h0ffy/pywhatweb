import sys
import os
			
class tektroniks_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p>Transfering you to login page in 2 seconds...</p>' }
			{ "text" : '<td width="100"><label id="AU_LOGIN_ID_label" for="AU_LOGIN_ID" dataType=" required="true">User Name:</label></td>' }
			{ "url" : '/login.htm", "model" : '/<meta name="Classification" content="(Tektroniks|DATAcentre) - ([^"]+)" \/>/", "offset" : '1 }
			{ "string" : /<meta name="Copyright" content="&copy;(20[\d\-]+) (Tektroniks|DATAcentre)" \/>/ }
			{ "search" : 'headers[server]", "version" : '/^Tektroniks\/([^\s]+)$/ }
			{ "search" : 'headers[www-authenticate]", "text" : 'Basic realm="Tektroniks"' }
	]

