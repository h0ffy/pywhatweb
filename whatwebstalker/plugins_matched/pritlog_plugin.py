import plugins
			
class Pluginpritlog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<em id="jserror">Please enable Javascript for full functionality.</em>" },
			{ "text" : "Powered by <a href="http://pritlog.com/">Pritlog</a>" },
		]
		return(self.rules)

