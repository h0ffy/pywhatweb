import plugins
			
class Plugincacti_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Login to Cacti</title>" },
			{ "text" : "<body bgcolor="#FFFFFF" onload="document.login.login_username.focus()">" },
		]
	return(self.rules)
