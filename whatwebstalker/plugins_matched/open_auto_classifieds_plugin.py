import sys
import os
			
class Pluginopen_auto_classifieds_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<p>Powered by <a href="http://www.openautoclassifieds.com/index.php">Open Auto Classifieds</a>" },
			{ "version" : "/			<p>Powered by <a href="http:\/\/www.openautoclassifieds.com[^"]*">Open Auto Classifieds v([\d\.a-z]+)/" },
			{ "version" : "/			<p>Powered by Open Auto Classifieds v([\d\.a-z]+)/" },
		]

