import plugins
			
class Pluginviewvc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>ViewVC Repository Listing</title>" },
			{ "text" : "<!-- ViewVC :: http://www.viewvc.org/ -->" },
			{ "text" : "<!-- ViewCVS -- http://viewcvs.sourceforge.net/" },
			{ "version" : "%r{Powered by <a href="http://(viewcvs.sourceforge.net|viewvc.tigris.org)/">(ViewCVS|ViewVC) ([^<]+)</a></td>}", "offset" : "2 },
			{ "version" : "/<meta name="generator" content="View(VC|CVS) ([^"]+)"/", "offset" : "1 },
		]
		return(self.rules)
