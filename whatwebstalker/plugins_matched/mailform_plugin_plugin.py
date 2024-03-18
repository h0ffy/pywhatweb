import plugins
			
class Pluginmailform_plugin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/www.h-fj.com\/blog\/mtplgdoc\/mailformv[\d\.\_]+.php"[^>]*>Powered by Mailform plugin[s]? V([\d\.]+)<\/a>/i },
			{ "version" : "/<a href="http:\/\/www.h-fj.com\/blog\/mtplgdoc\/mailformv[\d\.\_]+.php"[^>]*>Powered by Mailform V([\d\.]+)<\/a>/i },
		]
			return(self.rules)
