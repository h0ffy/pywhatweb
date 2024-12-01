import plugins
			
class Pluginprolink_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<! Copyright (c) Realtek Semiconductor Corp.", "2003. All Rights Reserved. ->" },
			{ "text" : "<title>PROLiNK ADSL Router</title>" },
			{ "text" : "<title>RFwell ADSL Router Status</title>" },
			{ "text" : "<FRAME SRC="attention.htm" NAME="attention" FRAMEBORDER="NO" SCROLLING="NO" MARGINWIDTH="0" MARGINHEIGHT="0">" },
			{ "md5" : "8be83109b0aaabae7737b28e666ba116", "url" : "/images/logo.gif" },
		]
	return(self.rules)
