import plugins
			
class Pluginrainmail_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<form action='/cgi-bin/openwebmail/openwebmail.pl'" },
			{ "certainty" : "75", "text" : "<!--  SCRIPT CONFIGURATION SECTION -->" },
			{ "text" : "<TD width=50%><font color="ffffff" size="1"face="Verdana", "Helvetica">Rainmail is a product of :</font>" },
			{ "text" : "<div align="center">.: <b>Rainmail Intranet Login </b> :.</div>" },
			{ "url" : "/chpasswd.php", "text" : "<TD><font color="ffffff" size="1"face="Verdana", "Arial", "Helvetica", "sans-serif">Rainmail is a product of :</font></TD>" },
		]
	return(self.rules)

