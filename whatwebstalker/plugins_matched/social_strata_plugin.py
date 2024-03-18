import plugins
			
class Pluginsocial_strata_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:"/eve/personal?x_myspace_page=profile" "Powered by Social Strata"" },
			{ "text" : "<a href="http://socialstrata.com/landing/goto.php?a=eve" target="_blank">Powered by Social Strata</a>" },
			{ "version" : "/Powered by: <a target="_blank" href="http:\/\/eveforenterprise\.com">Groupee<\/a><SUP>TM<\/SUP> \(version ([\d\.]+)\) from Groupee Inc\./" },
		]
	return(self.rules)
