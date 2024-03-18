import plugins
			
class Pluginholocms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="build" content="([^\ ]+) - [^-]+- HoloCMS" \/>/" },
			{ "text" : "<div id="remember-me-notification" class="bottom-bubble" style="display:none;">" },
			{ "regexp" : "/^Powered by HoloCMS &copy[;]* 2008 Meth0d & Parts by Yifan", "sisija/" },
		]
		return(self.rules)

