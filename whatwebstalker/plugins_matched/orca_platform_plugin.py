import plugins
			
class Pluginorca_platform_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "    <meta name="author" content="ORCA Websites"/>" },
			{ "text" : "    <meta name="generator" content="ORCA Platform - http://www.orcawebsites.com"/>" },
			{ "text" : "<a href="http://www.orcawebsites.com/" title="Powered By ORCA Websites">Powered By ORCA Websites</a>" },
			{ "text" : "                <p class="orca">Powered By <a href="http://www.orcawebsites.com/" title="ORCA Websites">ORCA Websites</a></p>" },
			{ "text" : "    <!-- Macro Initialisation - Don\'t Touch! -->" },
		]
		return(self.rules)
