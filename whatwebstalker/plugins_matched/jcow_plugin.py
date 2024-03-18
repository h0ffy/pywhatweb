import plugins
			
class Pluginjcow_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="Generator" content="Jcow Social Networking Software\. ([\d\.]+)" \/>/" },
			{ "version" : "/Powered by <a href="http:\/\/www\.jcow\.net" title="Social Networking Software", "Community Software" target="_blank"><strong>Jcow<\/strong> ([\d\.]+)<\/a>/" },
			{ "text" : "<meta name="Generator" content="Powered by Jcow" />" },
			{ "text" : "<!-- do NOT remove the Jcow Attribution Information -->" },
			{ "text" : "<!-- jcow branding -->" },
			{ "text" : "<!-- end jcow_application_box -->" },
		]
		return(self.rules)
