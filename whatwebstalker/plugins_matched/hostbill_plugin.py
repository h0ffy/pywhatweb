import plugins
			
class Pluginhostbill_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- part below is not css valid. remove it if you want this document to be css valid -->" },
			{ "text" : "</div><br/><center>Powered by <a href="http://hostbillapp.com" target="_blank"><strong>HostBill</strong></a></center><br/></div>" },
		]
		return(self.rules)
