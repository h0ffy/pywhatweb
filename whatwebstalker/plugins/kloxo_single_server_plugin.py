import plugins
			
class Pluginkloxo_single_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title> HyperVM 2.0 </title>" },
			{ "text" : "<title> Kloxo </title>" },
			{ "text" : "<title> Lxadmin </title>" },
			{ "certainty" : "75", "text" : "Use a valid username and password to gain access to the console</b>" },
			{ "text" : "@import url("/htmllib/lib/admin_login.css");" },
		]
	return(self.rules)
