import plugins
			
class Pluginsearchfit_shopping_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "This Website is generated by SearchFit Shopping Cart"},
			{ "text" : "<a class="footer_link_system" target="_blank" style="font-size: 10px;" href="http://www.searchfit.com/'},
			{ "text" : "new SearchFitAnalytics("'},
		]
	return(self.rules)
