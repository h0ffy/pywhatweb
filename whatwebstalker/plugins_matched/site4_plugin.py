import sys
import os
			
class site4_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "path" : '/error.asp", "text" : '<title>SITE4.dk Site4 Setup Error..</title>' },
			{ "text" : '<div class="caption" align="center"><b>A Site4 event or error occured..</b></div></td>' },
			{ "text" : 'To read more about SITE4.dk please <a class="smalltext" style="text-decoration:none;" href="http://www.site4.dk"><b>click here</b></a>' },
		]

