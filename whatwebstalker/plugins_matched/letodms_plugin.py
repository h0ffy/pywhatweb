import sys
import os
			
class Pluginletodms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<div class="disclaimer">This is a classified area. Access is permitted only to authorized personnel. Any violation will be prosecuted according to the national and international laws.</div>" },
			{ "text" : "letoDMS free document management system - www.letodms.com</div></body>" },
			{ "search" : "headers[location]", "regexp" : "/out\/out\.ViewFolder\.php/" },
		]

