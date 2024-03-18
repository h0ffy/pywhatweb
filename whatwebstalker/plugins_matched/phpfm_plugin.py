import plugins
			
class Pluginphpfm_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href='http:\/\/phpfm.zalon.dk\/' target='_new' class='bottom'>PHPFM<\/a> ([\d\.]+)<\/td>/" },
		]
	return(self.rules)

