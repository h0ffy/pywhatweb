import plugins
			
class Pluginw_agora_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "inurl:"w-agora" ext:php3" },
			{ "text" : "<CAPTION><B>System Administrator's Informations (login : <u>admin</u>)</B></CAPTION>" },
			{ "version" : "/<META NAME="GENERATOR" Content="w-agora version ([\d\.]+)"[\/]?>/i },
			{ "text" : "<table border bgcolor="#eeeeee" align="center" cellspacing=0 cellpadding=5 width=400><tr><td align=center><font face="Arial", "Verdana" color="#FF2020">Cannot access configuration file: ./conf/site_agora.php3</td></tr></table>" },
		]
	return(self.rules)
