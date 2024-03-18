import sys
import os
			
class Pluginacollab_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>ACollab : Accessible Collaboration Environment:" },
		]
		return(self.rules)

