import plugins
			
class Pluginblogengine.net_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="shortcut icon" href="pics/blogengine.ico" type="image/x-icon" />" },
			{ "regexp" : "/Powered by[\r\n\s]*<a href="http:\/\/www.dotnetblogengine.net[\/]?"[^>]*>BlogEngine.NET<\/a>/" },
			{ "version" : "/Powered by[\r\n\s]*<a href="http:\/\/www.dotnetblogengine.net[\/]?"[^>]*>BlogEngine.NET<\/a>[\r\n\s]*([\d\.]+)/" },
		]
	return(self.rules)
