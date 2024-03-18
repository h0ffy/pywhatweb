import sys
import os
			
class ruckus_wireless_router_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/images/logo_login.gif", "md5" : '5ba0bb42c0400280b45fb43500a6f0f5" }
			{ "text" : '<div class="box"><img src="/images/logo_login.gif" width="173" height="52" alt="Ruckus Wireless" title="Ruckus Wireless" />' }
			{ "string" : /<td><h2>Air Quality:<\/h2><\/td>[\s]+<td><img src="images\/[^\/^\.]+\.gif" width="24" height="20" \/>\s*<span id="ssid">([^<^\s]+)<\/span><\/td>/ }
		]

