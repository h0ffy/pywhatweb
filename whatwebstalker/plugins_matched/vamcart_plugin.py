import plugins
			
class Pluginvamcart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<link type="text\/css" href="[^"]+\/stylesheets\/load\/vamcart\.css" rel="stylesheet"  media="screen"\/>/" },
			{ "text" : "<!-- Powered by: VamCart (http://vamcart.com) -->" },
			{ "text" : "<p><a href="http://vamcart.com/">PHP Shopping Cart</a> <a href="http://vamcart.com/">VamCart</a></p>" },
		]
		return(self.rules)
