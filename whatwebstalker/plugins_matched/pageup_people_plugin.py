import sys
import os
			
class pageup_people_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : 'Powered by PageUp People"", "certainty" : '75 }
			{ "text" : '<a class="pageupLink" href="http://www.pageuppeople.com" target="self">Powered by PageUp People</a>' }
	]

