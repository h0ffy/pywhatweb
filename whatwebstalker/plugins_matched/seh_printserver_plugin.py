import sys
import os
			
class seh_printserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : "/status/general_en.html", "model" : "/<TR><TD> Print server model<TD> ([^<]*)},
			{ "url" : "/status/general_en.html", "version" : "/<TR><TD> Software version<TD> ([^<]*)},
			{ "url" : "/status/general_en.html", "string" : /<TR><TD> Default print server name<TD> ([^<]*)},
		]

