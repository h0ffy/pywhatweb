import plugins
			
class Plugincisco_adaptive_security_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Cisco Systems", "Inc. Network Access</title>", "certainty" : "75 },
			{ "search" : "headers[server]", "regexp" : "/^Adaptive Security Appliance HTTP\/1\.1$/" },
			{ "regexp" : "/<FORM ACTION="\/netaccess\/redirect\.html">\s+<INPUT type=hidden name=sid VALUE=/" },
		]
		return(self.rules)
