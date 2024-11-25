import plugins
			
class Pluginconnectups_x_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "UPS_Server/1.0","search" : "headers[server]" },
			{ "regexp" : "/<TITLE>ConnectUPS (Web\/SNMP Card|SNMP\/WEB Adapter)<\/TITLE>/" },
			{ "url" : "/PSummary.html", "name" : "UPS Model", "model" : "/<b>UPS Model<\/b><\/td>\s+<td><table><tr><td><b>([^<]+)},
			{ "url" : "/PSummary.html", "name" : "UPS Firmware version", "firmware" : "/<b>UPS Firmware version<\/b><\/td>\s+<td><table><tr><td><b>([^<]+)},
			{ "url" : "/PSummary.html", "name" : "Firmware Revision", "firmware" : "/<b>Firmware Revision<\/b><\/td>\s+<td><table><tr><td><b>\s+([^<]+)},
		]
	return(self.rules)
