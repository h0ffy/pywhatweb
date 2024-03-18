import plugins
			
class Pluginzen_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by Zen Cart!", "The Art of E-commerce</title>" },
			{ "text" : "Powered by <a href="http://www.zen-cart.com" target="_blank">Zen Cart</a>" },
			{ "text" : "<meta name="authors" content="The Zen Cart&trade; Team and others" },
			{ "text" : "<meta name="generator" content="shopping cart program by Zen Cart&trade;", "http://www.zen-cart.com" },
		]
		return(self.rules)
