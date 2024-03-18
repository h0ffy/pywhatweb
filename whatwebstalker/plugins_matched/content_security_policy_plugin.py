import plugins
			
class Plugincontent_security_policy_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[x-content-security-policy]", "string" : /^(.*)$/" },
			{ "search" : "headers[x-webkit-csp]", "string" : /^(.*)$/" },
		]
		return(self.rules)
