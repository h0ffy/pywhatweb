import plugins
			
class Pluginprtg_network_monitor_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<title>PRTG Network Monitor \(([^\)]+)\)&nbsp;\|&nbsp;Welcome<\/title>/" },
			{ "version" : "/<link rel="stylesheet" type="text\/css" href="\/css\/prtgmini\.css\?prtgversion=([^"]+)" media="print,screen,projection" \/>/" },
			{ "version" : "/^PRTG/", "search" : "headers[server]" },
			{ "version" : "/^PRTG\/([^\s]+)$/", "search" : "headers[server]" },
		]
		return(self.rules)
