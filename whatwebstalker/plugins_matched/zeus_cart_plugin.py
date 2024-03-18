import plugins
			
class Pluginzeus_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img src="images/warning.gif">Warning: Installation directory exists ZEUSCART ROOT DIRECTORY/install. Please remove/rename this directory for security reasons." },
			{ "text" : "Powered by <a href="http://www.ajsquare.com/products/ecom/" style="color:#716f6f;" target="_blank">ZeusCart</a>" },
			{ "text" : "<title>:: Zeuscart Admin Panel</title>" },
			{ "version" : "/<title>[\s]+ZeusCart V([\d\.]+)[\s]+<\/title>/" },
		]
		return(self.rules)
