import plugins
			
class Pluginphp_server_monitor_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>PHP Server Monitor</title>" },
			{ "text" : "<div class="opensource"><a href="index.php"><img src="img/opensource.png" alt="Open Source" height="101px" /></a></div>" },
			{ "version" : "/Powered by <a href="http:\/\/phpservermon\.sourceforge\.net" target="_blank">PHP Server Monitor v([\d\.]+)<\/a><br\/>/" },
		]
	return(self.rules)

