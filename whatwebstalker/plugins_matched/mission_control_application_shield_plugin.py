import plugins
			
class Pluginmission_control_application_shield_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img id="logo" src="/srm-error-pages/images/logo.gif" alt="mission control application shield" ></td><td><p class="notification">Notification</p></td>" },
			{ "search" : "headers[server]", "regexp" : "/^Mission Control Application Shield$/" },
		]
		return(self.rules)
