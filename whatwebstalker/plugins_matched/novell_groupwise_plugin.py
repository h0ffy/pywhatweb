import plugins
			
class Pluginnovell_groupwise_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- START NOVELL SERVICES -->" },
			{ "text" : "<!-- START GROUPWISE WEBACCESS -->" },
			{ "text" : "<!-- ========== GroupWise WebAccess Form ========== -->" },
			{ "ghdb" : "intitle:"novell webaccess" inurl:"servlet/webacc" -filetype:html" },
			{ "text" : "<title>Novell Web Services</title>"},
			{ "text" : "<TITLE>Novell WebAccess</TITLE>" },
			{ "version" : "/^&copy; Copyright 1993-20[\d]{2} Novell", "Inc. All rights reserved.[\s]+<BR>Version ([\d\.]+)$/" },
		]
		return(self.rules)

