import sys
import os
			
class Pluginkerio_winroute_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^Kerio WinRoute Firewall Embedded Web Server$/" },
			{ "version" : "/<A HREF="\/http_restr">Web policy<\/A><br>[\s]+Kerio WinRoute Firewall ([^\s^>]+)<br>&copy;/" },
			{ "url" : "/nonauth/gfx/kerio_logo.gif", "md5" : "d9f42bd071f2f3f1dc7cdb628af4c596", "version" : "6.x" },
			{ "text" : "<meta HTTP-EQUIV="Refresh" content="0;URL=/internal/ntlm/dologin.php?internal=0">	<title>Kerio WinRoute Firewall - Login Page - Kerio WinRoute Firewall</title>" },
		]

