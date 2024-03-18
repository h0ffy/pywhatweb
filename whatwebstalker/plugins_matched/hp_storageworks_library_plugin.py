import plugins
			
class Pluginhp_storageworks_library_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/login.ssi", "text" : "<TD class="mastheadIcon"><img src="signin_logo.gif" border="0" alt="HP"></TD>" },
			{ "url" : "/login.ssi", "version" : "/<TITLE>HP StorageWorks (MSL[^\s]+) Tape Library Webpages<\/TITLE>/" },
			{ "url" : "/index.htm", "md5" : "63a4689c098daa89f62cc13069571204" },
		]
	return(self.rules)

