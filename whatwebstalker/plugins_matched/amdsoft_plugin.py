import sys
import os
			
class Pluginamdsoft_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/style="color: aliceblue"><span style="color: gray">Powered\s+by<\/span> <\/span><a href="http:\/\/www\.iranfairit\.com">/" },
		]
		return(self.rules)

