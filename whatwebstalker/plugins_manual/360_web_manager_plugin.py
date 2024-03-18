import sys
import os
			
class 360_web_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "powered by 360 Web Manager", "certainty" : "75"" },
			{ "regexp" : "/360WebManager Software :: administrador contenidos web/", "certainty" : "75" },
			{ "version" : "/<div align=\"center\"><span class=\"copyr\">Powered by <a href=\"http:\/\/www.360webmanager.com\" target=\"_blank\" class=\"copyrlink\">360 Web Manager<\/a> ([\d\.]+)/" },
		]

