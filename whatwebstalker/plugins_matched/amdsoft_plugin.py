import sys
import os
			
class Pluginamdsoft_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/style="color: aliceblue"><span style="color: gray">Powered\s+by<\/span> <\/span><a href="http:\/\/www\.iranfairit\.com">/" },
		]

