import plugins
			
class Pluginnetshelter_vpn_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HEAD><TITLE>Welcome to NetShelter</TITLE></HEAD>" },
			{ "url" : "/images/sb_logo.gif", "md5" : "ffacfeae7e203bd8de5c9da889d217ec" },
			{ "search" : "headers[server]", "regexp" : "/^NetShelter\/VPN$/" },
		]
	return(self.rules)
