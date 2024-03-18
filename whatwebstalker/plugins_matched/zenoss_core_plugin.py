import plugins
			
class Pluginzenoss_core_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="copyright">[\s]+<p>Copyright &copy; 2005-20[\d]{2} Zenoss", "Inc\. \| Version[\s]+<span>([^\s^<]+)<\/span>[\s]+/" },
			{ "text" : "<link rel="shortcut icon" type="image/x-icon" href="/zport/dmd/favicon.ico" />" },
		]
		return(self.rules)

