import plugins
			
class Pluginunimep_station_controller_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<META Name="Description" Content="UniMep Station Controller">" },
			{ "text" : "<center><a href="cgi-bin/usc.ver.cgi">USC&nbsp;Version</a>" },
			{ "string" : /<TITLE>([A-F:\d]{17}) UniMep Station Controller<\/TITLE>/" },
			{ "text" : "<a href="cgi-bin/log.log.cgi" target="_blank">Log1.cgi</a>&nbsp;<a href="/Log.log" target="_blank">Log1.log</a>" },
			{ "text" : "<input type='button' value='Cashier' onclick=\"window.open('/cgi-bin/cashier.cgi?usc_ip=" },
		]
		return(self.rules)

