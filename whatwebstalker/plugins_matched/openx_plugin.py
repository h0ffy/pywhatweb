import plugins
			
class Pluginopenx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<body class="hasInterface hasGradient hasSidebar " onload="initPage();">" },
			{ "text" : "<div id="oaHeaderBranding" class="brandingAdServer">OpenX</div>" },
			{ "text" : "<span class="tab-s">Welcome to OpenX</span><br />" },
			{ "version" : "/<meta name="generator" content="OpenX v([^\s]+) - http:\/\/www\.openx\.org"( \/)?>/" },
		]
	return(self.rules)
