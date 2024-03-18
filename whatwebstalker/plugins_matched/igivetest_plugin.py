import plugins
			
class Pluginigivetest_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/iGiveTest\.com" target=_blank>iGiveTest v([\d\.]+)<\/a>/" },
			{ "version" : "/<tr><td colspan=[\d] align=right>Powered by iGiveTest v([\d\.]+)<\/a><\/td><\/tr>/" },
			{ "certainty" : "25", "text" : "<form action="index.php" method=post name=signinform>" },
		]
		return(self.rules)
