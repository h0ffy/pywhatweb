import plugins
			
class Pluginphpcollab_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/^<!-- Powered by PhpCollab v([\d\.]+) \/\/-->$/" },
			{ "version" : "/^<p id="footer">PhpCollab v([\d\.]+)[\s]*<\/p>$/" },
		]
		return(self.rules)
