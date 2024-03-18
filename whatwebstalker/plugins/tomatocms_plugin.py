import plugins
			
class Plugintomatocms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="http://www.tomatocms.com" title="Powered by TomatoCMS" target="_blank">" },
			{ "text" : "	Tomato.Core.Widget.Loader.baseUrl = 'http://" },
			{ "text" : "					<h1>TomatoCMS Install Wizard</h1>", "version" : "Install Page" },
		]
	return(self.rules)
