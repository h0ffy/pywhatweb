import plugins
			
class Pluginsonicwall_firewall_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^SonicWALL$/" },
			{ "url" : "/auth1.html", "module" : /<div align="right">Click <a href="sslvpn" onClick="top\.location\.href='sslvpn'";>here<\/a> for (sslvpn) login/" },
			{ "url" : "/auth1.html", "firmware" : "/<link href="swl_login-([^"]+)\.css" rel="stylesheet" type="text\/css">/" },
		]
	return(self.rules)
