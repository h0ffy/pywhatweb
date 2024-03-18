import plugins
			
class Pluginairos_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "cache_images(['main_top.png", "'main.png", "'link.png", "'net.png", "'4dv.png", "'srv.png", "'system.png", "'border.gif", "'spectr.gif']);" },
		]
		return(self.rules)
