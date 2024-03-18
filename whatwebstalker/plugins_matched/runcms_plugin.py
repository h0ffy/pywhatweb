import plugins
			
class Pluginruncms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by RunCMS" inurl:module inurl:viewcat.php" },
			{ "version" : "/<div align='center'><a href='http:\/\/www.runcms.org\/' target='_blank'> Powered by  RunCms ([\d\.a-z]+)[^&]* &copy; [\d]{4}-[\d]{4} /" },
			{ "version" : "/<meta name="generator" content="[\s^"]*RUNCMS ([\d\.a-z]+)[^"]*"/i },
		]
		return(self.rules)
