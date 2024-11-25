import plugins
			
class Pluginispcp_omega_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>ispCP Omega a Virtual Hosting Control System</title>" },
			{ "text" : "Powered by <a class="login" href="http://www.isp-control.net" target="_blank">ispCP Omega" },
			{ "text" : "themes/omega_original/images/login/login_lock.jpg" },
		]
	return(self.rules)
