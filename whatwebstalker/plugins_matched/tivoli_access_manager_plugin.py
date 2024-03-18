import plugins
			
class Plugintivoli_access_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Access Manager for e-business Login</TITLE>" },
			{ "text" : "<!-- Copyright (C) 2000 Tivoli Systems", "Inc. -->" },
			{ "text" : "<!--- DO NOT TRANSLATE OR MODIFY any part of the hidden parameter(s) --->" },
			{ "text" : "var warningString = "<B>WARNING:</B> To maintain your login session", "make sure that your browser is configured to accept Cookies.";" },
		]
		return(self.rules)
