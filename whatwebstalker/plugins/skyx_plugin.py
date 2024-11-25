import plugins
			
class Pluginskyx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="skyx_status">SkyX status: enhancing</div>" },
			{ "text" : "<script language="javascript" type="text/javascript" src="/skyxgui.js"></script>" },
			{ "string" : /<div id="hostname"><a href="Misc">Hostname<\/a>: ([^\s^<]+)<\/div>/" },
			{ :"regxp" : "/^SkyX /", "search" : "headers[server]" },
			{ "version" : "/^SkyX HTTPS ([^\s]+)$/", "search" : "headers[server]" },
		]
	return(self.rules)
