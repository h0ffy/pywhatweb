import sys
import os
			
class unimep_station_controller_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<META Name="Description" Content="UniMep Station Controller">" },
			{ "text" : "<center><a href="cgi-bin/usc.ver.cgi">USC&nbsp;Version</a>" },
			{ "string" : /<TITLE>([A-F:\d]{17}) UniMep Station Controller<\/TITLE>/" },
			{ "text" : "<a href="cgi-bin/log.log.cgi" target="_blank">Log1.cgi</a>&nbsp;<a href="/Log.log" target="_blank">Log1.log</a>" },
			{ "text" : "<input type='button' value='Cashier' onclick=\"window.open('/cgi-bin/cashier.cgi?usc_ip=" },
		]

