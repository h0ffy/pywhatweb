import sys
import os
			
class dada_mail_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Powered by Dada Mail" filetype:cgi inurl:mail.cgi' }
			{ "regexp" : '/<!-- Dada Mail is Copyright 1999 - 20[\d]{2} Justin Simoni -->/ }
			{ "version" : '/Powered by <a href="http:\/\/(mojo.skazat.com|dadamailproject.com)" target="_blank" style="font-size:10px;font-family:Verdana,Arial">Dada Mail ([^\s^<]+)/", "offset" : '1 }
	]
