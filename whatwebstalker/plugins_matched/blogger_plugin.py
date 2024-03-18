import plugins
			
class Pluginblogger_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta content='blogger' name='generator'/>"},
			{ "name" : "Powered by link", "regexp" : "/<a href="http:\/\/www.blogger.com"><img [^>]* alt="Powered by Blogger"><\/a>},
		]
		return(self.rules)

