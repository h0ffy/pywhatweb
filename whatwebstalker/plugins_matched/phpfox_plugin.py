import plugins
			
class Pluginphpfox_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered By <a href="http:\/\/www\.phpfox\.com\/"[^>]*>phpFoX<\/a> Version ([\d\.]+)/" },
			{ "version" : "/<a href="http:\/\/www\.phpfox\.com\/"[^>]*>Powered by phpFoX Version ([\d\.]+)<\/a>/" },
		]
		return(self.rules)

