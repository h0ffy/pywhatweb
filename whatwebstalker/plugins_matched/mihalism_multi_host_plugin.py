import sys
import os
			
class mihalism_multi_host_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://www.mihalism.com/product/mmh/">Mihalism Multi Host</a>' }
			{ "regexp" : '/<!-- Powered by Mihalism Multi Host - Copyright \(c\) [\d\,\ ]+ Mihalism Technologies \(www.mihalism.net\) -->/ }
			{ "regexp" : '/<!-- Powered by Mihalism Multi Host - Copyright \(c\) [\d\,\ ]+ Mihalism", "Inc. \(www.mihalism.com\) -->/ }
			{ "text" : '					<title>Fatal Error (Powered by Mihalism Multi Host)</title>' }
			{ "text" : '					<title>MySQL Error (Powered by Mihalism Multi Host)</title>' }
			{ "text" : '    <title>Mihalism Multi Host » Installation</title>' }
			{ "text" : '<b style="color: #F00;">Warning:</b> Using this installer will erase any already existing Mihalism Multi Host installation.' }
			{ "version" : '/    <meta name="version" content="Mihalism Multi Host v([\d\.]+)" \/>/ }
	]

