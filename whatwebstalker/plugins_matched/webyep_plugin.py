import plugins
			
class Pluginwebyep_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p class="warning">To edit these pages with WebYep you need to <strong>enable JavaScript</strong> in your Web" },
			{ "text" : "<html><!-- InstanceBegin template="/Templates/panels.dwt.php" codeOutsideHTMLIsLocked="false" -->" },
		]
	return(self.rules)
