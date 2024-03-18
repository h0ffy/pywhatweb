import plugins
			
class Pluginpagecookery_microblog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/pagecookery.com\/" target="_blank">PageCookery<\/a> Microblog ([\d\.]{1,5})/" },
		]
		return(self.rules)
