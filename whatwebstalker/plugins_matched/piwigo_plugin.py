import plugins
			
class Pluginpiwigo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Piwigo (aka PWG)", "see piwigo.org">" },
			{ "text" : "<meta name="generator" content="Piwigo", "piwigo.org">" },
			{ "regexp" : "/<div id="copyright">\s+<a name="EoP"><\/a>\s+<!-- End of Page -->/" },
			{ "regexp" : "/Powered by\s+<a href="http:\/\/piwigo\.org" class="Piwigo">/" },
		]
	return(self.rules)

