import plugins
			
class Pluginzomplog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://zomplog.zomp.nl" target="_blank">Zomplog</a>" },
			{ "text" : "<title>Zomplog &rsaquo; Login</title>" },
			{ "text" : "<td width="135"><div align="right"><span class="style1"><a href="http://www.zomp.nl/zomplog/" target="_blank">zomplog &rsaquo;&rsaquo;</a> </span></div></td>" },
			{ "text" : "<meta name="generator" content="Zomplog" />" },
			{ "text" : "/* Navbar (Zomplog-specific) */" },
		]
	return(self.rules)

