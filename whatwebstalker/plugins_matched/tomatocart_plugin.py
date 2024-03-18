import plugins
			
class Plugintomatocart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="TomatoCart Open Source Shopping Cart Solutions" />" },
			{ "text" : "Powered by <a href="http://www.tomatocart.com" target="_blank">TomatoCart</a>" },
			{ "md5" : "600924763aa7af6c968f53e0f6d9e608", "url" : "/templates/glass_gray/images/tomatocart.ico" },
		]
	return(self.rules)
