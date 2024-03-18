import plugins
			
class Plugincs_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	text_required_group_product: "Please select a product for the required group [group_name]'," },
			{ "regexp" : "/Powered by <a href="http:\/\/www.cs-cart.com" target="_blank"[^>]+>CS-Cart - Shopping Cart Software<\/a>/" },
			{ "text" : "<title>CS-Cart. Powerful PHP shopping cart software</title>" },
		]
			return(self.rules)
