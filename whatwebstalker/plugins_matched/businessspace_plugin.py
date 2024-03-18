import sys
import os
			
class Pluginbusinessspace_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "  <title>Login to our community network!</title>" },
			{ "text" : "				&copy; BusinessSpace			</div>" },
			{ "text" : "This is a place for people building a circle of professional contacts", "open to sharing new business opportunities", "and looking to fully promote and showcase their capabilities." />" },
		]
		return(self.rules)

