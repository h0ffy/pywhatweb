import sys
import os
			
class invision_power_board_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '(Powered by Invision Power Board)</title>' },
			{ "text" : 'index.php?app=core&amp;module=global&amp;section=rss&amp;type=forums&amp;id=' },
			{ "regexp" : '/<script [^>]+src='[^']+\/ipb\.js/ },
			{ "text" : '<div id="ipbwrapper">' },
			{ "regexp" : '/<div [^>]*class='copyright'>Powered by <[^>]+>Invision Power Board<\/a>/ },
			{ "text" : 'Powered By <a href='http://www.invisionboard.com' style='text-decoration:none' target='_blank'>IP.Board</a>" },
			{ "regexp" : '/&copy; [0-9]+ &nbsp;<a href='http:\/\/www\.invisionpower\.com'[^>]*>IPS", "Inc</ },
			{ "regexp" : '/&copy; [0-9]+ &nbsp;<a href='http:\/\/www\.invisionpower\.com'[^>]*>IPS", "<abbr title='Incorporated'>Inc<\/abbr></ },
			{ "version" : '/Powered by <a [^>]+>Invision Power Board<\/a>([^&]+) &copy; 20[0-9]+/", "name" : 'powered by 1" },
			{ "version" : '/([0-9\.]+) &copy; 20[0-9]+ &nbsp;<a href='http:\/\/www\.invisionpower\.com'[^>]+>IPS/", "name" : 'powered by 2" },
			{ "version" : '/Invision Power Board<\/a>[\s]+v([0-9\.]+) &copy;/", "name" : 'powered by 3" },
			{ "version" : '/Invision Power Board<\/a>([^&]+)&copy; 20[0-9]+ &nbsp;<a href='http:\/\/www\.invisionpower\.com'/", "name" : 'powered by 4" },
		]

