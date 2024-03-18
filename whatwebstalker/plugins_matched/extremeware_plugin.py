import plugins
			
class Pluginextremeware_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^ExtremeWare\/([^\s]+)$/" },
			{ "md5" : "a18d6970836e3302e4d6d085e8f9d31b", "url" : "/Images/extremelogan" },
			{ "md5" : "bf368990304c878ce2924bc21b3f06d9", "url" : "/Images/extremelogan" },
			{ "text" : "<title>ExtremeWare Management Interface</title>" },
			{ "text" : "<center><img src="Images/extremelogan"><a href="extremebasepage" target="_top"><h2>Logon</h2></a><P><P><TABLE BORDER="0"><TR><TD NOWRAP><TT><FONT COLOR="#000000">" },
		]
	return(self.rules)
