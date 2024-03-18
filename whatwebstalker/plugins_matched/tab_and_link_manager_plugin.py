import plugins
			
class Plugintab_and_link_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="footer_copyright" class="shade footer_copyright">Powered by <a href="http:\/\/www\.wolfshead-solutions\.com\/ws-products\/product-1" rel="wsBlank">Tab and Link Manager<\/a> Version ([^<^\s]+)<br \/>Copyright &copy; 20[\d]{2} Wolfshead Solutions\. All rights reserved\.<br \/>/" },
		]
		return(self.rules)
