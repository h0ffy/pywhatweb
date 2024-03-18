import plugins
			
class Pluginmantisbt_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<div align="right"><a href="http:\/\/www.mantisbt.org" title="Free Web Based Bug Tracker"><img src="[^"]*images\/mantis_logo_button.gif" width="88" height="35" alt="Powered by Mantis Bugtracker" border="0" \/><\/a><\/div>/" },
			{ "regexp" : "/<div align="right"><a href="http:\/\/www.mantis(bugtracker.com|bt.org)" title="Powered by Mantis Bugtracker"><img src="[^"]*images\/mantis_logo_button.gif" width="88" height="35" alt="Powered by Mantis Bugtracker" border="0" \/><\/a><\/div>/" },
			{ "version" : "/<span class="timer"><a href="http:\/\/www.mantisbt.org\/" title="Free Web Based Bug Tracker">Mantis(BT)? ([\d\.]+)<\/a>\[<a href="http:\/\/www.mantisbt.org\/"  title="Free Web Based Bug Tracker" target="_blank">\^<\/a>\]<\/span>/", "offset" : "1 },
			{ "version" : "/<span class="timer"><a href="http:\/\/www.mantis(bugtracker.com|bt.org)\/">Mantis ([\d\.]+)<\/a>\[<a href="http:\/\/www.mantis(bugtracker.com|bt.org)\/" target="_blank">\^<\/a>\]<\/span>/", "offset" : "1 },
			{ "string" : "Install", "text" : "<title> MantisBT Administration - Installation  </title>" },
		]
	return(self.rules)
