import plugins
			
class Pluginepic_web_honeypot_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<center><font size="3" face="monospace">******************************** Epic Web Honeypot ********************************</font></center>" },
			{ "version" : "/<center><font size="3" face="monospace">\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Version ([^\s]+) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*<\/font><\/center>/" },
			{ "text" : "<!-- Added OS fingerprints - creds - nmap and honeyd nmap.prints file!-->" },
		]
		return(self.rules)
