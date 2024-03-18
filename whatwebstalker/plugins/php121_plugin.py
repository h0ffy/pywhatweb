import plugins
			
class Pluginphp121_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>PHP121 - Please login or register</title>" },
			{ "text" : "<title>PHP121 - New User</title>" },
			{ "version" : "/<center>Powered by <a target="_blank" style="TEXT-DECORATION: none; COLOR: #000066; FONT-SIZE: 10px" href="http:\/\/www.php121.com"><U>PHP121<\/U><\/a> v([\d\.]+)<\/center>/" },
		]
	return(self.rules)
