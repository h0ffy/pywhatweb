import plugins
			
class Plugindradis_framework_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "effective information sharing - <a href="http://dradisframework.org/">http://dradisframework.org</a>" },
			{ "text" : "<div id="back"><a href="/">&lsaquo; back to the app.</a></div>" },
			{ "text" : "<p id="wizard">Not familiar with Dradis? Checkout the <a href="/wizard">Wizard</a>.</p>" },
			{ "text" : "<li>Integration with existing systems and tools through <a href="http://Dradisframework.org/server_plugins.html">server plugins</a>.</li>" },
			{ "version" : "/<title>First Time User's Wizard - dradis v([\d\.]+)<\/title>/" },
		]
		return(self.rules)
