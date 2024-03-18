import plugins
			
class Pluginminecraft_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<span>Map type:</span><select id="mode" onchange="show(1,$(\'#mode\').val())">", "os" : "MineOS (Linux)" },
			{ "text" : "<title>MineOS Admin Page</title>", "os" : "MineOS (Linux)" },
		]
	return(self.rules)
