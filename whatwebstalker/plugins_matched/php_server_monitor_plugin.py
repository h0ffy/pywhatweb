import sys
import os
			
class php_server_monitor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>PHP Server Monitor</title>' }
			{ "text" : '<div class="opensource"><a href="index.php"><img src="img/opensource.png" alt="Open Source" height="101px" /></a></div>' }
			{ "version" : '/Powered by <a href="http:\/\/phpservermon\.sourceforge\.net" target="_blank">PHP Server Monitor v([\d\.]+)<\/a><br\/>/ }
		]

