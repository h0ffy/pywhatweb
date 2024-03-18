import plugins
			
class Plugincuteflow_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/cuteflow\.org" target="_blank"><img src="images\/cuteflow_logo_small\.png" border="0"\s?\/><\/a><br>\s+<strong style="font-size:8pt;font-weight:normal">Version ([^\s^<]+)<\/strong><br>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^strMyLanguage=/" },
		]
	return(self.rules)

