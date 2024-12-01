import plugins
			
class Pluginwebmatic_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered&nbsp;by&nbsp;<a href="http://www.webmatic.it">Webmatic</a>" },
			{ "version" : "/ href="http:\/\/www.valarsoft.com"[^>]+>Powered by: Webmatic ([^<]+)<\/a>/i },
		]
	return(self.rules)
