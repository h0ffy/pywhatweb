import plugins
			
class Pluginsecure_snapgear_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/img/logo.ico", "md5" : "a27c392bc74b2d5c0e10fa7c1132c74d" },
			{ "model" : "/<td class="menu"><div class="logo"><a href="\/cgi-bin\/cgix\/default"><img class="logo" alt="([^"]+)" src="\/img\/logo\.gif"><\/a>/" },
			{ "string" : /<html><head><title>([^\s]+)\nManagement Console<\/title>/" },
			{ "string" : /<html><head><title>([^\s]+) - SnapGear Management Console\n<\/title>/" },
		]
		return(self.rules)
