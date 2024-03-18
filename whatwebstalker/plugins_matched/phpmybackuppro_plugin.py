import plugins
			
class Pluginphpmybackuppro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[www-authenticate]", "regexp" : "/[bB]asic realm="phpMyBackupPro"/" },
			{ "text" : "Please login (use your MySQL username and password): <a href="index.php?login=TRUE">Login</a>" },
		]
		return(self.rules)
