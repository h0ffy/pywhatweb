import plugins
			
class Pluginnetjuke_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Start Primary Header -->" },
			{ "text" : "<!-- Begin Primary Footer -->" },
			{ "text" : "onClick=\"window.open('alphabet.php?do=alpha.artists','NetjukeRemote'" },
		]
	return(self.rules)

