import plugins
			
class Plugincisco_vpn_3000_concentrator_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Cisco Systems", "Inc. VPN 3000 Concentrator " },
			{ "text" : "<p>You are using an old browser or have disabled JavaScript. You <b>must</b> use version 4 or higher of Netscape Navigator/Communicator or version 4 or higher of Microsoft Internet Explorer with JavaScript enabled.</p>" },
		]
	return(self.rules)
