import plugins
			
class Pluginiceshop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p id="power_by"><a href="http://www.iceshop.nl" target="_blank">Powered by ICEshop</a></p>" },
			{ "text" : "Powered by <a class="link copyright02" href="http://www.iceshop.nl/" target="_blank">ICEshop</a>" },
			{ "text" : "<dl class="box boxLogo  box02 iceshop">" },
		]
	return(self.rules)
