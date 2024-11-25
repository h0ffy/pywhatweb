import plugins
			
class Plugininterspire_shopping_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<meta name="generator" content="Interspire Shopping Cart" />" },
			{ "regexp" : "/				Powered by <a href="http:\/\/www.interspire.com\/shoppingcart[\/]*" target="_blank" class="PoweredBy">Interspire Shopping Cart<\/a>/" },
		]
	return(self.rules)
