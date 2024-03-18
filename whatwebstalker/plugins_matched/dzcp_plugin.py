import plugins
			
class Plugindzcp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script language="javascript" type="text\/javascript" src="..\/inc\/_templates_\/[^\/]+\/_js\/dzcp.js"><\/script>/" },
			{ "regexp" : "/<!--\[ DZCP .{1} by Frank "deV!L" Herrmann - www.dzcp.de \]-->/" },
			{ "regexp" : "/<!--\[ DZCP .{1} by Frank "deV!L" Herrmann - www.dzcp.de & Patrick "Richy" Richert - www.my-starmedia.de\]-->/" },
		]
		return(self.rules)
