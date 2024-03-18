import plugins
			
class Pluginphxeventmanager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td><div class="minicalmonth"><a href="/?y=" },
			{ "certainty" : "75", "text" : "<script type="text/javascript" src="pem-includes/xajax/xajax_js/xajax_core.js"></script>" },
			{ "version" : "/<div id="footer">\s+Copyright &copy; 20[\d]{2}[^\n]+\s+Powered by phxEventManager ([^<]+)<br \/>/" },
		]
		return(self.rules)
