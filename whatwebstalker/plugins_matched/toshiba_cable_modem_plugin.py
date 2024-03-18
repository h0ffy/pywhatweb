import plugins
			
class Plugintoshiba_cable_modem_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Toshiba Cable Modem PCX3000</TITLE>", "certainty" : "75 },
			{ "url" : "/pcx3k.gif", "md5" : "b70118d64dc5a404f82467bbf3858524", "model" : "PCX3000" },
			{ "url" : "/up.html", "text" : "<BR><FONT color=navy size=5>Toshiba Cable Modem Diagnostics Page &nbsp;</FONT>" },
			{ "url" : "/up.html", "string" : /<STRONG>CMTS MAC Address:<FONT color="#980040">([^<]+)<\/FONT><\/STRONG>/" },
			{ "url" : "/up.html", "model" : "/<STRONG>&nbsp;&nbsp;MODEL[\r\n]*<FONT COLOR="#980040">([^\s^<]+)<\/FONT>/" },
			{ "url" : "/up.html", "firmware" : "/;&nbsp;HW_REV[\r\n]*<FONT COLOR="#980040">([^\s^<]+)<\/FONT>/" },
			{ "url" : "/up.html", "version" : "/;&nbsp;SW_REV[\r\n]*<FONT COLOR="#980040">([^\s^<]+)<\/FONT>/" },
		]
	return(self.rules)
