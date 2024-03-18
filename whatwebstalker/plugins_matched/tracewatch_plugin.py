import sys
import os
			
class tracewatch_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<h1 class="main"><a href="http://www.tracewatch.com/"><img alt="TraceWatch" title="TraceWatch" src="./base/img/tracewatch" },
			{ "version" : "/<a href="http:\/\/www\.tracewatch\.com\/">TraceWatch<\/a> V?([^\s]+) Copyright &copy;2004-20[\d]{2} Arash Dejkam/" },
		]

