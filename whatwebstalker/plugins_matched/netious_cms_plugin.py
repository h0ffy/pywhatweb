import plugins
			
class Pluginnetious_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "&nbsp; &nbsp; Powered by <a href="http://www.netious.com" title="Netious.com - free scripts", "CMS-based internet services", "RSS editors">netious.com</a>" },
			{ "text" : "&nbsp; &nbsp; Powered by <a href="http://www.netious.com" title="Netious.com - free scripts", "CMS-based services", "RSS editors">netious.com</a>" },
			{ "text" : "<center><a href="../" title="Home page"><b class=visible>Go back to the home page of the service</b></a></center>" },
			{ "text" : "<title>CMS - powered by netious.com</title>" },
			{ "text" : "&nbsp; &nbsp; Powered by <a href="http://pl.netious.com" title="Netious.com - Polska. Darmowe strony internetowe z CMS.">netious.com</a>" },
		]
		return(self.rules)
