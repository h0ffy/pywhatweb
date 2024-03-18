import plugins
			
class Plugininfinet_wireless_wanflex_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="InfiNet Wireless Company" />" },
			{ "search" : "headers[server]", "version" : "/^WANFlex HTTP Daemon v([^\s]+)$/" },
		]
	return(self.rules)

