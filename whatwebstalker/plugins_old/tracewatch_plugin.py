import plugins
			
class Plugintracewatch_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<h1 class="main"><a href="http://www.tracewatch.com/"><img alt="TraceWatch" title="TraceWatch" src="./base/img/tracewatch" },
			{ "version" : "/<a href="http:\/\/www\.tracewatch\.com\/">TraceWatch<\/a> V?([^\s]+) Copyright &copy;2004-20[\d]{2} Arash Dejkam/" },
		]
	return(self.rules)
