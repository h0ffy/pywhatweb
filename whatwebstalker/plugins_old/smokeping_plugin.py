import plugins
			
class Pluginsmokeping_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<tr><td class="menuitem" colspan="2">&nbsp;-&nbsp;<a class="menulink" HREF="?target=" },
			{ "version" : "/<A HREF="http:\/\/oss\.oetiker\.ch\/smokeping\/counter\.cgi\/([^\s\/\"]+)"><img border="0" src="[^"]+"><\/a>/" },
		]
	return(self.rules)
